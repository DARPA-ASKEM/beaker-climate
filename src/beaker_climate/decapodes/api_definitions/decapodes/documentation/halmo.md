


# Couple Ice and Water Dynamics




Let's use Decapodes to implement the incompressible Navier-Stokes as given by [Mohamed et al.](https://arxiv.org/abs/1508.01166). We will run these dynamics [on the sphere](https://youtu.be/k0hFhAvhHvs?si=Wi9-OgBbAODtxMtb). We will couple this model with Halfar glacier dynamics [on the sphere](https://algebraicjulia.github.io/Decapodes.jl/dev/ice_dynamics/#2-Manifold-in-3D). For the initial conditions of the Halfar ice thickness, we will use an idealized polar ice cap.


Note that the time scale at which ice creeps is much larger than the time scale at which the water in the ocean would flow. So we can either choose to model a very slow moving fluid around the ice (like a storm on a gas giant), or we can choose to model on a shorter timescale, on which the ice does not move very much.


```julia
# AlgebraicJulia Dependencies
using Catlab
using CombinatorialSpaces
using Decapodes
using DiagrammaticEquations

# External Dependencies
using CairoMakie
using ComponentArrays
using GeometryBasics: Point3
using JLD2
using LinearAlgebra
using MLStyle
using OrdinaryDiffEq
Point3D = Point3{Float64};
```




## Specify our models


Our first component is the Mohamed et al. formulation of the incompressible Navier-Stokes equations. We will call the flow here "w". This will be the flow after collisions with glaciers are considered.


This is [Equation 10](https://arxiv.org/abs/1508.01166) for N=2.


```julia
eq10forN2 = @decapode begin
  (𝐮,w)::DualForm1
  (P, 𝑝ᵈ)::DualForm0
  μ::Constant

  𝑝ᵈ == P + 0.5 * ι₁₁(w,w)

  ∂ₜ(𝐮) == μ * ∘(d, ⋆, d, ⋆)(w) + (-1)*⋆₁⁻¹(∧ᵈᵖ₁₀(w, ⋆(d(w)))) + d(𝑝ᵈ)
end
to_graphviz(eq10forN2)
```
