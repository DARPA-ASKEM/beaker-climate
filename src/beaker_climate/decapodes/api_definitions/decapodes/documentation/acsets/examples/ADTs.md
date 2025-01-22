




# Specifying acsets using Algebraic Data Types


ACSets are an extremely flexible data representation that can store anything you can put in a database. But in order to construct them, you might want something that feels more like a custom programming language. The Graphviz software comes with a custom language called dot files for specifying the data of a graph that Graphviz will draw. In order to make implementing these linguisting interfaces easier, ACSets.jl supports an Algebraic Data Types approach to specification of ACSets.


```julia
using ACSets, ACSets.ADTs
using MLStyle
using Test
import ACSets.ADTs: symb2string
```


Our schema will be labeled graphs. These are graphs with vertex labels.


```julia
SchLabeledGraph = BasicSchema([:E,:V], [(:src,:E,:V),(:tgt,:E,:V)],
                          [:L], [(:label,:V,:L)])

@acset_type LabeledGraph(SchLabeledGraph, index=[:src,:tgt])
```


```
Main.LabeledGraph
```


The basic principle is a nested expression syntax for specifying the ACSet.


```julia
s = Statement(:E, [Value(2), Value(3)])
```


```
  E(2,3)
```


You can extract information from an expression with pattern matching from MLStyle.jl


```julia
get_table(s) = @match s begin
    Statement(t, e) => t
    _ => nothing
end
get_arg1(s) = @match s begin
    Statement(t, e) => e[1]
end

@test get_table(s) == :E
@test get_arg1(s) == Value(2)
```


```
Test Passed
```


These statements can be grouped together into a list an tagged with the type of ACSet you want to make.


```julia
gspec = ACSetSpec(
    :(LabeledGraph{Symbol}),
    [
        Statement(:V, [Kwarg(:label, Value(:a))])
        Statement(:V, [Kwarg(:label, Value(:b))])
        Statement(:V, [Kwarg(:label, Value(:c))])
        Statement(:E, [Value(1), Value(3)])
        Statement(:E, [Value(2), Value(3)])
    ]
)
```


```
LabeledGraph{Symbol} begin 
  V(label=a)
  V(label=b)
  V(label=c)
  E(1,3)
  E(2,3)
 end
```


These expressions can be serialized as strings:


```julia
sprint(show, gspec)
```


```
"LabeledGraph{Symbol} begin \n  V(label=a)\n  V(label=b)\n  V(label=c)\n  E(1,3)\n  E(2,3)\n end"
```


Or as Julia code:


```julia
generate_expr(gspec)
```


```
quote
    #= /home/matt/.julia/packages/ACSets/7LOk7/src/ADTs.jl:94 =#
    X = LabeledGraph{Symbol}()
    #= /home/matt/.julia/packages/ACSets/7LOk7/src/ADTs.jl:95 =#
    add_part!(X, :V, label = :a)
    add_part!(X, :V, label = :b)
    add_part!(X, :V, label = :c)
    add_part!(X, :E, 1, 3)
    add_part!(X, :E, 2, 3)
end
```


From the ACSetSpec you can construct the ACSet that it specifies.


```julia
gspec = ACSetSpec(
    :(LabeledGraph{Symbol}),
    [
        Statement(:V, [Kwarg(:label, Value(:a))])
        Statement(:V, [Kwarg(:label, Value(:b))])
        Statement(:V, [Kwarg(:label, Value(:c))])
        Statement(:E, [Kwarg(:src, Value(1)), Kwarg(:tgt, Value(3))])
        Statement(:E, [Kwarg(:src, Value(2)), Kwarg(:tgt, Value(3))])
    ]
)
g = construct(LabeledGraph{Symbol}, gspec)
```

<div class="c-set">
<span class="c-set-summary">Main.__atexample__named__ADTs.LabeledGraph{Symbol} {E:2, V:3, L:0}</span>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">E</th>
      <th style = "text-align: right;">src</th>
      <th style = "text-align: right;">tgt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">3</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">3</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">V</th>
      <th style = "text-align: right;">label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">a</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">b</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">c</td>
    </tr>
  </tbody>
</table>
</div>


There is an embedding of `ACSetSpec` into `Expr`:


```julia
hspec = acsetspec(:(LabeledGraph{Symbol}),quote
    V(label=a)
    V(label=b)
    V(label=c)
    E(src=1,tgt=3)
    E(src=2,tgt=3)
end
)
```


```
LabeledGraph{Symbol} begin 
  V(label=a)
  V(label=b)
  V(label=c)
  E(src=1,tgt=3)
  E(src=2,tgt=3)
 end
```


The `acsetspec` function is a good example of embedding your custom language into Julia syntax That save you the trouble of writing your own lexer and parser for your custom language.


```julia
construct(LabeledGraph{Symbol}, hspec) == construct(LabeledGraph{Symbol}, gspec)
```


```
true
```


You can export your specification to a dictionary and put that dictionary into a JSON document this gives you a nice way of serializing the ACSet that is machine readable and row oriented. The ACSet serialization is by column oriented which might be inconvenient for your consumers.


```julia
to_dict(gspec)
```


```
Dict{Symbol, Any} with 2 entries:
  :type => "LabeledGraph{Symbol}"
  :data => Dict{Symbol, Any}[Dict(:table=>:V, :fields=>Dict(:label=>:a)), Dict(…
```

