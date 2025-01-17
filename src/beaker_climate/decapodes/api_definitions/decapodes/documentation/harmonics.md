


# Harmonics of the Sphere


This page shows how to use Decapodes tooling to explore the harmonics of a discrete manifold. This isn't using any Decapodes specific code, but it  is emblematic of a more advanced analysis you might want to do on your Decapode.


In this case we are trying to visualize the roots of the Laplacian on a discrete manifold.


Load the dependencies


```julia
# Meshing:
using CombinatorialSpaces
using CoordRefSystems
using GeometryBasics: Point3
const Point3D = Point3{Float64};

# Visualization:
using CairoMakie

# Simulation:
using LinearAlgebra
```


Load the mesh


```julia
const RADIUS = 1.0
s = loadmesh(Icosphere(3, RADIUS));
sd = EmbeddedDeltaDualComplex2D{Bool, Float64, Point3D}(s);
subdivide_duals!(sd, Barycenter());
```


Compute the Laplacian eigenvectors using [LinearAlgebra.eigen](https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/#LinearAlgebra.eigen). This requires making the sparse Laplacian matrix dense with `collect`. Alternatively, use [Arpack.jl](https://arpack.julialinearalgebra.org/stable/).


```julia
Δ0 = -Δ(0,sd)
λ = eigen(collect(Δ0))
```


```
LinearAlgebra.Eigen{Float64, Float64, Matrix{Float64}, Vector{Float64}}
values:
162-element Vector{Float64}:
  5.1599355192809e-15
  1.8501953398214102
  1.922934108104094
  1.9658810495474313
  5.1462209107764405
  5.528877811211739
  5.639164681656202
  5.737050666884091
  5.859943695790215
  9.317272553998718
  ⋮
 77.17507216665024
 86.50765980625523
 86.51040566694287
 86.58168500302754
 86.59363600121762
 86.67718662766472
 86.68365853045168
 86.68546749816448
 86.68738445511202
vectors:
162×162 Matrix{Float64}:
 0.0785674  -0.00139719  -0.104545   …   0.000848792  -0.00294379
 0.0785674   0.0696797    0.0192111      0.153257     -0.00715503
 0.0785674   0.107855    -0.0713353     -0.488914      0.487552
 0.0785674   0.00417104  -0.128525       0.00110173   -0.00296474
 0.0785674  -0.112362    -0.0657565      0.575396      0.387291
 0.0785674  -0.0834091    0.0226547  …  -0.117539      0.00955895
 0.0785674   0.114972     0.0665464      0.216674     -0.476139
 0.0785674   0.0820901   -0.0259179      0.115597     -0.00385017
 0.0785674  -0.0704939   -0.0222209     -0.155239      0.0135661
 0.0785674  -0.110218     0.0716917     -0.301402     -0.409684
 ⋮                                   ⋱   ⋮            
 0.0785674   0.0323531   -0.130654       0.00544982   -0.00626171
 0.0785674   0.0306632   -0.122617       0.00539986   -0.00625665
 0.0785674   0.0654118   -0.113619   …  -0.0338602     0.0338033
 0.0785674  -0.0284136   -0.0111406     -0.0102456     0.000514537
 0.0785674   0.02021     -0.0121854      0.0124337    -0.000887686
 0.0785674  -0.0018298   -0.0418315     -0.000199872  -0.000553123
 0.0785674   0.0856251   -0.068554      -0.0357922     0.0341249
 0.0785674   0.0508548   -0.0772451  …   0.00421754   -0.00604669
 0.0785674   0.0734731   -0.040202       0.0163659    -0.00595885
```


Let's check that our eigenvalues satisfy the right equation. The first eigenvector should be the kernel of the laplacian. So the following norm should be close to 0.


```julia
q1 = λ.vectors[:,1]
norm(Δ0 *q1)
```


```
5.810279247141448e-14
```


The first eigenvector is boring to visualize, because it is constant. So we will make some plots of the second eigenvector. If you run this on the desktop, you can use GLMakie and get an interactive plot to explore. We will just draw two angles.


```julia
q = λ.vectors[:,2]
fig = Figure()
Label(fig[1, 1, Top()], "Default Angle", padding = (0, 0, 5, 0))
ax = LScene(fig[1,1], scenekw=(lights=[],))
msh = CairoMakie.mesh!(ax, s, color=q)
Colorbar(fig[1,2], msh, size=32)
# Second Angle
Label(fig[2, 1, Top()], "Bottom Angle", padding = (0, 0, 5, 0))
ax = LScene(fig[2,1], scenekw=(lights=[],))
update_cam!(ax.scene, Vec3f(-1/2,-1/2,1.0/2), Vec3f(1,1,1), Vec3f(0, 0, 1))
msh = CairoMakie.mesh!(ax, s, color=q)
Colorbar(fig[2,2], msh, size=32)
fig
```


```julia
q = λ.vectors[:,12]
fig = Figure()
Label(fig[1, 1, Top()], "Default Angle", padding = (0, 0, 5, 0))
ax = LScene(fig[1,1], scenekw=(lights=[],))
msh = CairoMakie.mesh!(ax, s, color=q)
Colorbar(fig[1,2], msh, size=32)
# Second Angle
Label(fig[2, 1, Top()], "Bottom Angle", padding = (0, 0, 5, 0))
ax = LScene(fig[2,1], scenekw=(lights=[],))
update_cam!(ax.scene, Vec3f(-1/2,-1/2,1.0/2), Vec3f(1,1,1), Vec3f(0, 0, 1))
msh = CairoMakie.mesh!(ax, s, color=q)
Colorbar(fig[2,2], msh, size=32)
fig
```




# Exploring solutions with Krylov methods


We can also use the information about the eigenvectors for spectral techniques in solving the equations. Krylov methods are a bridge between linear solvers and spectral information.


```julia
using Krylov
b = zeros(nv(sd))
b[1] = 1
b[end] = -1
x, stats = Krylov.gmres(Δ0, b, randn(nv(sd)), restart=true, memory=20, atol = 1e-10, rtol=1e-8, history=true, itmax=10000)
x̂ = x .- sum(x)./length(x)
norm(x̂)
stats
norm(Δ0*(x) - b)
```

