


# Parsers


This module `Catlab.Parsers` provides parsing expression grammars to support domain-specific languages (DSLs) for constructing diagrams of various kinds. The DSLs, implemented as Julia string macros, are based on the syntax of their `Catlab.Programs` counterparts which are based on the syntax of the Julia language but often interpret that syntax very differently from standard Julia programs.


As of now, there is currently only one parsing expression grammar for constructing wiring diagrams:


  * [`relation_str`](@ref) for constructing undirected wiring diagrams.




## API

**`Catlab.Parsers.ParserCore`** &mdash; *Module*.



Core components of a Parsing Expression Grammar

**`Catlab.Parsers.ParserCore.collect`** &mdash; *Method*.



Collect

This function collects and flattens arguments of the PEG.jl rule format "(arg & (ws & comma & ws & arg)[*])[:?]" only. It supports lists such as "()" and "(a)" and "(a,b,c)"

**`Catlab.Parsers.ParserCore.parse_identifier`** &mdash; *Method*.



Parse Identifier

This function parses an identifier into a symbol or integer. If the identifier is a number, it will be parsed as an integer, otherwise it will be parsed as a symbol.

**`Catlab.Parsers.RelationalParser`** &mdash; *Module*.



```julia
RelationalParser
```

Parses string input into a `RelationDiagram` via a string macro combined with a parsing expression grammar that generates an ADT representation of an UWD to be constructed into an ACSet.

**`Catlab.Parsers.RelationalParser.@relation_str`** &mdash; *Macro*.



Relation String Macro

This macro parses a string representation of a UWD into an ACSet representation. It operates by parsing a string input into an UWDExpr object. Then it constructs a RelationDiagram object from the UWDExpr object.

