


# Library Reference

**`ACSets.ACSetInterface.ACSet`** &mdash; *Type*.



Abstract base type for acsets, static or dynamic.

**`ACSets.ACSetInterface.DenseParts`** &mdash; *Type*.



Part IDs are densely packed without gaps.

Mutations are eager and garbage collection is a no-op. Deletion or identification of parts may invalidate external references to particular parts.

**`ACSets.ACSetInterface.MarkAsDeleted`** &mdash; *Type*.



Mark parts as deleted when they are removed.

Deletions are lazy and arrays are not resized until garbage collection. Parts can be deleted without invalidating external references to other parts.

**`ACSets.ACSetInterface.MarkAsDeletedUnionFind`** &mdash; *Type*.



Combination of [`MarkAsDeleted`](api.md#ACSets.ACSetInterface.MarkAsDeleted) and [`UnionFind`](api.md#ACSets.ACSetInterface.UnionFind).

**`ACSets.ACSetInterface.PartsType`** &mdash; *Type*.



Type of part IDs to use in an acset.

The choice of parts type does not alter the mathematical model but it does affect the performance tradeoffs of the acset data structure, the assumptions that can be made about the part IDs, and whether garbage collection ([`gc!`](api.md#ACSets.ACSetInterface.gc!)) is relevant.

Type parameter `S` is the collection type (`Int`, `BitSet`, etc) and type parameter `T` is the element type (`Int`, `Symbol`, etc), mirroring the two type parameters of `FinSet` in Catlab.

The default choice of parts type is [`DenseParts`](api.md#ACSets.ACSetInterface.DenseParts).

**`ACSets.ACSetInterface.UnionFind`** &mdash; *Type*.



Allow distinct part IDs to refer to the same logical part.

Implemented using union-find. Garbage collection is an operation that makes sense to perform. Parts can be identified with each other without invalidating external references to particular parts.

**`ACSets.ACSetInterface.acset_name`** &mdash; *Function*.



Get the name of an acset at runtime

**`ACSets.ACSetInterface.acset_schema`** &mdash; *Function*.



Get the schema of an acset at runtime.

**`ACSets.ACSetInterface.add_part!`** &mdash; *Method*.



Add part of given type to acset, optionally setting its subparts.

Returns the ID of the added part.

See also: [`add_parts!`](api.md#ACSets.ACSetInterface.add_parts!).

**`ACSets.ACSetInterface.add_parts!`** &mdash; *Function*.



Add parts of given type to acset, optionally setting their subparts.

Returns the range of IDs for the added parts.

See also: [`add_part!`](api.md#ACSets.ACSetInterface.add_part!-Tuple{ACSet, Symbol, Any}).

**`ACSets.ACSetInterface.cascading_rem_part!`** &mdash; *Method*.



Remove part and all parts incident to it, recursively.

Cf. [`rem_part!`](api.md#ACSets.ACSetInterface.rem_part!), which is not recursive.

**`ACSets.ACSetInterface.cascading_rem_parts!`** &mdash; *Function*.



Remove parts and all parts incident to them, recursively.

The parts may be supplied in any order and may include duplicates.

Cf. [`rem_parts!`](api.md#ACSets.ACSetInterface.rem_parts!-Tuple{ACSet, Any, Any}), which is not recursive.

**`ACSets.ACSetInterface.codom_parts`** &mdash; *Function*.



Get the parts of the codomain of a morphism in an acset

dom_parts(acs, f) == parts(acs, Y)

where Y is the codom of the f in the schema

**`ACSets.ACSetInterface.constructor`** &mdash; *Function*.



Get a nullary callable which constructs an (empty) ACSet of the same type

**`ACSets.ACSetInterface.copy_parts!`** &mdash; *Function*.



Copy parts from a C-set to a C′-set.

The selected parts must belong to both schemas. All subparts common to the selected parts, including data attributes, are preserved. Thus, if the selected parts form a sub-C-set, then the whole sub-C-set is preserved. On the other hand, if the selected parts do *not* form a sub-C-set, then some copied parts will have undefined subparts.

TODO: handle colons

**`ACSets.ACSetInterface.copy_parts_only!`** &mdash; *Function*.



Copy parts from a C-set to a C′-set, ignoring all non-data subparts.

The selected parts must belong to both schemas. Attributes common to both schemas are also copied, but no other subparts are copied.

See also: [`copy_parts!`](api.md#ACSets.ACSetInterface.copy_parts!).

**`ACSets.ACSetInterface.dom_parts`** &mdash; *Function*.



Get the parts of the domain of a morphism in an acset

dom_parts(acs, f) == parts(acs, X)

where X is the dom of the f in the schema

**`ACSets.ACSetInterface.gc!`** &mdash; *Function*.



Garbage collect in an acset.

For some choices of [`PartsType`](api.md#ACSets.ACSetInterface.PartsType), this function is a no-op.

**`ACSets.ACSetInterface.has_part`** &mdash; *Function*.



Whether an acset has a part with the given name.

**`ACSets.ACSetInterface.incident`** &mdash; *Function*.



Get superparts incident to part in acset.

If the subpart is indexed, this takes constant time; otherwise, it takes linear time. As with [`subpart`](api.md#ACSets.ACSetInterface.subpart), both single and vectorized access, as well as chained access, are supported. Note that sequences of morphisms are supplied in the usual left-to-right order, so that

```
incident(g, x, [:src, :vattr])
```

returns the list of all edges whose source vertex has vertex attribute `x`.

If the chaining of subparts is given as a tuple (e.g.; (:src, :vattr)), then code generation is used to check that the subparts and their order is a valid composition and to improve performance.

Note that when the subpart is indexed, this function returns a view of the underlying index, which should not be mutated. To ensure that a fresh copy is returned, regardless of whether indexing is enabled, set the keyword argument `copy=true`.

**`ACSets.ACSetInterface.maxpart`** &mdash; *Function*.



Maximum possible part value of given type in an acset.

**`ACSets.ACSetInterface.nparts`** &mdash; *Function*.



Number of parts of given type in an acset.

**`ACSets.ACSetInterface.parts`** &mdash; *Method*.



Parts of given type in an acset.

**`ACSets.ACSetInterface.parts_type`** &mdash; *Method*.



Get the type used to store parts IDs.

**`ACSets.ACSetInterface.pretty_tables`** &mdash; *Method*.



Display an acset using PrettyTables.jl.

This works for any acset that implements [`tables`](api.md#ACSets.ACSetInterface.tables).

**`ACSets.ACSetInterface.rem_free_vars!`** &mdash; *Method*.



Remove all AttrType parts that are not in the image of any of the attributes.

**`ACSets.ACSetInterface.rem_part!`** &mdash; *Function*.



Remove part from a C-set.

The part is removed using the "pop and swap" strategy familiar from [Graphs.jl](https://github.com/JuliaGraphs/Graphs.jl), where the "removed" part is actually replaced by the last part, which is then deleted. This strategy has important performance benefits since only the last part must be assigned a new ID, as opposed to assigning new IDs to *every* part following the removed part.

The removal operation is *not* recursive. When a part is deleted, any superparts incident to it are retained, but their subparts become undefined (equal to the integer zero). For example, in a graph, if you call `rem_part!` on a vertex, the edges incident the `src` and/or `tgt` vertices of the edge become undefined but the edge itself is not deleted.

Indexing has both positive and negative impacts on performance. On the one hand, indexing reduces the cost of finding affected superparts from linear time to constant time. On the other hand, the indices of subparts must be updated when the part is removed. For example, in a graph, indexing `src` and `tgt` makes removing vertices faster but removing edges (slightly) slower.

See also: [`rem_parts!`](api.md#ACSets.ACSetInterface.rem_parts!-Tuple{ACSet, Any, Any}).

**`ACSets.ACSetInterface.rem_parts!`** &mdash; *Method*.



Remove parts from a C-set.

The parts must be supplied in sorted order, without duplicates.

See also: [`rem_part!`](api.md#ACSets.ACSetInterface.rem_part!).

**`ACSets.ACSetInterface.set_subpart!`** &mdash; *Function*.



Mutate subpart of a part in a C-set.

Both single and vectorized assignment are supported.

See also: [`set_subparts!`](api.md#ACSets.ACSetInterface.set_subparts!-Union{Tuple{keys}, Tuple{ACSet, Any, NamedTuple{keys}}} where keys).

**`ACSets.ACSetInterface.set_subparts!`** &mdash; *Method*.



Mutate subparts of a part in a C-set.

Both single and vectorized assignment are supported.

See also: [`set_subpart!`](api.md#ACSets.ACSetInterface.set_subpart!).

**`ACSets.ACSetInterface.subpart`** &mdash; *Function*.



Get subpart of part in acset.

Both single and vectorized access are supported, with a view of the underlying data being returned in the latter case. Chaining, or composition, of subparts is also supported. For example, given a vertex-attributed graph `g`,

```
subpart(g, e, [:src, :vattr])
```

returns the vertex attribute of the source vertex of the edge `e`. As a shorthand, subparts can also be accessed by indexing:

```
g[e, :src] == subpart(g, e, :src)
```

If the chaining of subparts is given as a tuple (e.g.; (:src, :vattr)), then code generation is used to check that the subparts and their order is a valid composition and to improve performance.

Be warned that indexing with lists of subparts works just like `subpart`: `g[e,[:src,:vattr]]` is equivalent to `subpart(g, e, [:src,:vattr])`. This convention differs from DataFrames but note that the alternative interpretation of `[:src,:vattr]` as two independent columns does not even make sense, since they have different domains (belong to different tables).

**`ACSets.ACSetInterface.subpart_type`** &mdash; *Function*.



Get the type assigned to a subpart in an acset, i.e.

subpart_type(acs::WeightedGraph{T}, :weight) == T

**`ACSets.ACSetInterface.tables`** &mdash; *Function*.



Get a named tuple of Tables.jl-compatible tables from an acset

**`ACSets.ACSetInterface.undefined_subparts`** &mdash; *Function*.



Given a hom, find which parts in its domain are undefined.

**`ACSets.ACSetInterface.@acset`** &mdash; *Macro*.



This provides a shorthand for constructing an acset by giving its parts and subparts

Usage:

@acset WeightedGraph{String} begin   V = 2   E = 1   src = [1]   tgt = [2]   weight = ["fig"] end

**`ACSets.ACSetSerialization`** &mdash; *Module*.



Serializing and deserializing acsets to/from different formats.

**`ACSets.ACSetSerialization.read_acset!`** &mdash; *Function*.



Mutating variant of [`read_acset`](api.md#ACSets.ACSetSerialization.read_acset-Tuple{Any, Any}).

**Arguments**

  * `acset`: acset to write to
  * `source`: source to read from

**`ACSets.ACSetSerialization.read_acset`** &mdash; *Method*.



Read/deserialize an acset from an external source.

Supported source types include:

  * `AbstractDict`: assumed to be JSON data
  * `XLSX.XLSXFile`: Microsoft Excel file (requires XLSX.jl)

**Arguments**

  * `cons`: constructor for acset, e.g., the type of a struct acset
  * `source`: source to read from

**`ACSets.ColumnImplementations.AttrVar`** &mdash; *Type*.



Maps from attribute variables can go into arbitrary Julia types or other  variables (indexed by integers). This wrapper types allows us to not confuse  our Attr Variable indices with the Julia type of Int

**`ACSets.ColumnImplementations.DenseColumn`** &mdash; *Type*.



A column for a vec-backed unindexed attr

**`ACSets.ColumnImplementations.DenseFinColumn`** &mdash; *Type*.



A column for a vec-backed unindexed hom

**`ACSets.ColumnImplementations.DenseIndexedColumn`** &mdash; *Type*.



A column for a vec-backed indexed attr

**`ACSets.ColumnImplementations.DenseIndexedFinColumn`** &mdash; *Type*.



A column for a vec-backed indexed hom

**`ACSets.ColumnImplementations.DenseInjectiveColumn`** &mdash; *Type*.



A column for a vec-backed unindexed attr

**`ACSets.ColumnImplementations.DenseInjectiveFinColumn`** &mdash; *Type*.



A column for a vec-backed injective hom

**`ACSets.ColumnImplementations.SparseColumn`** &mdash; *Type*.



A column for a dict-backed unindexed hom with key type K

**`ACSets.ColumnImplementations.SparseFinColumn`** &mdash; *Type*.



A column for a dict-backed unindexed hom with key type K

**`ACSets.ColumnImplementations.SparseIndexedColumn`** &mdash; *Type*.



A column for a dict-backed indexed hom with key type K

**`ACSets.ColumnImplementations.SparseIndexedFinColumn`** &mdash; *Type*.



A column for a dict-backed indexed hom with key type K

**`ACSets.ColumnImplementations.SparseInjectiveColumn`** &mdash; *Type*.



A column for a dict-backed injective hom with key type K

**`ACSets.ColumnImplementations.SparseInjectiveFinColumn`** &mdash; *Type*.



A column for a dict-backed injective hom with key type K

**`ACSets.ColumnImplementations.indexchoice`** &mdash; *Method*.



Convert specification of indexing via lists of indexed and unique_indexed morphisms into a specific enum choice.

**`ACSets.Columns.Column`** &mdash; *Type*.



A column wraps a mapping and a cache of its preimages, and provides methods that do coordinated updates of both.

Abstract Fields:

  * m::Mapping{S,T}
  * pc::PreimageCache{S,T}

**`ACSets.Defaults.Default`** &mdash; *Type*.



This is a hack in order to pass in a default initializer for `DefaultVecMap` as a type parameter

**`ACSets.DenseACSets`** &mdash; *Module*.



These are ACSets where the set associated to each object is of the form `1:n`

**`ACSets.DenseACSets.AnonACSet`** &mdash; *Type*.



This works the same as something made with `@acset_type`, only the types of the parts and subparts are stored as type parameters. Thus, this can be used with any schema.

**`ACSets.DenseACSets.BitSetParts`** &mdash; *Type*.



Parts IDs are a subset of contiguous integers from 1 to n.

**`ACSets.DenseACSets.DynamicACSet`** &mdash; *Type*.



This is a SimpleACSet which has the schema as a field value rather than as a type parameter.

**`ACSets.DenseACSets.DynamicACSet`** &mdash; *Method*.



Cast StructACSet into a DynamicACSet

**`ACSets.DenseACSets.IntParts`** &mdash; *Type*.



Part IDs are contiguous integers from 1 to n.

**`ACSets.DenseACSets.SimpleACSet`** &mdash; *Type*.



A `SimpleACSet` is an abstract type for any acset that has a certain layout

Specifically, subtypes of `SimpleACSet` are expected to have a `parts` field which is a mapping from symbols to ints, and a `subparts` field which is a mapping from symbols to columns, which are any data structure that satisfies the interface given in Columns.jl.

**`ACSets.DenseACSets.StructACSet`** &mdash; *Type*.



A `StructACSet` is a SimpleACSet where the schema and the types assigned to the attrtypes are available in the type.

**`ACSets.DenseACSets.StructACSet`** &mdash; *Method*.



Cast DynamicACSet into a StructACSet

**`ACSets.DenseACSets.StructCSet`** &mdash; *Type*.



A special case where there are no attributes.

**`ACSets.ACSetInterface.gc!`** &mdash; *Method*.



Reindex the parts of the acset such that there are no gaps between the indices. Return a vector for each part mapping the new parts into the old parts. 

**`ACSets.ACSetInterface.incident`** &mdash; *Method*.



Calling incident on a range of values, e.g. `incident(G, 1:2, :src)` is  equivalent to concatenating the results of incident on each part, i.e.  `[incident(G,1,:src), incident(G,2,:src)]`.

**`ACSets.DenseACSets.ACSetTableType`** &mdash; *Method*.



This takes an ACSet type, and produces an AnonACSet which represents an acset with just the object passed in, and then all of the attributes of that object.

TODO: rename this to be less confusing with ACSetTable. Maybe ASet (attributed set)

**`ACSets.DenseACSets.AnonACSetType`** &mdash; *Method*.



This can be used to fill out the type parameters to an AnonACSet ahead of time.

**`ACSets.DenseACSets.delete_subobj!`** &mdash; *Method*.



Return a mapping of from parts of updated X to the old X

Note: the correctness is dependent on the implementation details of `rem_parts!`

**`ACSets.DenseACSets.delete_subobj`** &mdash; *Method*.



Identify which parts of an ACSet need to be deleted if some initial collection  of parts is to be deleted. E.g. deleting a vertex deletes its edge

**`ACSets.DenseACSets.genericize`** &mdash; *Method*.



The type variables that we have generated might not match up with the type variables that are created as generic parameters to the struct acset, this is a way of making the two line up

**`ACSets.DenseACSets.idx`** &mdash; *Method*.



Get index of row in parent acset.

Given an `ACSetRow` object from the Tables.jl interface, return the ID of the correspond part in the parent acset the row was derived from.

**`ACSets.DenseACSets.pi_type`** &mdash; *Method*.



Creates a named tuple type

**`ACSets.DenseACSets.pi_type_elt`** &mdash; *Method*.



Creates a quoted element of a named tuple

**`ACSets.DenseACSets.struct_acset`** &mdash; *Method*.



Create the struct declaration for a `StructACSet` from a Presentation

**`Base.parent`** &mdash; *Method*.



Get parent acset.

Given a `ACSetTable` or `ACSetRow` object from the Tables.jl interface, return the parent acset the object was derived from.

**`ACSets.DenseACSets.@abstract_acset_type`** &mdash; *Macro*.



We want control over the type class hierarchy of acsets; this allows us to create abstract types that subtype StructACSet. For instance, we might have an `AbstractGraph` type, and then assume (this is not enforced) that any subtype of `AbstractGraph` has `E,V,src,tgt` in its schema.

**`ACSets.DenseACSets.@acset_type`** &mdash; *Macro*.



This macro creates custom structs that subclass `StructACSet{S}` for specific `S`. These are used for acsets whose schema is known at compile time.

**`ACSets.ACSetSerialization.ExcelACSets`** &mdash; *Module*.



Read acsets from Microsoft Excel files.

**`ACSets.ACSetSerialization.ExcelACSets.read_xlsx_acset`** &mdash; *Method*.



Read acset from an Excel (.xlsx) file.

This is a convenience function that loads the Excel file and then calls [`read_acset`](api.md#ACSets.ACSetSerialization.read_acset-Tuple{Any, Any}). To use this function, the package XLSX.jl must be installed and imported.

**Arguments**

  * `cons`: constructor for acset, e.g., the acset type for struct acsets
  * `source`: filename or IO stream from which to read Excel file
  * `tables=(;)`: dictionary or named tuple mapping object names in acset schema to Excel table specifications

**`ACSets.IndexUtils.deletesorted!`** &mdash; *Method*.



Delete one occurrence of value from sorted vector, if present.

Returns whether an occurence was found and deleted.

**`ACSets.IndexUtils.insertsorted!`** &mdash; *Method*.



Insert into sorted vector, preserving the sorting.

**`ACSets.InterTypes.ACSetTypeSpec`** &mdash; *Type*.



A specification for the type of an acset.

**Fields**

  * `genericname::Union{Symbol, Nothing}`: The name for the generic version of the acset, with type parameters.

    Note that the name assigned to this in the declaration is the name *with* type parameters pre-specified.

    If there are no attribute types, then this is nothing.
  * `abstract_type::Union{Symbol, Nothing}`: The parent abstract type for the acset.
  * `schemaname::Symbol`
  * `schema::TypedSchema{Symbol, InterType}`
  * `index::Vector{Symbol}`
  * `unique_index::Vector{Symbol}`

**`ACSets.InterTypes.AbstractACSetType`** &mdash; *Type*.



An abstract acset type which ACSets can subtype. Mostly used for backwards compatibility with AlgebraicJulia code.

**`ACSets.InterTypes.Alias`** &mdash; *Type*.



An alias for an existing type

**`ACSets.InterTypes.Field`** &mdash; *Type*.



A field of a struct. Used in [`Variant`](api.md#ACSets.InterTypes.Variant) and `Record`.

The `T` parameter will always be [`InterType`](api.md#ACSets.InterTypes.InterType), but this is mutually-recursive with `InterType` so we have to be generic here.

**`ACSets.InterTypes.InterType`** &mdash; *Type*.



An intertype expression representing a type.

TODO: Generic types TODO: Remove anonymous sums, anonymous products TODO: Separate out primitives, so that this is something like

```julia
@data InterType begin
  PrimType(prim::InterTypePrimitive)
  TypeRef(path::RefPath)
  TypeApp(type::InterType, args::Vector{InterType})
end
```

**`ACSets.InterTypes.InterTypeDecl`** &mdash; *Type*.



An intertype declaration.

Does not include the name of the declaration.

**`ACSets.InterTypes.InterTypeModule`** &mdash; *Type*.



A collection of intertype declarations packaged together. May refer to other InterTypeModules via the `imports` field.

**`ACSets.InterTypes.JSONTarget`** &mdash; *Type*.



```julia
JSONTarget
```

Specifies a serialization target of JSON Schema when generating a module.

TODO: This should really be called something like JSONSchemaTarget.

**`ACSets.InterTypes.JacksonTarget`** &mdash; *Type*.



```julia
JacksonTarget
```

Targets the creation of a directory full of `.java` files that use the Jackson JSON library.

**`ACSets.InterTypes.NamedACSetType`** &mdash; *Type*.



An acset type, with customizations like choice of indices, etc.

**`ACSets.InterTypes.PydanticTarget`** &mdash; *Type*.



```julia
PydanticTarget
```

Targets the creation of `.py` files that use the Pydantic library which enables integration with the Python language (specifically when (de)serializing JSON).

**`ACSets.InterTypes.RefPath`** &mdash; *Type*.



A non-empty linked list of symbols representing something like `foo.bar.baz`.

**`ACSets.InterTypes.RefThere`** &mdash; *Type*.



E.g. mod.name

**`ACSets.InterTypes.SExp`** &mdash; *Type*.



A very simple s-expression data structure.

We use this to write the intertype schema to a string and then hash it to get a version identifier.

**`ACSets.InterTypes.SchemaDecl`** &mdash; *Type*.



A schema for acsets. Does not declare the acset type yet, however, that is done by [`NamedACSetType`](api.md#ACSets.InterTypes.NamedACSetType).

**`ACSets.InterTypes.Struct`** &mdash; *Type*.



A struct type, also known as a product type or record type.

**`ACSets.InterTypes.SumType`** &mdash; *Type*.



A sum type, also known as a tagged union.

**`ACSets.InterTypes.Variant`** &mdash; *Type*.



One of the summands of a sum type.

Like [`Field`](api.md#ACSets.InterTypes.Field), the `T` parameter will always be [`InterType`](api.md#ACSets.InterTypes.InterType), but this is mutually-recursive with `InterType` so we have to be generic here.

**`ACSets.InterTypes.VariantOf`** &mdash; *Type*.



A variant of a sum type, i.e. one of the summands. These are implicitly produced when declaring a sum type, and the data of the variant (i.e. the fields) are in the parent sum type.

**`ACSets.InterTypes.generate_module`** &mdash; *Function*.



```julia
generate_module(mod::Module, target::Type{<:ExportTarget}, path="."; target_specific_args...)
```

Generate files that define the intertypes for the specified target. 

**`ACSets.InterTypes.tojsonschema`** &mdash; *Method*.



```julia
tojsonschema(type::InterType)
```

Convert an InterType to a JSONSchema representation.

TODO: We could use multiple dispatch instead of the `@match` here, which might be cleaner

**`ACSets.InterTypes.topy`** &mdash; *Method*.



```julia
topy(intertype::InterType; forward_ref=true)
```

Converts an intertype into a python code string.

TODO: See comment for [`toexpr`](api.md#ACSets.Schemas.toexpr)

TODO: Should we use something like a stringbuilder instead of manually concatenating strings? I.e., a tree of strings with O(1) append/splice, that we write out to a single string at the end?

**`ACSets.Schemas.toexpr`** &mdash; *Function*.



```julia
function toexpr(x) end
```

Used to convert intertype data types to `Expr`.

TODO: Should we unify [`tojsonschema`](api.md#ACSets.InterTypes.tojsonschema-Tuple{InterType}), [`toexpr`](api.md#ACSets.Schemas.toexpr), and [`topy`](api.md#ACSets.InterTypes.topy-Tuple{InterType}) into a single function with an extra argument to control dispatch?

**`ACSets.InterTypes.@intertypes`** &mdash; *Macro*.



```julia
@intertypes "file.it" module modulename end
```

Used to import an intertypes file into Julia.

TODO: maybe we should just build a .jl file from an .it file directly.

**`ACSets.ACSetSerialization.JSONACSets`** &mdash; *Module*.



JSON serialization of acsets and acset schemas.

**`ACSets.ACSetSerialization.JSONACSets.acset_schema_json_schema`** &mdash; *Method*.



Returns the JSON schema for the JSON serialization of ACSet schemas.

The result is a JSON-able object (dictionary) from which a `JSONSchema.Schema` can be constructed, using the package JSONSchema.jl.

**`ACSets.ACSetSerialization.JSONACSets.generate_json_acset`** &mdash; *Method*.



Generate JSON-able object representing an ACSet.

Inverse to [`parse_json_acset`](api.md#ACSets.ACSetSerialization.JSONACSets.parse_json_acset-Tuple{Any, AbstractDict}).

**`ACSets.ACSetSerialization.JSONACSets.generate_json_acset_schema`** &mdash; *Method*.



Generate JSON-able object representing an ACSet schema.

Given an ACSet schema (either a `Schema` or a `Presentation`), such as `SchGraph` or `SchWeightedGraph`, construct a JSON-able dictionary with keys "Ob", "Hom", "AttrType", and "Attr", conforming to the JSON Schema in [`acset_schema_json_schema`](api.md#ACSets.ACSetSerialization.JSONACSets.acset_schema_json_schema-Tuple{}).

Inverse to [`parse_json_acset_schema`](api.md#ACSets.ACSetSerialization.JSONACSets.parse_json_acset_schema-Tuple{Type{BasicSchema}, AbstractDict}).

**`ACSets.ACSetSerialization.JSONACSets.parse_json_acset`** &mdash; *Method*.



Parse JSON-able object or JSON string representing an ACSet.

Inverse to [`generate_json_acset`](api.md#ACSets.ACSetSerialization.JSONACSets.generate_json_acset-Tuple{ACSet}).

**`ACSets.ACSetSerialization.JSONACSets.parse_json_acset_schema`** &mdash; *Method*.



Parse JSON-able object or JSON string representing an ACSet schema.

Given a JSON object specifying a presentation of an ACSet schema, construct a schema object: either a `Schema` or, by default, a `Presentation`.

Inverse to [`generate_json_acset_schema`](api.md#ACSets.ACSetSerialization.JSONACSets.generate_json_acset_schema-Tuple{Schema}).

**`ACSets.ACSetSerialization.JSONACSets.read_json_acset`** &mdash; *Method*.



Deserialize an ACSet object from a JSON file.

Inverse to [`write_json_acset`](api.md#ACSets.ACSetSerialization.JSONACSets.write_json_acset-Tuple{ACSet, AbstractString}).

**`ACSets.ACSetSerialization.JSONACSets.read_json_acset_schema`** &mdash; *Method*.



Deserialize ACSet schema from JSON file.

Similar to [`parse_json_acset_schema`](api.md#ACSets.ACSetSerialization.JSONACSets.parse_json_acset_schema-Tuple{Type{BasicSchema}, AbstractDict}) except reads from a file. Inverse to [`write_json_acset_schema`](api.md#ACSets.ACSetSerialization.JSONACSets.write_json_acset_schema-Tuple{Any, AbstractString}).

**`ACSets.ACSetSerialization.JSONACSets.write_json_acset`** &mdash; *Method*.



Serialize an ACSet object to a JSON file.

Inverse to [`read_json_acset`](api.md#ACSets.ACSetSerialization.JSONACSets.read_json_acset-Tuple{Any, AbstractString}).

**`ACSets.ACSetSerialization.JSONACSets.write_json_acset_schema`** &mdash; *Method*.



Serialize ACSet schema to JSON file.

Similar to [`generate_json_acset_schema`](api.md#ACSets.ACSetSerialization.JSONACSets.generate_json_acset_schema-Tuple{Schema}) except writes to a file. Inverse to [`read_json_acset_schema`](api.md#ACSets.ACSetSerialization.JSONACSets.read_json_acset_schema-Tuple{Any, AbstractString}).

**`JSON3.write`** &mdash; *Method*.



Dispatch for ACSet

Dispatches write to accept ACSets

**`ACSets.Mappings.Mapping`** &mdash; *Type*.



A mapping is essentially an AbstractDict, but we support a couple more methods, like `map`, and so in order to not do type piracy we make our own abstract type to define methods on. Additionally, access to undefined indices will return nothing rather than erroring; this means that a Mapping{K,Nothing} will behave as if everything is undefined. Don't do this.

**`ACSets.NautyInterface`** &mdash; *Module*.



Compute automorphism group via nauty.c

**`ACSets.NautyInterface.CSetNautyRes`** &mdash; *Type*.



NautyResults must satisfy the following interface

  * strhsh: string value representing the isomorphism class
  * orbits: partitions of Cset parts into orbits e.g. if E#2 = E#5, then these two elements are symmetric
  * generators: generating automorphisms of the automorphism group
  * ngroup: number of elements in the automorphism group
  * canonmap: isomorphism from the input into the canonoical isomorph
  * canon: canonical isomorph (codom of `canonmap`)

**`ACSets.NautyInterface.CSetNautyRes`** &mdash; *Method*.



CSetNautyRes for an empty ACSet

**`ACSets.NautyInterface.UnDiGraph`** &mdash; *Type*.



Data structure for simple undirected graph.

**`ACSets.NautyInterface.all_autos`** &mdash; *Method*.



Take advantage of the very special structure of automorphism generators given by nauty to efficiently enumerate the automorphism group. We iteratively expand our automorphism group with each generator. A `while` loop  explores the possible words that we can built (starting with gₙ₊₁)

**`ACSets.NautyInterface.apply`** &mdash; *Method*.



Action of a permutation on a ACSet, X. Results in a new ACSet, Y, and a map X->Y

**`ACSets.NautyInterface.attr_dict`** &mdash; *Method*.



Get all attribute values that are touched upon by the ACSet. Order them.

**`ACSets.NautyInterface.call_nauty`** &mdash; *Function*.



Compute CSetNautyRes from an ACSet.

**`ACSets.NautyInterface.colornames`** &mdash; *Method*.



List of distinct node types in the undigraph representation of an ACSet

**`ACSets.NautyInterface.dreadnaut`** &mdash; *Method*.



Construct input for dreadnaut to compute automorphism group generators, canonical permutation/hash, and orbits.

Note the Julia colorsarray must be changed from being 1-indexed to 0-indexed.

Dreadnaut parameters:

n - # of vertices g - provide input graph via command line rather than via a file f - use an initial partition of the vertices in the undirected graph c - find a canonical graph b - write out a canonical graph x - run nauty z - make a canonical hash o - write out the orbits

**`ACSets.NautyInterface.from_adj`** &mdash; *Method*.



Convert symmetric adjacency matrix to an ACSet which is isomorphic to `X`.

The main work is reverse-engineering triangles of the form

```
                    ↗ src′ₙ
                  ↙    ↕
              eₙ <-> srcₙ <-> vₘ
```

into hom values for the resulting ACSet. We call srcₙ a "hom-object" and  src′ₙ a "pseudo-hom-object". eₙ is the "src ind" and vₘ is the "tgt ind"

**`ACSets.NautyInterface.get_colorsarray`** &mdash; *Method*.



Specify for nauty input what the initial partition is

**`ACSets.NautyInterface.get_oinds`** &mdash; *Method*.



Create partition of flattened indices (all parts altogether) to dict with  indices for each distinct object, e.g.:

{V => 1:8, E => 9:13, src => 14:18, tgt => 19:23,      src*... => 24:28, tgt*... => 29:33, weight => 34:38}

**`ACSets.NautyInterface.parse_orb`** &mdash; *Method*.



Parse / postprocess orbits from the end of dreadnaut input

**`ACSets.NautyInterface.parse_res`** &mdash; *Method*.



Parse nauty stdout text

**`ACSets.NautyInterface.prime`** &mdash; *Method*.



Avoid a name conflict with a user-defined ob or hom

**`ACSets.NautyInterface.to_perm`** &mdash; *Method*.



Convert an all-parts permutation into a symbol-indexed set of  permutations, given a partition of 1:n_total into ranges for each symbol.

**`ACSets.NautyInterface.to_udg`** &mdash; *Method*.



Convert C-Set to an adjacency matrix of an *undirected* simple graph.

the matrix has rows for all parts (e.g. |E| and |V|), all homs (e.g. |E| quantity of src & tgt nodes), and another copy of all homs (called, e.g., _src and _tgt). For a given edge in the category of elements eₙ – srcₙ –> vₘ, we set edges in the simple diagraph:

```
    ↗ _srcₙ
  ↙    ↕
eₙ <-> srcₙ <-> vₘ
```

For attributes, there is no possibility of Attr(X,X), so we simply have, e.g.:     eₘ <-> weightₘ <-> Numberₙ

**`ACSets.PreimageCaches.InjectiveCache`** &mdash; *Type*.



An preimage mapping for injective maps.

**`ACSets.PreimageCaches.PreimageCache`** &mdash; *Type*.



A `PreimageCache` is a cache of the preimage of a `Mapping`. Many of the methods for `PreimageCache` take in a `Mapping`; this is so that `PreimageCache` can choose how much to cache. That is, `PreimageCache` could be a unit type, and simply dynamically compute the preimage mapping on demand, or it could store the full preimage mapping, or perhaps something in between.

Just like a `Mapping`, an `PreimageCache` has a definable codomain, which is a subset of `T`. Calling `add_mapping!` and `remove_mapping!` on elements out of this definable codomain will error.

However, a `PreimageCache` is always defined on all of its definable codomain; it defaults to the empty set.

`PreimageCache` also has a notion of "stored" codomain, where preimages are actually stored.  It is only when the preimage is stored that referential equality of preimage sets will be preserved, and additionally storage can have performance implications.

`PreimageCache`s should support the following functions:

  * [`preimage`](api.md#ACSets.PreimageCaches.preimage)
  * [`assign!`](api.md#ACSets.PreimageCaches.assign!)
  * [`unassign!`](api.md#ACSets.PreimageCaches.unassign!)

**`ACSets.PreimageCaches.StoredPreimageCache`** &mdash; *Type*.



An preimage mapping that works by storing the preimages directly. Note: the storage should be a storage that defaults to making empty preimages when expanded or queried out of band, so for instance `DefaultVecMap{Preimage, DefaultEmpty{Preimage}}`

**`ACSets.PreimageCaches.TrivialCache`** &mdash; *Type*.



The trivial preimage mapping. It just computes preimages on the fly, and the operations for updating it are noops

**`ACSets.PreimageCaches.assign!`** &mdash; *Function*.



Arguments:

  * i::PreimageCache{S,T}
  * y::T
  * x::S

Add `x` to the preimage of `y`.

**`ACSets.PreimageCaches.preimage`** &mdash; *Function*.



Arguments:

  * dom::Iterable{S}
  * m::Mapping{S,T}
  * i::PreimageCache{S,T}
  * y::T

Returns an iterable of the values in the domain that map onto `y`.

**`ACSets.PreimageCaches.preimage_multi`** &mdash; *Method*.



Arguments:

  * dom::Iterable{S}
  * m::Mapping{S,T}
  * i::PreimageCache{S,T}
  * ys::Iterable{T}

Semantically, this is the same as mapping [`preimage`](api.md#ACSets.PreimageCaches.preimage) over `ys`, but the implementation might choose to use a view of an internal data structure of the index instead.

**`ACSets.PreimageCaches.unassign!`** &mdash; *Function*.



Arguments:

  * i::PreimageCache{S,T}
  * y::T
  * x::S

Remove `x` from the preimage of `y`.

**`ACSets.Schemas.arrows`** &mdash; *Function*.



Parameters:

  * s::Schema{Name}

Named Parameters:

  * just_names::Bool=false
  * from::Any = nothing
  * to::Any = nothing

Same deal as [`homs`](api.md#ACSets.Schemas.homs), but for homs and attributes.

**`ACSets.Schemas.attrs`** &mdash; *Function*.



Parameters:

  * s::Schema{Name}

Named Parameters:

  * just_names::Bool=false
  * from::Any = nothing
  * to::Any = nothing

Same deal as [`homs`](api.md#ACSets.Schemas.homs), but for attributes.

**`ACSets.Schemas.attrtypes`** &mdash; *Function*.



Parameters:

  * s::Schema{Name}

Returns an iterable of the names of the attrtypes for this schema.

**`ACSets.Schemas.homs`** &mdash; *Function*.



Parameters:

  * s::Schema{Name}

Named Parameters:

  * just_names::Bool=false
  * from::Any = nothing
  * to::Any = nothing

Defaults to returning an iterable of tuples `(f,x,y)` where `f` is the name of a homomorphism and `x` and `y` are its domain and codomain respectively.

If `just_names` is true, then it just returns the `f`s.

If `from` is not nothing then it should be either an object or an iterable of objects; this then filters to only morphisms that have domain in `from`. Mutatis mutandis for `to`.

**`ACSets.Schemas.objects`** &mdash; *Function*.



Parameters:

  * s::Schema{Name}

Returns an iterable of the names of the objects for this schema.

**`ACSets.Schemas.types`** &mdash; *Function*.



Returns objects and attrtypes.

**`AlgebraicInterfaces.codom`** &mdash; *Function*.



Parameters:

  * s::Schema{Name}
  * f::Name

Named Parameters:

  * from::Any = nothing

Same deal as [`dom`](api.md#AlgebraicInterfaces.dom), but for codomains.

**`AlgebraicInterfaces.dom`** &mdash; *Function*.



Parameters:

  * s::Schema{Name}
  * f::Name

Named Parameters:

  * to::Any = nothing

If `to` is nothing, then this returns the domain of the unique morphism with name `f`, and errors otherwise. If `to` is not nothing, then it should be either an object/attrtype or an iterable of objects/attrtypes, and this should return the domain of the unique morphism with codomain in `to`.

