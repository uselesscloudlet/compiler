import pydot


def draw(parent_name, child_name, graph):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)


def visit(node, graph, parent=None):
    for k, v in enumerate(reversed(node.leaves)):
        if len(v.leaves) > 0:
            if parent:
                draw(str(parent), str(v), graph)
            visit(v, graph, str(v))
        else:
            draw(str(parent), str(v), graph)
            if v.attr != v.value:
                draw(str(v), str(v.attr) + '(' + str(v.index) + ')', graph)
