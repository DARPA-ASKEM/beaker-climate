


# Library Reference

**`DiagrammaticEquations.DiagrammaticEquations`** &mdash; *Module*.



The DiagrammaticEquations module exports data structures which represent diagrammatic equations and functions which manipulate them.

**`DiagrammaticEquations.decapodeacset.SummationDecapode`** &mdash; *Method*.



```julia
function SummationDecapode(e::DecaExpr)
```

Takes a DecaExpr and returns a SummationDecapode ACSet.

**`Catlab.WiringDiagrams.WiringDiagramAlgebras.oapply`** &mdash; *Method*.



```julia
function oapply(relation::RelationDiagram, podes::Vector{D}) where {D<:OpenSummationDecapode}
```

Compose a list of Decapodes as specified by the given relation diagram.

The Decapodes must be given in the same order as they were specified in the relation.

State variables (such as the (C,V) given in the head of the following @relation) do not affect the result of a composition.

**Examples**

```julia-repl
julia> compose_diff_adv = @relation (C,V) begin
  diffusion(C, ϕ₁)
  advection(C, ϕ₂, V)
  superposition(ϕ₁, ϕ₂, ϕ, C)
end;

julia> oapply(compose_diff_adv, [(Diffusion, [:C, :ϕ]),
  (Advection, [:C, :ϕ, :V]), (Superposition, [:ϕ₁, :ϕ₂, :ϕ, :C])]);
```

**`DiagrammaticEquations.Decapode`** &mdash; *Method*.



```julia
function Decapode(e::DecaExpr)
```

Takes a DecaExpr and returns a Decapode ACSet.

**`DiagrammaticEquations.Open`** &mdash; *Method*.



```julia
Open(d::SummationDecapode{T,U,V}, names::AbstractVector{Symbol}) where {T,U,V}
```

creates an OpenSummationDecapode based on named variables rather than variable indices.  See AlgebraicPetri.jl's Open for the analogous verion for LabelledReactionNetworks.

**`DiagrammaticEquations.average_rewrite`** &mdash; *Method*.



```julia
function average_rewrite(d::SummationDecapode)
```

Compute each quantitity in the given Decapode by the average of all computation paths leading to that node.

**`DiagrammaticEquations.collate`** &mdash; *Method*.



```julia
function collate(equations, boundaries, uwd, symbols)
```

Create a collage of two Decapodes that simulates with boundary conditions. ```

**`DiagrammaticEquations.contract_operators`** &mdash; *Method*.



```julia
function contract_operators(d::SummationDecapode; white_list::Set{Symbol} = Set{Symbol}(), black_list::Set{Symbol} = Set{Symbol}())
```

Find chains of Op1s in the given Decapode, and replace them with a single Op1 with a vector of function names. After this process, all Vars that are not a part of any computation are removed. If a white list is provided, only chain those operators. If a black list is provided, do not chain those operators.

**`DiagrammaticEquations.default_composition_diagram`** &mdash; *Method*.



```julia
function default_composition_diagram(podes::Vector{D}, names::Vector{Symbol}) where {D<:SummationDecapode}
```

Given a list of Decapodes and their names, return a composition diagram which assumes that variables sharing the same name ought to be composed.

No Literals are exposed. Use [`unique_lits!`](api.md#DiagrammaticEquations.unique_lits!-Tuple{SummationDecapode}) after composing.

Throw an error if any individual Decapode already contains a repeated name (except for Literals).

If `only_states_terminals` is `true`, only expose state and terminal variables. Defaults to `false`.

Note that composing immediately with [`oapply`](api.md#Catlab.WiringDiagrams.WiringDiagramAlgebras.oapply-Union{Tuple{D}, Tuple{Catlab.Programs.RelationalPrograms.RelationDiagram, Vector{D}}} where D<:(Catlab.CategoricalAlgebra.StructuredCospans.StructuredMulticospan{Catlab.CategoricalAlgebra.StructuredCospans.DiscreteACSet{ACSets.DenseACSets.AnonACSet{ACSets.Schemas.TypeLevelBasicSchema{Symbol, Tuple{:Var}, Tuple{}, Tuple{:Type, :Operator, :Name}, Tuple{(:type, :Var, :Type), (:name, :Var, :Name)}, Tuple{}}, Tuple{Type, Operator, Name}, @NamedTuple{Var::ACSets.DenseACSets.IntParts, Type::ACSets.DenseACSets.IntParts, Operator::ACSets.DenseACSets.IntParts, Name::ACSets.DenseACSets.IntParts}, @NamedTuple{type::ACSets.ColumnImplementations.DenseColumn{Union{ACSets.ColumnImplementations.AttrVar, Type}, Array{Union{ACSets.ColumnImplementations.AttrVar, Type}, 1}}, name::ACSets.ColumnImplementations.DenseColumn{Union{ACSets.ColumnImplementations.AttrVar, Name}, Array{Union{ACSets.ColumnImplementations.AttrVar, Name}, 1}}}, ACSets.DenseACSets.IntParts}, SummationDecapode{Type, Operator, Name}}} where {Type, Operator, Name})) will fail if types do not match (e.g. (:infer, :Form0) or (:Form0, :Form1)).

**`DiagrammaticEquations.dot_rename!`** &mdash; *Method*.



```julia
dot_rename!(d::AbstractNamedDecapode)
```

Rename tangent variables by their depending variable appended with a dot. e.g. If D == ∂ₜ(C), then rename D to Ċ.

If a tangent variable updates multiple vars, choose one arbitrarily. e.g. If D == ∂ₜ(C) and D == ∂ₜ(B), then rename D to either Ċ or B ̇.

**`DiagrammaticEquations.expand_operators`** &mdash; *Method*.



```julia
function expand_operators(d::AbstractNamedDecapode)
```

If any unary operator is a composition, expand it out using intermediate variables.

**`DiagrammaticEquations.expand_operators`** &mdash; *Method*.



```julia
function expand_operators(d::SummationDecapode)
```

Find operations that are compositions, and expand them with intermediate variables.

**`DiagrammaticEquations.fill_names!`** &mdash; *Method*.



```julia
function fill_names!(d::AbstractNamedDecapode; lead_symbol::Symbol = Symbol("•"))
```

Provide a variable name to all the variables that don't have names.

**`DiagrammaticEquations.filterfor_forms`** &mdash; *Method*.



```julia
filterfor_forms(types::AbstractVector{Symbol})
```

Return any form type symbols.

**`DiagrammaticEquations.find_chains`** &mdash; *Method*.



```julia
function find_chains(d::SummationDecapode; white_list::Set{Symbol} = Set{Symbol}(), black_list::Set{Symbol} = Set{Symbol}())
```

Find chains of Op1s in the given Decapode. A chain ends when the target of the last Op1 is part of an Op2 or sum, or is a target of multiple Op1s. If a white list is provided, only chain those operators. If a black list is provided, do not chain those operators.

**`DiagrammaticEquations.find_dep_and_order`** &mdash; *Method*.



```julia
find_dep_and_order(d::AbstractNamedDecapode)
```

Find the order of each tangent variable in the Decapode, and the index of the variable that it is dependent on. Returns a tuple of (dep, order), both of which respecting the order in which incident(d, :∂ₜ, :op1) returns Vars.

**`DiagrammaticEquations.find_tgts_of_many_ops`** &mdash; *Method*.



```julia
function find_tgts_of_many_ops(d::SummationDecapode)
```

Searches SummationDecapode, d, for all Vars which have two or more distinct operations leading into the same variable.

**`DiagrammaticEquations.get_valid_op1s`** &mdash; *Method*.



```julia
function get_valid_op1s(deca_source::SummationDecapode, varID)
```

Searches SummationDecapode, deca_source, at the request varID and returns all op1s which are allowed to be averaged. Returns an array of indices of valid op1 sources.

Namely this is meant to exclude ∂ₜ from being included in an average.

**`DiagrammaticEquations.infer_state_names`** &mdash; *Method*.



```julia
function infer_state_names(d)
```

Find names of variables which have a time derivative or are not the source of a computation. See also: [`infer_states`](api.md#DiagrammaticEquations.infer_states-Tuple{SummationDecapode}).

**`DiagrammaticEquations.infer_states`** &mdash; *Method*.



```julia
function infer_states(d::SummationDecapode)
```

Find variables which have a time derivative or are not the source of a computation. See also: [`infer_terminals`](api.md#DiagrammaticEquations.infer_terminals-Tuple{SummationDecapode}).

**`DiagrammaticEquations.infer_terminal_names`** &mdash; *Method*.



```julia
function infer_terminal_names(d)
```

Find names of variables which have no children. See also: [`infer_terminals`](api.md#DiagrammaticEquations.infer_terminals-Tuple{SummationDecapode}).

**`DiagrammaticEquations.infer_terminals`** &mdash; *Method*.



```julia
function infer_terminals(d::SummationDecapode)
```

Find variables which have no children. See also: [`infer_states`](api.md#DiagrammaticEquations.infer_states-Tuple{SummationDecapode}).

**`DiagrammaticEquations.infer_types!`** &mdash; *Method*.



```julia
function infer_types!(d::SummationDecapode, op1_rules::Vector{NamedTuple{(:src_type, :tgt_type, :replacement_type, :op), NTuple{4, Symbol}}})
```

Infer types of Vars given rules wherein one type is known and the other not.

**`DiagrammaticEquations.is_expanded`** &mdash; *Method*.



```julia
is_expanded(d::AbstractNamedDecapode)
```

Check that no unary operator is a composition of unary operators.

**`DiagrammaticEquations.is_tgt_of_many_ops`** &mdash; *Method*.



```julia
function is_tgt_of_many_ops(d::SummationDecapode, var)
```

Return true if there are two or more distinct operations leading into Var var (not counting ∂ₜ).

**`DiagrammaticEquations.remove_neighborless_vars!`** &mdash; *Method*.



```julia
function remove_neighborless_vars!(d::SummationDecapode)
```

Remove all Vars from the given Decapode that are not part of any computation.

**`DiagrammaticEquations.replace_all_op1s!`** &mdash; *Method*.



```julia
function replace_all_op1s!(d::SummationDecapode, LHS::Union{Symbol, SummationDecapode}, RHS::Union{Symbol, SummationDecapode})
```

Given a Decapode, d, replace all instances of the left-hand-side unary operator with those of the right-hand-side.

Return true if any replacements were made, otherwise false.

See also: [`replace_op1!`](api.md#DiagrammaticEquations.replace_op1!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode}), [`replace_all_op2s!`](api.md#DiagrammaticEquations.replace_all_op2s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}, Int64, Int64})

**`DiagrammaticEquations.replace_all_op2s!`** &mdash; *Method*.



```julia
function replace_all_op2s!(d::SummationDecapode, LHS::Union{Symbol, SummationDecapode}, RHS::Union{Symbol, SummationDecapode}, proj1::Int, proj2::Int)
```

Given a Decapode, d, replace all instances of the left-hand-side binary operator with those of the right-hand-side.

proj1 and proj2 are the indices of the intended proj1 and proj2 in RHS.

Return true if any replacements were made, otherwise false.

See also: [`replace_op2!`](api.md#DiagrammaticEquations.replace_op2!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode, Int64, Int64}), [`replace_all_op1s!`](api.md#DiagrammaticEquations.replace_all_op1s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}})

**`DiagrammaticEquations.replace_all_op2s!`** &mdash; *Method*.



```julia
function replace_all_op2s!(d::SummationDecapode, LHS::Union{Symbol, SummationDecapode}, RHS::Union{Symbol, SummationDecapode})
```

Given a Decapode, d, replace all instances of the left-hand-side binary operator with those of the right-hand-side.

Search for distinguished variables "p1" and "p2" to serve as the proj1 and proj2 from RHS.

Return true if any replacements were made, otherwise false.

See also: [`replace_op2!`](api.md#DiagrammaticEquations.replace_op2!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode, Int64, Int64}), [`replace_all_op1s!`](api.md#DiagrammaticEquations.replace_all_op1s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}})

**`DiagrammaticEquations.replace_op1!`** &mdash; *Method*.



```julia
function replace_op1!(d::SummationDecapode, LHS::SummationDecapode, RHS::SummationDecapode)
```

Given a Decapode, d, replace at most one instance of the left-hand-side unary operator with those of the right-hand-side.

Return the index of the replaced unary operator, 0 if no match was found. See also: [`replace_op2!`](api.md#DiagrammaticEquations.replace_op2!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode, Int64, Int64}), [`replace_all_op1s!`](api.md#DiagrammaticEquations.replace_all_op1s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}})

**`DiagrammaticEquations.replace_op1!`** &mdash; *Method*.



```julia
function replace_op1!(d::SummationDecapode, LHS::Symbol, RHS::SummationDecapode)
```

Given a Decapode, d, replace at most one instance of the left-hand-side unary operator with those of the right-hand-side.

Return the index of the replaced operator, 0 if no match was found.

See also: [`replace_all_op1s!`](api.md#DiagrammaticEquations.replace_all_op1s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}})

**`DiagrammaticEquations.replace_op1!`** &mdash; *Method*.



```julia
function replace_op1!(d::SummationDecapode, LHS::Symbol, RHS::Symbol)
```

Given a Decapode, d, replace at most one instance of the left-hand-side unary operator with that of the right-hand-side.

Return the index of the replaced unary operator, 0 if no match was found. See also: [`replace_op2!`](api.md#DiagrammaticEquations.replace_op2!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode, Int64, Int64}), [`replace_all_op1s!`](api.md#DiagrammaticEquations.replace_all_op1s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}})

**`DiagrammaticEquations.replace_op2!`** &mdash; *Method*.



```julia
function replace_op2!(d::SummationDecapode, LHS::SummationDecapode, RHS::SummationDecapode, proj1::Int, proj2::Int)
```

Given a Decapode, d, replace at most one instance of the left-hand-side binary operator with those of the right-hand-side.

proj1 and proj2 are the indices of the intended proj1 and proj2 in RHS.

Return the index of the replaced binary operator, 0 if no match was found. See also: [`replace_op1!`](api.md#DiagrammaticEquations.replace_op1!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode}), [`replace_all_op2s!`](api.md#DiagrammaticEquations.replace_all_op2s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}, Int64, Int64})

**`DiagrammaticEquations.replace_op2!`** &mdash; *Method*.



```julia
function replace_op2!(d::SummationDecapode, LHS::Symbol, RHS::SummationDecapode, proj1::Int, proj2::Int)
```

Given a Decapode, d, replace at most one instance of the left-hand-side binary operator with those of the right-hand-side.

proj1 and proj2 are the indices of the intended proj1 and proj2 in RHS.

Return the index of the replaced operator, 0 if no match was found.

See also: [`replace_op1!`](api.md#DiagrammaticEquations.replace_op1!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode}), [`replace_all_op2s!`](api.md#DiagrammaticEquations.replace_all_op2s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}, Int64, Int64})

**`DiagrammaticEquations.replace_op2!`** &mdash; *Method*.



```julia
function replace_op2!(d::SummationDecapode, LHS::Symbol, RHS::Symbol)
```

Given a Decapode, d, replace at most one instance of the left-hand-side binary operator with that of the right-hand-side.

Return the index of the replaced binary operator, 0 if no match was found. See also: [`replace_op1!`](api.md#DiagrammaticEquations.replace_op1!-Tuple{SummationDecapode, SummationDecapode, SummationDecapode}), [`replace_all_op2s!`](api.md#DiagrammaticEquations.replace_all_op2s!-Tuple{SummationDecapode, Union{Symbol, SummationDecapode}, Union{Symbol, SummationDecapode}, Int64, Int64})

**`DiagrammaticEquations.resolve_overloads!`** &mdash; *Method*.



```julia
function resolve_overloads!(d::SummationDecapode, op1_rules::Vector{NamedTuple{(:src_type, :tgt_type, :resolved_name, :op), NTuple{4, Symbol}}})
```

Resolve function overloads based on types of src and tgt.

**`DiagrammaticEquations.safe_modifytype!`** &mdash; *Method*.



```julia
safe_modifytype!(d::SummationDecapode, var_idx::Int, new_type::Symbol)
```

This function calls `safe_modifytype` to safely modify a Decapode's variable type.

**`DiagrammaticEquations.safe_modifytype`** &mdash; *Method*.



```julia
safe_modifytype(org_type::Symbol, new_type::Symbol)
```

This function accepts an original type and a new type and determines if the original type   can be safely overwritten by the new type.

**`DiagrammaticEquations.transfer_children!`** &mdash; *Method*.



```julia
function transfer_children!(d::SummationDecapode, x, y)
```

Transfer the children of x to y.

**`DiagrammaticEquations.transfer_parents!`** &mdash; *Method*.



```julia
function transfer_parents!(d::SummationDecapode, x, y)
```

Transfer the parents of x to y. Also transfer TVar status from x to y.

**`DiagrammaticEquations.type_check_Decapodes_composition`** &mdash; *Method*.



```julia
function type_check_Decapodes_composition(relation::RelationDiagram, decs::Vector{OpenSummationDecapode})
```

Check that the types of all Vars connected by the same junction match.

This function only throws an error on the first type mismatch found.

**`DiagrammaticEquations.unique_by!`** &mdash; *Method*.



```julia
function unique_by!(acset, column_names::Vector{Symbol})
```

Given column names from the same table, remove duplicate rows.

WARNING: This function does not check if other tables index into the one given. Removal of rows is performed with prejudice.

See also: [`unique_by`](api.md#DiagrammaticEquations.unique_by-Tuple{Any, Symbol, Vector{Symbol}}).

**Examples**

```julia-repl
julia> unique_by!(parallel_arrows(Graph, 123), :E, [:src,:tgt]) == parallel_arrows(Graph, 1)
true
```

**`DiagrammaticEquations.unique_by`** &mdash; *Method*.



```julia
function unique_by(acset, column_names::Vector{Symbol})
```

Given column names from the same table, return a copy of the acset with duplicate rows removed. Removal of rows is performed with prejudice.

WARNING: This function does not check if other tables index into the one given. Removal of rows is performed with prejudice.

See also: [`unique_by!`](api.md#DiagrammaticEquations.unique_by!-Tuple{Any, Symbol, Vector{Symbol}}).

**Examples**

```julia-repl
julia> unique_by(parallel_arrows(Graph, 123), :E, [:src,:tgt]) == parallel_arrows(Graph, 1)
true
```

**`DiagrammaticEquations.unique_lits!`** &mdash; *Method*.



```julia
function unique_lits!(d::SummationDecapode)
```

Remove repeated Literals from a Decapode.

**`DiagrammaticEquations.@decapode`** &mdash; *Macro*.



```julia
macro decapode(e)
```

Construct a SummationDecapode using the Decapode Domain-Specific Language.

**`DiagrammaticEquations.Deca.op1_inf_rules_1D`** &mdash; *Constant*.



These are the default rules used to do type inference in the 1D exterior calculus.

**`DiagrammaticEquations.Deca.op1_inf_rules_2D`** &mdash; *Constant*.



These are the default rules used to do type inference in the 2D exterior calculus.

**`DiagrammaticEquations.Deca.op1_res_rules_1D`** &mdash; *Constant*.



These are the default rules used to do function resolution in the 1D exterior calculus.

**`DiagrammaticEquations.Deca.op1_res_rules_2D`** &mdash; *Constant*.



These are the default rules used to do function resolution in the 2D exterior calculus.

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



```julia
Graphics.to_graphviz(F::AbstractDecapode; directed = true, kw...)
```

Visualize the given Decapode through Graphviz. Ensure that you have called `using Catlab.Graphics` before-hand, and have a way of visualizing SVG files in your current environment.

**`DiagrammaticEquations.Deca.recursive_delete_parents`** &mdash; *Method*.



```julia
function recursive_delete_parents!(d::SummationDecapode, to_delete::Vector{Int64})
```

Delete the given nodes and their parents in the Decapode, recursively.

**`DiagrammaticEquations.Deca.unicode!`** &mdash; *Method*.



```julia
function unicode!(d::SummationDecapode)
```

Replace ASCII operators with their Unicode equivalents.

**`DiagrammaticEquations.Deca.vec_to_dec!`** &mdash; *Method*.



```julia
function vec_to_dec!(d::SummationDecapode)
```

Replace Vector Calculus operators with Discrete Exterior Calculus equivalents.

**`DiagrammaticEquations.resolve_overloads!`** &mdash; *Method*.



```julia
function resolve_overloads!(d::SummationDecapode)
```

Resolve function overloads based on types of src and tgt.

