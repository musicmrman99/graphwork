"""
A set of helper functions for using graphviz

>>> from graphwork import *

This is the information being graphed. Remember: A string is a list of
characters.
>>> print(gw_example_small_fixed())

`G(edges)` is short-hand for:
  render(mkgraph(edges))

`open=True` tells it to open the image in your image viewer app. If your image
viewer updates the displayed image when the image file changes on disk, you
won't need to supply this argument again (until you close your image viewer
app).
>>> G(gw_example_small_fixed(), open=True)

Can also pass graph attributes, eg. up-down orientation.
>>> G(gw_example_small_fixed(), graph_attrs={rankdir='UD'}, open=True)

Can also pass vertices - useful for disconnected vertices. These are combined
with those mentioned in edges.
Note: The graph can only be limited in size - don't go crazy or it will crash.
>>> (edges, vertices) = gw_example_large_random()
>>> print(edges)
>>> print(vertices)
>>> G(edges, vertices, open=True)
"""

import graphviz
import random

# Creating Graphs
# --------------------------------------------------

# You can edit this after import
default_graph_attrs = {
    "rankdir": "LR"
}

def make_generic_node(
        graph: graphviz.Graph,
        name: str, label: str = None, attrs: dict = {}):
    """
    Create a node in graph with name, label and attributes.
    """

    graph.node(name, label, **attrs)

def make_generic_edge(
        graph: graphviz.Graph,
        tail: str, head: str, attrs: dict = {}):
    """
    Create an edge in graph with end points and attributes.
    
    Note: If only (tail, head) need to be given, and both are single-character
    names, a two-character string can be unpacked as arguments, eg:
      make_generic_edge(graph, *'AB')
    """

    graph.edge(tail, head, **attrs)

def mkgraph(
        edges: list, vertices: list = None, attrs: dict = None,
        mkedge=make_generic_edge, mknode=make_generic_node
):
    """
    Create and return a graphviz `Graph` object containing the given edges.

    edges is an iterable of tuples, where each tuple's items are passed to
    mkedge(). The number and types of elements of each tuple must match the
    signature of mkedge().
    
    If given, vertices is an iterable of tuples, where each tuple's items are
    passed to mknode(). If some disconnected vertices (those that have no edges
    connected to them) must be included, they must be given in vertices. Any
    vertices attached to an edge may also be included in vertices, but does not
    have to be unless it requires a label or additional attributes.
    """

    # Make the graph
    graph_attrs = dict(default_graph_attrs)
    if (attrs != None):
        graph_attrs.update(attrs)

    graph = graphviz.Graph(graph_attr=graph_attrs)

    # Add vertices first
    if vertices != None:
        for vertex in vertices:
            try:
                mknode(graph, vertex)
            except:
                mknode(graph, *vertex)

    # Add all edges
    for edge in edges:
        mkedge(graph, *edge)

    return graph

# Rendering and Showing
# --------------------------------------------------

def render(graph: graphviz.Graph, open=False):
    """
    Render the given Graph object to an image file.

    The file is always named "render.png".

    If `open` is True, open the image in your OS's default image viewer.
    """

    graph.render("render", format="png", view=open, cleanup=True)

def show(graph: graphviz.Graph):
    """
    Show the given Graph object.

    Short-hand for:
    >>> render(graph, open=True)
    """

    render(graph, open=True)

# G()
# --------------------------------------------------

def G(edges, vertices=None, graph_attrs=None, open=False):
    """
    Create the graph and render it immediately.

    Short-hand for:
    >>> render(mkgraph(edges, vertices, graph_attrs), open=open)
    """

    render(mkgraph(edges, vertices, graph_attrs), open=open)

# Examples
# --------------------------------------------------

_gw_example_small_fixed_edges = [
    ('TS',22), ('TU',20), ('TV',23), ('SU',18), ('UV',19), ('UW',17),
    ('UX',18), ('VW',16), ('WX',18), ('WZ',18), ('XY',17), ('ZY',15)
]
def gw_example_small_fixed():
    """
    An example of the inputs the functions in this module expect.

    Use `G(gw_example_small_fixed(), open=True)` to display this example.
    """

    return map(
        lambda e: (*e[0], {"weight": e[1]}),
        _gw_example_small_fixed_edges
    )

# Warning: A large value for num_edges (eg. 1000) will timeout on load of the
#   graph.
_vertex_name_range = 1000
_num_vertices = 100
_num_edges = 50
def gw_example_large_random():
    """
    A larger example of using G().

    Use `G(*gw_example_large_random(), open=True)` to display this example.
    """
    
    # Generate vertices
    rand_vertices = [
        str(random.randrange(_vertex_name_range))
        for _ in range(_num_vertices)
    ]

    # Generate edges
    rand_edges = [
        (
            str(random.choice(rand_vertices)), # tail vertex
            str(random.choice(rand_vertices)), # head vertex
            {"weight": 1} # edge weight
        )
        for _ in range(_num_edges)
    ]

    return (rand_edges, rand_vertices)
