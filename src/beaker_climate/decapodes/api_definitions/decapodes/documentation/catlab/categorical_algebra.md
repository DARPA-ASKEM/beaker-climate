


# Categorical algebra




## Sets and Relations


The following APIs implement FinSet, the category of Finite Sets (actually the skeleton of FinSet). The objects of this category are natural numbers where `n` represents a set with `n` elements. The morphisms are functions between such sets. We use the skeleton of FinSet in order to ensure that all sets are finite and morphisms can be stored using lists of integers. Finite relations are built out of FinSet and can be used to do some relational algebra.

**`Catlab.CategoricalAlgebra.Sets`** &mdash; *Module*.



Category of (possibly infinite) sets and functions.

This module defines generic types for the category of sets ([`SetOb`](categorical_algebra.md#Catlab.CategoricalAlgebra.Sets.SetOb), [`SetFunction`](categorical_algebra.md#Catlab.CategoricalAlgebra.Sets.SetFunction)), as well as a few basic concrete types, such as a wrapper type to view Julia types as sets ([`TypeSet`](categorical_algebra.md#Catlab.CategoricalAlgebra.Sets.TypeSet)). Extensive support for finite sets is provided by another module, [`FinSets`](@ref).

**`Catlab.CategoricalAlgebra.Sets.ConstantFunction`** &mdash; *Type*.



Function in **Set** taking a constant value.

**`Catlab.CategoricalAlgebra.Sets.PredicatedSet`** &mdash; *Type*.



Set defined by a predicate (boolean-valued function) on a Julia data type.

**`Catlab.CategoricalAlgebra.Sets.SetFunction`** &mdash; *Type*.



Abstract type for morphism in the category **Set**.

Every instance of `SetFunction{<:SetOb{T},<:SetOb{T′}}` is callable with elements of type `T`, returning an element of type `T′`.

Note: This type would be better called simply `Function` but that name is already taken by the base Julia type.

**`Catlab.CategoricalAlgebra.Sets.SetOb`** &mdash; *Type*.



Abstract type for object in the category **Set**.

The type parameter `T` is the element type of the set.

Note: This type is more abstract than the built-in Julia types `AbstractSet` and `Set`, which are intended for data structures for finite sets. Those are encompassed by the subtype [`FinSet`](@ref).

**`Catlab.CategoricalAlgebra.Sets.TypeSet`** &mdash; *Type*.



A Julia data type regarded as a set.

**`AlgebraicInterfaces.Ob`** &mdash; *Method*.



Forgetful functor Ob: Cat → Set.

Sends a category to its set of objects and a functor to its object map.

**`Catlab.CategoricalAlgebra.FinSets`** &mdash; *Module*.



The category of finite sets and functions, and its skeleton.

**`Catlab.CategoricalAlgebra.FinSets.FinDomFunction`** &mdash; *Type*.



Function out of a finite set.

This class of functions is convenient because it is exactly the class that can be represented explicitly by a vector of values from the codomain.

**`Catlab.CategoricalAlgebra.FinSets.FinFunction`** &mdash; *Type*.



Function between finite sets.

The function can be defined implicitly by an arbitrary Julia function, in which case it is evaluated lazily, or explictly by a vector of integers. In the vector representation, the function (1↦1, 2↦3, 3↦2, 4↦3), for example, is represented by the vector [1,3,2,3].

FinFunctions can be constructed with or without an explicitly provided codomain. If a codomain is provided, by default the constructor checks it is valid.

This type is mildly generalized by [`FinDomFunction`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinSets.FinDomFunction).

**`Catlab.CategoricalAlgebra.FinSets.FinSet`** &mdash; *Type*.



Finite set.

A finite set has abstract type `FinSet{S,T}`. The second type parameter `T` is the element type of the set and the first parameter `S` is the collection type, which can be a subtype of `AbstractSet` or another Julia collection type. In addition, the skeleton of the category **FinSet** is the important special case `S = Int`. The set ${1,…,n}$ is represented by the object `FinSet(n)` of type `FinSet{Int,Int}`.

**`Catlab.CategoricalAlgebra.FinSets.HashJoin`** &mdash; *Type*.



[Hash join](https://en.wikipedia.org/wiki/Hash_join) algorithm.

**`Catlab.CategoricalAlgebra.FinSets.JoinAlgorithm`** &mdash; *Type*.



Algorithm for limit of cospan or multicospan with feet being finite sets.

In the context of relational databases, such limits are called *joins*. The trivial join algorithm is [`NestedLoopJoin`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinSets.NestedLoopJoin), which is algorithmically equivalent to the generic algorithm `ComposeProductEqualizer`. The algorithms [`HashJoin`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinSets.HashJoin) and [`SortMergeJoin`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinSets.SortMergeJoin) are usually much faster. If you are unsure what algorithm to pick, use [`SmartJoin`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinSets.SmartJoin).

**`Catlab.CategoricalAlgebra.FinSets.NestedLoopJoin`** &mdash; *Type*.



[Nested-loop join](https://en.wikipedia.org/wiki/Nested_loop_join) algorithm.

This is the naive algorithm for computing joins.

**`Catlab.CategoricalAlgebra.FinSets.SmartJoin`** &mdash; *Type*.



Meta-algorithm for joins that attempts to pick an appropriate algorithm.

**`Catlab.CategoricalAlgebra.FinSets.SortMergeJoin`** &mdash; *Type*.



[Sort-merge join](https://en.wikipedia.org/wiki/Sort-merge_join) algorithm.

**`Catlab.CategoricalAlgebra.FinSets.SubFinSet`** &mdash; *Type*.



Subset of a finite set.

**`Catlab.CategoricalAlgebra.FinSets.SubOpBoolean`** &mdash; *Type*.



Algorithm to compute subobject operations using elementwise boolean logic.

**`Catlab.CategoricalAlgebra.FinSets.TabularLimit`** &mdash; *Type*.



Limit of finite sets viewed as a table.

Any limit of finite sets can be canonically viewed as a table ([`TabularSet`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinSets.TabularSet)) whose columns are the legs of the limit cone and whose rows correspond to elements of the limit object. To construct this table from an already computed limit, call `TabularLimit(::AbstractLimit; ...)`. The column names of the table are given by the optional argument `names`.

In this tabular form, applying the universal property of the limit is trivial since it is just tupling. Thus, this representation can be useful when the original limit algorithm does not support efficient application of the universal property. On the other hand, this representation has the disadvantage of generally making the element type of the limit set more complicated.

**`Catlab.CategoricalAlgebra.FinSets.TabularSet`** &mdash; *Type*.



Finite set whose elements are rows of a table.

The underlying table should be compliant with Tables.jl. For the sake of uniformity, the rows are provided as named tuples, which assumes that the table is not "extremely wide". This should not be a major limitation in practice but see the Tables.jl documentation for further discussion.

**`Catlab.CategoricalAlgebra.FinSets.VarFunction`** &mdash; *Type*.



Data type for a morphism of VarSet{T}s. Note we can equivalently view these  as morphisms [n]+T -> [m]+T fixing T or as morphisms [n] -> [m]+T, in the typical Kleisli category yoga. 

Currently, domains are treated as VarSets. The codom field is treated as a FinSet{Int}. Note that the codom accessor gives a VarSet while the codom field is just that VarSet's  FinSet of AttrVars. This could be generalized to being FinSet{Symbol} to allow for symbolic attributes. (Likewise, AttrVars will have to wrap Any rather than Int)

**`Catlab.CategoricalAlgebra.FinSets.VarSet`** &mdash; *Type*.



Control dispatch in the category of VarFunctions

**`ACSets.PreimageCaches.preimage`** &mdash; *Method*.



The preimage (inverse image) of the value y in the codomain.

**`Catlab.CategoricalAlgebra.FinSets.is_indexed`** &mdash; *Method*.



Whether the given function is indexed, i.e., supports efficient preimages.

**`Catlab.CategoricalAlgebra.FinRelations`** &mdash; *Module*.



The category of finite sets and relations, and its skeleton.

**`Catlab.CategoricalAlgebra.FinRelations.BoolRig`** &mdash; *Type*.



The rig of booleans.

This struct is needed because in base Julia, the product of booleans is another boolean, but the sum of booleans is coerced to an integer: `true + true == 2`.

**`Catlab.CategoricalAlgebra.FinRelations.FinRel`** &mdash; *Type*.



Object in the category of finite sets and relations.

See also: [`FinSet`](@ref).

**`Catlab.CategoricalAlgebra.FinRelations.FinRelation`** &mdash; *Type*.



Binary relation between finite sets.

A morphism in the category of finite sets and relations. The relation can be represented implicitly by an arbitrary Julia function mapping pairs of elements to booleans or explicitly by a matrix (dense or sparse) taking values in the rig of booleans ([`BoolRig`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinRelations.BoolRig)).

**`Catlab.CategoricalAlgebra.FinRelations.FinRelationCallable`** &mdash; *Type*.



Relation in FinRel defined by a callable Julia object.

**`Catlab.CategoricalAlgebra.FinRelations.FinRelationMatrix`** &mdash; *Type*.



Relation in FinRel represented by a boolean matrix.

Boolean matrices are also known as logical matrices or relation matrices.




## Free Diagrams, Limits, and Colimits


The following modules define free diagrams in an arbitrary category and specify limit and colimit cones over said diagrams. Thes constructions enjoy the fullest support for FinSet and are used below to define presheaf categories as C-Sets. The general idea of these functions is that you set up a limit computation by specifying a diagram and asking for a limit or colimit cone, which is returned as a struct containing the apex object and the leg morphisms. This cone structure can be queried using the functions [`apex`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.apex-Tuple{Multispan}) and [`legs`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.legs-Tuple{Multispan}). Julia's multiple dispatch feature is heavily used to specialize limit and colimit computations for various diagram shapes like product/coproduct and equalizer/coequalizer. As a consumer of this API, it is highly recommended that you use multiple dispatch to specialize your code on the diagram shape whenever possible.

**`Catlab.CategoricalAlgebra.FreeDiagrams`** &mdash; *Module*.



Free diagrams in a category.

A [free diagram](https://ncatlab.org/nlab/show/free+diagram) in a category is a diagram whose shape is a free category. Examples include the empty diagram, pairs of objects, discrete diagrams, parallel pairs, composable pairs, and spans and cospans. Limits and colimits are most commonly taken over free diagrams.

**`Catlab.CategoricalAlgebra.FreeDiagrams.BipartiteFreeDiagram`** &mdash; *Type*.



A free diagram with a bipartite structure.

Such diagrams include most of the fixed shapes, such as spans, cospans, and parallel morphisms. They are also the generic shape of diagrams for limits and colimits arising from undirected wiring diagrams. For limits, the boxes correspond to vertices in $V₁$ and the junctions to vertices in $V₂$. Colimits are dual.

**`Catlab.CategoricalAlgebra.FreeDiagrams.BipartiteFreeDiagram`** &mdash; *Method*.



Convert a free diagram to a bipartite free diagram.

Reduce a free diagram to a free bipartite diagram with the same limit (the default, `colimit=false`) or the same colimit (`colimit=true`). The reduction is essentially the same in both cases, except for the choice of where to put isolated vertices, where we follow the conventions described at [`cone_objects`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.cone_objects-Tuple{Any}) and [`cocone_objects`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.cocone_objects-Tuple{Any}). The resulting object is a bipartite free diagram equipped with maps from the vertices of the bipartite diagram to the vertices of the original diagram.

**`Catlab.CategoricalAlgebra.FreeDiagrams.ComposableMorphisms`** &mdash; *Type*.



Composable morphisms in a category.

Composable morphisms are a sequence of morphisms in a category that form a path in the underlying graph of the category.

For the common special case of two morphisms, see [`ComposablePair`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.ComposablePair).

**`Catlab.CategoricalAlgebra.FreeDiagrams.ComposablePair`** &mdash; *Type*.



Pair of composable morphisms in a category.

[Composable pairs](https://ncatlab.org/nlab/show/composable+pair) are a common special case of [`ComposableMorphisms`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.ComposableMorphisms).

**`Catlab.CategoricalAlgebra.FreeDiagrams.Cospan`** &mdash; *Type*.



Cospan of morphisms in a category.

A common special case of [`Multicospan`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.Multicospan). See also [`Span`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.Span).

**`Catlab.CategoricalAlgebra.FreeDiagrams.DiscreteDiagram`** &mdash; *Type*.



Discrete diagram: a diagram with no non-identity morphisms.

**`Catlab.CategoricalAlgebra.FreeDiagrams.FixedShapeFreeDiagram`** &mdash; *Type*.



Abstract type for free diagram of fixed shape.

**`Catlab.CategoricalAlgebra.FreeDiagrams.Multicospan`** &mdash; *Type*.



Multicospan of morphisms in a category.

A multicospan is like a [`Cospan`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.Cospan) except that it may have a number of legs different than two. A limit of this shape is a pullback.

**`Catlab.CategoricalAlgebra.FreeDiagrams.Multispan`** &mdash; *Type*.



Multispan of morphisms in a category.

A [multispan](https://ncatlab.org/nlab/show/multispan) is like a [`Span`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.Span) except that it may have a number of legs different than two. A colimit of this shape is a pushout.

**`Catlab.CategoricalAlgebra.FreeDiagrams.ParallelMorphisms`** &mdash; *Type*.



Parallel morphims in a category.

[Parallel morphisms](https://ncatlab.org/nlab/show/parallel+morphisms) are just morphisms with the same domain and codomain. A (co)limit of this shape is a (co)equalizer.

For the common special case of two morphisms, see [`ParallelPair`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.ParallelPair).

**`Catlab.CategoricalAlgebra.FreeDiagrams.ParallelPair`** &mdash; *Type*.



Pair of parallel morphisms in a category.

A common special case of [`ParallelMorphisms`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.ParallelMorphisms).

**`Catlab.CategoricalAlgebra.FreeDiagrams.Span`** &mdash; *Type*.



Span of morphims in a category.

A common special case of [`Multispan`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.Multispan). See also [`Cospan`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.Cospan).

**`Catlab.CategoricalAlgebra.FreeDiagrams.apex`** &mdash; *Method*.



Apex of multispan or multicospan.

The apex of a multi(co)span is the object that is the (co)domain of all the [`legs`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.legs-Tuple{Multispan}).

**`Catlab.CategoricalAlgebra.FreeDiagrams.bundle_legs`** &mdash; *Method*.



Bundle together legs of a multi(co)span.

For example, calling `bundle_legs(span, SVector((1,2),(3,4)))` on a multispan with four legs gives a span whose left leg bundles legs 1 and 2 and whose right leg bundles legs 3 and 4. Note that in addition to bundling, this function can also permute legs and discard them.

The bundling is performed using the universal property of (co)products, which assumes that these (co)limits exist.

**`Catlab.CategoricalAlgebra.FreeDiagrams.cocone_objects`** &mdash; *Method*.



Objects in diagram that will have explicit legs in colimit cocone.

See also: [`cone_objects`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.cone_objects-Tuple{Any}).

**`Catlab.CategoricalAlgebra.FreeDiagrams.cone_objects`** &mdash; *Method*.



Objects in diagram that will have explicit legs in limit cone.

In category theory, it is common practice to elide legs of limit cones that can be computed from other legs, especially for diagrams of certain fixed shapes. For example, when it taking a pullback (the limit of a cospan), the limit object is often treated as having two projections, rather than three. This function encodes such conventions by listing the objects in the diagram that will have corresponding legs in the limit object created by Catlab.

See also: [`cocone_objects`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.cocone_objects-Tuple{Any}).

**`Catlab.CategoricalAlgebra.FreeDiagrams.diagram_type`** &mdash; *Function*.



Given a diagram in a category $C$, return Julia type of objects and morphisms in $C$ as a tuple type of form $Tuple{Ob,Hom}$.

**`Catlab.CategoricalAlgebra.FreeDiagrams.feet`** &mdash; *Method*.



Feet of multispan or multicospan.

The feet of a multispan are the codomains of the [`legs`](categorical_algebra.md#Catlab.CategoricalAlgebra.FreeDiagrams.legs-Tuple{Multispan}).

**`Catlab.CategoricalAlgebra.FreeDiagrams.left`** &mdash; *Method*.



Left leg of span or cospan.

**`Catlab.CategoricalAlgebra.FreeDiagrams.legs`** &mdash; *Method*.



Legs of multispan or multicospan.

The legs are the morphisms comprising the multi(co)span.

**`Catlab.CategoricalAlgebra.FreeDiagrams.right`** &mdash; *Method*.



Right leg of span or cospan.

**`Catlab.CategoricalAlgebra.Limits`** &mdash; *Module*.



Limits and colimits in a category.

**`Catlab.CategoricalAlgebra.Limits.AbstractColimit`** &mdash; *Type*.



Abstract type for colimit in a category.

The standard concrete subtype is [`Colimit`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.Colimit), although for computational reasons certain categories may use different subtypes to include extra data.

**`Catlab.CategoricalAlgebra.Limits.AbstractLimit`** &mdash; *Type*.



Abstract type for limit in a category.

The standard concrete subtype is [`Limit`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.Limit), although for computational reasons certain categories may use different subtypes to include extra data.

**`Catlab.CategoricalAlgebra.Limits.Colimit`** &mdash; *Type*.



Colimit in a category.

**`Catlab.CategoricalAlgebra.Limits.ColimitAlgorithm`** &mdash; *Type*.



Algorithm for computing colimits.

**`Catlab.CategoricalAlgebra.Limits.ComposeCoproductCoequalizer`** &mdash; *Type*.



Compute pushout by composing a coproduct with a coequalizer.

See also: [`ComposeProductEqualizer`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.ComposeProductEqualizer).

**`Catlab.CategoricalAlgebra.Limits.ComposeProductEqualizer`** &mdash; *Type*.



Compute pullback by composing a product with an equalizer.

See also: [`ComposeCoproductCoequalizer`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.ComposeCoproductCoequalizer).

**`Catlab.CategoricalAlgebra.Limits.Limit`** &mdash; *Type*.



Limit in a category.

**`Catlab.CategoricalAlgebra.Limits.LimitAlgorithm`** &mdash; *Type*.



Algorithm for computing limits.

**`Catlab.CategoricalAlgebra.Limits.SpecializeColimit`** &mdash; *Type*.



Meta-algorithm that reduces general colimits to common special cases.

Dual to [`SpecializeLimit`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.SpecializeLimit).

**`Catlab.CategoricalAlgebra.Limits.SpecializeLimit`** &mdash; *Type*.



Meta-algorithm that reduces general limits to common special cases.

Reduces limits of free diagrams that happen to be discrete to products. If this fails, fall back to the given algorithm (if any).

TODO: Reduce free diagrams that are (multi)cospans to (wide) pullbacks.

**`Catlab.CategoricalAlgebra.Limits.ToBipartiteColimit`** &mdash; *Type*.



Compute a colimit by reducing the diagram to a free bipartite diagram.

**`Catlab.CategoricalAlgebra.Limits.ToBipartiteLimit`** &mdash; *Type*.



Compute a limit by reducing the diagram to a free bipartite diagram.

**`Catlab.CategoricalAlgebra.FreeDiagrams.apex`** &mdash; *Method*.



Synonymous with `ob` in the case of `Limit`s, but  present here to allow a `Limit` to be implicitly  treated like a `Multispan`.

**`Catlab.CategoricalAlgebra.Limits.coimage`** &mdash; *Method*.



https://en.wikipedia.org/wiki/Coimage

**`Catlab.CategoricalAlgebra.Limits.colimit`** &mdash; *Method*.



Colimit of a diagram.

To define colimits in a category with objects `Ob`, override the method `colimit(::FreeDiagram{Ob})` for general colimits or `colimit(::D)` with suitable type `D <: FixedShapeFreeDiagram{Ob}` for colimits of specific shape, such as coproducts or coequalizers.

See also: [`limit`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.limit-Tuple{Any})

**`Catlab.CategoricalAlgebra.Limits.epi_mono`** &mdash; *Method*.



The image and coimage are isomorphic. We get this isomorphism using univeral properties.

```
  CoIm′ ╌╌> I ↠ CoIm
    ┆ ⌟     |
    v       v
    I   ⟶  R ↩ Im
    |       ┆
    v    ⌜  v
    R ╌╌> Im′
```

**`Catlab.CategoricalAlgebra.Limits.image`** &mdash; *Method*.



https://en.wikipedia.org/wiki/Image*(category*theory)#Second_definition

**`Catlab.CategoricalAlgebra.Limits.limit`** &mdash; *Method*.



Limit of a diagram.

To define limits in a category with objects `Ob`, override the method `limit(::FreeDiagram{Ob})` for general limits or `limit(::D)` with suitable type `D <: FixedShapeFreeDiagram{Ob}` for limits of specific shape, such as products or equalizers.

See also: [`colimit`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.colimit-Tuple{Any})

**`Catlab.CategoricalAlgebra.Limits.pullback`** &mdash; *Method*.



Pullback of a pair of morphisms with common codomain.

To implement for a type `T`, define the method `limit(::Cospan{T})` and/or `limit(::Multicospan{T})` or, if you have already implemented products and equalizers, rely on the default implementation.

**`Catlab.CategoricalAlgebra.Limits.pushout`** &mdash; *Method*.



Pushout of a pair of morphisms with common domain.

To implement for a type `T`, define the method `colimit(::Span{T})` and/or `colimit(::Multispan{T})` or, if you have already implemented coproducts and coequalizers, rely on the default implementation.

**`Catlab.Theories.coequalizer`** &mdash; *Method*.



Coequalizer of morphisms with common domain and codomain.

To implement for a type `T`, define the method `colimit(::ParallelPair{T})` or `colimit(::ParallelMorphisms{T})`.

**`Catlab.Theories.copair`** &mdash; *Method*.



Copairing of morphisms: universal property of coproducts/pushouts.

To implement for coproducts of type `T`, define the method `universal(::BinaryCoproduct{T}, ::Cospan{T})` and/or `universal(::Coproduct{T}, ::Multicospan{T})` and similarly for pushouts.

**`Catlab.Theories.coproduct`** &mdash; *Method*.



Coproduct of objects.

To implement for a type `T`, define the method `colimit(::ObjectPair{T})` and/or `colimit(::DiscreteDiagram{T})`.

**`Catlab.Theories.create`** &mdash; *Method*.



Unique morphism out of an initial object.

To implement for a type `T`, define the method `universal(::Initial{T}, ::SMulticospan{0,T})`.

**`Catlab.Theories.delete`** &mdash; *Method*.



Unique morphism into a terminal object.

To implement for a type `T`, define the method `universal(::Terminal{T}, ::SMultispan{0,T})`.

**`Catlab.Theories.equalizer`** &mdash; *Method*.



Equalizer of morphisms with common domain and codomain.

To implement for a type `T`, define the method `limit(::ParallelPair{T})` and/or `limit(::ParallelMorphisms{T})`.

**`Catlab.Theories.factorize`** &mdash; *Method*.



Factor morphism through (co)equalizer, via the universal property.

To implement for equalizers of type `T`, define the method `universal(::Equalizer{T}, ::SMultispan{1,T})`. For coequalizers of type `T`, define the method `universal(::Coequalizer{T}, ::SMulticospan{1,T})`.

**`Catlab.Theories.initial`** &mdash; *Method*.



Initial object.

To implement for a type `T`, define the method `colimit(::EmptyDiagram{T})`.

**`Catlab.Theories.pair`** &mdash; *Method*.



Pairing of morphisms: universal property of products/pullbacks.

To implement for products of type `T`, define the method `universal(::BinaryProduct{T}, ::Span{T})` and/or `universal(::Product{T}, ::Multispan{T})` and similarly for pullbacks.

**`Catlab.Theories.product`** &mdash; *Method*.



Product of objects.

To implement for a type `T`, define the method `limit(::ObjectPair{T})` and/or `limit(::DiscreteDiagram{T})`.

**`Catlab.Theories.terminal`** &mdash; *Method*.



Terminal object.

To implement for a type `T`, define the method `limit(::EmptyDiagram{T})`.

**`Catlab.Theories.universal`** &mdash; *Function*.



```julia
universal(lim,cone)
```

Universal property of (co)limits.

Compute the morphism whose existence and uniqueness is guaranteed by the universal property of (co)limits.

See also: [`limit`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.limit-Tuple{Any}), [`colimit`](categorical_algebra.md#Catlab.CategoricalAlgebra.Limits.colimit-Tuple{Any}).

**`Catlab.CategoricalAlgebra.Limits.@cartesian_monoidal_instance`** &mdash; *Macro*.



Define cartesian monoidal structure using limits.

Implements an instance of [`ThCartesianCategory`](@ref) assuming that finite products have been implemented following the limits interface.

**`Catlab.CategoricalAlgebra.Limits.@cocartesian_monoidal_instance`** &mdash; *Macro*.



Define cocartesian monoidal structure using colimits.

Implements an instance of [`ThCocartesianCategory`](@ref) assuming that finite coproducts have been implemented following the colimits interface.




## Categories

**`Catlab.CategoricalAlgebra.Categories`** &mdash; *Module*.



2-category of categories, functors, and natural transformations.

Categories in mathematics appear in the large, often as categories of sets with extra structure, and in the small, as algebraic structures that generalize groups, monoids, preorders, and graphs. This division manifests in Catlab as well. Large categories (in spirit, if not in the [technical sense](https://ncatlab.org/nlab/show/large+category)) occur throughout Catlab as `@instance`s of the theory of categories. For computational reasons, small categories are usually presented by generators and relations.

This module provides a minimal interface to accomodate both situations. Category instances are supported through the wrapper type [`TypeCat`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.TypeCat). Finitely presented categories are provided by another module, [`FinCats`](@ref).

**`Catlab.CategoricalAlgebra.Categories.Cat`** &mdash; *Type*.



Alias for [`Category`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.Category).

**`Catlab.CategoricalAlgebra.Categories.CatSize`** &mdash; *Type*.



Size of a category, used for dispatch and subtyping purposes.

A [`Category`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.Category) type having a particular `CatSize` means that categories of that type are *at most* that large.

**`Catlab.CategoricalAlgebra.Categories.Category`** &mdash; *Type*.



Abstract base type for a category.

The objects and morphisms in the category have Julia types `Ob` and `Hom`, respectively. Note that these types do *not* necessarily form an `@instance` of the theory of categories, as they may not meaningfully form a category outside the context of this object. For example, a finite category regarded as a reflexive graph with a composition operation might have type `Cat{Int,Int}`, where the objects and morphisms are numerical identifiers for vertices and edges in the graph.

The basic operations available in any category are: [`dom`](categorical_algebra.md#AlgebraicInterfaces.dom-Tuple{Category, Any}), [`codom`](categorical_algebra.md#AlgebraicInterfaces.codom-Tuple{Category, Any}), [`id`](categorical_algebra.md#AlgebraicInterfaces.id-Tuple{Category, Any}), [`compose`](categorical_algebra.md#AlgebraicInterfaces.compose-Tuple{Category, Vararg{Any}}).

**`Catlab.CategoricalAlgebra.Categories.CompositeFunctor`** &mdash; *Type*.



Composite of functors.

**`Catlab.CategoricalAlgebra.Categories.Functor`** &mdash; *Type*.



Abstract base type for a functor between categories.

A functor has a domain and a codomain ([`dom`](categorical_algebra.md#AlgebraicInterfaces.dom-Tuple{Category, Any}) and [`codom`](categorical_algebra.md#AlgebraicInterfaces.codom-Tuple{Category, Any})), which are categories, and object and morphism maps, which can be evaluated using [`ob_map`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.ob_map-Tuple{Functor, Any}) and [`hom_map`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.hom_map-Tuple{Functor, Any}). The functor object can also be called directly when the objects and morphisms have distinct Julia types. This is sometimes but not always the case (see [`Category`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.Category)), so when writing generic code one should prefer the `ob_map` and `hom_map` functions.

**`Catlab.CategoricalAlgebra.Categories.FunctorCallable`** &mdash; *Type*.



Functor defined by two Julia callables, an object map and a morphism map.

**`Catlab.CategoricalAlgebra.Categories.IdentityFunctor`** &mdash; *Type*.



Identity functor on a category.

**`Catlab.CategoricalAlgebra.Categories.LargeCatSize`** &mdash; *Type*.



Size of a large category, such as Set.

To the extent that they form a category, we regard Julia types and functions ([`TypeCat`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.TypeCat)) as forming a large category.

**`Catlab.CategoricalAlgebra.Categories.OppositeCat`** &mdash; *Type*.



Opposite category, where morphism are reversed.

Call `op(::Cat)` instead of directly instantiating this type.

**`Catlab.CategoricalAlgebra.Categories.OppositeFunctor`** &mdash; *Type*.



Opposite functor, given by the same mapping between opposite categories.

Call `op(::Functor)` instead of directly instantiating this type.

**`Catlab.CategoricalAlgebra.Categories.Transformation`** &mdash; *Type*.



Abstract base type for a natural transformation between functors.

A natural transformation $α: F ⇒ G$ has a domain $F$ and codomain $G$ ([`dom`](categorical_algebra.md#AlgebraicInterfaces.dom-Tuple{Category, Any}) and [`codom`](categorical_algebra.md#AlgebraicInterfaces.codom-Tuple{Category, Any})), which are functors $F,G: C → D$ having the same domain $C$ and codomain $D$. The transformation consists of a component $αₓ: Fx → Gx$ in $D$ for each object $x ∈ C$, accessible using [`component`](categorical_algebra.md#Catlab.CategoricalAlgebra.Categories.component) or indexing notation (`Base.getindex`).

**`Catlab.CategoricalAlgebra.Categories.TypeCat`** &mdash; *Type*.



Pair of Julia types regarded as a category.

The Julia types should form an `@instance` of the theory of categories (`Theories.Category`).

**`AlgebraicInterfaces.codom`** &mdash; *Method*.



Codomain of morphism in category.

**`AlgebraicInterfaces.compose`** &mdash; *Method*.



Compose morphisms in a category.

**`AlgebraicInterfaces.dom`** &mdash; *Method*.



Domain of morphism in category.

**`AlgebraicInterfaces.hom`** &mdash; *Function*.



Coerce or look up morphism in category.

See also: [`ob`](categorical_algebra.md#AlgebraicInterfaces.ob).

**`AlgebraicInterfaces.id`** &mdash; *Method*.



Identity morphism on object in category.

**`AlgebraicInterfaces.ob`** &mdash; *Function*.



Coerce or look up object in category.

Converts the input to an object in the category, which should be of type `Ob` in a category of type `Cat{Ob,Hom}`. How this works depends on the category, but a common case is to look up objects, which might be integers or GAT expressions, by their human-readable name, usually a symbol.

See also: [`hom`](categorical_algebra.md#AlgebraicInterfaces.hom).

**`Catlab.CategoricalAlgebra.Categories.co`** &mdash; *Function*.



2-cell dual of a 2-category.

**`Catlab.CategoricalAlgebra.Categories.codom_ob`** &mdash; *Method*.



Codomain object of natural transformation.

Given $α: F ⇒ G: C → D$, this function returns $D$.

**`Catlab.CategoricalAlgebra.Categories.component`** &mdash; *Function*.



Component of natural transformation.

**`Catlab.CategoricalAlgebra.Categories.dom_ob`** &mdash; *Method*.



Domain object of natural transformation.

Given $α: F ⇒ G: C → D$, this function returns $C$.

**`Catlab.CategoricalAlgebra.Categories.hom_map`** &mdash; *Method*.



Evaluate functor on morphism.

**`Catlab.CategoricalAlgebra.Categories.is_hom_equal`** &mdash; *Method*.



Are two morphisms in a category equal?

By default, just checks for equality of Julia objects using $==$. In some categories, checking equality of morphisms may involve nontrivial reasoning.

**`Catlab.CategoricalAlgebra.Categories.ob_map`** &mdash; *Method*.



Evaluate functor on object.

**`GATlab.Stdlib.StdModels.op`** &mdash; *Method*.



Oppositization 2-functor.

The oppositization endo-2-functor on Cat, sending a category to its opposite, is covariant on objects and morphisms and contravariant on 2-morphisms, i.e., is a 2-functor $op: Catᶜᵒ → Cat$. For more explanation, see the [nLab](https://ncatlab.org/nlab/show/opposite+category).

**`Catlab.CategoricalAlgebra.FinCats`** &mdash; *Module*.



2-category of finitely presented categories.

This module is for the 2-category **Cat** what the module [`FinSets`](@ref) is for the category **Set**: a finitary, combinatorial setting where explicit calculations can be carried out. We emphasize that the prefix `Fin` means "finitely presented," not "finite," as finite categories are too restrictive a notion for many purposes. For example, the free category on a graph is finite if and only if the graph is DAG, which is a fairly special condition. This usage of `Fin` is also consistent with `FinSet` because for sets, being finite and being finitely presented are equivalent.

**`Catlab.CategoricalAlgebra.FinCats.FinCat`** &mdash; *Type*.



A finitely presented (but not necessarily finite!) category.

**`Catlab.CategoricalAlgebra.FinCats.FinCatGraph`** &mdash; *Type*.



Abstract type for category backed by finite generating graph.

**`Catlab.CategoricalAlgebra.FinCats.FinCatGraphEq`** &mdash; *Type*.



Category presented by a finite graph together with path equations.

The objects of the category are vertices in the graph and the morphisms are paths, quotiented by the congruence relation generated by the path equations. See (Spivak, 2014, *Category theory for the sciences*, §4.5).

**`Catlab.CategoricalAlgebra.FinCats.FinCatPathGraph`** &mdash; *Type*.



Abstract type for category whose morphisms are paths in a graph.

(Or equivalence classes of paths in a graph, but we compute with

**`Catlab.CategoricalAlgebra.FinCats.FinCatPresentation`** &mdash; *Type*.



Category defined by a `Presentation` object.

The presentation type can, of course, be a category (`Theories.Category`). It can also be a schema (`Theories.Schema`). In this case, the schema's objects and attribute types are regarded as the category's objects and the schema's morphisms, attributes, and attribute types as the category's morphisms (where the attribute types are identity morphisms). When the schema is formalized as a profunctor whose codomain category is discrete, this amounts to taking the collage of the profunctor.

**`Catlab.CategoricalAlgebra.FinCats.FinCatSize`** &mdash; *Type*.



Size of a finitely presented category.

**`Catlab.CategoricalAlgebra.FinCats.FinDomFunctor`** &mdash; *Type*.



A functor out of a finitely presented category.

**`Catlab.CategoricalAlgebra.FinCats.FinDomFunctorMap`** &mdash; *Type*.



Functor out of a finitely presented category given by explicit mappings.

**`Catlab.CategoricalAlgebra.FinCats.FinFunctor`** &mdash; *Type*.



A functor between finitely presented categories.

**`Catlab.CategoricalAlgebra.FinCats.FinTransformation`** &mdash; *Type*.



A natural transformation whose domain category is finitely generated.

This type is for natural transformations $α: F ⇒ G: C → D$ such that the domain category $C$ is finitely generated. Such a natural transformation is given by a finite amount of data (one morphism in $D$ for each generating object of $C$) and its naturality is verified by finitely many equations (one equation for each generating morphism of $C$).

**`Catlab.CategoricalAlgebra.FinCats.FinTransformationMap`** &mdash; *Type*.



Natural transformation with components given by explicit mapping.

**`Catlab.CategoricalAlgebra.FinCats.FreeCatGraph`** &mdash; *Type*.



Free category generated by a finite graph.

The objects of the free category are vertices in the graph and the morphisms are (possibly empty) paths.

**`Catlab.CategoricalAlgebra.FinCats.Path`** &mdash; *Type*.



Path in a graph.

The path is allowed to be empty but always has definite start and end points (source and target vertices).

**`Catlab.CategoricalAlgebra.FinCats.collect_hom`** &mdash; *Method*.



Collect assignments of functor's morphism map as a vector.

**`Catlab.CategoricalAlgebra.FinCats.collect_ob`** &mdash; *Method*.



Collect assignments of functor's object map as a vector.

**`Catlab.CategoricalAlgebra.FinCats.components`** &mdash; *Method*.



Components of a natural transformation.

**`Catlab.CategoricalAlgebra.FinCats.dom_to_graph`** &mdash; *Method*.



Reinterpret a functor on a finitely presented category as a functor on the equivalent category (ignoring equations) free on a graph. Also normalizes the input to have vector ob*map and hom*map, with valtype optionally specified. This is useful when the domain is empty or when the maps might be tightly typed but need to allow for types such as that of identity morphisms upon mutation.

**`Catlab.CategoricalAlgebra.FinCats.force`** &mdash; *Function*.



Force evaluation of lazily defined function or functor. The resulting ob*map and hom*map are guaranteed to have  valtype or eltype, as appropriate, equal to Ob and Hom, respectively. 

**`Catlab.CategoricalAlgebra.FinCats.functoriality_failures`** &mdash; *Method*.



Failures of the purported functor on a presented category to be functorial.

Similar to [`is_functorial`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinCats.is_functorial-Tuple{Functor{Dom} where Dom<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom})}) (and with the same caveats) but returns iterators of functoriality failures: one for domain incompatibilities, one for codomain incompatibilities, and one for equations that are not satisfied.

**`Catlab.CategoricalAlgebra.FinCats.graph`** &mdash; *Method*.



Graph underlying a finitely presented category whose  object and hom generators are indexable, other than one explicitly generated by a graph.

**`Catlab.CategoricalAlgebra.FinCats.graph`** &mdash; *Method*.



Generating graph for a finitely presented category.

**`Catlab.CategoricalAlgebra.FinCats.hom_generator`** &mdash; *Function*.



Coerce or look up morphism generator in a finitely presented category.

Since morphism generators often have a different data type than morphisms (e.g., in a free category on a graph, the morphism generators are edges and the morphisms are paths), the return type of this function is generally different than that of [`hom`](categorical_algebra.md#AlgebraicInterfaces.hom).

**`Catlab.CategoricalAlgebra.FinCats.hom_generator_name`** &mdash; *Function*.



Name of morphism generator, if any.

When morphism generators have names, this function is a one-sided inverse to [`hom_generator`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinCats.hom_generator). See also: [`ob_generator_name`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinCats.ob_generator_name).

**`Catlab.CategoricalAlgebra.FinCats.hom_generators`** &mdash; *Function*.



Morphism generators of finitely presented category.

**`Catlab.CategoricalAlgebra.FinCats.is_discrete`** &mdash; *Method*.



Is the category discrete?

A category is *discrete* if it is has no non-identity morphisms.

**`Catlab.CategoricalAlgebra.FinCats.is_free`** &mdash; *Method*.



Is the category freely generated?

**`Catlab.CategoricalAlgebra.FinCats.is_functorial`** &mdash; *Method*.



Is the purported functor on a presented category functorial?

This function checks that functor preserves domains and codomains. When `check_equations` is `true` (the default is `false`), it also purports to check that the functor preserves all equations in the domain category. No nontrivial  checks are currently implemented, so this only functions for identity functors.

See also: [`functoriality_failures'](@ref) and [`is_natural`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinCats.is_natural-Tuple{Transformation{C, D, Dom, Codom} where {C<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom}), D<:Category, Dom<:(Functor{Dom} where Dom<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom})), Codom<:(Functor{Dom} where Dom<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom}))}}).

**`Catlab.CategoricalAlgebra.FinCats.is_initial`** &mdash; *Method*.



Dual to a [final functor](https://ncatlab.org/nlab/show/final+functor), an *initial functor* is one for which pulling back diagrams along it does not change the limits of these diagrams.

This amounts to checking, for a functor C->D, that, for every object d in Ob(D), the comma category (F/d) is connected.

**`Catlab.CategoricalAlgebra.FinCats.is_natural`** &mdash; *Method*.



Is the transformation between `FinDomFunctors` a natural transformation?

This function uses the fact that to check whether a transformation is natural, it suffices to check the naturality equations on a generating set of morphisms of the domain category. In some cases, checking the equations may be expensive or impossible. When the keyword argument `check_equations` is `false`, only the domains and codomains of the components are checked.

See also: [`is_functorial`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinCats.is_functorial-Tuple{Functor{Dom} where Dom<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom})}).

**`Catlab.CategoricalAlgebra.FinCats.make_map`** &mdash; *Method*.



Maps `f` over a `UnitRange` to produce a `Vector`, or else over anything to produce a `Dict`. The type paramter functions to ensure the return type is as desired even when the input is empty.

**`Catlab.CategoricalAlgebra.FinCats.mappairs`** &mdash; *Method*.



Map two given functions across the respective keys and values of a dictionary.

**`Catlab.CategoricalAlgebra.FinCats.mapvals`** &mdash; *Method*.



Map a function, which may depend on the key, across the values of a dictionary.

**`Catlab.CategoricalAlgebra.FinCats.ob_generator`** &mdash; *Function*.



Coerce or look up object generator in a finitely presented category.

Because object generators usually coincide with objects, the default method for [`ob`](categorical_algebra.md#AlgebraicInterfaces.ob) in finitely presented categories simply calls this function.

**`Catlab.CategoricalAlgebra.FinCats.ob_generator_name`** &mdash; *Function*.



Name of object generator, if any.

When object generators have names, this function is a one-sided inverse to [`ob_generator`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinCats.ob_generator) in that `ob_generator(C, ob_generator_name(C, x)) == x`.

**`Catlab.CategoricalAlgebra.FinCats.ob_generators`** &mdash; *Function*.



Object generators of finitely presented category.

The object generators of finite presented category are almost always the same as the objects. In principle, however, it is possible to have equations between objects, so that there are fewer objects than object generators.

**`Catlab.CategoricalAlgebra.FinCats.presentation`** &mdash; *Method*.



Computes the graph generating a finitely presented category. Ignores any attribute side and any equations. Optionally returns the mappings from generators to their indices in the resulting graph.




## Acsets




### Overview and Theory


For an in depth look into the theory behind acsets, we refer the reader to [our paper](https://arxiv.org/abs/2106.04703) on the subject, which also gives some sense as to how the implementation works. Here, we give a brief tutorial before the the API documentation.


The most essential part of the acset machinery is the schema. The schema *parameterizes* the acset: each schema corresponds to a different type of acset. Schemas consist of four parts.


  * Objects $X,Y$ (`(X,Y,Z)::Ob`)
  * Homomorphisms $f \colon X \to Y$ (`f :: Hom(X,Y)`), which go from objects to objects
  * Attribute types $\mathtt{T}$ (`T :: AttrType`)
  * Attributes $a \colon X \to \mathtt{T}$ (`a :: Attr(X,T)`), which go from objects to data types


For those with a categorical background, a schema is a presentation of a category $|S|$ along with a functor $S$ from $|S|$ to the arrow category $0 \to 1$, such that $S^{-1}(1)$ is discrete.


An acset $F$ on a schema consists of...


  * a set $F(X)$ of "primary keys" for each object
  * a function $F(f) \colon F(X) \to F(Y)$ for each morphism
  * a Julia data type $F(\mathtt{T})$ for each data type $\mathtt{T}$
  * a function $F(a) \colon F(X) \to F(\mathtt{T})$ for each attribute $a$.


For those with a categorical background, an acset on a schema $S$ consists of a functor from $S$ to $\mathsf{Set}$, such that objects in $S^{-1}(0)$ map to finite sets, and objects in $S^{-1}(1)$ map to sets that represent types. For any particular functor $K \colon S^{-1}(1) \to \mathsf{Set}$, we can also take the category of acsets that restrict to this map on $S^{-1}$.


We can also add equations to this presentation, but we currently do nothing with those equations in the implementation; they mostly serve as documentation.


We will now give an example of how this all works in practice.


```julia
using GATlab, Catlab.CategoricalAlgebra

# Write down the schema for a weighted graph
@present SchWeightedGraph(FreeSchema) begin
  V::Ob
  E::Ob
  src::Hom(E,V)
  tgt::Hom(E,V)
  T::AttrType
  weight::Attr(E,T)
end

# Construct the type used to store acsets on the previous schema
# We *index* src and tgt, which means that we store not only
# the forwards map, but also the backwards map.
@acset_type WeightedGraph(SchWeightedGraph, index=[:src,:tgt])

# Construct a weighted graph, with floats as edge weights
g = @acset WeightedGraph{Float64} begin
  V = 4
  E = 5
  src = [1,1,1,2,3]
  tgt = [2,3,4,4,4]
  weight = [7.2, 9.3, 9.4, 0.1, 42.0]
end
```

<div class="c-set">
<span class="c-set-summary">Main.__atexample__296.WeightedGraph{Float64} {V:4, E:5, T:0}</span>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">E</th>
      <th style = "text-align: right;">src</th>
      <th style = "text-align: right;">tgt</th>
      <th style = "text-align: right;">weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">7.2</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">3</td>
      <td style = "text-align: right;">9.3</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">4</td>
      <td style = "text-align: right;">9.4</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">4</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">4</td>
      <td style = "text-align: right;">0.1</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">5</td>
      <td style = "text-align: right;">3</td>
      <td style = "text-align: right;">4</td>
      <td style = "text-align: right;">42.0</td>
    </tr>
  </tbody>
</table>
</div>




### API


The mathematical abstraction of an acset can of course be implemented in many different ways. Currently, there are three implementations of acsets in Catlab, which share a great deal of code.


These implementations can be split into two categories.


The first category is **static acset types**. In this implementation, different schemas correspond to different Julia types. Methods on these Julia types are then custom-generated for the schema, using [CompTime.jl](https://github.com/AlgebraicJulia/CompTime.jl).


Under this category, there are two classes of static acset types. The first class is acset types that are generated using the `@acset_type` macro. These acset types are custom-derived structs. The advantage of this is that the structs have names like `Graph` or `WiringDiagram` that are printed out in error messages. The disadvantage is that if you are taking in schemas at runtime, you have to `eval` code in order to use them.


Here is an example of using `@acset_type`


```julia
@acset_type WeightedGraph(SchWeightedGraph, index=[:src,:tgt])
g = WeightedGraph()
```


The second class is `AnonACSet`s. Like acset types derived from `@acset_type`, these contain the schema in their type. However, they also contain the type of their fields in their types, so the types printed out in error messages are long and ugly. The advantage of these is that they can be used in situations where the schema is passed in at runtime, and they don't require using `eval` to create a new acset type.


Here is an example of using `AnonACSet`


```julia
const WeightedGraph = AnonACSetType(SchWeightedGraph, index=[:src,:tgt])
g = WeightedGraph()
```


The second category is **dynamic acset types**. Currently, there is just one type that falls under this category: `DynamicACSet`. This type has a **field** for the schema, and no code-generation is done for operations on acsets of this type. This means that if the schema is large compared to the data, this type will often be faster than the static acsets.


However, dynamics acsets are a new addition to Catlab, and much of the machinery of limits, colimits, and other high-level acset constructions assumes that the schema of an acset can be derived from the type. Thus, more work will have to be done before dynamic acsets become a drop-in replacement for static acsets.


Here is an example of using a dynamic acset


```julia
g = DynamicACSet("WeightedGraph", SchWeightedGraph; index=[:src,:tgt])
```

**`Catlab.CategoricalAlgebra.CSets`** &mdash; *Module*.



Categories of C-sets and attributed C-sets.

**`Catlab.CategoricalAlgebra.CSets.ACSetMorphism`** &mdash; *Type*.



Common type for `ACSetTransformation` and `CSetTransformation`.

**`Catlab.CategoricalAlgebra.CSets.ACSetTransformation`** &mdash; *Type*.



Transformation between attributed C-sets.

Homomorphisms of attributed C-sets generalize homomorphisms of C-sets ([`CSetTransformation`](categorical_algebra.md#Catlab.CategoricalAlgebra.CSets.CSetTransformation)), which you should understand before reading this.

A *homomorphism* of attributed C-sets with schema S: C ↛ A (a profunctor) is a natural transformation between the corresponding functors col(S) → Set, where col(S) is the collage of S. When the components on attribute types, indexed by objects of A, are all identity functions, the morphism is called *tight*; in general, it is called *loose*. With this terminology, acsets on a fixed schema are the objects of an ℳ-category (see `Catlab.Theories.MCategory`). Calling `ACSetTransformation` will construct a tight or loose morphism as appropriate, depending on which components are specified.

Since every tight morphism can be considered a loose one, the distinction between tight and loose may seem a minor technicality, but it has important consequences because limits and colimits in a category depend as much on the morphisms as on the objects. In particular, limits and colimits of acsets differ greatly depending on whether they are taken in the category of acsets with tight morphisms or with loose morphisms. Tight morphisms suffice for many purposes, including most applications of colimits. However, when computing limits of acsets, loose morphisms are usually preferable. For more information about limits and colimits in these categories, see [`TightACSetTransformation`](categorical_algebra.md#Catlab.CategoricalAlgebra.CSets.TightACSetTransformation) and [`LooseACSetTransformation`](categorical_algebra.md#Catlab.CategoricalAlgebra.CSets.LooseACSetTransformation).

**`Catlab.CategoricalAlgebra.CSets.ACSetTransformation`** &mdash; *Method*.



Move components as first argument

**`Catlab.CategoricalAlgebra.CSets.ACSetTransformation`** &mdash; *Method*.



A map f (from A to B) as a map from A to a subobject of B

**i.e. get the image of f as a subobject of B**

**`Catlab.CategoricalAlgebra.CSets.ACSetTransformation`** &mdash; *Method*.



A map f (from A to B) as a map of subobjects of A to subjects of B

**`Catlab.CategoricalAlgebra.CSets.CSetTransformation`** &mdash; *Type*.



Transformation between C-sets.

Recall that a C-set homomorphism is a natural transformation: a transformation between functors C → Set satisfying the naturality axiom for every morphism, or equivalently every generating morphism, in C.

This data type records the data of a C-set transformation. Naturality is not strictly enforced but is expected to be satisfied. It can be checked using the function [`is_natural`](categorical_algebra.md#Catlab.CategoricalAlgebra.FinCats.is_natural-Tuple{Transformation{C, D, Dom, Codom} where {C<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom}), D<:Category, Dom<:(Functor{Dom} where Dom<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom})), Codom<:(Functor{Dom} where Dom<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom}))}}).

If the schema of the dom and codom has attributes, this has the semantics of  being a valid C-set transformation on the combinatorial data alone (including  attribute variables, if any).

**`Catlab.CategoricalAlgebra.CSets.LooseACSetTransformation`** &mdash; *Type*.



Loose transformation between attributed C-sets.

Limits and colimits in the category of attributed C-sets and loose homomorphisms are computed pointwise on both objects *and* attribute types. This implies that (co)limits of Julia types must be computed. Due to limitations in the expressivity of Julia's type system, only certain simple kinds of (co)limits, such as products, are supported.

Alternatively, colimits involving loose acset transformations can be constructed with respect to explicitly given attribute type components for the legs of the cocone, via the keyword argument `type_components` to `colimit` and related functions. This uses the universal property of the colimit. To see how this works, notice that a diagram of acsets and loose acset transformations can be expressed as a diagram D: J → C-Set (for the C-sets) along with another diagram A: J → C-Set (for the attribute sets) and a natural transformation α: D ⇒ A (assigning attributes). Given a natural transformation τ: A ⇒ ΔB to a constant functor ΔB, with components given by `type_components`, the composite transformation α⋅τ: D ⇒ ΔB is a cocone under D, hence factors through the colimit cocone of D. This factoring yields an assigment of attributes to the colimit in C-Set.

For the distinction between tight and loose, see [`ACSetTranformation`](@ref).

**`Catlab.CategoricalAlgebra.CSets.SubCSet`** &mdash; *Type*.



Sub-C-set of a C-set.

**`Catlab.CategoricalAlgebra.CSets.TightACSetTransformation`** &mdash; *Type*.



Tight transformation between attributed C-sets.

The category of attributed C-sets and tight homomorphisms is isomorphic to a slice category of C-Set, as explained in our paper "Categorical Data Structures for Technical Computing". Colimits in this category thus reduce to colimits of C-sets, by a standard result about slice categories. Limits are more complicated and are currently not supported.

For the distinction between tight and loose, see [`ACSetTranformation`](@ref).

**`ACSets.ACSetInterface.copy_parts!`** &mdash; *Method*.



Copy parts from a set-valued `FinDomFunctor` to an `ACSet`.

**`Catlab.CategoricalAlgebra.CSets.abstract_attributes`** &mdash; *Function*.



For any ACSet, X, a canonical map A→X where A has distinct variables for all attributes valued in attrtypes present in `abstract` (by default: all attrtypes)

**`Catlab.CategoricalAlgebra.CSets.in_bounds`** &mdash; *Method*.



Check whether an ACSetTransformation is still valid, despite possible deletion  of elements in the codomain. An ACSetTransformation that isn't in bounds will  throw an error, rather than return `false`, if run through `is_natural`.

**`Catlab.CategoricalAlgebra.CSets.is_cartesian`** &mdash; *Function*.



```julia
is_cartesian(f,hs)
```

Checks if an acset transformation `f` is cartesian at the homs in the list `hs`. Expects the homs to be given as a list of `Symbol`s.

**`Catlab.CategoricalAlgebra.CSets.naturality_failures`** &mdash; *Method*.



Returns a dictionary whose keys are contained in the names in `arrows(S)` and whose value at `:f`, for an arrow `(f,c,d)`, is a lazy iterator over the elements of X(c) on which α's naturality square for f does not commute. Components should be a NamedTuple or Dictionary with keys contained in the names of S's morphisms and values vectors or dicts defining partial functions from X(c) to Y(c).

**`Catlab.CategoricalAlgebra.CSets.show_naturality_failures`** &mdash; *Method*.



Pretty-print failures of transformation to be natural.

See also: [`naturality_failures`](categorical_algebra.md#Catlab.CategoricalAlgebra.CSets.naturality_failures-Tuple{Any, Any, Any}).

**`Catlab.CategoricalAlgebra.FinCats.is_natural`** &mdash; *Method*.



Check naturality condition for a purported ACSetTransformation, α: X→Y.  For each hom in the schema, e.g. h: m → n, the following square must commute:

```text
     αₘ
  Xₘ --> Yₘ
Xₕ ↓  ✓  ↓ Yₕ
  Xₙ --> Yₙ
     αₙ
```

You're allowed to run this on a named tuple partly specifying an ACSetTransformation, though at this time the domain and codomain must be fully specified ACSets.

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations`** &mdash; *Module*.



Functorial data migration for attributed C-sets.

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.DataMigrationFunctor`** &mdash; *Type*.



Data migration functor given contravariantly. Stores a contravariant migration.

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.internal_hom`** &mdash; *Method*.



Objects: Fᴳ(c) = C-Set(C × G, F)    where C is the representable c

Given a map f: a->b, we compute that f(Aᵢ) = Bⱼ by constructing the following:           Aᵢ     A × G → F   f*↑ ↑ ↑ ↗ Bⱼ       find the hom Bⱼ that makes this commute     B × G 

where f* is given by `yoneda`.

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.migrate!`** &mdash; *Method*.



Contravariantly migrate data from the acset `Y` to the acset `X`.

This is the mutating variant of [`migrate!`](categorical_algebra.md#Catlab.CategoricalAlgebra.FunctorialDataMigrations.migrate!-Tuple{ACSet, ACSet, Catlab.CategoricalAlgebra.FunctorialDataMigrations.AbstractDataMigration}). When the functor on schemas is the identity, this operation is equivalent to [`copy_parts!`](categorical_algebra.md#ACSets.ACSetInterface.copy_parts!-Tuple{ACSet, Functor{Dom} where Dom<:(Category{Ob, Hom, Catlab.CategoricalAlgebra.FinCats.FinCatSize} where {Ob, Hom})}).

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.migrate`** &mdash; *Method*.



Apply a $Δ$ migration by simple precomposition.

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.migrate`** &mdash; *Method*.



Contravariantly migrate data from the acset `Y` to a new acset of type `T`.

The mutating variant of this function is [`migrate!`](categorical_algebra.md#Catlab.CategoricalAlgebra.FunctorialDataMigrations.migrate!-Tuple{ACSet, ACSet, Catlab.CategoricalAlgebra.FunctorialDataMigrations.AbstractDataMigration}).

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.representable`** &mdash; *Method*.



Construct a representable C-set.

Recall that a *representable* C-set is one of form $C(c,-): C → Set$ for some object $c ∈ C$.

This function computes the $c$ representable as the left pushforward data migration of the singleton ${c}$-set along the inclusion functor ${c} ↪ C$, which works because left Kan extensions take representables to representables (Mac Lane 1978, Exercise X.3.2). Besides the intrinsic difficulties with representables (they can be infinite), this function thus inherits any limitations of our implementation of left pushforward data migrations.

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.subobject_classifier`** &mdash; *Method*.



The subobject classifier Ω in a presheaf topos is the presheaf that sends each  object A to the set of sieves on it (equivalently, the set of subobjects of the  representable presheaf for A). Counting subobjects gives us the *number* of A  parts; the hom data for f:A->B for subobject Aᵢ is determined via:

Aᵢ ↪ A  ↑    ↑ f*   PB⌝↪ B          (PB picks out a subobject of B, up to isomorphism.)

(where A and B are the representables for objects A and B and f* is the unique  map from B into the A which sends the point of B to f applied to the point of A)

Returns the classifier as well as a dictionary of subobjects corresponding to  the parts of the classifier.

**`Catlab.CategoricalAlgebra.FunctorialDataMigrations.yoneda`** &mdash; *Method*.



Compute the Yoneda embedding of a category C in the category of C-sets.

Because Catlab privileges copresheaves (C-sets) over presheaves, this is the *contravariant* Yoneda embedding, i.e., the embedding functor C^op → C-Set.

The first argument `cons` is a constructor for the ACSet, such as a struct acset type. If representables have already been computed (which can be expensive), they can be supplied via the `cache` keyword argument.

Returns a `FinDomFunctor` with domain `op(C)`.

**`GATlab.Models.SymbolicModels.functor`** &mdash; *Method*.



Gives the underlying schema functor of a data migration  seen as a functor of acset categories.

**`Catlab.CategoricalAlgebra.Chase`** &mdash; *Module*.



The chase is an algorithm which subjects a C-Set instance to constraints  expressed in the language of regular logic, called embedded dependencies  (EDs, or 'triggers'). 

A morphism S->T, encodes an embedded dependency. If the pattern  S is matched (via a homomorphism S->I), we demand there exist a morphism T->I  (for some database instance I) that makes the triangle commute in order to  satisfy the dependency (if this is not the case, then the trigger is 'active').

Homomorphisms can merge elements and introduce new ones. The former kind are called "equality generating dependencies" (EGDs) and the latter "tuple generating dependencies" (TGDs). Any homomorphism can be factored into EGD and TGD components by, respectively, restricting the codomain to the image or restricting the domain to the coimage.

**`Catlab.CategoricalAlgebra.Chase.chase`** &mdash; *Method*.



```julia
chase(I::ACSet, Σ::AbstractDict, n::Int)
```

Chase a C-Set or C-Rel instance given a list of embedded dependencies. This may not terminate, so a bound `n` on the number of iterations is required.

```
[,]
```

ΣS  ⟶ Iₙ ⊕↓      ⋮  (resulting morphism)  ΣT ... Iₙ₊₁

There is a copy of S and T for each active trigger. A trigger is a map from S into the current instance. What makes it 'active' is that there is no morphism from T to I that makes the triangle commute.

Each iteration constructs the above pushout square. The result is a morphism, so that one can keep track of the provenance of elements in the original CSet instance within the chased result.

Whether or not the result is due to success or timeout is returned as a boolean flag.

TODO: this algorithm could be made more efficient by homomorphism caching.

**`Catlab.CategoricalAlgebra.StructuredCospans`** &mdash; *Module*.



Structured cospans.

This module provides a generic interface for structured cospans with a concrete implementation for attributed C-sets.

**`Catlab.CategoricalAlgebra.StructuredCospans.OpenACSetLeg`** &mdash; *Type*.



Leg of a structured (multi)cospan of acsets in R-form.

A convenience type that contains the data of an acset transformation, except for the codomain, since that data is already given by the decoration of the R-form structured cospan.

**`Catlab.CategoricalAlgebra.StructuredCospans.StructuredCospan`** &mdash; *Type*.



Structured cospan.

The first type parameter `L` encodes a functor L: A → X from the base category `A`, often FinSet, to a category `X` with "extra structure." An L-structured cospan is then a cospan in X whose feet are images under L of objects in A. The category X is assumed to have pushouts.

Structured cospans form a double category with no further assumptions on the functor L. To obtain a symmetric monoidal double category, L must preserve finite coproducts. In practice, L usually has a right adjoint R: X → A, which implies that L preserves all finite colimits. It also allows structured cospans to be constructed more conveniently from an object x in X plus a cospan in A with apex R(x).

See also: [`StructuredMulticospan`](categorical_algebra.md#Catlab.CategoricalAlgebra.StructuredCospans.StructuredMulticospan).

**`Catlab.CategoricalAlgebra.StructuredCospans.StructuredCospan`** &mdash; *Method*.



Construct structured cospan in R-form.

**`Catlab.CategoricalAlgebra.StructuredCospans.StructuredCospan`** &mdash; *Method*.



Construct structured cospan in L-form.

**`Catlab.CategoricalAlgebra.StructuredCospans.StructuredCospanOb`** &mdash; *Type*.



Object in the category of L-structured cospans.

**`Catlab.CategoricalAlgebra.StructuredCospans.StructuredMulticospan`** &mdash; *Type*.



Structured multicospan.

A structured multicospan is like a structured cospan except that it may have a number of legs different than two.

See also: [`StructuredCospan`](categorical_algebra.md#Catlab.CategoricalAlgebra.StructuredCospans.StructuredCospan).

**`Catlab.CategoricalAlgebra.StructuredCospans.StructuredMulticospan`** &mdash; *Method*.



Construct structured multicospan in R-form.

**`Catlab.CategoricalAlgebra.StructuredCospans.OpenACSetTypes`** &mdash; *Method*.



Create types for open attributed C-sets from an attributed C-set type.

The type parameters of the given acset type should *not* be instantiated with specific Julia types. This function returns a pair of types, one for objects, a subtype of [`StructuredCospanOb`](categorical_algebra.md#Catlab.CategoricalAlgebra.StructuredCospans.StructuredCospanOb), and one for morphisms, a subtype of [`StructuredMulticospan`](categorical_algebra.md#Catlab.CategoricalAlgebra.StructuredCospans.StructuredMulticospan). Both types will have the same type parameters for attribute types as the given acset type.

Mathematically speaking, this function sets up structured (multi)cospans with a functor $L: A → X$ between categories of acsets that creates "discrete acsets." Such a "discrete acset functor" is a functor that is left adjoint to a certain kind of forgetful functor between categories of acsets, namely one that is a pullback along an inclusion of schemas such that the image of inclusion has no outgoing arrows. For example, the schema inclusion ${V} ↪ {E ⇉ V}$ has this property but ${E} ↪ {E ⇉ V}$ does not.

See also: [`OpenCSetTypes`](categorical_algebra.md#Catlab.CategoricalAlgebra.StructuredCospans.OpenCSetTypes-Union{Tuple{X}, Tuple{Type{X}, Vararg{Any}}} where X<:(StructCSet)).

**`Catlab.CategoricalAlgebra.StructuredCospans.OpenCSetTypes`** &mdash; *Method*.



Create types for open C-sets from a C-set type.

A special case of [`OpenACSetTypes`](categorical_algebra.md#Catlab.CategoricalAlgebra.StructuredCospans.OpenACSetTypes-Union{Tuple{X}, Tuple{S}, Tuple{Type{X}, Symbol}} where {S, X<:(StructACSet{S})}). See there for details.

