


# Introduction to Decapodes




Discrete Exterior Calculus Applied to Partial and Ordinary Differential Equations (Decapodes) is a diagrammatic language used to express systems of ordinary and partial differential equations. Decapodes provides a visual framework for understanding the coupling between variables within a PDE or ODE system, and a combinatorial data structure for working with them. Below, we provide a high-level overview of how Decapodes can be generated and interpreted.




## Your First Decapode


In the Decapodes graphical paradigm, nodes represent variables and arrows represent operators which relate variables to each other. Since Decapodes applies this diagrammatic language specifically to the Discrete Exterior Calculus (DEC), variables are typed by the dimension and orientation of the information they contain. So a variable of type `Form0` will be the 0-dimensional data points defined the vertices of a mesh. Similarly, `Form1` will be values stored on edges of the mesh and `Form2` will be values stored on the surfaces of the mesh.


Below, we provide a Decapode with just a single variable `C` and display it.


```julia
using Catlab
using Decapodes
using DiagrammaticEquations

Variable = @decapode begin
  C::Form0
end;

to_graphviz(Variable)
```




The resulting diagram contains a single node, showing the single variable in this system. We can add a second variable:


```julia
TwoVariables = @decapode begin
  C::Form0
  dC::Form1
end;

to_graphviz(TwoVariables)
```




We can also add a relationship between them. In this case, we make an equation which states that `dC` is the derivative of `C`:


```julia
Equation = @decapode begin
  C::Form0
  dC::Form1

  dC == d(C)
end;

to_graphviz(Equation)
```




Here, the two nodes represent the two variables, and the arrow between them shows how they are related by the derivative.




## A Little More Complicated


Now that we've seen how to construct a simple equation, it's time to move on to some actual PDE systems! One classic PDE example is the diffusion equation. This equation states that the change of concentration at each point is proportional to the Laplacian of the concentration.


```julia
Diffusion = @decapode begin
  (C, Ċ)::Form0
  ϕ::Form1

  # Fick's first law
  ϕ ==  k(d₀(C))

  # Diffusion equation
  Ċ == ⋆₀⁻¹(dual_d₁(⋆₁(ϕ)))
  ∂ₜ(C) == Ċ

end;

to_graphviz(Diffusion)
```




The resulting Decapode shows the relationships between the three variables with the triangle diagram. Note that these diagrams are automatically layed-out by [Graphviz](https://graphviz.org/).




## Bring in the Dynamics


Now that we have a reasonably complex PDE, we can demonstrate some of the developed tooling for actually solving the PDE. Currently, the tooling will automatically generate an explicit method for solving the system (using [DifferentialEquations.jl](https://github.com/SciML/DifferentialEquations.jl?tab=readme-ov-file) to handle time-stepping and instability detection).


`Torus_30x10` is a default mesh that is downloaded via `Artifacts.jl` when a user installs [CombinatorialSpaces.jl](https://github.com/AlgebraicJulia/CombinatorialSpaces.jl). If we wanted, we could also instantiate any `.obj` file of triangulated faces as a simplicial set although we do not here.


We will also upload a non-periodic mesh for the sake of visualization, as well as a mapping between the points on the periodic and non-periodic meshes.


```julia
using CairoMakie
using CombinatorialSpaces

plot_mesh = loadmesh(Rectangle_30x10())
periodic_mesh = loadmesh(Torus_30x10())
point_map = loadmesh(Point_Map())

fig = Figure()
ax = CairoMakie.Axis(fig[1,1], aspect = AxisAspect(3.0))
wireframe!(ax, plot_mesh)
fig
```


Now we create a function which links the names of functions used in the Decapode to their implementations. Note that many DEC operators are already defined for you.


As an example, we chose to define `k` as a function that multiplies an input by `0.05`. We could have alternately chosen to represent `k` as a `Constant` that we multiply by in the Decapode itself.


We then compile the simulation by using `gen_sim` and create functional simulation by calling the evaluated `sim`  with the mesh and our `generate` function.


```@example DEC
using MLStyle

function generate(sd, my_symbol; hodge=DiagonalHodge())
  op = @match my_symbol begin
    :k => x -> 0.05*x
    x => error("Unmatched operator $my_symbol")
  end
  return op
end

sim = eval(gensim(Diffusion))
fₘ = sim(periodic_mesh, generate, DiagonalHodge())
```


We go ahead and set up our initial conditions for this problem. In this case we generate a Gaussian and apply it to our mesh.


```julia
using Distributions
c_dist = MvNormal([7, 5], [1.5, 1.5])
c = [pdf(c_dist, [p[1], p[2]]) for p in periodic_mesh[:point]]

fig = Figure()
ax = CairoMakie.Axis(fig[1,1], aspect = AxisAspect(3.0))
mesh!(ax, plot_mesh; color=c[point_map])
fig
```


Finally, we solve this PDE problem using the `Tsit5()` solver provided by DifferentialEquations.jl.


```@example DEC
using LinearAlgebra
using ComponentArrays
using OrdinaryDiffEq

u₀ = ComponentArray(C=c)

prob = ODEProblem(fₘ, u₀, (0.0, 100.0))
sol = solve(prob, Tsit5());
sol.retcode
```


Now that the simulation has succeeded we can plot out our results with [CairoMakie.jl](https://github.com/MakieOrg/Makie.jl).


```@example DEC
# Plot the result
times = range(0.0, 100.0, length=150)
colors = [sol(t).C[point_map] for t in times]

# Initial frame
fig = Figure()
ax = CairoMakie.Axis(fig[1,1], aspect = AxisAspect(3.0))
pmsh = mesh!(ax, plot_mesh; color=colors[1], colorrange = extrema(vcat(colors...)))
Colorbar(fig[1,2], pmsh)
framerate = 30

# Animation
record(fig, "diffusion.gif", range(0.0, 100.0; length=150); framerate = 30) do t
  pmsh.color = sol(t).C[point_map]
end
```


![Your first Decapode!](diffusion.gif)




## Merging Multiple Physics


Now that we've seen the basic pipeline, it's time for a more complex example that demonstrates some of the benefits reaped from using [Catlab.jl](https://github.com/AlgebraicJulia/Catlab.jl) as the backend to our data structures. In this example, we will take two separate physics (diffusion and advection), and combine them together using a higher-level composition pattern.


We begin by defining the three systems we need. The first two systems are the relationships between concentration and flux under diffusion and advection respectively. The third is the relationship between the two fluxes and the change of concentration under superposition of fluxes.


```julia
Diffusion = @decapode begin
  C::Form0
  ϕ::Form1

  # Fick's first law
  ϕ ==  k(d₀(C))
end

Advection = @decapode begin
  C::Form0
  ϕ::Form1
  V::Form1

  ϕ == ∧₀₁(C,V)
end

Superposition = @decapode begin
  (C, Ċ)::Form0
  (ϕ, ϕ₁, ϕ₂)::Form1

  ϕ == ϕ₁ + ϕ₂
  Ċ == ⋆₀⁻¹(dual_d₁(⋆₁(ϕ)))
  ∂ₜ(C) == Ċ
end
```


The diffusion Decapode.




The advection Decapode.




And the superposition Decapode.




Next, we define the pattern of composition which we want to compose these physics under. This pattern of composition is described by an undirected wiring diagram, which has the individual physics as nodes and the shared variables as the small junctions.


```julia
compose_diff_adv = @relation (C, V) begin
  diffusion(C, ϕ₁)
  advection(C, ϕ₂, V)
  superposition(ϕ₁, ϕ₂, ϕ, C)
end

draw_composition(compose_diff_adv)
```




After this, the physics can be composed as follows:


```julia
DiffusionAdvection_cospan = oapply(compose_diff_adv,
                  [Open(Diffusion, [:C, :ϕ]),
                   Open(Advection, [:C, :ϕ, :V]),
                   Open(Superposition, [:ϕ₁, :ϕ₂, :ϕ, :C])])
DiffusionAdvection = apex(DiffusionAdvection_cospan)

to_graphviz(DiffusionAdvection)
```




Similar to before, this physics can be compiled and executed. Note that this process now requires another value to be defined, namely the velocity vector field. We do this using a custom operator called `flat_op`. This operator is basically the flat operator from CombinatorialSpaces.jl, but specialized to account for the periodic mesh.


We could instead represent the domain as the surface of an object with equivalent boundaries in 3D.




```@example DEC
using LinearAlgebra
using MLStyle

function generate(sd, my_symbol; hodge=DiagonalHodge())
  op = @match my_symbol begin
    :k => x -> 0.05*x
    x => error("Unmatched operator $my_symbol")
  end
  return (args...) -> op(args...)
end

sim = eval(gensim(DiffusionAdvection))
fₘ = sim(periodic_mesh, generate, DiagonalHodge())

velocity(p) = [-0.5, -0.5, 0.0]
v = flat_op(periodic_mesh, DualVectorField(velocity.(periodic_mesh[triangle_center(periodic_mesh),:dual_point])); dims=[30, 10, Inf])

u₀ = ComponentArray(C=c,V=v)

prob = ODEProblem(fₘ, u₀, (0.0, 100.0))
sol = solve(prob, Tsit5());

# Plot the result
times = range(0.0, 100.0, length=150)
colors = [sol(t).C[point_map] for t in times]

# Initial frame
fig = Figure()
ax = CairoMakie.Axis(fig[1,1], aspect = AxisAspect(3.0))
pmsh = mesh!(ax, plot_mesh; color=colors[1], colorrange = extrema(vcat(colors...)))
Colorbar(fig[1,2], pmsh)
framerate = 30

# Animation
record(fig, "diff_adv.gif", range(0.0, 100.0; length=150); framerate = 30) do t
  pmsh.color = sol(t).C[point_map]
end
```


![Your first composed Decapode!](diff_adv.gif)


```
[ Info: Page built in 3 seconds.
[ Info: This page was last built at 2025-01-17T11:30:53.145.
```
