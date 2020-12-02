import pydot


def draw(parent_name, child_name, graph):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)


def visit(node, graph, parent=None):
    for k, v in enumerate(reversed(node.leaves)):
        if len(v.leaves) > 0:
            # We start with the root node whose parent is None
            # we don't want to graph the None node
            if parent:
                draw(str(parent), str(v), graph)
            visit(v, graph, str(v))
        else:
            draw(str(parent), str(v), graph)
            # drawing the label using a distinct name
            if v.attr != v.value:
                draw(str(v), str(v.attr) + '(' + str(v.index) + ')', graph)
