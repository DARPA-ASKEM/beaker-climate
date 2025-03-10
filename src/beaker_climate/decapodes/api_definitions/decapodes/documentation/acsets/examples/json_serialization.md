




# Serializing acsets as JSON


Catlab supports the serialization of attributed C-sets (acsets) into JSON with their schemas. This functionality should allow you to interoperate with database representations in other languages by serializing both the data and the type into a network interoperability layer.


```julia
import JSON3, JSONSchema

using ACSets
```


You can interact with the schema representation using JSON Schema with the `write_json_acset_schema` and `read_json_acset_schema` functions.


```julia
function roundtrip_json_acset_schema(schema)
  mktempdir() do dir
    path = joinpath(dir, "schema.json")
    write_json_acset_schema(schema, path)
    read_json_acset_schema(path)
  end
end
```


```
roundtrip_json_acset_schema (generic function with 1 method)
```




## The JSONSchema for Schemas


The following code shows how to view the schema for storing schemas. You can see that this data is encoded in the standardized JSONSchema format, which is a generic way of representing data structures that are serialized to JSON. Notice that there are properties for Homs and Obs. The Homs have fields like name, dom, and codom. The Obs just have a name. AttrTypes are like Obs, but they store the name of the type that the attribute can have. In Julia, the Schemas are parametric in the AttrTypes so that uses can set those types at instance creation time. Attrs are the names of columns that point into the AttrTypes.


```julia
json_schema = JSONSchema.Schema(acset_schema_json_schema())
JSON3.print(json_schema, 2)
```


```
A JSONSchema2
```




## Example 1: Discrete Dynamical Systems


Here is an example of an ACSet schema for Discrete Dynamical Systems. A DDS is just a set `X` whose elements we call states, and a function `next`, which take the current state and gives you the next state. Such systems are used to model processes that occur autonomously and are the simplest possible dynamical system.


```julia
SchDDS = BasicSchema([:X], [(:next,:X,:X)])

JSON3.print(generate_json_acset_schema(SchDDS), 2)
```


```
OrderedCollections.OrderedDict{String, Any}("version" => Dict("ACSets" => "0.0.0", "ACSetSchema" => "0.0.1"), "Ob" => [Dict("name" => "X")], "Hom" => [Dict("name" => "next", "codom" => "X", "dom" => "X")], "AttrType" => Dict{String, String}[], "Attr" => Dict{String, String}[], "equations" => Any[])2
```


LabeledDDS are a variation on DDS where the states can have symbolic names. In Catlab, every element of an object has to be identified by its integer row number. This comes out of a tradition in database design where every table has a natural number primary key. In mathematics, we often want to think of the state space not as a set of integers, but as an arbitrary set. In Catlab, we call that set the Labels and use a `label` attribute to implement the mapping of state numbers to state labels. This way the underlying database implementation can still be designed aroung natural number primary keys, but the user can use symbolic labels. Note also that this shows the schema inheritance. We state that a `SchLabeledDDS` inherits from `SchDDS` by adding a `label` attribute of type `Label`.


```julia
SchLabeledDDS = BasicSchema([:X], [(:next,:X,:X)],
                            [:Label], [(:label,:X,:Label)])

JSON3.print(generate_json_acset_schema(SchLabeledDDS), 2)
```


```
OrderedCollections.OrderedDict{String, Any}("version" => Dict("ACSets" => "0.0.0", "ACSetSchema" => "0.0.1"), "Ob" => [Dict("name" => "X")], "Hom" => [Dict("name" => "next", "codom" => "X", "dom" => "X")], "AttrType" => [Dict("name" => "Label")], "Attr" => [Dict("name" => "label", "codom" => "Label", "dom" => "X")], "equations" => Any[])2
```




## Example 2: Labeled DDS


With the LabeledDDS, we will create an instance by specifying data that fits the schema. Then we will create the JSON output to show how it is encoded. The JSON encoded schema above tells you how to read the JSON encoded data below. You can see that the `LabeledDDS` will have a set for `X` with a `Hom` for `next` and an attribute for `label`. Thus we can expect to see the JSON encoding of a single table database below:     1. The first level of JSON is keyed by the table names     2. Each Table is an array of rows     3. Each row is an object keyed by fields. This is the simplest way to put a relational database in a JSON document. It is a little redundant, because the field names are repeated for each row. But that makes it easy to emit and easy to parse. If this becomes a problem, we can upgrade to a more efficient representation by writing more sophisticated parsers. Something like https://github.com/JuliaIO/MsgPack.jl would be appropriate.


```julia
@acset_type LabeledDDS(SchLabeledDDS, index=[:next, :label])

ldds = LabeledDDS{Int}()
add_parts!(ldds, :X, 4, next=[2,3,4,1], label=[100, 101, 102, 103])
JSON3.print(generate_json_acset(ldds),2)
```


```
OrderedCollections.OrderedDict{Symbol, Any}(:X => @NamedTuple{_id::Int64, next::Int64, label::Int64}[(_id = 1, next = 2, label = 100), (_id = 2, next = 3, label = 101), (_id = 3, next = 4, label = 102), (_id = 4, next = 1, label = 103)], :Label => @NamedTuple{_id::Int64}[])2
```




## Example 3: Graphs


Relational databases are great, because they are capable of representing almost anything that can be stored on a computer. We move up to graphs, which is a nice data structure you have probably seen before. Notably, graphs have two tables, one for edges and one for vertices. These are the category theorist's graph, which means that they support multiple parallel edges and self-loops.


```julia
# Syntax available in Catlab:
# @present SchGraph(FreeSchema) begin
#   V::Ob
#   E::Ob
#   src::Hom(E,V)
#   tgt::Hom(E,V)
# end

SchGraph = BasicSchema([:V,:E], [(:src,:E,:V),(:tgt,:E,:V)])

JSON3.print(generate_json_acset_schema(SchGraph), 2)
```


```
OrderedCollections.OrderedDict{String, Any}("version" => Dict("ACSets" => "0.0.0", "ACSetSchema" => "0.0.1"), "Ob" => [Dict("name" => "V"), Dict("name" => "E")], "Hom" => [Dict("name" => "src", "codom" => "V", "dom" => "E"), Dict("name" => "tgt", "codom" => "V", "dom" => "E")], "AttrType" => Dict{String, String}[], "Attr" => Dict{String, String}[], "equations" => Any[])2
```


An example graph with 4 vertices and 2 edges.


```julia
@acset_type Graph(SchGraph, index=[:src, :tgt])

g = Graph()
add_parts!(g, :V, 4)
add_parts!(g, :E, 2, src=[1,2], tgt=[2,3])
```


```
1:2
```


Note that the vertices are listed out in a somewhat silly way. They are given as a table with no columns, so they show up in the JSON as a bunch of empty objects. This is for consistency with our next example.


```julia
JSON3.print(generate_json_acset(g), 2)
```


```
OrderedCollections.OrderedDict{Symbol, Any}(:V => @NamedTuple{_id::Int64}[(_id = 1,), (_id = 2,), (_id = 3,), (_id = 4,)], :E => @NamedTuple{_id::Int64, src::Int64, tgt::Int64}[(_id = 1, src = 1, tgt = 2), (_id = 2, src = 2, tgt = 3)])2
```




## Example 4: Vertex and Edge Labeled Graph Graph Schema


You can extend schemas by adding more tables and columns. This inheritance is flattened when you serialize to JSON, but could be encoded in a future version.


```julia
# Syntax available in Catlab:
# @present SchVELabeledGraph <: SchGraph begin
#    Label::AttrType
#    vlabel::Attr(V,Label)
#    elabel::Attr(E,Label)
# end

SchVELabeledGraph = BasicSchema([:V,:E], [(:src,:E,:V),(:tgt,:E,:V)],
  [:Label], [(:vlabel,:V,:Label),(:elabel,:E,:Label)])

JSON3.print(generate_json_acset_schema(SchVELabeledGraph), 2)
```


```
OrderedCollections.OrderedDict{String, Any}("version" => Dict("ACSets" => "0.0.0", "ACSetSchema" => "0.0.1"), "Ob" => [Dict("name" => "V"), Dict("name" => "E")], "Hom" => [Dict("name" => "src", "codom" => "V", "dom" => "E"), Dict("name" => "tgt", "codom" => "V", "dom" => "E")], "AttrType" => [Dict("name" => "Label")], "Attr" => [Dict("name" => "vlabel", "codom" => "Label", "dom" => "V"), Dict("name" => "elabel", "codom" => "Label", "dom" => "E")], "equations" => Any[])2
```


An example labeled graph using symbols for the vertex and edge names. Note that you can use unicode symbols in Julia.


```julia
@acset_type VELabeledGraph(SchVELabeledGraph, index=[:src,:tgt])

lg = VELabeledGraph{Symbol}()
add_parts!(lg, :V, 4, vlabel=[:a, :b, :c, :d])
add_parts!(lg, :E, 2, src=[1,2], tgt=[2,3], elabel=[:e₁, :e₂])
```


```
1:2
```


This Graph is represented by the following JSON. Now you can see that the vertices have their `vlabels`


```julia
JSON3.print(generate_json_acset(lg), 2)
```


```
OrderedCollections.OrderedDict{Symbol, Any}(:V => @NamedTuple{_id::Int64, vlabel::Symbol}[(_id = 1, vlabel = :a), (_id = 2, vlabel = :b), (_id = 3, vlabel = :c), (_id = 4, vlabel = :d)], :E => @NamedTuple{_id::Int64, src::Int64, tgt::Int64, elabel::Symbol}[(_id = 1, src = 1, tgt = 2, elabel = :e₁), (_id = 2, src = 2, tgt = 3, elabel = :e₂)], :Label => @NamedTuple{_id::Int64}[])2
```

