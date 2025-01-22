


# Wiring diagrams

**`Catlab.WiringDiagrams.DirectedWiringDiagrams`** &mdash; *Module*.



Data structure for (directed) wiring diagrams, aka string diagrams.

A (directed) wiring diagram consists of a collection of boxes with input and output ports connected by wires. A box can be atomic (possessing no internal structure) or can itself be a wiring diagram. Thus, wiring diagrams can be nested recursively. Wiring diagrams are closely related to what the CS literature calls "directed graphs with ports" or more simply "port graphs". The main difference is that a wiring diagram has an "outer box": a wiring diagram has its own ports that can be connected to the ports of its boxes.

This module provides a generic data structure for wiring diagrams. Arbitrary data can be attached to the boxes, ports, and wires of a wiring diagram. The diagrams are "abstract" in the sense that they cannot be directly rendered as raster or vector graphics. However, they form a useful intermediate representation that can be serialized to and from GraphML or translated into Graphviz or other declarative diagram languages.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.AbstractBox`** &mdash; *Type*.



Base type for any box (node) in a wiring diagram.

This type represents an arbitrary black box with inputs and outputs.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.Box`** &mdash; *Type*.



An atomic box in a wiring diagram.

These boxes have no internal structure.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.Port`** &mdash; *Type*.



A port on a box to which wires can be connected.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.PortKind`** &mdash; *Type*.



Kind of port: input or output.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.Wire`** &mdash; *Type*.



A wire connecting one port to another.

**`Catlab.CategoricalAlgebra.FinCats.graph`** &mdash; *Method*.



Grapn underlying wiring diagram, including parts for noin-internal wires.

The graph has two special vertices representing the input and output boundaries of the outer box.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.encapsulate`** &mdash; *Method*.



Encapsulate multiple boxes within a single sub-diagram.

This operation is a (one-sided) inverse to subsitution, see [`substitute`](wiring_diagrams.md#Catlab.WiringDiagrams.DirectedWiringDiagrams.substitute-Tuple{WiringDiagram}).

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.encapsulated_subdiagram`** &mdash; *Method*.



Create an encapsulating box for a set of boxes in a wiring diagram.

To a first approximation, the union of input ports of the given boxes will become the inputs ports of the encapsulating box and likewise for the output ports. However, when copies or merges occur, as in a cartesian or cocartesian category, a simplification procedure may reduce the number of ports on the encapsulating box.

Specifically:

1. Each input port of an encapsulated box will have at most one incoming wire

from the encapsulating outer box, and each output port of an encapsulated box will have at most one outgoing wire to the encapsulating outer box.

2. A set of ports connected to the same outside (non-encapsulated) ports will be

simplified into a single port of the encapsulating box.

See also `induced_subdiagram`.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.in_wires`** &mdash; *Method*.



Get all wires coming into the box.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.in_wires`** &mdash; *Method*.



Get all wires coming into the port.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.induced_subdiagram`** &mdash; *Method*.



The wiring diagram induced by a subset of its boxes.

See also `encapsulated_subdiagram`.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.internal_graph`** &mdash; *Method*.



Graph underlying wiring diagram, with edges for internal wires only.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.ocompose`** &mdash; *Method*.



Operadic composition of wiring diagrams.

This generic function has two different signatures, corresponding to the "full" and "partial" notions of operadic composition (Yau, 2018, *Operads of Wiring Diagrams*, Definitions 2.3 and 2.10).

This operation is a simple wrapper around [`substitute`](wiring_diagrams.md#Catlab.WiringDiagrams.DirectedWiringDiagrams.substitute-Tuple{WiringDiagram}).

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.out_wires`** &mdash; *Method*.



Get all wires coming out of the box.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.out_wires`** &mdash; *Method*.



Get all wires coming out of the port.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.singleton_diagram`** &mdash; *Method*.



Wiring diagram with a single box connected to the outer ports.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.substitute`** &mdash; *Method*.



Substitute wiring diagrams for boxes.

Performs one or more substitutions. When performing multiple substitutions, the substitutions are simultaneous.

This operation implements the operadic composition of wiring diagrams, see also [`ocompose`](wiring_diagrams.md#Catlab.WiringDiagrams.DirectedWiringDiagrams.ocompose-Tuple{WiringDiagram, Vector{<:WiringDiagram}}).

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.validate_ports`** &mdash; *Method*.



Check compatibility of source and target ports.

The default implementation is a no-op.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.wires`** &mdash; *Method*.



Get all wires coming into or out of the box.

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams`** &mdash; *Module*.



Data structure for undirected wiring diagrams.

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams.AbstractUWD`** &mdash; *Type*.



Abstract type for UWDs, typed or untyped, possibly with extra attributes.

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams.HasUWD`** &mdash; *Type*.



Abstract type for C-sets that contain a UWD.

This type includes UWDs, scheduled UWDs, and nested UWDs.

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams.TypedUWD`** &mdash; *Type*.



A typed undirected wiring diagram.

A UWD whose ports and junctions must be compatibly typed.

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams.UntypedUWD`** &mdash; *Type*.



An undirected wiring diagram.

The most basic kind of UWD, without types or other extra attributes.

**`Catlab.WiringDiagrams.DirectedWiringDiagrams.add_wire!`** &mdash; *Method*.



Wire together two ports in an undirected wiring diagram.

A convenience method that creates and sets junctions as needed. Ports are only allowed to have one junction, so if both ports already have junctions, then the second port is assigned the junction of the first. The handling of the two arguments is otherwise symmetric.

FIXME: When both ports already have junctions, the two junctions should be *merged*. To do this, we must implement `merge_junctions!` and thus also `rem_part!`.

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams.cospan_diagram`** &mdash; *Method*.



Undirected wiring diagram defined by a cospan.

The wiring diagram has a single box. The ports of this box, the outer ports, the junctions, and the connections between them are defined by the cospan. Thus, this function generalizes [`singleton_diagram`](wiring_diagrams.md#Catlab.WiringDiagrams.DirectedWiringDiagrams.singleton_diagram-Tuple{Type, AbstractBox}).

See also: [`junction_diagram`](wiring_diagrams.md#Catlab.WiringDiagrams.UndirectedWiringDiagrams.junction_diagram-Union{Tuple{UWD}, Tuple{Type{UWD}, SetFunction{Dom, Codom} where {Dom<:(FinSet{Int64}), Codom<:(FinSet{Int64})}}, Tuple{Type{UWD}, SetFunction{Dom, Codom} where {Dom<:(FinSet{Int64}), Codom<:(FinSet{Int64})}, Any}} where UWD<:AbstractUWD).

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams.junction_diagram`** &mdash; *Method*.



Undirected wiring diagram with no boxes, only junctions.

See also: [`singleton_diagram`](wiring_diagrams.md#Catlab.WiringDiagrams.DirectedWiringDiagrams.singleton_diagram-Tuple{Type, AbstractBox}), [`cospan_diagram`](wiring_diagrams.md#Catlab.WiringDiagrams.UndirectedWiringDiagrams.cospan_diagram-Union{Tuple{UWD}, Tuple{Type{UWD}, SetFunction{Dom, Codom} where {Dom<:(FinSet{Int64}), Codom<:(FinSet{Int64})}, SetFunction{Dom, Codom} where {Dom<:(FinSet{Int64}), Codom<:(FinSet{Int64})}}, Tuple{Type{UWD}, SetFunction{Dom, Codom} where {Dom<:(FinSet{Int64}), Codom<:(FinSet{Int64})}, SetFunction{Dom, Codom} where {Dom<:(FinSet{Int64}), Codom<:(FinSet{Int64})}, Any}} where UWD<:AbstractUWD).

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams`** &mdash; *Module*.



Wiring diagrams as a symmetric monoidal category.

This module provides a high-level categorical interface to wiring diagrams, building on the low-level imperative interface and the operadic interface. It also defines data types and functions to represent diagonals, codiagonals, duals, caps, cups, daggers, and other gadgets in wiring diagrams.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.BoxOp`** &mdash; *Type*.



Box wrapping another box.

Represents unary operations on boxes in wiring diagrams.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.Junction`** &mdash; *Type*.



Junction node in a wiring diagram.

Junction nodes are used to explicitly represent copies, merges, deletions, creations, caps, and cups.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.PortOp`** &mdash; *Type*.



Port value wrapping another value.

Represents unary operations on ports in wiring diagrams.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.Ports`** &mdash; *Type*.



A list of ports.

The objects in categories of wiring diagrams.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.add_junctions`** &mdash; *Method*.



Add junction nodes to wiring diagram.

Transforms from the implicit to the explicit representation of diagonals and codiagonals. This operation is inverse to `rem_junctions`.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.implicit_mcopy`** &mdash; *Method*.



Implicit copy in wiring diagram.

Copies are represented by multiple outgoing wires from a single port and deletions by no outgoing wires.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.implicit_mmerge`** &mdash; *Method*.



Implicit merge in wiring diagram.

Merges are represented by multiple incoming wires into a single port and creations by no incoming wires.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.junction_caps`** &mdash; *Method*.



Wiring diagram of nested caps made out of junction nodes.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.junction_cups`** &mdash; *Method*.



Wiring diagram of nested cups made out of junction nodes.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.junctioned_mcopy`** &mdash; *Method*.



Explicit copy in wiring diagram.

Copies and deletions are represented by junctions (boxes of type `Junction`).

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.junctioned_mmerge`** &mdash; *Method*.



Explicit merge in wiring diagram.

Merges and creations are represented by junctions (boxes of type `Junction`).

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.merge_junctions`** &mdash; *Method*.



Merge adjacent junction nodes into single junctions.

**`Catlab.WiringDiagrams.MonoidalDirectedWiringDiagrams.rem_junctions`** &mdash; *Method*.



Remove junction nodes from wiring diagram.

Transforms from the explicit to the implicit representation of diagonals and codiagonals. This operation is inverse to `add_junctions`.

**`Catlab.WiringDiagrams.UndirectedWiringDiagrams.junction_diagram`** &mdash; *Method*.



Wiring diagram with a junction node for each of the given ports.

**`GATlab.Models.SymbolicModels.functor`** &mdash; *Method*.



Apply functor in a category of wiring diagrams.

Defined by compatible mappings of ports and boxes.

**`Catlab.WiringDiagrams.WiringDiagramAlgorithms`** &mdash; *Module*.



Algorithms on wiring diagrams.

**`Catlab.Graphs.GraphAlgorithms.topological_sort`** &mdash; *Method*.



Topological sort of boxes in wiring diagram.

Returns a list of box IDs, excluding the outer box's input and output IDs.

**`Catlab.WiringDiagrams.WiringDiagramAlgorithms.crossing_minimization_by_sort`** &mdash; *Method*.



Crossing minimization by sorting a univariate statistic.

The boxes in `sources` and/or `targets` are fixed and the boxes in `vs` are permuted. A permutation `σ` of the latter is returned, such that `vs[σ]` are the sorted box IDs. Both one-sided and two-sided crossing minimization are supported, depending on whether just one, or both, of `sources` and `targets` are given.

In this simple but popular heuristic algorithm, the boxes are permuted by sorting a univariate statistic of the positions of incoming and/or outgoing wires. Typical choices are:

  * `mean`: the sample mean, yielding the "barycenter method"
  * `median`: the sample median

In both cases, this algorithm has the property that if there is a permutation with no crossings, it will find it.

**`Catlab.WiringDiagrams.WiringDiagramAlgorithms.normalize_cartesian!`** &mdash; *Method*.



Put a wiring diagram for a cartesian category into normal form.

This function puts a wiring diagram representing a morphism in a free cartesian category into normal form. Copies and deletions are simplified as much as possible.

**`Catlab.WiringDiagrams.WiringDiagramAlgorithms.normalize_copy!`** &mdash; *Method*.



Normalize copies in a wiring diagram.

This function maximizes sharing of intermediate computations in a wiring diagram where copies are natural.

This algorithm is basically the same as the congruence closure algorithm on term graphs, in the special case of the empty relation R = ∅ (Baader & Nipkow, 1998, Term Rewriting and All That, Sec. 4.4). The main difference is the possibility of zero or many function outputs.

**`Catlab.WiringDiagrams.WiringDiagramAlgorithms.normalize_delete!`** &mdash; *Method*.



Normalize deletions in a wiring diagram.

This function removes all unused intermediate computations in a wiring diagram where deletion is natural.

**`Catlab.WiringDiagrams.WiringDiagramSerialization`** &mdash; *Module*.



Conventions for serialization of wiring diagrams.

Defines a consistent set of names for boxes, ports, and wires to be used when serializing wiring diagrams, as well as conventions for serializing box, port, and wire attributes.

**`Catlab.WiringDiagrams.GraphMLWiringDiagrams`** &mdash; *Module*.



Serialize abstract wiring diagrams as GraphML.

Serialization of box, port, and wire values can be overloaded by data type (see `convert_to_graphml_data` and `convert_from_graphml_data`).

GraphML is the closest thing to a de jure and de facto standard in the space of graph data formats, supported by a variety of graph applications and libraries. We depart mildly from the GraphML spec by allowing JSON data attributes for GraphML nodes, ports, and edges.

References:

  * GraphML Primer: http://graphml.graphdrawing.org/primer/graphml-primer.html
  * GraphML DTD: http://graphml.graphdrawing.org/specification/dtd.html

**`Catlab.WiringDiagrams.GraphMLWiringDiagrams.generate_graphml`** &mdash; *Method*.



Generate GraphML representing a wiring diagram.

**`Catlab.WiringDiagrams.GraphMLWiringDiagrams.parse_graphml`** &mdash; *Method*.



Parse a wiring diagram from a GraphML string or XML document.

**`Catlab.WiringDiagrams.GraphMLWiringDiagrams.read_graphml`** &mdash; *Method*.



Read a wiring diagram from a GraphML file.

**`Catlab.WiringDiagrams.GraphMLWiringDiagrams.write_graphml`** &mdash; *Method*.



Write a wiring diagram to a file as GraphML.

**`Catlab.WiringDiagrams.JSONWiringDiagrams`** &mdash; *Module*.



Serialize abstract wiring diagrams as JSON.

JSON data formats are convenient when programming for the web. Unfortunately, no standard for JSON graph formats has gained any kind of widespread adoption. We adopt a format compatible with that used by the KEILER project and its successor ELK (Eclipse Layout Kernel). This format is roughly feature compatible with GraphML, supporting nested graphs and ports. It also supports layout information like node position and size.

References:

  * KEILER's JSON graph format: https://rtsys.informatik.uni-kiel.de/confluence/display/KIELER/JSON+Graph+Format
  * ELK's JSON graph format: https://www.eclipse.org/elk/documentation/tooldevelopers/graphdatastructure/jsonformat.html

**`Catlab.WiringDiagrams.JSONWiringDiagrams.generate_json_graph`** &mdash; *Method*.



Generate a JSON dict representing a wiring diagram.

**`Catlab.WiringDiagrams.JSONWiringDiagrams.parse_json_graph`** &mdash; *Method*.



Parse a wiring diagram from a JSON string or dict.

**`Catlab.WiringDiagrams.JSONWiringDiagrams.read_json_graph`** &mdash; *Method*.



Read a wiring diagram from a JSON file.

**`Catlab.WiringDiagrams.JSONWiringDiagrams.write_json_graph`** &mdash; *Method*.



Write a wiring diagram to a file as JSON.

