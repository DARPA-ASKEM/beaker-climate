


# Graphics

**`Catlab.Graphics.GraphvizGraphs`** &mdash; *Module*.



Graphviz support for Catlab's graph types.

**`Catlab.Graphics.GraphvizGraphs.parse_graphviz`** &mdash; *Method*.



Parse Graphviz output in JSON format.

Returns a property graph with graph layout and other metadata. Each node has a position and size.

All units are in points. Note that Graphviz has 72 points per inch.

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



Convert a property graph to a Graphviz graph.

This method is usually more convenient than direct AST manipulation for creating simple Graphviz graphs. For more advanced features, like nested subgraphs, you must use the Graphviz AST.

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



Visualize a bipartite graph using Graphviz.

Works for both directed and undirected bipartite graphs. Both types of vertices in the bipartite graph become nodes in the Graphviz graph.

**Arguments**

  * `prog="dot"`: Graphviz program to use
  * `graph_attrs`: Graph-level Graphviz attributes
  * `node_attrs`: Node-level Graphviz attributes
  * `edge_attrs`: Edge-level Graphviz attributes
  * `node_labels=false`: whether to label nodes and if so, which pair of data attributes to use
  * `edge_labels=false`: whether to label edges and if so, which data attribute (undirected case) or pair of attributes (directed case) to use
  * `invis_edge=true`: whether to add invisible edges between vertices of same type, which ensures that the order of the nodes is preserved.

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



Convert a graph to a Graphviz graph.

A simple default style is applied. For more control over the visual appearance, first convert the graph to a property graph, define the Graphviz attributes as needed, and finally convert the property graph to a Graphviz graph.

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



Visualize a graph homomorphism using Graphviz.

Visualize a homomorphism (`ACSetTransformation`) between two graphs (instances of `AbstractGraph`). By default, the domain and codomain are drawn as subgraphs and the vertex mapping is drawn using dotted edges, whereas the edge map is suppressed. The vertex and edge mapping can also be shown using colors, via the `node_colors` and `edge_colors` keyword arguments.

**Arguments**

  * `draw_codom=true`: whether to draw the codomain graph
  * `draw_mapping=true`: whether to draw the vertex mapping using edges
  * `prog="dot"`: Graphviz program to use
  * `graph_attrs`: Graph-level Graphviz attributes
  * `node_attrs`: Node-level Graphviz attributes
  * `edge_attrs`: Edge-level Graphviz attributes
  * `node_labels=false`: whether to draw node labels and which vertex attribute to use
  * `edge_labels=false`: whether to draw edge labels and which edge attribute to use
  * `node_colors=!draw_codom`: whether and how to color nodes based on vertex map
  * `edge_colors=!draw_codom`: whether and how to color edges based on edge map

**`Catlab.Graphics.GraphvizGraphs.to_graphviz_property_graph`** &mdash; *Method*.



Convert graph or other structure to a property graph suitable for Graphviz.

This function is an intermediate step in many methods of the generic function [`to_graphviz`](graphics.md#Catlab.Graphics.GraphvizGraphs.to_graphviz-Tuple{AbstractPropertyGraph}), but can be useful in its own right for customizing the Graphviz graph beyond whatever options are supported by [`to_graphviz`](graphics.md#Catlab.Graphics.GraphvizGraphs.to_graphviz-Tuple{AbstractPropertyGraph}).

**`Catlab.Graphics.ComposeWiringDiagrams`** &mdash; *Module*.



Draw wiring diagrams using Compose.jl.

**`Catlab.Graphics.ComposeWiringDiagrams.ComposePicture`** &mdash; *Type*.



A Compose context together with a given width and height.

We need this type because contexts have no notion of size or aspect ratio, but wiring diagram layouts have fixed aspect ratios.

**`Catlab.Graphics.ComposeWiringDiagrams.layout_to_composejl`** &mdash; *Method*.



Draw a wiring diagram in Compose.jl using the given layout.

**`Catlab.Graphics.ComposeWiringDiagrams.to_composejl`** &mdash; *Method*.



Draw a wiring diagram in Compose.jl.

**`Catlab.Graphics.GraphvizWiringDiagrams`** &mdash; *Module*.



Lay out and draw wiring diagrams using Graphviz.

This module requires Graphviz v2.42 or higher.

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



Draw an undirected wiring diagram using Graphviz.

Creates an undirected, bipartite Graphviz graph, with the boxes and outer ports of the diagram becoming nodes of one kind and the junctions of the diagram becoming nodes of the second kind.

**Arguments**

  * `graph_name="G"`: name of Graphviz graph
  * `prog="neato"`: Graphviz program, usually "neato" or "fdp"
  * `box_labels=false`: if boolean, whether to label boxes with their number;  if a symbol, name of data attribute for box label
  * `port_labels=false`: whether to label ports with their number
  * `junction_labels=false`: if boolean, whether to label junctions with their number; if a symbol, name of data attribute for junction label
  * `junction_size="0.075"`: size of junction nodes, in inches
  * `implicit_junctions=false`: whether to represent a junction implicity as a wire when it has exactly two incident ports
  * `graph_attrs=Dict()`: top-level graph attributes
  * `node_attrs=Dict()`: top-level node attributes
  * `edge_attrs=Dict()`: top-level edge attributes

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



Draw a circular port graph using Graphviz.

Creates a Graphviz graph. Ports are currently not respected in the image, but the port index for each box can be displayed to provide clarification.

**Arguments**

  * `graph_name="G"`: name of Graphviz graph
  * `prog="neato"`: Graphviz program, usually "neato" or "fdp"
  * `box_labels=false`: whether to label boxes with their number
  * `port_labels=false`: whether to label ports with their number
  * `graph_attrs=Dict()`: top-level graph attributes
  * `node_attrs=Dict()`: top-level node attributes
  * `edge_attrs=Dict()`: top-level edge attributes

TODO: The lack of ports might be able to be resolved by introducing an extra node per port which is connected to its box with an edge of length 0.

**`Catlab.Graphics.GraphvizGraphs.to_graphviz`** &mdash; *Method*.



Draw a wiring diagram using Graphviz.

The input can also be a morphism expression, in which case it is first converted into a wiring diagram. This function requires Graphviz v2.42 or higher.

**Arguments**

  * `graph_name="G"`: name of Graphviz digraph
  * `orientation=TopToBottom`: orientation of layout. One of `LeftToRight`, `RightToLeft`, `TopToBottom`, or `BottomToTop`.
  * `node_labels=true`: whether to label the nodes
  * `labels=false`: whether to label the edges
  * `label_attr=:label`: what kind of edge label to use (if `labels` is true). One of `:label`, `:xlabel`, `:headlabel`, or `:taillabel`.
  * `port_size="24"`: minimum size of ports on box, in points
  * `junction_size="0.05"`: size of junction nodes, in inches
  * `outer_ports=true`: whether to display the outer box's input and output ports. If disabled, no incoming or outgoing wires will be shown either!
  * `anchor_outer_ports=true`: whether to enforce ordering of the outer box's input and output, i.e., ordering of the incoming and outgoing wires
  * `graph_attrs=Dict()`: top-level graph attributes
  * `node_attrs=Dict()`: top-level node attributes
  * `edge_attrs=Dict()`: top-level edge attributes
  * `cell_attrs=Dict()`: main cell attributes in node HTML-like label

**`Catlab.Graphics.GraphvizWiringDiagrams.graphviz_layout`** &mdash; *Method*.



Lay out directed wiring diagram using Graphviz.

Note: At this time, only the positions and sizes of the boxes, and the positions of the outer ports, are used. The positions of the box ports and the splines for the wires are ignored.

**`Catlab.Graphics.TikZWiringDiagrams`** &mdash; *Module*.



Draw wiring diagrams using TikZ.

**`Catlab.Graphics.TikZWiringDiagrams.layout_to_tikz`** &mdash; *Method*.



Draw a wiring diagram in TikZ using the given layout.

**`Catlab.Graphics.TikZWiringDiagrams.to_tikz`** &mdash; *Method*.



Draw a wiring diagram in TikZ.

**`Catlab.Graphics.WiringDiagramLayouts`** &mdash; *Module*.



Backend-agnostic layout of wiring diagrams via morphism expressions.

This module lays out wiring diagrams for visualization, independent of any specific graphics system. It uses the structure of a morphism expression to determine the layout. Thus, the first step of the algorithm is to convert the wiring diagram to a symbolic expression, using the submodule `WiringDiagrams.Expressions`. Morphism expressions may also be given directly.

**`Catlab.Graphics.WiringDiagramLayouts.LayoutOrientation`** &mdash; *Type*.



Orientation of wiring diagram.

**`Catlab.Graphics.WiringDiagramLayouts.layout_box`** &mdash; *Method*.



Lay out a box and its ports.

By default the box is rectangular, but other shapes are also supported.

**`Catlab.Graphics.WiringDiagramLayouts.layout_diagram`** &mdash; *Method*.



Lay out a wiring diagram or morphism expression for visualization.

If a wiring diagram is given, it is first to converted to a morphism expression.

The layout is calculated with respect to a cartesian coordinate system with origin at the center of the diagram and the positive y-axis pointing *downwards*. Box positions are relative to their centers. All positions and sizes are dimensionless (unitless).

