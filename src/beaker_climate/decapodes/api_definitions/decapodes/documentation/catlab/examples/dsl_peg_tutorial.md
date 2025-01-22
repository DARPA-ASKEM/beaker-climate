




# Domain Specific Parsing Expression Grammars


The purpose of this documentation is to provide a high-level tutorial on utilizing parsing expression grammars for domain-specific language development within Catlab. This tutorial will provide a brief overview of the PEG.jl library and how it is used. Additionally, this tutorial will demonstrate a use case of PEG.jl in the context of parsing a simple language for defining undirected wiring diagrams.




## Developing a Parsing Expression Grammar for Catlab




### PEG.jl


PEG.jl is a parsing expression grammar library for Julia. It allows us to define a grammar via a macro `@rule`. This allows us to define a formal set of rules for parsing a language. Let us look at a brief example of how this looks.


First, we import the necessary modules.


```julia
using PEG
```


Next, we define a simple grammar for parsing a language that contains a single word.


```julia
@rule simpleGrammar = "hello"
```


```
simpleGrammar (generic function with 2 methods)
```


If we were to parse a string that contained `"hello"` using `parse_whole(simpleGrammar, "hello")`, we would get a successful parse.


Ideally, we want to parse a more complex language than just the word "Hello". We can utilize the `@rule` macro to create multiple rules nested within each other. See how this mimics a recursive descent parser? Let us illustrate this with a simple example: parsing a language that contains a singular function call.


```julia
@rule functionCall = identifier & r"\(" & arguments & r"\)"
@rule arguments = (identifier & r"\s*" & r","p)[*] & identifier
@rule identifier = r"[a-zA-Z_][a-zA-Z0-9_]*"
```


```
identifier (generic function with 2 methods)
```


We can read the above grammar left to right and top to bottom.


  * We have a function call that expects an identifier followed by an open parenthesis, a list of arguments, and a closing parenthesis.
  * The arguments are a list of identifiers separated by commas with optional whitespaces.
  * An identifier is a string that starts with a letter or underscore and is followed by letters, numbers, or underscores.


We can also define transformations for our rules that allow us to modify how our parse tree is generated.


Additionally, we can make changes to elements in our parse tree to better suit our needs. This is illustrated below.


```julia
@rule transformationRule = identifier & r"\(" & arguments & r"\)" |> v -> v[1]
```


```
transformationRule (generic function with 2 methods)
```


The above rule will only return the identifier from the function call. This is done by using the `|>` operator to apply a transformation to the parse tree. The transformation is a lambda function that takes the parse tree as input and returns the desired output. We could make a tree more complex by calling functions within our lambda that express semantic analysis. For more PEG.jl specific syntax, please refer to the [PEG.jl documentation](https://github.com/wdebeaum/PEG.jl)




### Motivation For Developing a PEG for Catlab


The motivation behind developing a parsing expression grammar to support domain specifc languages within Catlab lies in two core reasons:


  * To discontinue dependency on Julia metaprogramming for defining domain specific languages.

      * Metaprogramming restricts developers to Julia syntax. This can be limiting when we want DSL features that contradict Julia syntax.
  * To provide a simpler way to develop and maintain domain specific languages.

      * PEG.jl provides a more readable and maintainable way to define a grammar.

          * This allows for easier debugging and development of domain specific languages.
      * Reusability of exportable grammar rules means less reinventing the wheel.

          * Less reinventing the wheel means less time spent on development.




### Developing a PEG for Catlab


Core components for developing a domain specific language in Catlab exist in the `Catlab.Parsers` module. `Catlab.Parsers.ParserCore` provides the core functionality for developing a PEG.


Currently `ParserCore` supports lexical rules as follows:


```julia
@rule ws = r"\s*"
@rule eq = r"="p
@rule lparen = r"\("
@rule rparen = r"\)"
@rule comma = r","p
@rule EOL = "\n" , r";"
@rule colon = r":"p
@rule ident = r"[^:{}→\n;=,\(\)\s]+"
```


```
ident (generic function with 2 methods)
```


The above rules allow us to break our string input into tokens. The above rules can be imported into your parsing expression grammar via: `using Catlab.Parsers.ParserCore`.


`ParserCore` also provides basic syntax for defining a PEG. For instance, the `expr` rule will parse a Julia expression.


`ParserCore` also provides functions that can be called within transformations:


  * `parse_identifier`: Called to properly construct an `ident` into a symbol or integer.
  * `collect`: Called to collect a list of elements into a flattened list.


In the future, `ParserCore` will contain more general rules for parsing domain specific languages. More specific rules are defined in their respective modules within `Catlab.Parsers`. While `ParserCore` is a work in progress, `Catlab.Parsers.RelationalParser` holds important domain specifc language constructs which we can reuse. This module contains the parsing expression grammar for building undirected wiring diagrams. For those who want to get ahead on developing domain specific languages now, `RelationalParser` has core constructs one may copy into their own parsing expression grammar. Let us illustrate some core PEG rules from `RelationalParser` that offer reusability.




#### Core PEG Rules


`@rule args = (arg & (ws & comma & ws & arg)[*])[:?]  |> v -> collect(v)`


The above rule defines a list of arguments separated by commas.


  * It requires lexical rules for whitespace and commas.
  * It uses the `collect` function to flatten the list of arguments.
  * You will need to define your `arg` rule specific to your language.


`@rule line = ws & statement & r"[^\S\r\n]*" & EOL |> v->v[2]`


The above rule defines a line of code with an undefined statement rule. The statement rule will depend on what your language allows. For instance, this might be a function call.


`@rule body = r"{\s*"p & line[*] & r"\n?}"p |> v->v[2]`


The above rule defines a body of code enclosed in braces.


These are the core syntactical constructs that are likely to remain the same across domain specific languages. By reusing these rules, you can save time and effort in developing your own parsing expression grammar.




## Parsing a Simple Language for Defining Undirected Wiring Diagrams


Now, let's look at a use case of developing a domain specific language for defining undirected wiring diagrams. First, lets import the necessary modules for this tutorial. GraphViz will need to be installed to output the diagrams.


```julia
using Catlab.Parsers, Catlab.WiringDiagrams, Catlab.Graphics
```




### Basic Language syntax


Our language supports the following syntax:


  * We are expected to call our language using the `relation` string macro.
  * The first unit in our syntax is the definition of outer ports: `(x, z)`.
  * The second unit is the `where` clause: `where (x,y,z)`.
  * The third unit is the relations that make up the diagram: `{R(x,y); S(y,z);}`.


Let us look at a few examples of how this language can be used.




### Untyped Undirected Wiring Diagram


In this example, we will parse a simple language for defining an untyped undirected wiring diagram.


```julia
unTypedDiagram = relation"(x,z) where (x,y,z) {R(x,y); S(y,z);}"
to_graphviz(unTypedDiagram, box_labels=:name)
```

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.43.0 (0)
 -->
<!-- Title: G Pages: 1 -->
<svg width="57pt" height="220pt"
 viewBox="0.00 0.00 57.00 219.74" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 215.74)">
<title>G</title>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-215.74 53,-215.74 53,4 -4,4"/>
<!-- n1 -->
<g id="box1" class="node">
<title>n1</title>
<ellipse fill="none" stroke="black" cx="31" cy="-71.29" rx="18" ry="18"/>
<text text-anchor="middle" x="31" y="-67.59" font-family="Serif" font-size="14.00">R</text>
</g>
<!-- n5 -->
<!-- junction -->
<g id="junction1" class="node">
<title>n5</title>
<ellipse fill="black" stroke="black" cx="39.23" cy="-36.16" rx="2.5" ry="2.5"/>
</g>
<!-- n1&#45;&#45;n5 -->
<g id="edge1" class="edge">
<title>n1&#45;&#45;n5</title>
<path fill="none" stroke="black" d="M35.11,-53.73C36.46,-47.96 37.81,-42.2 38.58,-38.92"/>
</g>
<!-- n6 -->
<!-- junction -->
<g id="junction2" class="node">
<title>n6</title>
<ellipse fill="black" stroke="black" cx="29.17" cy="-107.36" rx="2.5" ry="2.5"/>
</g>
<!-- n1&#45;&#45;n6 -->
<g id="edge3" class="edge">
<title>n1&#45;&#45;n6</title>
<path fill="none" stroke="black" d="M30.08,-89.33C29.78,-95.24 29.48,-101.16 29.31,-104.53"/>
</g>
<!-- n2 -->
<g id="box2" class="node">
<title>n2</title>
<ellipse fill="none" stroke="black" cx="24.41" cy="-143.16" rx="18" ry="18"/>
<text text-anchor="middle" x="24.41" y="-139.46" font-family="Serif" font-size="14.00">S</text>
</g>
<!-- n2&#45;&#45;n6 -->
<g id="edge4" class="edge">
<title>n2&#45;&#45;n6</title>
<path fill="none" stroke="black" d="M26.79,-125.26C27.57,-119.39 28.35,-113.51 28.8,-110.17"/>
</g>
<!-- n7 -->
<!-- junction -->
<g id="junction3" class="node">
<title>n7</title>
<ellipse fill="black" stroke="black" cx="13.69" cy="-177.66" rx="2.5" ry="2.5"/>
</g>
<!-- n2&#45;&#45;n7 -->
<g id="edge5" class="edge">
<title>n2&#45;&#45;n7</title>
<path fill="none" stroke="black" d="M19.05,-160.41C17.29,-166.07 15.53,-171.73 14.53,-174.95"/>
</g>
<!-- n3 -->
<!-- n3&#45;&#45;n5 -->
<g id="edge2" class="edge">
<title>n3&#45;&#45;n5</title>
<path fill="none" stroke="black" d="M44.19,-1.38C43.55,-5.84 40.67,-26.01 39.62,-33.42"/>
</g>
<!-- n4 -->
<!-- n4&#45;&#45;n7 -->
<g id="edge6" class="edge">
<title>n4&#45;&#45;n7</title>
<path fill="none" stroke="black" d="M0.83,-210.41C2.48,-206.21 9.94,-187.21 12.68,-180.24"/>
</g>
</g>
</svg>




### Typed Undirected Wiring Diagram


Now, let us look at a typed example


```julia
TypedDiagram = relation"(x,y,z) where (x:X, y:Y, z:Z, w:W) {
  R(x,w);
  S(y,w);
  T(z,w);}"
to_graphviz(TypedDiagram, box_labels=:name)
```

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.43.0 (0)
 -->
<!-- Title: G Pages: 1 -->
<svg width="205pt" height="197pt"
 viewBox="0.00 0.00 205.07 197.09" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 193.09)">
<title>G</title>
<polygon fill="white" stroke="transparent" points="-4,4 -4,-193.09 201.07,-193.09 201.07,4 -4,4"/>
<!-- n1 -->
<g id="box1" class="node">
<title>n1</title>
<ellipse fill="none" stroke="black" cx="56.97" cy="-49.19" rx="18" ry="18"/>
<text text-anchor="middle" x="56.97" y="-45.49" font-family="Serif" font-size="14.00">R</text>
</g>
<!-- n7 -->
<!-- junction -->
<g id="junction1" class="node">
<title>n7</title>
<ellipse fill="black" stroke="black" cx="29" cy="-23.81" rx="2.5" ry="2.5"/>
</g>
<!-- n1&#45;&#45;n7 -->
<g id="edge1" class="edge">
<title>n1&#45;&#45;n7</title>
<path fill="none" stroke="black" d="M43.64,-37.09C38.69,-32.6 33.63,-28 30.95,-25.57"/>
</g>
<!-- n10 -->
<!-- junction -->
<g id="junction4" class="node">
<title>n10</title>
<ellipse fill="black" stroke="black" cx="87.06" cy="-76.06" rx="2.5" ry="2.5"/>
</g>
<!-- n1&#45;&#45;n10 -->
<g id="edge7" class="edge">
<title>n1&#45;&#45;n10</title>
<path fill="none" stroke="black" d="M70.61,-61.37C76.08,-66.26 81.81,-71.37 84.85,-74.08"/>
</g>
<!-- n2 -->
<g id="box2" class="node">
<title>n2</title>
<ellipse fill="none" stroke="black" cx="125.37" cy="-63.43" rx="18" ry="18"/>
<text text-anchor="middle" x="125.37" y="-59.73" font-family="Serif" font-size="14.00">S</text>
</g>
<!-- n8 -->
<!-- junction -->
<g id="junction2" class="node">
<title>n8</title>
<ellipse fill="black" stroke="black" cx="161.15" cy="-51.32" rx="2.5" ry="2.5"/>
</g>
<!-- n2&#45;&#45;n8 -->
<g id="edge3" class="edge">
<title>n2&#45;&#45;n8</title>
<path fill="none" stroke="black" d="M142.42,-57.66C148.76,-55.52 155.23,-53.32 158.66,-52.16"/>
</g>
<!-- n2&#45;&#45;n10 -->
<g id="edge8" class="edge">
<title>n2&#45;&#45;n10</title>
<path fill="none" stroke="black" d="M108.01,-69.15C100.88,-71.5 93.42,-73.96 89.62,-75.22"/>
</g>
<!-- n3 -->
<g id="box3" class="node">
<title>n3</title>
<ellipse fill="none" stroke="black" cx="78.84" cy="-115.56" rx="18" ry="18"/>
<text text-anchor="middle" x="78.84" y="-111.86" font-family="Serif" font-size="14.00">T</text>
</g>
<!-- n9 -->
<!-- junction -->
<g id="junction3" class="node">
<title>n9</title>
<ellipse fill="black" stroke="black" cx="71.14" cy="-152.54" rx="2.5" ry="2.5"/>
</g>
<!-- n3&#45;&#45;n9 -->
<g id="edge5" class="edge">
<title>n3&#45;&#45;n9</title>
<path fill="none" stroke="black" d="M75.08,-133.62C73.74,-140.07 72.38,-146.59 71.66,-150.04"/>
</g>
<!-- n3&#45;&#45;n10 -->
<g id="edge9" class="edge">
<title>n3&#45;&#45;n10</title>
<path fill="none" stroke="black" d="M82.57,-97.66C84.1,-90.31 85.7,-82.62 86.51,-78.7"/>
</g>
<!-- n4 -->
<!-- n4&#45;&#45;n7 -->
<g id="edge2" class="edge">
<title>n4&#45;&#45;n7</title>
<path fill="none" stroke="black" d="M1.2,-1.08C4.77,-3.99 20.89,-17.17 26.81,-22.02"/>
</g>
<!-- n5 -->
<!-- n5&#45;&#45;n8 -->
<g id="edge4" class="edge">
<title>n5&#45;&#45;n8</title>
<path fill="none" stroke="black" d="M195.69,-41.52C191.26,-42.78 171.23,-48.46 163.87,-50.55"/>
</g>
<!-- n6 -->
<!-- n6&#45;&#45;n9 -->
<g id="edge6" class="edge">
<title>n6&#45;&#45;n9</title>
<path fill="none" stroke="black" d="M63.86,-187.7C64.8,-183.18 69.02,-162.79 70.57,-155.31"/>
</g>
</g>
</svg>


Furthermore, we can generate more complex diagrams with different types. This domain specific language supports symbol types, integer types, expression types, as well as mixed types. The above typed diagram illustrated the use of symbol types.


The syntax for integer types is as follows: `x:1`


The syntax for expression types is as follows: `x:n(1)`


The syntax for mixed types is as follows: `x:X, y:1, z:n(1), w:W`




### Named Ports


Undirected Wiring Diagrams may also contain named ports. This motivates our language to support such a feature. Below is an example of a diagram with named ports.


```julia
employeeDirectory = relation"(e=e, e′=e′) where (e:Employee, e′:Employee, d:Department) {
    Employee(id=e, department=d);
    Employee(id=e′, department=d);}"
```

<div class="c-set">
<span class="c-set-summary">Catlab.WiringDiagrams.RelationDiagrams.TypedNamedRelationDiagram{Symbol, Symbol, Symbol} {Box:2, Port:4, OuterPort:2, Junction:3, Type:0, Name:0, VarName:0}</span>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Box</th>
      <th style = "text-align: right;">name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">Employee</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">Employee</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Port</th>
      <th style = "text-align: right;">box</th>
      <th style = "text-align: right;">junction</th>
      <th style = "text-align: right;">port_type</th>
      <th style = "text-align: right;">port_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">Employee</td>
      <td style = "text-align: right;">id</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">3</td>
      <td style = "text-align: right;">Department</td>
      <td style = "text-align: right;">department</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">Employee</td>
      <td style = "text-align: right;">id</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">4</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">3</td>
      <td style = "text-align: right;">Department</td>
      <td style = "text-align: right;">department</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">OuterPort</th>
      <th style = "text-align: right;">outer_junction</th>
      <th style = "text-align: right;">outer_port_type</th>
      <th style = "text-align: right;">outer_port_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">Employee</td>
      <td style = "text-align: right;">e</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">Employee</td>
      <td style = "text-align: right;">e′</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Junction</th>
      <th style = "text-align: right;">junction_type</th>
      <th style = "text-align: right;">variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">Employee</td>
      <td style = "text-align: right;">e</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">Employee</td>
      <td style = "text-align: right;">e′</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">Department</td>
      <td style = "text-align: right;">d</td>
    </tr>
  </tbody>
</table>
</div>




### Infered Context


Our language also supports a context of variables for a undirected wiring diagram. If the parameters in the `where` clause are omitted, we can infer these.


Below is an example of a diagram with inferred context.


```julia
inferredCase = relation"(x,y,z) where () {R(x,y); S(y,z);}"
```

<div class="c-set">
<span class="c-set-summary">Catlab.WiringDiagrams.RelationDiagrams.UntypedUnnamedRelationDiagram{Symbol, Symbol} {Box:2, Port:4, OuterPort:3, Junction:3, Name:0, VarName:0}</span>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Box</th>
      <th style = "text-align: right;">name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">R</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">S</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Port</th>
      <th style = "text-align: right;">box</th>
      <th style = "text-align: right;">junction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">2</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">2</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">4</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">3</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">OuterPort</th>
      <th style = "text-align: right;">outer_junction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">2</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">3</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Junction</th>
      <th style = "text-align: right;">variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">x</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">y</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">z</td>
    </tr>
  </tbody>
</table>
</div>




### Closed Diagram


Lastly, in the case we want a closed diagram, we simply omit the outer ports in the diagram. This is illustrated below.


```julia
parsed = relation"() where (S:Pop, I:Pop, R:Pop, D:Pop) {
  infect(S,I,I,I)
  disease(I,R)
  disease(I,D);}"
```

<div class="c-set">
<span class="c-set-summary">Catlab.WiringDiagrams.RelationDiagrams.TypedUnnamedRelationDiagram{Symbol, Symbol, Symbol} {Box:3, Port:8, OuterPort:0, Junction:4, Type:0, Name:0, VarName:0}</span>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Box</th>
      <th style = "text-align: right;">name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">infect</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">disease</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">disease</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Port</th>
      <th style = "text-align: right;">box</th>
      <th style = "text-align: right;">junction</th>
      <th style = "text-align: right;">port_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">4</td>
      <td style = "text-align: right;">1</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">5</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">6</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">3</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">7</td>
      <td style = "text-align: right;">3</td>
      <td style = "text-align: right;">2</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">8</td>
      <td style = "text-align: right;">3</td>
      <td style = "text-align: right;">4</td>
      <td style = "text-align: right;">Pop</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr class = "header headerLastRow">
      <th class = "rowLabel" style = "font-weight: bold; text-align: right;">Junction</th>
      <th style = "text-align: right;">junction_type</th>
      <th style = "text-align: right;">variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">1</td>
      <td style = "text-align: right;">Pop</td>
      <td style = "text-align: right;">S</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">2</td>
      <td style = "text-align: right;">Pop</td>
      <td style = "text-align: right;">I</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">3</td>
      <td style = "text-align: right;">Pop</td>
      <td style = "text-align: right;">R</td>
    </tr>
    <tr>
      <td class = "rowLabel" style = "font-weight: bold; text-align: right;">4</td>
      <td style = "text-align: right;">Pop</td>
      <td style = "text-align: right;">D</td>
    </tr>
  </tbody>
</table>
</div>

