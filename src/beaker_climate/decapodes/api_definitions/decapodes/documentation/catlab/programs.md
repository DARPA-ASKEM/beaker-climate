


# Programs


The module `Catlab.Programs` provides domain-specific languages (DSLs) for constructing diagrams of various kinds. The DSLs, implemented as Julia macros, are based on the syntax of the Julia language but often interpret that syntax very differently from standard Julia programs. Conversely, this module offers preliminary support for generating Julia code from wiring diagrams.


There are two major macros for constructing wiring diagrams:


  * [`@program`](programs.md#Catlab.Programs.ParseJuliaPrograms.@program-Tuple{Any, Vararg{Any}}), for directed wiring diagrams (DWDs)
  * [`@relation`](programs.md#Catlab.Programs.RelationalPrograms.@relation-Tuple), for undirected wiring diagrams (UWDs)


There is a family of related macros for constructing category-theoretic [diagrams](https://ncatlab.org/nlab/show/diagram) included in `DataMigrations.jl`.




## API

**`Catlab.Programs.GenerateJuliaPrograms`** &mdash; *Module*.



Compile or evaluate morphisms as Julia programs.

**`Catlab.Programs.GenerateJuliaPrograms.Block`** &mdash; *Type*.



A block of Julia code with input and output variables.

**`Catlab.Programs.GenerateJuliaPrograms.CompileState`** &mdash; *Type*.



Internal state for compilation of morphism into Julia code.

**`Catlab.Programs.GenerateJuliaPrograms.compile_block`** &mdash; *Method*.



Compile a morphism expression into a block of Julia code.

**`Catlab.Programs.GenerateJuliaPrograms.compile_expr`** &mdash; *Method*.



Compile a morphism expression into a Julia function expression.

**`Catlab.Programs.GenerateJuliaPrograms.evaluate`** &mdash; *Method*.



Evaluate a morphism as a function.

If the morphism will be evaluated only once (possibly with vectorized inputs), then direct evaluation will be much faster than compiling (via `compile`) and evaluating a standard Julia function.

Compare with [`functor`](categorical_algebra.md#GATlab.Models.SymbolicModels.functor-Tuple{DataMigrationFunctor}).

**`GATlab.Syntax.GATs.compile`** &mdash; *Method*.



Compile a morphism expression into a Julia function.

**`Catlab.Programs.ParseJuliaPrograms`** &mdash; *Module*.



Parse Julia programs into morphisms represented as wiring diagrams.

**`Catlab.Programs.ParseJuliaPrograms.parse_wiring_diagram`** &mdash; *Method*.



Parse a wiring diagram from a Julia function expression.

For more information, see the corresponding macro [`@program`](programs.md#Catlab.Programs.ParseJuliaPrograms.@program-Tuple{Any, Vararg{Any}}).

**`Catlab.Programs.ParseJuliaPrograms.@program`** &mdash; *Macro*.



Parse a wiring diagram from a Julia program.

For the most part, this is standard Julia code but a few liberties are taken with the syntax. Products are represented as tuples. So if `x` and `y` are variables of type $X$ and $Y$, then `(x,y)` has type $X ⊗ Y$. Also, both `()` and `nothing` are interpreted as the monoidal unit $I$.

Unlike standard Julia, the function call expressions `f(x,y)` and `f((x,y))` are equivalent. Consequently, given morphisms $f: W → X ⊗ Y$ and $g: X ⊗ Y → Z$, the code

```julia
x, y = f(w)
g(x,y)
```

is equivalent to `g(f(w))`. In standard Julia, at most one of these calls to `g` would be valid, unless `g` had multiple signatures.

The diagonals (copying and deleting) of a cartesian category are implicit in the Julia syntax: copying is variable reuse and deleting is variable non-use. For the codiagonals (merging and creating), a special syntax is provided, reinterpreting Julia's vector literals. The merging of `x1` and `x2` is represented by the vector `[x1,x2]` and creation by the empty vector `[]`. For example, `f([x1,x2])` translates to `compose(mmerge(X),f)`.

This macro is a wrapper around [`parse_wiring_diagram`](programs.md#Catlab.Programs.ParseJuliaPrograms.parse_wiring_diagram-Tuple{Presentation, Expr}).

**`Catlab.Programs.RelationalPrograms`** &mdash; *Module*.



Parse relation expressions in Julia syntax into undirected wiring diagrams.

**`Catlab.Programs.RelationalPrograms.parse_relation_diagram`** &mdash; *Method*.



Parse an undirected wiring diagram from a relation expression.

For more information, see the corresponding macro [`@relation`](programs.md#Catlab.Programs.RelationalPrograms.@relation-Tuple).

**`Catlab.Programs.RelationalPrograms.@relation`** &mdash; *Macro*.



Construct an undirected wiring diagram using relation notation.

Unlike the `@program` macro for directed wiring diagrams, this macro departs significantly from the usual semantics of the Julia programming language. Function calls with $n$ arguments are now interpreted as assertions that an $n$-ary relation holds at a particular point. For example, the composite of binary relations $R ⊆ X × Y$ and $S ⊆ Y × Z$ can be represented as an undirected wiring diagram by the macro call

```julia
@relation (x,z) where (x::X, y::Y, z::Z) begin
  R(x,y)
  S(y,z)
end
```

In general, the context in the `where` clause defines the set of junctions in the diagram and variable sharing defines the wiring of ports to junctions. If the `where` clause is omitted, the set of junctions is inferred from the variables used in the macro call.

The ports and junctions of the diagram may be typed or untyped, and the ports may be named or unnamed. Thus, four possible types of undirected wiring diagrams may be returned, with the type determined by the form of relation header:

1. Untyped, unnamed: `@relation (x,z) where (x,y,z) ...`
2. Typed, unnamed: `@relation (x,z) where (x::X, y::Y, z::Z) ...`
3. Untyped, named: `@relation (out1=x, out2=z) where (x,y,z) ...`
4. Typed, named: `@relation (out=1, out2=z) where (x::X, y::Y, z::Z) ...`

All four types of diagram are subtypes of [`RelationDiagram`](@ref).

