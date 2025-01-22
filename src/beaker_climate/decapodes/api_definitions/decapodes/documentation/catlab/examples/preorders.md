




# Preorders


[![](https://img.shields.io/badge/show-nbviewer-579ACA.svg)](https://nbviewer.jupyter.org/github/AlgebraicJulia/Catlab.jl/blob/gh-pages/dev/generated/sketches/preorders.ipynb)


Many of the ideas in category theory can be viewed as generalizations of preorders or monoids. This sketch shows some features of Catlab through the lens of preorders. You will see examples of defining GATs, Presentations, Syntax, and Functors. These are illustrated with preorders or thin categories, which are particularly simple cases of categories.


```julia
using Core: GeneratedFunctionStub
using Test

using Catlab.Theories, Catlab.CategoricalAlgebra
import Catlab.Theories: compose
```




# Definition of a Preorder formalized as a GAT


The following definitions can be found in the `Catlab.Theories` module.


```julia
""" Theory of *preorders*

Preorders encode the axioms of reflexivity and transitivity as term constructors.
"""
@theory Preorder{El,Leq} begin
  El::TYPE
  Leq(lhs::El, rhs::El)::TYPE
  @op (≤) := Leq

  # Preorder axioms are lifted to term constructors in the GAT.
  reflexive(A::El)::(A≤A) # ∀ A there is a term reflexive(A) which implies A≤A
  transitive(f::(A≤B), g::(B≤C))::(A≤C) ⊣ (A::El, B::El, C::El)

  # Axioms of the GAT are equivalences on terms or simplification rules in the logic
  f == g ⊣ (A::El, B::El, f::(A≤B), g::(A≤B))
  # Read as (f⟹ A≤B ∧ g⟹ A≤B) ⟹ f ≡ g
end
```




# Preorders are Thin Categories


Definition of a thin category


```julia
@theory ThinCategory{Ob,Hom} <: Category{Ob,Hom} begin
  f == g ⊣ (A::Ob, B::Ob, f::Hom(A,B), g::Hom(A,B))
end
```


of course this definition extends the GAT of categories


```julia
@theory Category{Ob,Hom} begin
  # Unicode aliases.
  @op begin
  (→) := Hom
  (⋅) := compose
  end

  """ Object in a category """
  Ob::TYPE

  """ Morphism in a category """
  Hom(dom::Ob,codom::Ob)::TYPE

  id(A::Ob)::(A → A)
  compose(f::(A → B), g::(B → C))::(A → C) ⊣ (A::Ob, B::Ob, C::Ob)

  # Category axioms.
  ((f ⋅ g) ⋅ h == f ⋅ (g ⋅ h)
  ⊣ (A::Ob, B::Ob, C::Ob, D::Ob, f::(A → B), g::(B → C), h::(C → D)))
  f ⋅ id(B) == f ⊣ (A::Ob, B::Ob, f::(A → B))
  id(A) ⋅ f == f ⊣ (A::Ob, B::Ob, f::(A → B))
end
```


Exercise: construct an isomorphism between the theory of thin categories and the theory of preorders. Show that they have the same models.


Once you have a GAT defined using the `@theory` macro, you can define presentations, which are logical syntax for giving examples of the theory. The GAT contains type and term constructors that you can use to write expressions. A presentation uses those expressions to create a specific example of the theory. We define `P` to be a preorder with 3 elements and 2 ≤ relationships.


```julia
@present P(FreeThinCategory) begin
  (X,Y,Z)::Ob
  f::Hom(X,Y)
  g::Hom(Y,Z)
end
```


```
Presentation{Catlab.Theories.ThThinCategory.Meta.T, Symbol}(Catlab.Theories.FreeThinCategory, (Ob = Catlab.Theories.FreeThinCategory.Ob{:generator}[X, Y, Z], Hom = Catlab.Theories.FreeThinCategory.Hom{:generator}[f, g]), Dict(:Z => (:Ob => 3), :f => (:Hom => 1), :X => (:Ob => 1), :Y => (:Ob => 2), :g => (:Hom => 2)), Pair[])
```


another example


```julia
@present Q(FreeThinCategory) begin
  (X,Y,Z)::Ob
  f::Hom(X,Y)
  g::Hom(Y,Z)
  Y′::Ob
  f′::Hom(X,Y′)
  g′::Hom(Y′,Z)
end
```


```
Presentation{Catlab.Theories.ThThinCategory.Meta.T, Symbol}(Catlab.Theories.FreeThinCategory, (Ob = Catlab.Theories.FreeThinCategory.Ob{:generator}[X, Y, Z, Y′], Hom = Catlab.Theories.FreeThinCategory.Hom{:generator}[f, g, f′, g′]), Dict(:Z => (:Ob => 3), :f => (:Hom => 1), :f′ => (:Hom => 3), :X => (:Ob => 1), :Y => (:Ob => 2), :g => (:Hom => 2), :Y′ => (:Ob => 4), :g′ => (:Hom => 4)), Pair[])
```


Exercise: draw the Hasse diagrams for these preorders by hand.




# Composition is transitivity


expressions in the presentation are paths in the Hasse Diagram


```julia
function compose(P::Presentation, vs::Vector{Symbol})
  compose(collect(generator(P, v) for v in vs))
end
```


```
compose (generic function with 76 methods)
```


expressions are represented at expression trees


```julia
ex = compose(P, [:f, :g])
```


```
f⋅g: X → Z
```


the head of an expression is the root of the expression tree


```julia
head(ex)
```


```
:compose
```


the julia type of the expression


```julia
typeof(ex)
```


```
Catlab.Theories.FreeThinCategory.Hom{:compose}
```


the GAT type of the expression


```julia
gat_typeof(ex)
```


```
:Hom
```


the parameters of the GAT Type


```julia
gat_type_args(ex)
```


```
2-element Vector{GATExpr}:
 X
 Z
```


in any thin category there is at most one morphism between any pair of objects. In symbols: ex₁::Hom(X,Y) ∧ ex₂::Hom(X,Y) ⟹ ex₁ == ex₂


```julia
function thinequal(ex₁::FreeThinCategory.Hom, ex₂::FreeThinCategory.Hom)
  dom(ex₁) == dom(ex₂) && codom(ex₁) == codom(ex₂)
end

@test thinequal(ex, compose(P, [:f,:g])⋅id(generator(P,:Z)))
```


```
Test Passed
```


Thinking in terms of preorders, the composite f⋅g::Hom(X,Z) is a proof that X ≤ Z in logical notation you would say f::Hom(X,Y) and g::Hom(Y,Z) ⊢ f⋅g::Hom(X,Z) given a proof that X≤Y and a proof of Y≤Z then ⋅ will create a proof of X≤Z by composing the proofs sequentially like chaining inequalities in math a key aspect of category theory is that you want to work constructively you don't want to know that there exists a composite, you want to hold onto that composite. in programming, the way that you hold onto things is putting data into data structures. While computers can access things by offset or addresses, programmers want to use names so when we prove in P that X≤Z, we name that proof by adding it as a generator


```julia
@present P₂(FreeThinCategory) begin
  (X,Y,Z)::Ob
  f::Hom(X,Y)
  g::Hom(Y,Z)
  h::Hom(X,Z)
end

ex = compose(P₂, [:f, :g])
```


```
f⋅g: X → Z
```


Now that we have a name for h, we can see that thinequal knows that f⋅g == h because according to the definition of a thin category, any two morphisms with the same domain and codomain are equal.


```julia
@test thinequal(ex, generator(P₂, :h))
```


```
Test Passed
```


There is an imperative interface to manipulating presentations by mutating them for this purpose


```julia
P₂′ = copy(P)
add_generator!(P₂′, Hom(:h, P[:X], P[:Z]))
generators(P₂′)
```


```
6-element Vector{Any}:
 X
 Y
 Z
 f: X → Y
 g: Y → Z
 h: X → Z
```


We could avoid this naming the homs situation by giving all the homs the same name however, then when you tried to write down a morphism, you wouldn't be able to refer to a specific one by name, because they are all named ≤.


```julia
@present R(FreeThinCategory) begin
  (x,y,z)::Ob
  (≤)::Hom(x,y)
end
generators(R)
```


```
4-element Vector{Any}:
 x
 y
 z
 ≤: x → y
```


Catlab won't let you make a presentation where the homs have the same exact name. So, this will error:


```julia
@present Q(FreeThinCategory) begin
  (x,y,z)::Ob
  (≤)::Hom(x,y)
  (≤)::Hom(y,z)
  (≤)::Hom(x,z)
end
```


However, you can omit the names for homs with the following syntax, which is useful for thin categories.


```julia
@present Q(FreeThinCategory) begin
  (x,y,z)::Ob
  ::Hom(x,y)
  ::Hom(y,z)
  ::Hom(x,z)
end
```


In a thin category, all the homs with the same domain and codomain are the same, so why don't we name them by their the domain and codomain and then use the property that any two homs with the same name are the same to encode the thinness. This is what the Hasse diagram representation does for us. The edges in the diagram are encoding the presentation data into a combinatorial object that we can visualize. There are many reasons to encode a logical structure into a combinatorial strucuture, one is that we generally have ways of drawing combinatorial objects that convey their saliant structure and enable visual reasoning. Another is algorithms, isomorphism between the combinatorial representations provide some of the isomorphisms between the logical structures. in this case, a graph homomorphism between Hasse Diagrams construct isomorphisms between the preorders they present. The converse is not true since there can be many Graphs that present the same preorder.




# Monotone Maps


a generator is in the set of homs if it is in the list of generators


```julia
in_homs(f::FreeThinCategory.Hom{:generator}, C::FinCat) =
  f in hom_generators(C)
```


```
in_homs (generic function with 1 method)
```


a composite hom is in the list set of homs if all of its components are.


```julia
in_homs(f::FreeThinCategory.Hom{:compose}, C::FinCat) =
  all(fᵢ->in_homs(fᵢ, C), args(f))
```


```
in_homs (generic function with 2 methods)
```


we can check if a map is functorial, which is called monotone for preorders.


1. make sure all the objects in the domain are sent to objects in the codomain
2. make sure all the homs are sent to homs in the codomain
3. check that the domains and codomainss of the homs match


```julia
function is_functorial(F::FinFunctor)
  pₒ = map(ob_generators(dom(F))) do X
    F(X) in ob_generators(codom(F))
  end |> all

  pₕ = map(hom_generators(dom(F))) do f
    in_homs(F(f), codom(F))
  end |> all

  pᵩ = map(hom_generators(dom(F))) do f
    FX = F(dom(f))
    FY = F(codom(f))
    Ff = F(f)
    dom(Ff) == FX && codom(Ff) == FY
  end |> all
  return pₒ && pₕ && pᵩ
end

@present Q(FreeThinCategory) begin
  (a,b,c,d)::Ob
  ab::Hom(a,b)
  bc::Hom(b,c)
  cd::Hom(c,d)
end
generators(Q)

Fₒ = Dict(:X=>:a, :Y=>:b, :Z=>:c)
Fₕ = Dict(:f=>:ab, :g=>:bc)
F = FinFunctor(Fₒ, Fₕ, P, Q)
@test is_functorial(F)

Fₒ = Dict(:X=>:a, :Y=>:b, :Z=>:d)
Fₕ = Dict(:f=>:ab, :g=>[:bc, :cd])
F = FinFunctor(Fₒ, Fₕ, P, Q)
@test is_functorial(F)


Fₒ = Dict(:X=>:a, :Y=>:b, :Z=>:c)
Fₕ = Dict(:f=>:ab, :g=>[:bc, :cd])
F = FinFunctor(Fₒ, Fₕ, P, Q)
@test !is_functorial(F)
```


```
Test Passed
```


Monotone maps are functors for thin categories. One of the benefits of category theory is that we find abstractions that work in multiple domains. The abstraction of preserving the domains and codomains of morphisms is a key abstraction that we can use to define many notions in mathematics.

