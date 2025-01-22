


# Sheaves


Sheaves are useful for modeling spatial data. The classic example is continuous functions over a topological space. If you have a function defined at every point in a topological space, then you can think about covers of your space and how that function restricts to subspaces of their domain. When you have locally defined functions that agree on overlapping domains, you can extend them to one function defined on the union of their domains.


Sheaves are a generalization of this idea. The motivating example of sheaves of vectors is implemented and described in the vignettes.

**`Catlab.Sheaves.FVectPushforward`** &mdash; *Constant*.



```julia
FreeVect{T} where T <: Number
```

The covariant free vector space functor.  The returned  function f✶ sums over preimages.

**`Catlab.Sheaves.FVectPullback`** &mdash; *Type*.



```julia
FVectPullback{T} where T <: Number
```

The contravariant free vector space functor.  The returned function f✶ restricts via precomposition.

**`Catlab.Sheaves.MatchingError`** &mdash; *Type*.



```julia
MatchingError
```

An Exception type for when sections over a sheaf fail to match, that is when they don't agree on the overlaps implied by a cover. This stores the list MatchingFailures encountered when walking the cover.

**`Catlab.Sheaves.MatchingFailure`** &mdash; *Type*.



```julia
MatchingFailure
```

An type for when sections over a sheaf fail to match, that is when they don't agree on the overlaps implied by a cover.

**`Catlab.Sheaves.diagnose_match`** &mdash; *Method*.



```julia
diagnose_match(X::Sheaf, cover, sections; debug=false)
```

For each object X in the diagram, check that all the sections restrict to the same value along the Hom(X, -).

The arguments haave the same interpretation as in `extend`.

**`Catlab.Sheaves.extend`** &mdash; *Method*.



```julia
extend(X::AbstractSheaf, cover::AbstractCover, sections::AbstractVector)
```

Extend a collection of sections to the unique section that restricts to the sections provided. The `sections` vector needs to be indexed in the same order as `enumerate(cover)`.

**`Catlab.Sheaves.extend`** &mdash; *Method*.



```julia
extend(X::Sheaf{T, FVectPullback}, cover::ColimCover, sections::Vector{Vector{R}}; check=true, debug=false) where {T<:DiagramTopology, R}
```

This method implements the extension operation for the diagram topology on FinSet for the Free Vector Space functor. The implementation does copies the value of the ith section into the jth spot as indicated by the legs of the cocone.

**`Catlab.Sheaves.restrict`** &mdash; *Method*.



```julia
restrict(X::AbstractSheaf, s::Section, f::Hom) where Hom
```

If you supply a wrapped section, you should get a back a wrapped section.

**`Catlab.Sheaves.restrict`** &mdash; *Method*.



```julia
restrict(X::AbstractSheaf, s::Data, f::Hom) where {Data, Hom}
```

Restrict a section along a morphism in the sheaf. This is to apply the sheaf's functor to the morphism f and then apply that function to the data supplied.  We can assume that you can directly call that applied functor on data, because sheaves take C to **Set**.

