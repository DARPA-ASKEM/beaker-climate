


# Graphs

**`Catlab.Graphs.BasicGraphs`** &mdash; *Module*.



Data structures for graphs, based on C-sets.

This module provides the category theorist's four basic kinds of graphs: graphs (aka directed multigraphs), symmetric graphs, reflexive graphs, and symmetric reflexive graphs. It also defines half-edge graphs, which are isomorphic to symmetric graphs, and a few standard kinds of attributed graphs, such as weighted graphs.

The graphs API generally follows that of [Graphs.jl](https://github.com/JuliaGraphs/Graphs.jl), with some departures due to differences between the data structures.

**`Catlab.Graphs.BasicGraphs.AbstractGraph`** &mdash; *Type*.



Abstract type for graphs, aka directed multigraphs.

**`Catlab.Graphs.BasicGraphs.AbstractHalfEdgeGraph`** &mdash; *Type*.



Abstract type for half-edge graphs, possibly with data attributes.

**`Catlab.Graphs.BasicGraphs.AbstractLabeledGraph`** &mdash; *Type*.



Abstract type for labeled graphs.

**`Catlab.Graphs.BasicGraphs.AbstractReflexiveGraph`** &mdash; *Type*.



Abstract type for reflexive graphs, possibly with data attributes.

**`Catlab.Graphs.BasicGraphs.AbstractSymmetricGraph`** &mdash; *Type*.



Abstract type for symmetric graph, possibly with data attributes.

**`Catlab.Graphs.BasicGraphs.AbstractSymmetricReflexiveGraph`** &mdash; *Type*.



Abstract type for symmetric reflexive graphs, possibly with data attributes.

**`Catlab.Graphs.BasicGraphs.AbstractSymmetricWeightedGraph`** &mdash; *Type*.



Abstract type for symmetric weighted graphs.

**`Catlab.Graphs.BasicGraphs.AbstractWeightedGraph`** &mdash; *Type*.



Abstract type for weighted graphs.

**`Catlab.Graphs.BasicGraphs.Graph`** &mdash; *Type*.



A graph, also known as a directed multigraph.

**`Catlab.Graphs.BasicGraphs.HalfEdgeGraph`** &mdash; *Type*.



A half-edge graph.

[Half-edge graphs](https://www.algebraicjulia.org/blog/post/2020/09/cset-graphs-2/) are a variant of undirected graphs whose edges are pairs of "half-edges" or "darts". Half-edge graphs are isomorphic to symmetric graphs but have a different data model.

**`Catlab.Graphs.BasicGraphs.HasGraph`** &mdash; *Type*.



Abstract type for C-sets that contain a graph.

This type encompasses C-sets where the schema for graphs is a subcategory of C. This includes, for example, graphs, symmetric graphs, and reflexive graphs, but not half-edge graphs.

**`Catlab.Graphs.BasicGraphs.HasVertices`** &mdash; *Type*.



Abstract type for C-sets that contain vertices.

This type encompasses C-sets where the schema C contains an object `V` interpreted as vertices. This includes, for example, graphs and half-edge graphs, but not bipartite graphs or wiring diagrams.

**`Catlab.Graphs.BasicGraphs.LabeledGraph`** &mdash; *Type*.



A labeled graph.

By convention, a "labeled graph" without qualification is a vertex-labeled graph. We do not require that the label be unique, and in this data type, the label attribute is not indexed.

**`Catlab.Graphs.BasicGraphs.ReflexiveGraph`** &mdash; *Type*.



A reflexive graph.

[Reflexive graphs](https://ncatlab.org/nlab/show/reflexive+graph) are graphs in which every vertex has a distinguished self-loop.

**`Catlab.Graphs.BasicGraphs.SymmetricGraph`** &mdash; *Type*.



A symmetric graph, or graph with an orientation-reversing edge involution.

Symmetric graphs are closely related, but not identical, to undirected graphs.

**`Catlab.Graphs.BasicGraphs.SymmetricReflexiveGraph`** &mdash; *Type*.



A symmetric reflexive graph.

Symmetric reflexive graphs are both symmetric graphs ([`SymmetricGraph`](graphs.md#Catlab.Graphs.BasicGraphs.SymmetricGraph)) and reflexive graphs ([`ReflexiveGraph`](graphs.md#Catlab.Graphs.BasicGraphs.ReflexiveGraph)) such that the reflexive loops are fixed by the edge involution.

**`Catlab.Graphs.BasicGraphs.SymmetricWeightedGraph`** &mdash; *Type*.



A symmetric weighted graph.

A symmetric graph in which every edge has a numerical weight, preserved by the edge involution.

**`Catlab.Graphs.BasicGraphs.WeightedGraph`** &mdash; *Type*.



A weighted graph.

A graph in which every edge has a numerical weight.

**`Base.inv`** &mdash; *Method*.



Involution on half-edge(s) in a half-edge graph.

**`Base.inv`** &mdash; *Method*.



Involution on edge(s) in a symmetric graph.

**`Catlab.Graphs.BasicGraphs.add_dangling_edge!`** &mdash; *Method*.



Add a dangling edge to a half-edge graph.

A "dangling edge" is a half-edge that is paired with itself under the half-edge involution. They are usually interpreted differently than "self-loops", i.e., a pair of distinct half-edges incident to the same vertex.

**`Catlab.Graphs.BasicGraphs.add_dangling_edges!`** &mdash; *Method*.



Add multiple dangling edges to a half-edge graph.

**`Catlab.Graphs.BasicGraphs.add_edge!`** &mdash; *Method*.



Add an edge to a graph.

**`Catlab.Graphs.BasicGraphs.add_edges!`** &mdash; *Method*.



Add multiple edges to a graph.

**`Catlab.Graphs.BasicGraphs.add_vertex!`** &mdash; *Method*.



Add a vertex to a graph.

**`Catlab.Graphs.BasicGraphs.add_vertices!`** &mdash; *Method*.



Add multiple vertices to a graph.

**`Catlab.Graphs.BasicGraphs.add_vertices_with_indices!`** &mdash; *Method*.



Add vertices with preallocated src/tgt indexes

**`Catlab.Graphs.BasicGraphs.all_neighbors`** &mdash; *Method*.



Union of in-neighbors and out-neighbors in a graph.

**`Catlab.Graphs.BasicGraphs.degree`** &mdash; *Method*.



Total degree of a vertex

Equivalent to length(all_neighbors(g,v)) but faster

**`Catlab.Graphs.BasicGraphs.edges`** &mdash; *Method*.



Edges in a graph, or between two vertices in a graph.

**`Catlab.Graphs.BasicGraphs.half_edges`** &mdash; *Method*.



Half-edges in a half-edge graph, or incident to a vertex.

**`Catlab.Graphs.BasicGraphs.has_edge`** &mdash; *Method*.



Whether the graph has the given edge, or an edge between two vertices.

**`Catlab.Graphs.BasicGraphs.has_vertex`** &mdash; *Method*.



Whether the graph has the given vertex.

**`Catlab.Graphs.BasicGraphs.induced_subgraph`** &mdash; *Method*.



Subgraph induced by a set of a vertices.

The [induced subgraph](https://en.wikipedia.org/wiki/Induced_subgraph) consists of the given vertices and all edges between vertices in this set.

**`Catlab.Graphs.BasicGraphs.inedges`** &mdash; *Method*.



Edges coming into a vertex

**`Catlab.Graphs.BasicGraphs.inneighbors`** &mdash; *Method*.



In-neighbors of vertex in a graph.

**`Catlab.Graphs.BasicGraphs.ne`** &mdash; *Method*.



Number of edges in a graph, or between two vertices in a graph.

In a symmetric graph, this function counts both edges in each edge pair, so that the number of edges in a symmetric graph is twice the number of edges in the corresponding undirected graph (at least when the edge involution has no fixed points).

**`Catlab.Graphs.BasicGraphs.neighbors`** &mdash; *Method*.



Neighbors of vertex in a graph.

In a graph, this function is an alias for [`outneighbors`](graphs.md#Catlab.Graphs.BasicGraphs.outneighbors-Tuple{AbstractGraph, Int64}); in a symmetric graph, a vertex has the same out-neighbors and as in-neighbors, so the distinction is moot.

In the presence of multiple edges, neighboring vertices are given *with multiplicity*. To get the unique neighbors, call `unique(neighbors(g))`.

**`Catlab.Graphs.BasicGraphs.nv`** &mdash; *Method*.



Number of vertices in a graph.

**`Catlab.Graphs.BasicGraphs.outedges`** &mdash; *Method*.



Edges coming out of a vertex

**`Catlab.Graphs.BasicGraphs.outneighbors`** &mdash; *Method*.



Out-neighbors of vertex in a graph.

**`Catlab.Graphs.BasicGraphs.refl`** &mdash; *Method*.



Reflexive loop(s) of vertex (vertices) in a reflexive graph.

**`Catlab.Graphs.BasicGraphs.rem_edge!`** &mdash; *Method*.



Remove an edge from a graph.

**`Catlab.Graphs.BasicGraphs.rem_edges!`** &mdash; *Method*.



Remove multiple edges from a graph.

**`Catlab.Graphs.BasicGraphs.rem_vertex!`** &mdash; *Method*.



Remove a vertex from a graph.

When `keep_edges` is false (the default), all edges incident to the vertex are also deleted. When `keep_edges` is true, incident edges are preserved but their source/target vertices become undefined.

**`Catlab.Graphs.BasicGraphs.rem_vertices!`** &mdash; *Method*.



Remove multiple vertices from a graph.

Edges incident to any of the vertices are treated as in [`rem_vertex!`](graphs.md#Catlab.Graphs.BasicGraphs.rem_vertex!-Tuple{HasVertices, Int64}).

**`Catlab.Graphs.BasicGraphs.vertex`** &mdash; *Method*.



Incident vertex (vertices) of half-edge(s) in a half-edge graph.

**`Catlab.Graphs.BasicGraphs.vertices`** &mdash; *Method*.



Vertices in a graph.

**`Catlab.Graphs.BasicGraphs.weight`** &mdash; *Method*.



Weight(s) of edge(s) in a weighted graph.

**`Catlab.Theories.src`** &mdash; *Method*.



Source vertex (vertices) of edges(s) in a graph.

**`Catlab.Theories.tgt`** &mdash; *Method*.



Target vertex (vertices) of edges(s) in a graph.

**`Catlab.Graphs.BipartiteGraphs`** &mdash; *Module*.



Bipartite graphs, directed and undirected, as C-sets.

A graph theorist might call these "bipartitioned graphs," as in a graph *equipped with* a bipartition, as opposed to "bipartite graphs," as in a graph that *can be* bipartitioned. Here we use the former notion, which is more natural from the structuralist perspective, but the latter terminology, which is shorter and more familiar.

**`Catlab.Graphs.BipartiteGraphs.AbstractBipartiteGraph`** &mdash; *Type*.



Abstract type for bipartite graphs.

**`Catlab.Graphs.BipartiteGraphs.AbstractUndirectedBipartiteGraph`** &mdash; *Type*.



Abstract type for undirected bipartite graphs.

**`Catlab.Graphs.BipartiteGraphs.BipartiteGraph`** &mdash; *Type*.



A bipartite graph, better known as a [bipartite directed multigraph](https://cs.stackexchange.com/a/91521).

Directed bipartite graphs are isomorphic to port hypergraphs and to whole grain Petri nets.

**`Catlab.Graphs.BipartiteGraphs.HasBipartiteGraph`** &mdash; *Type*.



Abstract type for C-sets that contain a (directed) bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.HasBipartiteVertices`** &mdash; *Type*.



Abstract type for C-sets that contain a bipartition of vertices.

**`Catlab.Graphs.BipartiteGraphs.UndirectedBipartiteGraph`** &mdash; *Type*.



An undirected bipartite graph.

It is a matter of perspective whether to consider such graphs "undirected," in the sense that the edges have no orientation, or "unidirected," in the sense that all edges go from vertices of type 1 to vertices of type 2.

**`Catlab.Graphs.BipartiteGraphs.add_edges₁₂!`** &mdash; *Method*.



Add edges from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.add_edges₂₁!`** &mdash; *Method*.



Add edges from V₂ to V₁ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.add_edge₁₂!`** &mdash; *Method*.



Add edge from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.add_edge₂₁!`** &mdash; *Method*.



Add edge from V₂ to V₁ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.add_vertex₁!`** &mdash; *Method*.



Add a vertex of type 1 to a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.add_vertex₂!`** &mdash; *Method*.



Add a vertex of type 2 to a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.add_vertices₁!`** &mdash; *Method*.



Add vertices of type 1 to a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.add_vertices₂!`** &mdash; *Method*.



Add vertices of type 2 to a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.edges₁₂`** &mdash; *Method*.



Edges from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.edges₂₁`** &mdash; *Method*.



Edges from V₂ to V₁ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.ne₁₂`** &mdash; *Method*.



Number of edges from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.ne₂₁`** &mdash; *Method*.



Number of edges from V₂ to V₁ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.nv₁`** &mdash; *Method*.



Number of vertices of type 1 in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.nv₂`** &mdash; *Method*.



Number of vertices of type 2 in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_edges₁₂!`** &mdash; *Method*.



Remove edges from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_edges₂₁!`** &mdash; *Method*.



Remove edges from V₂ to V₁ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_edge₁₂!`** &mdash; *Method*.



Remove edge from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_edge₂₁!`** &mdash; *Method*.



Remove edge from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_vertex₁!`** &mdash; *Method*.



Remove vertex of type 1 from a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_vertex₂!`** &mdash; *Method*.



Remove vertex of type 2 from a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_vertices₁!`** &mdash; *Method*.



Remove vertices of type 1 from a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.rem_vertices₂!`** &mdash; *Method*.



Remove vertices of type 2 from a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.src₁`** &mdash; *Method*.



Source vertex of edge from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.src₂`** &mdash; *Method*.



Source vertex of edge from V₂ to V₁ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.tgt₁`** &mdash; *Method*.



Target vertex of edge from V₂ to V₁ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.tgt₂`** &mdash; *Method*.



Target vertex of edge from V₁ to V₂ in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.vertices₁`** &mdash; *Method*.



Vertices of type 1 in a bipartite graph.

**`Catlab.Graphs.BipartiteGraphs.vertices₂`** &mdash; *Method*.



Vertices of type 2 in a bipartite graph.

**`Catlab.Graphs.NamedGraphs`** &mdash; *Module*.



Extends the basic graph types with vertex and/or edge names.

Naming vertices and edges and looking them up by name is a common requirement. This module provides a simple interface and default graph types for named graphs. Names are understood to be unique within the graph but are *not* assumed to be strings or symbols.

**`Catlab.Graphs.NamedGraphs.AbstractNamedGraph`** &mdash; *Type*.



Abstract type for graph with named vertices and edges.

**`Catlab.Graphs.NamedGraphs.NamedGraph`** &mdash; *Type*.



Graph with named vertices and edges.

**`Catlab.Graphs.NamedGraphs.edge_name`** &mdash; *Method*.



Name of an edge in a graph.

By default, the name of an edge is its ID.

**`Catlab.Graphs.NamedGraphs.edge_named`** &mdash; *Method*.



Get edge in graph with given name.

**`Catlab.Graphs.NamedGraphs.has_edge_names`** &mdash; *Method*.



Whether a graph has edge names distinct from its edge IDs.

**`Catlab.Graphs.NamedGraphs.has_vertex_names`** &mdash; *Method*.



Whether a graph has vertex names distinct from its vertex IDs.

**`Catlab.Graphs.NamedGraphs.vertex_name`** &mdash; *Method*.



Name of a vertex in a graph.

By default, the name of a vertex is its ID.

**`Catlab.Graphs.NamedGraphs.vertex_named`** &mdash; *Method*.



Get vertex in graph with given name.

**`Catlab.Graphs.PropertyGraphs.AbstractPropertyGraph`** &mdash; *Type*.



Abstract type for graph with properties.

Concrete types are [`PropertyGraph`](graphs.md#Catlab.Graphs.PropertyGraphs.PropertyGraph) and [`SymmetricPropertyGraph`](graphs.md#Catlab.Graphs.PropertyGraphs.SymmetricPropertyGraph).

**`Catlab.Graphs.PropertyGraphs.PropertyGraph`** &mdash; *Type*.



Graph with properties.

"Property graphs" are graphs with arbitrary named properties on the graph, vertices, and edges. They are intended for applications with a large number of ad-hoc properties. If you have a small number of known properties, it is better and more efficient to create a specialized C-set type using `@acset_type`.

See also: [`SymmetricPropertyGraph`](graphs.md#Catlab.Graphs.PropertyGraphs.SymmetricPropertyGraph).

**`Catlab.Graphs.PropertyGraphs.SymmetricPropertyGraph`** &mdash; *Type*.



Symmetric graphs with properties.

The edge properties are preserved under the edge involution, so these can be interpreted as "undirected" property (multi)graphs.

See also: [`PropertyGraph`](graphs.md#Catlab.Graphs.PropertyGraphs.PropertyGraph).

**`Catlab.Graphs.PropertyGraphs.eprops`** &mdash; *Method*.



Properties of edge in a property graph.

**`Catlab.Graphs.PropertyGraphs.get_eprop`** &mdash; *Method*.



Get property of edge or edges in a property graph.

**`Catlab.Graphs.PropertyGraphs.get_gprop`** &mdash; *Method*.



Get graph-level property of a property graph.

**`Catlab.Graphs.PropertyGraphs.get_vprop`** &mdash; *Method*.



Get property of vertex or vertices in a property graph.

**`Catlab.Graphs.PropertyGraphs.gprops`** &mdash; *Method*.



Graph-level properties of a property graph.

**`Catlab.Graphs.PropertyGraphs.set_eprop!`** &mdash; *Method*.



Set property of edge or edges in a property graph.

**`Catlab.Graphs.PropertyGraphs.set_eprops!`** &mdash; *Method*.



Set multiple properties of an edge in a property graph.

**`Catlab.Graphs.PropertyGraphs.set_gprop!`** &mdash; *Method*.



Set graph-level property in a property graph.

**`Catlab.Graphs.PropertyGraphs.set_gprops!`** &mdash; *Method*.



Set multiple graph-level properties in a property graph.

**`Catlab.Graphs.PropertyGraphs.set_vprop!`** &mdash; *Method*.



Set property of vertex or vertices in a property graph.

**`Catlab.Graphs.PropertyGraphs.set_vprops!`** &mdash; *Method*.



Set multiple properties of a vertex in a property graph.

**`Catlab.Graphs.PropertyGraphs.vprops`** &mdash; *Method*.



Properties of vertex in a property graph.

**`Catlab.Graphs.GraphAlgorithms`** &mdash; *Module*.



Algorithms on graphs based on C-sets.

**`Catlab.Graphs.GraphAlgorithms.connected_component_projection`** &mdash; *Function*.



Projection onto (weakly) connected components of a graph.

Returns a function in FinSet{Int} from the vertex set to the set of components.

**`Catlab.Graphs.GraphAlgorithms.connected_components`** &mdash; *Method*.



(Weakly) connected components of a graph.

Returns a vector of vectors, which are the components of the graph.

**`Catlab.Graphs.GraphAlgorithms.enumerate_paths`** &mdash; *Method*.



Enumerate all paths of an acyclic graph, indexed by src+tgt

**`Catlab.Graphs.GraphAlgorithms.topological_sort`** &mdash; *Method*.



Topological sort of a directed acyclic graph.

The [depth-first search](https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search) algorithm is adapted from the function `topological_sort_by_dfs` in Graphs.jl.

**`Catlab.Graphs.GraphAlgorithms.transitive_reduction!`** &mdash; *Method*.



Transitive reduction of a DAG.

The algorithm computes the longest paths in the DAGs and keeps only the edges corresponding to longest paths of length 1. Requires a topological sort, which is computed if it is not supplied.

**`Catlab.Graphs.GraphGenerators.complete_graph`** &mdash; *Method*.



Complete graph on $n$ vertices.

**`Catlab.Graphs.GraphGenerators.cycle_graph`** &mdash; *Method*.



Cycle graph on $n$ vertices.

When $n = 1$, this is a loop graph.

**`Catlab.Graphs.GraphGenerators.erdos_renyi`** &mdash; *Method*.



```julia
erdos_renyi(GraphType, n, ne)
```

Create an [Erdős–Rényi](http://en.wikipedia.org/wiki/Erdős–Rényi_model) random graph with `n` vertices and `ne` edges.

**References**

  * https://github.com/JuliaGraphs/LightGraphs.jl/blob/2a644c2b15b444e7f32f73021ec276aa9fc8ba30/src/SimpleGraphs/generators/randgraphs.jl

**`Catlab.Graphs.GraphGenerators.erdos_renyi`** &mdash; *Method*.



```julia
erdos_renyi(GraphType, n, p)
```

Create an [Erdős–Rényi](http://en.wikipedia.org/wiki/Erdős–Rényi_model) random graph with `n` vertices. Edges are added between pairs of vertices with probability `p`.

**Optional Arguments**

  * `seed=-1`: set the RNG seed.
  * `rng`: set the RNG directly

**References**

  * https://github.com/JuliaGraphs/LightGraphs.jl/blob/2a644c2b15b444e7f32f73021ec276aa9fc8ba30/src/SimpleGraphs/generators/randgraphs.jl

**`Catlab.Graphs.GraphGenerators.expected_degree_graph`** &mdash; *Method*.



```julia
expected_degree_graph(GraphType, ω)
```

Given a vector of expected degrees `ω` indexed by vertex, create a random undirected graph in which vertices `i` and `j` are connected with probability `ω[i]*ω[j]/sum(ω)`.

**Optional Arguments**

  * `seed=-1`: set the RNG seed.
  * `rng`: set the RNG directly

**Implementation Notes**

The algorithm should work well for `maximum(ω) << sum(ω)`. As `maximum(ω)` approaches `sum(ω)`, some deviations from the expected values are likely.

**References**

  * Connected Components in Random Graphs with Given Expected Degree Sequences, Linyuan Lu and Fan Chung. [https://link.springer.com/article/10.1007%2FPL00012580](https://link.springer.com/article/10.1007%2FPL00012580)
  * Efficient Generation of Networks with Given Expected Degrees, Joel C. Miller and Aric Hagberg. [https://doi.org/10.1007/978-3-642-21286-4_10](https://doi.org/10.1007/978-3-642-21286-4_10)
  * https://github.com/JuliaGraphs/LightGraphs.jl/blob/2a644c2b15b444e7f32f73021ec276aa9fc8ba30/src/SimpleGraphs/generators/randgraphs.jl#L187

**`Catlab.Graphs.GraphGenerators.parallel_arrows`** &mdash; *Method*.



Graph with two vertices and $n$ parallel edges.

**`Catlab.Graphs.GraphGenerators.path_graph`** &mdash; *Method*.



Path graph on $n$ vertices.

**`Catlab.Graphs.GraphGenerators.star_graph`** &mdash; *Method*.



Star graph on $n$ vertices.

In the directed case, the edges point outward.

**`Catlab.Graphs.GraphGenerators.watts_strogatz`** &mdash; *Method*.



```julia
watts_strogatz(n, k, β)
```

Return a [Watts-Strogatz](https://en.wikipedia.org/wiki/Watts_and_Strogatz_model) small world random graph with `n` vertices, each with expected degree `k` (or `k

  * 1`if`k`is odd). Edges are randomized per the model based on probability`β`.

The algorithm proceeds as follows. First, a perfect 1-lattice is constructed, where each vertex has exacly `div(k, 2)` neighbors on each side (i.e., `k` or `k - 1` in total). Then the following steps are repeated for a hop length `i` of `1` through `div(k, 2)`.

1. Consider each vertex `s` in turn, along with the edge to its `i`th nearest neighbor `t`, in a clockwise sense.
2. Generate a uniformly random number `r`. If `r ≥ β`, then the edge `(s, t)` is left unaltered. Otherwise, the edge is deleted and *rewired* so that `s` is connected to some vertex `d`, chosen uniformly at random from the entire graph, excluding `s` and its neighbors. (Note that `t` is a valid candidate.)

For `β = 0`, the graph will remain a 1-lattice, and for `β = 1`, all edges will be rewired randomly.

**Optional Arguments**

  * `is_directed=false`: if true, return a directed graph.
  * `seed=-1`: set the RNG seed.

**References**

  * Collective dynamics of ‘small-world’ networks, Duncan J. Watts, Steven H. Strogatz. [https://doi.org/10.1038/30918](https://doi.org/10.1038/30918)
  * Small Worlds, Duncan J. watts. [https://en.wikipedia.org/wiki/Special:BookSources?isbn=978-0691005416](https://en.wikipedia.org/wiki/Special:BookSources?isbn=978-0691005416)
  * https://github.com/JuliaGraphs/LightGraphs.jl/blob/2a644c2b15b444e7f32f73021ec276aa9fc8ba30/src/SimpleGraphs/generators/randgraphs.jl#L187

**`Catlab.Graphs.GraphGenerators.wheel_graph`** &mdash; *Method*.



Wheel graph on $n$ vertices.

In the directed case, the outer cycle is directed and the spokes point outward.

