




# Basic Sheaf Constructions


This example shows how to use a sheaf Catlab. We use the DiagramTopology on FinSet and the Free Vector Space functor to illustrate this process.


```julia
using Test
using Catlab.CategoricalAlgebra
using Catlab.CategoricalAlgebra.Categories
using Catlab.Sheaves
import Catlab.CategoricalAlgebra.Categories: do_ob_map, do_hom_map
using Catlab.CategoricalAlgebra.Matrices: MatrixDom
import Catlab.Sheaves: pullback_matrix, FinSetCat
```


The Topology that we are using is the `DiagramTopology`, which says that a cover of an object `c` is any diagram with `c` as its colimit. The cocone of the diagram gives you a basis for the sieve that covers `c`. The legs of the cocone can be interpreted as open subsets of `c` whose union is `c`. Because colimits are functorial and the base category is adhesive, the diagram topology is well defined.


We have two different implementations of equivalent sheaves. The `VectSheaf` implementation uses julia functions and the `VectSheafMat` implementation uses sparse matrices.


```julia
VectSheaf = Sheaf(DiagramTopology(), FVectPullback())
VectSheafMat = Sheaf(DiagramTopology(), FMatPullback())
```


```
Sheaf{DiagramTopology, FMatPullback}(DiagramTopology(), FMatPullback())
```


We want to introduce a cover of the set ${1...4}$ with two open sets ${1,2,3}$ and ${1,2,4}$. To do that, we will construct a pushout.


```julia
f = FinFunction([1,2], 3)
g = FinFunction([1,2], 3)
S = ColimCover(pushout(f,g))
```


```
ColimCover(FinSet(4)):
  FinFunction([1, 2, 3], 3, 4)
  FinFunction([1, 2, 4], 3, 4)
```


The main API of a sheaf is that you can:


1. restrict sections along a morphism,
2. check if a collection of local sections match on the overlaps,
3. and extend a collection of local sections if they match.


We can restrict a global section along the first leg


```julia
v = [1,2,3,4]
v₁ = restrict(VectSheaf, v, legs(S)[1])
```


```
3-element Vector{Int64}:
 1
 2
 3
```


Or the second leg.


```julia
v₂ = restrict(VectSheaf, v, legs(S)[2])
```


```
3-element Vector{Int64}:
 1
 2
 4
```


Notice that we got two different values, but that the first two entries of those restricted vectors agree. That is because our two legs have an overlap in the first two dimensions. If we restrict again by the arrows in our diagram (f,g) we should get the same answer.


```julia
restrict(VectSheaf, v₁, f)  == restrict(VectSheaf, v₂, g)
```


```
true
```


A sheaf requires:


  * a notion of dividing up a space into pieces (the open coverage),
  * a way of measuring data over the pieces (the set of sections given by the functor on objects), along with
  * ways of relating measurements on a piece to measurements on a subpiece (the restriction maps given by the functor).


Functoriality of the the sheaf tells you that restricting the same data along commuting paths will always give you the same data on the common piece.


The sheaf condition requires that you can compute an extension of local data to global data. There is no way to derive this operation from the contravariant functor of the sheaf so providing it is part of the API in defining a new sheaf.


```julia
extend(VectSheaf, S, [[1.0, 2,3], [1,2.0,6]])
```


```
4-element Vector{Float64}:
 1.0
 2.0
 3.0
 6.0
```


If the local sections don't match, then extending will fail.


```julia
@test_throws MatchingError extend(VectSheaf, S, [[1.0, 2,3], [1,3.0,6]])
```


```
Test Passed
      Thrown: MatchingError{MatchingFailure}
```


extend(VectSheaf, S, [[1.0, 2,3], [1,3.0,6]])


Pushouts are the covers with only two subobjects, but the sheaf works on diagrams of any size.


```julia
D = FreeDiagram(FinSet.([3,2,3,3]), # list of objects
 [ # list of (hom, src, tgt) tuples
  (FinFunction([1,2], 3), 2,1),
  (FinFunction([1,2], 3), 2,3),
  (FinFunction([1,2], 3), 2,4)
  ]
)

K = ColimCover(D)

section_data = [Float64[1,2,3],
   Float64[1,2],
   Float64[1,2,5],
   Float64[1,2,6]]

v = extend(VectSheaf, K, section_data; debug=true)
```


```
5-element Vector{Float64}:
 3.0
 1.0
 2.0
 5.0
 6.0
```


Our two sheaves should agree, because they are just two different implementations of the same sheaf.


```julia
global_section = extend(VectSheafMat, K, section_data)
v == global_section
```


```
false
```


If you put in bad data, you get MatchingErrors


```julia
section_data_bad = [Float64[1,2,3],
   Float64[1,2],
   Float64[1,3,5],
   Float64[1,3,6]]

@test_throws MatchingError extend(VectSheaf, K, section_data_bad)
@test_throws MatchingError extend(VectSheafMat, K, section_data_bad)
```


```
Test Passed
      Thrown: MatchingError{MatchingFailure}
```


if we disable the checks, VectSheafMat will solve a least squares problem instead of last write wins.


```julia
extend(VectSheafMat, K, section_data_bad, check=false)
```


```
5-element Vector{Float64}:
 3.0
 0.9999999999999998
 2.4999999999999996
 5.0
 6.0
```


Last write wins definition is different.


```julia
extend(VectSheaf, K, section_data_bad, check=false)
```


```
5-element Vector{Float64}:
 3.0
 1.0
 3.0
 5.0
 6.0
```


You can diagnose a matching error from the exception that extend throws.


```julia
try
  extend(VectSheaf, K, section_data_bad)
catch e
  e
end
```


```
MatchingError: Sections don't match on 4 overlaps:
MatchingFailure: Sections don't match on:
	FinFunction([2, 3, 1], 3, 5) and
	FinFunction([2, 3, 4], 3, 5)
	[1.0, 2.0] ◁ [1.0, 2.0, 3.0] but
	[1.0, 3.0] ◁ [1.0, 3.0, 5.0]
MatchingFailure: Sections don't match on:
	FinFunction([2, 3, 1], 3, 5) and
	FinFunction([2, 3, 5], 3, 5)
	[1.0, 2.0] ◁ [1.0, 2.0, 3.0] but
	[1.0, 3.0] ◁ [1.0, 3.0, 6.0]
MatchingFailure: Sections don't match on:
	FinFunction([2, 3], 2, 5) and
	FinFunction([2, 3, 4], 3, 5)
	[1.0, 2.0] ◁ [1.0, 2.0] but
	[1.0, 3.0] ◁ [1.0, 3.0, 5.0]
MatchingFailure: Sections don't match on:
	FinFunction([2, 3], 2, 5) and
	FinFunction([2, 3, 5], 3, 5)
	[1.0, 2.0] ◁ [1.0, 2.0] but
	[1.0, 3.0] ◁ [1.0, 3.0, 6.0]

```


This concludes our discussion of the sheaf API.

