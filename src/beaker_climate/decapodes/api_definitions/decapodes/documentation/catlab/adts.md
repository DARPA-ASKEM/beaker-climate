


# ADTs


This module `Catlab.ADTs` provides ADT representations for constructing diagrams.  Currently, it supports the RelationTerm ADT which yields a model capable of representing an UWD.




## API

**`Catlab.ADTs.ADTsCore`** &mdash; *Module*.



Core components of an ADT

**`Catlab.ADTs.ADTsCore.AbstractTerm`** &mdash; *Type*.



```julia
AbstractTerm
```

The super type for all ADT types. This abstract type exists so that we can write generic methods that work on any term in any of the domain specific syntaxes.

**`Catlab.ADTs.RelationTerm`** &mdash; *Module*.



RelationTerm

RelationTerm includes ADT representation of a UWD as well as functions to display UWD in text format and a constructor to create an ACSet Representation.

**`Catlab.ADTs.RelationTerm.UWDTerm`** &mdash; *Type*.



```julia
UWDTerm
```

Term specifying UWD.

**Subtypes**

1. UWDExpr: A list of outer ports, context of variables, and statements defining a UWD
2. Statement: R(x,y,z) a relation that acts on its arguments (which are Vars)

**Example**

To specify the following relation macro:

```julia
@relation (x, z) where (x::X, y::Y, z::Z, u::U) begin
  R(x,y)
  S(y,z)
  T(z,y,u)
end
```

Use the following SyntacticModels UWDTerm:

```julia
v1 = Typed(:x, :X)
v2 = Typed(:y, :Y)
v3 = Typed(:z, :Z)
v4 = Typed(:u, :U)
c = [v1, v2, v3, v4]
op = [v1, v3]
s = [Statement(:R, [v1,v2]),
  Statement(:S, [v2,v3]),
  Statement(:T, [v3,v2, v4])]
u = UWDExpr(op, c, s)
```

**`Catlab.ADTs.RelationTerm.Var`** &mdash; *Type*.



Var

Variables of a UWD. Types are the domain types, ScalarField, VectorField, Dual1Form, Primal2Form NOT Float64,Complex128

Subtypes include:

1. Untyped(var::Symbol)
2. Typed(var::Symbol, type::Union{Symbol, Int, Expr})
3. Kwarg(name::Symbol, var::Var)

which are used for representing typed or untyped variables as well as keyword-based vars.

