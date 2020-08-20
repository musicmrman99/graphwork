"""
A set of helper functions for using graphviz

>>> from graphwork import *
>>> 
>>> # This is the information being graphed. Remember: A string is a
>>> # list of characters.
>>> print(gw_example.vertices)
>>> print(gw_example.edges)
>>> 
>>> # `G(vertices, edges)` is short-hand for:
>>> #   quick_render(mkgraph(vertices, edges))
>>> #
>>> # `open=True` tells it to open the image in your image viewer app.
>>> #   If your image viewer updates the displayed image when the image
>>> #   file changes on disk, you won't need to supply this argument
>>> #   again (until you close your image viewer app).
>>> G(*gw_example(), open=True)
>>> G(*gw_example(), direction='UD', open=True)
"""

import graphviz

def mkgraph(vertices, edges, direction="LR"):
    """
    Creates and returns a Graph object containing the given vertices and
    edges.

    vertices must be an iterable of strings.
    edges must be an iterable of ((tail, head), weight) tuples. Note
    that for the purposes of (tail, head), a two-character string is
    valid, eg. ('AB',4) means `A -> B [weight = 4]`.
    """

    graph = graphviz.Graph(graph_attr={"rankdir": direction})
    for name in vertices:
        graph.node(name)
    for ((tail, head), weight) in edges:
        graph.edge(tail, head, weight=str(weight))
    return graph

def quick_render(g, open=False):
    """Render the given graph and open it in your image viewer."""
    g.render("quick_render", view=open, cleanup=True, format="png")

def G(vertices, edges, direction="LR", open=False):
    """
    Short-hand for:
    ```
    quick_render(mkgraph(vertices, edges, direction=direction), open=open)
    ```
    """

    quick_render(mkgraph(vertices, edges, direction), open=open)

class gw_example:
    """
    An example of the inputs the functions in this module expect.

    Use `G(*graphwork.example())` to display this example.
    """

    vertices = "STUVWXYZ"
    edges = [('TS',22), ('TU',20), ('TV',23), ('SU',18), ('UV',19), ('UW',17), ('UX',18), ('VW',16), ('WX',18), ('WZ',18), ('XY',17), ('ZY',15)]

    def __new__(cls):
        """
        Return a (vertices, edges) two-tuple of the vertices and edges
        defined in this class.
        """

        return (cls.vertices, cls.edges)