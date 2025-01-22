


# Library Reference






## Decapodes

**`Decapodes.CartesianPoint`** &mdash; *Type*.



```julia
CartesianPoint{T}(p)
```

a point in cartesian coordinates, intended as a wrapper around Point3 from GeometryBasics.

**`Decapodes.SpherePoint`** &mdash; *Type*.



```julia
SpherePoint{T}(p)
```

a point in spherical coordinates, intended as a wrapper around Point3 from GeometryBasics.

**`Decapodes.TangentBasis`** &mdash; *Method*.



```julia
tb(w)
```

Take a linear combinations of the tangent vectors at the base point.  Use this to get a vector tangent to the sphere in the coordinate system of the base point. If the base point is in spherical coordinates, this is the identity, if the base point is in cartesian coordinates, it returns the tangent vector in cartesian coordinates.

**`Decapodes.gensim`** &mdash; *Method*.



```julia
function gensim(d::AbstractNamedDecapode; dimension::Int=2)
```

Generate a simulation function from the given Decapode. The returned function can then be combined with a mesh and a function describing function mappings to return a simulator to be passed to `solve`.


```
[ Info: Page built in 3 seconds.
[ Info: This page was last built at 2025-01-17T11:27:43.743.
```

