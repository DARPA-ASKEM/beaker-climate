




# Symmetric Monoidal Categories


[![](https://img.shields.io/badge/show-nbviewer-579ACA.svg)](https://nbviewer.jupyter.org/github/AlgebraicJulia/Catlab.jl/blob/gh-pages/dev/generated/sketches/smc.ipynb)


This vignette supports section 4.4.3 of Seven Sketches in Compositionality, which introduces the definition of symmetric monoidal categories (SMCs). SMCs are a core concept in applied category theory and are a workhorse of Catlab's utility in computing applications. We will discuss the definition as a GAT, see examples of working with formulas, and conversions to wiring diagrams (sometimes called string diagrams). SMCs are useful for modeling mathematical structures like programs or processes where the objects represent data or things and the morphisms represent processes that happen to those things.


```julia
using GATlab, Catlab.Theories
using Catlab.CategoricalAlgebra
using Catlab.WiringDiagrams
using Catlab.Programs
using Catlab.Graphics
using Catlab.Graphics: Graphviz

draw(d::WiringDiagram) = to_graphviz(d,
  orientation=LeftToRight,
  labels=true, label_attr=:xlabel,
  node_attrs=Graphviz.Attributes(
    :fontname => "Courier",
  ),
  edge_attrs=Graphviz.Attributes(
    :fontname => "Courier",
  )
)
```


```
draw (generic function with 1 method)
```




## Definition


Let 𝒞 be a category, then a strict symmetric monoidal structure on 𝒞 has as data:


1. An object I called the monoidal unit
2. A functor ⊗: 𝒞×𝒞 → 𝒞 called the monoidal product.
3. A natural isomorphism σᵃᵇ: A⊗B → B⊗A


It has as axioms:


1. Left identity) I⊗C = C for all objects C in 𝒞
2. Right identity) C⊗I = C for all objects C in 𝒞
3. Associativity) (A⊗B)⊗C = A⊗(B⊗C) for all objects A,B,C in 𝒞
4. Involutivity) σ(σ(A,B)) = id(A⊗B)


In a category, you have a composition operation that captures the sequential kind of composition. For example in Set, you compose two functions f⋅g by first applying f and then applying g. In monoidal categories, you also have the parallel composition ⊗ which you can think of as representing the simultaneous exectution of two processes. We are familiar with the cartesian product in Set which takes two sets and forms the cartesian product. The cartesian product acts on functions in a similar way, f×g is the function that takes a tuple (x:dom(f),y:dom(g)) and applies them *in parallel* and returns (f(x), g(y)):(codom(f)×codom(g)). The axioms of an SMC require that these two operations work together. The Seven Sketches book suppresses an interesting axiom called the *interchange law* for brevity, but it is worth calling some attention to it. In order for the sequential and parallel composition operators to capture our intuition, we need to assert that for any functions with compatible domains we can interchange parallel and sequential operators. Formally, ((f ⊗ g) ⋅ (h ⊗ k) == (f ⋅ h) ⊗ (g ⋅ k) where (A::Ob, B::Ob, C::Ob, X::Ob, Y::Ob, Z::Ob, f::(A → B), h::(B → C), g::(X → Y), k::(Y → Z))). This axiom says that doing f and g in parallel and then h and k in parallel is the same as doing (f then h) and (g then k) in parallel. When using SMCs to model processes, this axiom is critical to making sure that scheduling those processes is coherent.


If the SMC is not strict, then the equations are replaced by natural isomorphisms. The choice of natural isomorphisms then becomes part of the data of the SMC. With MacLane's coherence theorem for SMCs mathematicians can think about strict SMCs and not really worry too much about the natural isomorphisms. As programmers, those chickens come home to roost and implementing an SMC requires making some choices about about how to do that strictification.


The Catlab definitions of SMC are repeated here for convenience. Catlab allows you to implement mathematical definitions in the language of Generalized Algebraic Theories (GATs), which are a good fit for the kind of natural language definitions that mathematicians will write. Because Catlab does relatively little type inference, the GAT version of a definition can be more verbose than you would get in natural language. For example, we have to be careful about spelling out the object for an identity morphism `id(A):A → A`. The notation  `@theory MonoidalCategory{Ob,Hom} <: Category{Ob,Hom}` says that a Monoidal Category is a type of Category with additional components and axioms. Catlab has only rudimentary support for Monoidal Categories that are not Symmetric Monoidal Categories. But we separate out the definitions for completeness.


```julia
@theory MonoidalCategory{Ob,Hom} <: Category{Ob,Hom} begin
  otimes(A::Ob, B::Ob)::Ob
  otimes(f::(A → B), g::(C → D))::((A ⊗ C) → (B ⊗ D)) ⊣
    (A::Ob, B::Ob, C::Ob, D::Ob)
  @op (⊗) := otimes
  munit()::Ob
  # Monoid axioms.
  #
  # The last two axioms are the naturality equations associated with the left
  # and right unitors, in the strict case where they are identities.
  (A ⊗ B) ⊗ C == A ⊗ (B ⊗ C) ⊣ (A::Ob, B::Ob, C::Ob)
  munit() ⊗ A == A ⊣ (A::Ob)
  A ⊗ munit() == A ⊣ (A::Ob)
  (f ⊗ g) ⊗ h == f ⊗ (g ⊗ h) ⊣ (A::Ob, B::Ob, C::Ob, X::Ob, Y::Ob, Z::Ob,
                                f::(A → X), g::(B → Y), h::(C → Z))
  id(munit()) ⊗ f == f ⊣ (A::Ob, B::Ob, f::(A → B))
  f ⊗ id(munit()) == f ⊣ (A::Ob, B::Ob, f::(A → B))
  # Functorality axioms.
  ((f ⊗ g) ⋅ (h ⊗ k) == (f ⋅ h) ⊗ (g ⋅ k)
    ⊣ (A::Ob, B::Ob, C::Ob, X::Ob, Y::Ob, Z::Ob,
       f::(A → B), h::(B → C), g::(X → Y), k::(Y → Z)))
  id(A ⊗ B) == id(A) ⊗ id(B) ⊣ (A::Ob, B::Ob)
end
```


To the definition of a monoidal category, we need to add the symmetry component. Catlab calls the swap morphism a braid, because that is how you visualize it in wiring diagrams, but we stick with the conventional σ unicode name. The macro `@op` tells Catlab that you want to use a unicode operator as an alias for you term constructor. If you are familiar with type theory, you might be wondering why we write the context after the terms. This is because human brains are pretty good at type inference based on notational convention and we want to mimic the English idiom "f⋅g, where f:A→B and g:B→C are functions".


```julia
@theory SymmetricMonoidalCategory{Ob,Hom} <: MonoidalCategory{Ob,Hom} begin
  braid(A::Ob, B::Ob)::((A ⊗ B) → (B ⊗ A))
  @op (σ) := braid
  # Involutivity axiom.
  σ(A,B) ⋅ σ(B,A) == id(A ⊗ B) ⊣ (A::Ob, B::Ob)
  # Coherence axioms.
  #
  # Note: The last two axioms are deducible from the first two axioms together
  # with the naturality equations for the left/right unitors. We record them for
  # the sake of clarity and uniformity.
  σ(A,B⊗C) == (σ(A,B) ⊗ id(C)) ⋅ (id(B) ⊗ σ(A,C)) ⊣ (A::Ob, B::Ob, C::Ob)
  σ(A⊗B,C) == (id(A) ⊗ σ(B,C)) ⋅ (σ(A,C) ⊗ id(B)) ⊣ (A::Ob, B::Ob, C::Ob)
  σ(A,munit()) == id(A) ⊣ (A::Ob)
  σ(munit(),A) == id(A) ⊣ (A::Ob)
  # Naturality axiom.
  (f ⊗ g) ⋅ σ(B,D) == σ(A,C) ⋅ (g ⊗ f) ⊣ (A::Ob, B::Ob, C::Ob, D::Ob,
                                          f::(A → B), g::(C → D))
end
```




## Presentations


Just like how a preorder can be presented with Hasse Diagram or a free category can be presented by a Graph, SMCs can be presented syntactically or combinatorially. We first start with the syntactic presentation using `@present`.


```julia
@present Cooking(FreeSymmetricMonoidalCategory) begin
  (WholeEgg, RawEgg, Shell, Egg, Pan, Cheese, Scramble)::Ob
  crack::Hom(WholeEgg, RawEgg⊗Shell)
  fry::Hom(RawEgg⊗Pan, Egg⊗Pan)
  scramble::Hom(RawEgg⊗Cheese⊗Pan, Scramble⊗Pan)
end
generators(Cooking)
```


```
10-element Vector{Any}:
 WholeEgg
 RawEgg
 Shell
 Egg
 Pan
 Cheese
 Scramble
 crack: WholeEgg → RawEgg⊗Shell
 fry: RawEgg⊗Pan → Egg⊗Pan
 scramble: RawEgg⊗Cheese⊗Pan → Scramble⊗Pan
```


One interpretation of an SMC is that the objects are resources and the Homs are processes the domain of the Hom is the list of resources that you need to perform the process and the codomain is the list of resources that the process produces. You can think of the SMC presentation as a namespace containing all the terms in the SMC.


The objects and morphisms are accessible by name


```julia
Cooking[:Egg]
Cooking[:fry]
```


```
fry: RawEgg⊗Pan → Egg⊗Pan
```


Then you can make complex terms using the unicode operators


```julia
((Cooking[:crack]⋅σ(Cooking[:RawEgg], Cooking[:Shell])) ⊗id(Cooking[:Pan])) ⋅ (id(Cooking[:Shell])⊗Cooking[:fry])
```


```
((crack⋅(RawEggσShell))⊗id{Pan})⋅(id{Shell}⊗fry): WholeEgg⊗Pan → Shell⊗Egg⊗Pan
```


Notice that Catlab will display the expected domain and codomain.


This is called point-free notation an it is very popular in the functional programming literature where it is used to mean implicit universal quantification over the function arguments. You can think of a morphism like a function that takes an element of each domain object as input and produces an element of each codomain object as output. Not all SMCs have interpretations as functions over sets, but just like groups can be viewed as a generalization of the symmetries of geometric shapes, SMCs can be viewed as a generalization of multivariate functions.


These presentations are very syntactic objects and expose an API for manipulating expressions.


```julia
for g in generators(Cooking)
  "$g is a $(gat_typeof(g)) with arguments $(gat_type_args(g))"
end
```


The `gat_typeof` function computes the algebraic type of a term by analogy to `Base.typeof` which computes the Julia type of a value.


```julia
homs = filter(generators(Cooking)) do g
  gat_typeof(g) == :Hom
end
```


```
3-element Vector{Any}:
 crack: WholeEgg → RawEgg⊗Shell
 fry: RawEgg⊗Pan → Egg⊗Pan
 scramble: RawEgg⊗Cheese⊗Pan → Scramble⊗Pan
```


When the term is a Hom, you can get the domain and codomain of the morphism with the `dom` and `codom` functions.


```julia
map(homs) do f
  "$f: $(dom(f)) → $(codom(f))"
end
```


```
3-element Vector{String}:
 "crack: WholeEgg → otimes(RawEgg,Shell)"
 "fry: otimes(RawEgg,Pan) → otimes(Egg,Pan)"
 "scramble: otimes(RawEgg,Cheese,Pan) → otimes(Scramble,Pan)"
```


The terms in a `FreeSymmetricMonoidalCategory` are trees that you can navigate with `head` and `args`. The `head` of an expression is the term constructor that created it. For SMCs, this can be `:generator`, `:otimes`, `:compose`, `:id`, or `:braid`. Then `args` will give you the list of arguments to the term constructor. For terms of type Object, this will just be the list of objects that went into constructing the object. For example A⊗B⊗C will have as its head `:otimes` and as the args `[A,B,C]`. Note that the head is a symbol, but the args are objects. For a term of type `Hom`, you have the same structure, but for Homs with the head `:generator`, you get the name of the morphism as a symbol as the first argument.


We can look at the head and args of object expressions.


```julia
headargs(x) = (head(x),args(x))
σ(Cooking[:Egg], Cooking[:Pan]) |> headargs
```


```
(:braid, Catlab.Theories.FreeSymmetricMonoidalCategory.Ob{:generator}[Egg, Pan])
```


And, morphsims


```julia
headargs(Cooking[:crack]⊗Cooking[:fry])
```


```
(:otimes, Catlab.Theories.FreeSymmetricMonoidalCategory.Hom{:generator}[crack, fry])
```


The base case is generators


```julia
headargs(Cooking[:Egg])
```


```
(:generator, [:Egg])
```


And, morphisms


```julia
headargs(Cooking[:crack])
```


```
(:generator, Any[:crack, WholeEgg, otimes(RawEgg,Shell)])
```


For a more complete introspection of the expression trees, you can call `dump(ex)` which will print a very verbose representation of the entire expression tree.


In order to compose morphisms sequentially, you have to make sure that the domains match up. In a typical SMC expression this can require padding with the identity morphism and braiding monoidal products into the right order.


```julia
compose(Cooking[:crack]⊗id(Cooking[:Pan]),
        (id(Cooking[:RawEgg])⊗ σ(Cooking[:Shell], Cooking[:Pan])),
        (Cooking[:fry]⊗id(Cooking[:Shell])))
```


```
(crack⊗id{Pan})⋅(id{RawEgg}⊗(ShellσPan))⋅(fry⊗id{Shell}): WholeEgg⊗Pan → Egg⊗Pan⊗Shell
```


At some point, prefix notation is more scalable than infix notation, so you might write this as a LISP programmer would.


```julia
compose(
  otimes(Cooking[:crack],
         id(Cooking[:Pan])),
  otimes(id(Cooking[:RawEgg]),
         σ(Cooking[:Shell], Cooking[:Pan])),
  otimes(Cooking[:fry],
         id(Cooking[:Shell])))
```


```
(crack⊗id{Pan})⋅(id{RawEgg}⊗(ShellσPan))⋅(fry⊗id{Shell}): WholeEgg⊗Pan → Egg⊗Pan⊗Shell
```


You can view this padding as requiring explicit instructions to do noting with all the objects you aren't using. In this example, we have to tell our chef


1. Crack the egg and do nothing with the pan.
2. Do nothing with the egg and swap the shell with the pan.
3. Fry the egg and do nothing with the shell.


Obviously, this is a very tedious way to write recipes. You need to have some syntactic sugar for all this padding and swapping.




## The Program Macro


The syntactic API above is useful for manipulating terms in an arbitrary GAT and is the formal language of Catlab for representing and manipulating algebraic structures. However, when we want to work with big expressions in an SMC, the tree structure inherent to formulas is too verbose, and we want to move to a port-graph structure called `DirectedWiringDiagrams`. This gives us the benefits of combinatorial data structures like graphs with the right expressional power for representing the morphisms in an SMC.


```julia
recipe = @program Cooking (e::WholeEgg, p::Pan) begin
  e′, shell = crack(e)
  return shell, fry(e′, p)
end
draw(recipe)
```

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.43.0 (0)
 -->
<!-- Title: G Pages: 1 -->
<svg width="259pt" height="116pt"
 viewBox="0.00 0.00 259.13 116.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 112)">
<title>G</title>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-112 255.13,-112 255.13,4 -4,4"/>
<!-- n0in1 -->
<!-- n0in2 -->
<!-- n0in1&#45;&gt;n0in2 -->
<!-- n1 -->
<!-- crack -->
<g id="n1" class="node">
<title>n1</title>
<polygon fill="none" stroke="black" points="85.1,-58 85.1,-106 137.1,-106 137.1,-58 85.1,-58"/>
<text text-anchor="start" x="90.1" y="-78.3" font-family="Courier,monospace" font-size="14.00">crack</text>
</g>
<!-- n0in1&#45;&gt;n1 -->
<!-- WholeEgg -->
<g id="e1" class="edge">
<title>n0in1:e&#45;&gt;n1:w</title>
<path fill="none" stroke="black" d="M49.1,-79C63.28,-79 67.97,-81.34 79.92,-81.89"/>
<polygon fill="black" stroke="black" points="80.06,-83.64 85.1,-82 80.14,-80.14 80.06,-83.64"/>
<text text-anchor="middle" x="33.5" y="-84.28" font-family="Courier,monospace" font-size="14.00">WholeEgg</text>
</g>
<!-- n2 -->
<!-- fry -->
<g id="n2" class="node">
<title>n2</title>
<polygon fill="none" stroke="black" points="173.6,-18 173.6,-66 208.6,-66 208.6,-18 173.6,-18"/>
<text text-anchor="start" x="178.6" y="-38.3" font-family="Courier,monospace" font-size="14.00">fry</text>
</g>
<!-- n0in2&#45;&gt;n2 -->
<!-- Pan -->
<g id="e2" class="edge">
<title>n0in2:e&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M49.1,-35C102.53,-35 117.05,-30.31 168.05,-30.01"/>
<polygon fill="black" stroke="black" points="168.11,-31.76 173.1,-30 168.1,-28.26 168.11,-31.76"/>
<text text-anchor="middle" x="98.55" y="-21.3" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n0out1 -->
<!-- n0out2 -->
<!-- n0out1&#45;&gt;n0out2 -->
<!-- n0out3 -->
<!-- n0out2&#45;&gt;n0out3 -->
<!-- n1&#45;&gt;n0out1 -->
<!-- Shell -->
<g id="e4" class="edge">
<title>n1:e&#45;&gt;n0out1:w</title>
<path fill="none" stroke="black" d="M137.1,-70C184.32,-70 194.47,-94.2 239.08,-95.91"/>
<polygon fill="black" stroke="black" points="239.07,-97.66 244.1,-96 239.14,-94.16 239.07,-97.66"/>
<text text-anchor="middle" x="211.71" y="-71.85" font-family="Courier,monospace" font-size="14.00">Shell</text>
</g>
<!-- n1&#45;&gt;n2 -->
<!-- RawEgg -->
<g id="e3" class="edge">
<title>n1:e&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M137.1,-94C159.15,-94 150.82,-60.01 168.12,-54.69"/>
<polygon fill="black" stroke="black" points="168.39,-56.42 173.1,-54 167.91,-52.96 168.39,-56.42"/>
<text text-anchor="middle" x="180.18" y="-77.55" font-family="Courier,monospace" font-size="14.00">RawEgg</text>
</g>
<!-- n2&#45;&gt;n0out2 -->
<!-- Egg -->
<g id="e5" class="edge">
<title>n2:e&#45;&gt;n0out2:w</title>
<path fill="none" stroke="black" d="M208.1,-54C222.23,-54 227,-54 238.93,-54"/>
<polygon fill="black" stroke="black" points="239.1,-55.75 244.1,-54 239.1,-52.25 239.1,-55.75"/>
<text text-anchor="middle" x="238.5" y="-42.8" font-family="Courier,monospace" font-size="14.00">Egg</text>
</g>
<!-- n2&#45;&gt;n0out3 -->
<!-- Pan -->
<g id="e6" class="edge">
<title>n2:e&#45;&gt;n0out3:w</title>
<path fill="none" stroke="black" d="M208.1,-30C224.03,-30 225.95,-15.72 238.82,-12.6"/>
<polygon fill="black" stroke="black" points="239.33,-14.3 244.1,-12 238.94,-10.82 239.33,-14.3"/>
<text text-anchor="middle" x="238.63" y="-24.77" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
</g>
</svg>


Catlab gives you the tools for drawing wiring diagrams. Visualization of wiring diagrams is the oldest part of Catlab and the original motivation for its development. The `@program` macro allows you to define wiring diagrams using a syntax that feels like Julia code.


The input wires are declared as *arguments* to the program, and the output wires are declared as *returns* from the function. Variables that are not consumed or by another function or returned by the program are automatically dropped.


```julia
recipe = @program Cooking (e::WholeEgg, p::Pan) begin
  e′, shell = crack(e)
  return fry(e′, p)
end
draw(recipe)
```

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.43.0 (0)
 -->
<!-- Title: G Pages: 1 -->
<svg width="259pt" height="91pt"
 viewBox="0.00 0.00 259.00 91.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 87)">
<title>G</title>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-87 255,-87 255,4 -4,4"/>
<!-- n0in1 -->
<!-- n0in2 -->
<!-- n0in1&#45;&gt;n0in2 -->
<!-- n1 -->
<!-- crack -->
<g id="n1" class="node">
<title>n1</title>
<polygon fill="none" stroke="black" points="85.1,-35 85.1,-83 137.1,-83 137.1,-35 85.1,-35"/>
<text text-anchor="start" x="90.1" y="-55.3" font-family="Courier,monospace" font-size="14.00">crack</text>
</g>
<!-- n0in1&#45;&gt;n1 -->
<!-- WholeEgg -->
<g id="e1" class="edge">
<title>n0in1:e&#45;&gt;n1:w</title>
<path fill="none" stroke="black" d="M49.1,-56C63.28,-56 67.97,-58.34 79.92,-58.89"/>
<polygon fill="black" stroke="black" points="80.06,-60.64 85.1,-59 80.14,-57.14 80.06,-60.64"/>
<text text-anchor="middle" x="33.5" y="-61.28" font-family="Courier,monospace" font-size="14.00">WholeEgg</text>
</g>
<!-- n2 -->
<!-- fry -->
<g id="n2" class="node">
<title>n2</title>
<polygon fill="none" stroke="black" points="173.6,-15 173.6,-63 208.6,-63 208.6,-15 173.6,-15"/>
<text text-anchor="start" x="178.6" y="-35.3" font-family="Courier,monospace" font-size="14.00">fry</text>
</g>
<!-- n0in2&#45;&gt;n2 -->
<!-- Pan -->
<g id="e2" class="edge">
<title>n0in2:e&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M49.1,-12C102.88,-12 116.74,-26.08 168.02,-26.96"/>
<polygon fill="black" stroke="black" points="168.09,-28.71 173.1,-27 168.12,-25.21 168.09,-28.71"/>
<text text-anchor="middle" x="98.55" y="-8.29" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n0out1 -->
<!-- n0out2 -->
<!-- n0out1&#45;&gt;n0out2 -->
<!-- n1&#45;&gt;n2 -->
<!-- RawEgg -->
<g id="e3" class="edge">
<title>n1:e&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M137.1,-71C153.55,-71 154.73,-54.86 168.07,-51.58"/>
<polygon fill="black" stroke="black" points="168.33,-53.31 173.1,-51 167.94,-49.83 168.33,-53.31"/>
<text text-anchor="middle" x="179.87" y="-65.06" font-family="Courier,monospace" font-size="14.00">RawEgg</text>
</g>
<!-- n2&#45;&gt;n0out1 -->
<!-- Egg -->
<g id="e4" class="edge">
<title>n2:e&#45;&gt;n0out1:w</title>
<path fill="none" stroke="black" d="M208.1,-51C222.66,-51 226.72,-58.01 238.82,-59.66"/>
<polygon fill="black" stroke="black" points="239,-61.42 244.1,-60 239.23,-57.93 239,-61.42"/>
<text text-anchor="middle" x="238.5" y="-44.25" font-family="Courier,monospace" font-size="14.00">Egg</text>
</g>
<!-- n2&#45;&gt;n0out2 -->
<!-- Pan -->
<g id="e5" class="edge">
<title>n2:e&#45;&gt;n0out2:w</title>
<path fill="none" stroke="black" d="M208.1,-27C222.66,-27 226.72,-19.99 238.82,-18.34"/>
<polygon fill="black" stroke="black" points="239.23,-20.07 244.1,-18 239,-16.58 239.23,-20.07"/>
<text text-anchor="middle" x="238.5" y="-26.35" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
</g>
</svg>


You can copy a value by using it more than once. This is visualized as a wire being split into two wires. Square brackets let you assert equality again. For material goods, you might not want to allow this merging and splitting.


```julia
recipe = @program Cooking (e₁::WholeEgg, e₂::WholeEgg, p::Pan) begin
  e, shell = crack(e₁)
  r₁, p₁ = fry(e, p)
  e, shell = crack(e₂)
  r₂, p₂ = fry(e, p)
  return r₁, r₂, [p₁,p₂]
end

draw(recipe)
```

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.43.0 (0)
 -->
<!-- Title: G Pages: 1 -->
<svg width="259pt" height="182pt"
 viewBox="0.00 0.00 259.10 182.30" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 178.3)">
<title>G</title>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-178.3 255.1,-178.3 255.1,4 -4,4"/>
<!-- n0in1 -->
<!-- n0in2 -->
<!-- n0in1&#45;&gt;n0in2 -->
<!-- n1 -->
<!-- crack -->
<g id="n1" class="node">
<title>n1</title>
<polygon fill="none" stroke="black" points="85.1,-126.3 85.1,-174.3 137.1,-174.3 137.1,-126.3 85.1,-126.3"/>
<text text-anchor="start" x="90.1" y="-146.6" font-family="Courier,monospace" font-size="14.00">crack</text>
</g>
<!-- n0in1&#45;&gt;n1 -->
<!-- WholeEgg -->
<g id="e1" class="edge">
<title>n0in1:e&#45;&gt;n1:w</title>
<path fill="none" stroke="black" d="M49.1,-138.3C64.12,-138.3 67.57,-147.82 80.05,-149.9"/>
<polygon fill="black" stroke="black" points="79.98,-151.65 85.1,-150.3 80.26,-148.16 79.98,-151.65"/>
<text text-anchor="middle" x="33.63" y="-148.12" font-family="Courier,monospace" font-size="14.00">WholeEgg</text>
</g>
<!-- n0in3 -->
<!-- n0in2&#45;&gt;n0in3 -->
<!-- n3 -->
<!-- crack -->
<g id="n3" class="node">
<title>n3</title>
<polygon fill="none" stroke="black" points="85.1,-60.3 85.1,-108.3 137.1,-108.3 137.1,-60.3 85.1,-60.3"/>
<text text-anchor="start" x="90.1" y="-80.6" font-family="Courier,monospace" font-size="14.00">crack</text>
</g>
<!-- n0in2&#45;&gt;n3 -->
<!-- WholeEgg -->
<g id="e3" class="edge">
<title>n0in2:e&#45;&gt;n3:w</title>
<path fill="none" stroke="black" d="M49.1,-84.3C63.23,-84.3 68,-84.3 79.93,-84.3"/>
<polygon fill="black" stroke="black" points="80.1,-86.05 85.1,-84.3 80.1,-82.55 80.1,-86.05"/>
<text text-anchor="middle" x="33.5" y="-73.1" font-family="Courier,monospace" font-size="14.00">WholeEgg</text>
</g>
<!-- n2 -->
<!-- fry -->
<g id="n2" class="node">
<title>n2</title>
<polygon fill="none" stroke="black" points="173.6,-87.3 173.6,-135.3 208.6,-135.3 208.6,-87.3 173.6,-87.3"/>
<text text-anchor="start" x="178.6" y="-107.6" font-family="Courier,monospace" font-size="14.00">fry</text>
</g>
<!-- n0in3&#45;&gt;n2 -->
<!-- Pan -->
<g id="e2" class="edge">
<title>n0in3:e&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M49.1,-32.3C89.11,-32.3 103.42,-29.71 137.1,-51.3 157.98,-64.68 148.1,-94.67 168.04,-98.82"/>
<polygon fill="black" stroke="black" points="167.96,-100.57 173.1,-99.3 168.29,-97.08 167.96,-100.57"/>
<text text-anchor="middle" x="124.61" y="-40.1" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n4 -->
<!-- fry -->
<g id="n4" class="node">
<title>n4</title>
<polygon fill="none" stroke="black" points="173.6,-21.3 173.6,-69.3 208.6,-69.3 208.6,-21.3 173.6,-21.3"/>
<text text-anchor="start" x="178.6" y="-41.6" font-family="Courier,monospace" font-size="14.00">fry</text>
</g>
<!-- n0in3&#45;&gt;n4 -->
<!-- Pan -->
<g id="e4" class="edge">
<title>n0in3:e&#45;&gt;n4:w</title>
<path fill="none" stroke="black" d="M49.1,-32.3C66.27,-32.3 68.23,-21.46 85.1,-18.3 107.82,-14.04 114.44,-13.77 137.1,-18.3 152.24,-21.33 155.22,-30.86 167.94,-32.91"/>
<polygon fill="black" stroke="black" points="167.98,-34.67 173.1,-33.3 168.25,-31.18 167.98,-34.67"/>
<text text-anchor="middle" x="98.62" y="-3.8" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n0out1 -->
<!-- n0out2 -->
<!-- n0out1&#45;&gt;n0out2 -->
<!-- n0out3 -->
<!-- n0out2&#45;&gt;n0out3 -->
<!-- n1&#45;&gt;n2 -->
<!-- RawEgg -->
<g id="e5" class="edge">
<title>n1:e&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M137.1,-162.3C158.66,-162.3 151.18,-129.71 167.75,-124.11"/>
<polygon fill="black" stroke="black" points="168.42,-125.78 173.1,-123.3 167.9,-122.32 168.42,-125.78"/>
<text text-anchor="middle" x="180.1" y="-146.6" font-family="Courier,monospace" font-size="14.00">RawEgg</text>
</g>
<!-- n2&#45;&gt;n0out1 -->
<!-- Egg -->
<g id="e7" class="edge">
<title>n2:e&#45;&gt;n0out1:w</title>
<path fill="none" stroke="black" d="M208.1,-123.3C222.28,-123.3 226.97,-120.96 238.92,-120.41"/>
<polygon fill="black" stroke="black" points="239.14,-122.16 244.1,-120.3 239.07,-118.66 239.14,-122.16"/>
<text text-anchor="middle" x="238.5" y="-125.61" font-family="Courier,monospace" font-size="14.00">Egg</text>
</g>
<!-- n2&#45;&gt;n0out3 -->
<!-- Pan -->
<g id="e8" class="edge">
<title>n2:e&#45;&gt;n0out3:w</title>
<path fill="none" stroke="black" d="M208.1,-99.3C238.83,-99.3 214.68,-42.58 238.98,-35.93"/>
<polygon fill="black" stroke="black" points="239.36,-37.65 244.1,-35.3 238.93,-34.17 239.36,-37.65"/>
<text text-anchor="middle" x="238.6" y="-56.09" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n3&#45;&gt;n4 -->
<!-- RawEgg -->
<g id="e6" class="edge">
<title>n3:e&#45;&gt;n4:w</title>
<path fill="none" stroke="black" d="M137.1,-96.3C158.66,-96.3 151.18,-63.71 167.75,-58.11"/>
<polygon fill="black" stroke="black" points="168.42,-59.78 173.1,-57.3 167.9,-56.32 168.42,-59.78"/>
<text text-anchor="middle" x="180.1" y="-76.85" font-family="Courier,monospace" font-size="14.00">RawEgg</text>
</g>
<!-- n4&#45;&gt;n0out2 -->
<!-- Egg -->
<g id="e9" class="edge">
<title>n4:e&#45;&gt;n0out2:w</title>
<path fill="none" stroke="black" d="M208.1,-57.3C224.55,-57.3 225.73,-73.44 239.07,-76.72"/>
<polygon fill="black" stroke="black" points="238.94,-78.47 244.1,-77.3 239.33,-74.99 238.94,-78.47"/>
<text text-anchor="middle" x="238.37" y="-70.84" font-family="Courier,monospace" font-size="14.00">Egg</text>
</g>
<!-- n4&#45;&gt;n0out3 -->
<!-- Pan -->
<g id="e10" class="edge">
<title>n4:e&#45;&gt;n0out3:w</title>
<path fill="none" stroke="black" d="M208.1,-33.3C222.25,-33.3 226.99,-34.86 238.93,-35.22"/>
<polygon fill="black" stroke="black" points="239.08,-36.97 244.1,-35.3 239.13,-33.47 239.08,-36.97"/>
<text text-anchor="middle" x="238.5" y="-23.09" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
</g>
</svg>


You can visualize the copy and delete morphisms explicitly with the `add_junctions` function. The dots with one wire input and multiple outputs are copying values and dots with no wires out are deletions (discarding values). Not all instances of a `SymmetricMonoidalCategory` support copy and delete, for example, in manufacturing you can't duplicate a resource, and in chemistry you can't discard species. Catlab would enforce that when you tried to interpret the wiring diagram in a specific SMC.


```julia
draw(add_junctions(recipe))
```

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.43.0 (0)
 -->
<!-- Title: G Pages: 1 -->
<svg width="299pt" height="166pt"
 viewBox="0.00 0.00 299.40 166.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 162)">
<title>G</title>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-162 295.4,-162 295.4,4 -4,4"/>
<!-- n0in1 -->
<!-- n0in2 -->
<!-- n0in1&#45;&gt;n0in2 -->
<!-- n1 -->
<!-- crack -->
<g id="n1" class="node">
<title>n1</title>
<polygon fill="none" stroke="black" points="85.1,-102 85.1,-150 137.1,-150 137.1,-102 85.1,-102"/>
<text text-anchor="start" x="90.1" y="-122.3" font-family="Courier,monospace" font-size="14.00">crack</text>
</g>
<!-- n0in1&#45;&gt;n1 -->
<!-- WholeEgg -->
<g id="e1" class="edge">
<title>n0in1:e&#45;&gt;n1:w</title>
<path fill="none" stroke="black" d="M49.1,-126C63.23,-126 68,-126 79.93,-126"/>
<polygon fill="black" stroke="black" points="80.1,-127.75 85.1,-126 80.1,-124.25 80.1,-127.75"/>
<text text-anchor="middle" x="33.5" y="-114.8" font-family="Courier,monospace" font-size="14.00">WholeEgg</text>
</g>
<!-- n0in3 -->
<!-- n0in2&#45;&gt;n0in3 -->
<!-- n3 -->
<!-- crack -->
<g id="n3" class="node">
<title>n3</title>
<polygon fill="none" stroke="black" points="85.1,-6 85.1,-54 137.1,-54 137.1,-6 85.1,-6"/>
<text text-anchor="start" x="90.1" y="-26.3" font-family="Courier,monospace" font-size="14.00">crack</text>
</g>
<!-- n0in2&#45;&gt;n3 -->
<!-- WholeEgg -->
<g id="e2" class="edge">
<title>n0in2:e&#45;&gt;n3:w</title>
<path fill="none" stroke="black" d="M49.1,-84C76.03,-84 58.92,-36.93 80,-30.68"/>
<polygon fill="black" stroke="black" points="80.38,-32.4 85.1,-30 79.91,-28.93 80.38,-32.4"/>
<text text-anchor="middle" x="33.64" y="-60.54" font-family="Courier,monospace" font-size="14.00">WholeEgg</text>
</g>
<!-- n5 -->
<!-- junction -->
<g id="n5" class="node">
<title>n5</title>
<ellipse fill="black" stroke="black" cx="111.1" cy="-74" rx="2" ry="2"/>
</g>
<!-- n0in3&#45;&gt;n5 -->
<!-- Pan -->
<g id="e3" class="edge">
<title>n0in3:e&#45;&gt;n5</title>
<path fill="none" stroke="black" d="M49.1,-42C67.63,-42 68.6,-54.59 85.1,-63 91.52,-66.27 99.12,-69.53 104.24,-71.64"/>
<polygon fill="black" stroke="black" points="103.84,-73.37 109.13,-73.62 105.15,-70.12 103.84,-73.37"/>
<text text-anchor="middle" x="97.62" y="-59.31" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n0out1 -->
<!-- n0out2 -->
<!-- n0out1&#45;&gt;n0out2 -->
<!-- n0out3 -->
<!-- n0out2&#45;&gt;n0out3 -->
<!-- n2 -->
<!-- fry -->
<g id="n2" class="node">
<title>n2</title>
<polygon fill="none" stroke="black" points="173.6,-110 173.6,-158 208.6,-158 208.6,-110 173.6,-110"/>
<text text-anchor="start" x="178.6" y="-130.3" font-family="Courier,monospace" font-size="14.00">fry</text>
</g>
<!-- n1&#45;&gt;n2 -->
<!-- RawEgg -->
<g id="e4" class="edge">
<title>n1:e&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M137.1,-138C151.57,-138 155.78,-144.23 167.84,-145.7"/>
<polygon fill="black" stroke="black" points="168.01,-147.46 173.1,-146 168.21,-143.96 168.01,-147.46"/>
<text text-anchor="middle" x="130" y="-145.76" font-family="Courier,monospace" font-size="14.00">RawEgg</text>
</g>
<!-- n7 -->
<!-- junction -->
<g id="n7" class="node">
<title>n7</title>
<ellipse fill="black" stroke="black" cx="190.6" cy="-90" rx="2" ry="2"/>
</g>
<!-- n1&#45;&gt;n7 -->
<!-- Shell -->
<g id="e10" class="edge">
<title>n1:e&#45;&gt;n7</title>
<path fill="none" stroke="black" d="M137.1,-114C147,-114 172.89,-99.71 184.19,-93.18"/>
<polygon fill="black" stroke="black" points="185.18,-94.63 188.61,-90.59 183.41,-91.61 185.18,-94.63"/>
<text text-anchor="middle" x="184.97" y="-96.7" font-family="Courier,monospace" font-size="14.00">Shell</text>
</g>
<!-- n2&#45;&gt;n0out1 -->
<!-- Egg -->
<g id="e12" class="edge">
<title>n2:e&#45;&gt;n0out1:w</title>
<path fill="none" stroke="black" d="M208.1,-146C240.5,-146 249.12,-136.09 279.1,-135.08"/>
<polygon fill="black" stroke="black" points="279.13,-136.83 284.1,-135 279.07,-133.33 279.13,-136.83"/>
<text text-anchor="middle" x="233.41" y="-129.35" font-family="Courier,monospace" font-size="14.00">Egg</text>
</g>
<!-- n6 -->
<!-- junction -->
<g id="n6" class="node">
<title>n6</title>
<ellipse fill="black" stroke="black" cx="246.1" cy="-48" rx="2" ry="2"/>
</g>
<!-- n2&#45;&gt;n6 -->
<!-- Pan -->
<g id="e8" class="edge">
<title>n2:e&#45;&gt;n6</title>
<path fill="none" stroke="black" d="M208.1,-122C237.78,-122 243.65,-73.79 244.82,-55.2"/>
<polygon fill="black" stroke="black" points="246.58,-54.91 245.07,-49.83 243.09,-54.74 246.58,-54.91"/>
<text text-anchor="middle" x="226.69" y="-78.2" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n4 -->
<!-- fry -->
<g id="n4" class="node">
<title>n4</title>
<polygon fill="none" stroke="black" points="173.6,-22 173.6,-70 208.6,-70 208.6,-22 173.6,-22"/>
<text text-anchor="start" x="178.6" y="-42.3" font-family="Courier,monospace" font-size="14.00">fry</text>
</g>
<!-- n3&#45;&gt;n4 -->
<!-- RawEgg -->
<g id="e5" class="edge">
<title>n3:e&#45;&gt;n4:w</title>
<path fill="none" stroke="black" d="M137.1,-42C152.7,-42 155.18,-54.69 167.91,-57.47"/>
<polygon fill="black" stroke="black" points="167.95,-59.23 173.1,-58 168.31,-55.75 167.95,-59.23"/>
<text text-anchor="middle" x="130.13" y="-53.82" font-family="Courier,monospace" font-size="14.00">RawEgg</text>
</g>
<!-- n8 -->
<!-- junction -->
<g id="n8" class="node">
<title>n8</title>
<ellipse fill="black" stroke="black" cx="190.6" cy="-2" rx="2" ry="2"/>
</g>
<!-- n3&#45;&gt;n8 -->
<!-- Shell -->
<g id="e11" class="edge">
<title>n3:e&#45;&gt;n8</title>
<path fill="none" stroke="black" d="M137.1,-18C154.78,-18 174.4,-9.6 183.87,-4.97"/>
<polygon fill="black" stroke="black" points="184.69,-6.52 188.35,-2.69 183.1,-3.4 184.69,-6.52"/>
<text text-anchor="middle" x="184.95" y="-9.4" font-family="Courier,monospace" font-size="14.00">Shell</text>
</g>
<!-- n4&#45;&gt;n0out2 -->
<!-- Egg -->
<g id="e13" class="edge">
<title>n4:e&#45;&gt;n0out2:w</title>
<path fill="none" stroke="black" d="M208.1,-58C242.89,-58 247.09,-86.83 278.77,-89.76"/>
<polygon fill="black" stroke="black" points="279.03,-91.52 284.1,-90 279.19,-88.03 279.03,-91.52"/>
<text text-anchor="middle" x="233.42" y="-62.65" font-family="Courier,monospace" font-size="14.00">Egg</text>
</g>
<!-- n4&#45;&gt;n6 -->
<!-- Pan -->
<g id="e9" class="edge">
<title>n4:e&#45;&gt;n6</title>
<path fill="none" stroke="black" d="M208.1,-34C219.91,-34 232.54,-40.31 239.57,-44.46"/>
<polygon fill="black" stroke="black" points="238.84,-46.07 244.01,-47.25 240.71,-43.11 238.84,-46.07"/>
<text text-anchor="middle" x="239.66" y="-27.08" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n5&#45;&gt;n2 -->
<!-- Pan -->
<g id="e6" class="edge">
<title>n5&#45;&gt;n2:w</title>
<path fill="none" stroke="black" d="M113.06,-74.72C116.41,-77.21 127.83,-85.74 137.1,-93 151.77,-104.47 152.54,-118.97 167.85,-121.59"/>
<polygon fill="black" stroke="black" points="167.98,-123.35 173.1,-122 168.26,-119.86 167.98,-123.35"/>
<text text-anchor="middle" x="130.57" y="-87.34" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n5&#45;&gt;n4 -->
<!-- Pan -->
<g id="e7" class="edge">
<title>n5&#45;&gt;n4:w</title>
<path fill="none" stroke="black" d="M113.1,-73.67C116.57,-72.49 128.35,-68.32 137.1,-63 153.01,-53.33 152.78,-37.37 167.89,-34.46"/>
<polygon fill="black" stroke="black" points="168.28,-36.18 173.1,-34 167.97,-32.7 168.28,-36.18"/>
<text text-anchor="middle" x="158.06" y="-44.75" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
<!-- n6&#45;&gt;n0out3 -->
<!-- Pan -->
<g id="e14" class="edge">
<title>n6&#45;&gt;n0out3:w</title>
<path fill="none" stroke="black" d="M248.25,-48C252.27,-48 266.12,-48 279.03,-48"/>
<polygon fill="black" stroke="black" points="279.1,-49.75 284.1,-48 279.1,-46.25 279.1,-49.75"/>
<text text-anchor="middle" x="278.9" y="-36.8" font-family="Courier,monospace" font-size="14.00">Pan</text>
</g>
</g>
</svg>


For more details about working with wiring diagrams in Catlab, you should look at the vignettes under wiring_diagrams which explain how wiring diagrams interact with SMC expressions and the basics of constructing and manipulation wiring diagrams.

