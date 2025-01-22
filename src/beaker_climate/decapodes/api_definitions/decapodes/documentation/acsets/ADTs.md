


# Library Reference


The ACSet Specification module with ADTs. This module is not rexported as the function names have not fully stabilized.

**`ACSets.ADTs.acsetspec`** &mdash; *Method*.



```julia
acsetspec(head::Symbol, body::Expr)
```

processes a Julia Expr specifying the ACSet construction into a the ADT representation. Approximate inverse to `show`

**`ACSets.ADTs.construct`** &mdash; *Method*.



```julia
construct(T::Type, sp::ACSetSpec)
```

invoke the constructor and build the acset by adding parts.

**`ACSets.ADTs.generate_expr`** &mdash; *Method*.



```julia
generate_expr(s::ACSetSpec)
```

creates a julia Expr that will generate the specified ACSet. 

**`ACSets.ADTs.label2index`** &mdash; *Method*.



```julia
label2index(s::ACSetSpec)
```

replace symbolic identifiers in an ACSet spec with the indices that have that label. This function assumes that all labels are globally unique across tables.  So prefix them with the table name if you want scopes. It also assumes that you don't have any other attributes of type symbol, so use strings instead.

**`ACSets.ADTs.to_dict`** &mdash; *Method*.



```julia
to_dict(s::ACSetSpec)
```

generates a dictionary representation the `ACSetSpec` (or any sub-term). This dict should be serializable with `JSON.json`.

**`Base.show`** &mdash; *Method*.



```julia
show(io::IO, s::AbstractACSetSpec)
```

generates a human readable string of the `ACSetSpec` (or any sub-term).

