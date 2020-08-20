# Graphwork
A small set of helper functions for using graphviz, especially from the interactive interpreter.

## Contents

Graphwork defines three functions:

- `mkgraph(vertices, edges, direction="LR")`

  Creates and returns a graphviz `Graph` object containing the given
  vertices and edges.

  `vertices` is an iterable of node names (`string`/`bytes` objects).
  `edges` is an iterable of `((vertex_1, vertex_2), weight)` tuples. Note that for the purposes of `(vertex_1, vertex_2)` tuples, a two-character string is valid, eg. `('AB', 4)` means `A <-> B [weight = 4]`.

- `qrender(graph, open=False)`

  'Quick' render the given `Graph` object to an image file.

  If `open` is True, open the image in your OS's default image viewer.

- `G(vertices, edges, direction="LR", open=False)`

  Shorthand for:
  ```
  qrender(
    mkgraph(vertices, edges, direction=direction),
    open=open
  )
  ```

## Other Resources

See `help(graphwork)` for examples.

See the [Graphviz manual](https://graphviz.readthedocs.io/en/stable/manual.html) for details about what the Python Graphviz library supports.
