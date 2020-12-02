from syntax.parser import Parser
from syntax.draw import visit
import json
import pprint
import pydot


class Leaf:
    leaf_ind = 0

    def __init__(self, value, leaves, attr):
        self.value = value
        self.leaves = leaves
        self.index = Leaf.leaf_ind
        self.attr = attr
        Leaf.leaf_ind += 1

    def __str__(self):
        return str(self.value) + "(" + str(self.index) + ")"

    def __repr__(self):
        return str(self.value) + "(" + str(self.index) + ")"

    def iteritems(self):
        items = []
        for i, leaf in enumerate(self.leaves):
            items.append((leaf, i))
        return items


lex_file = open('syntax/settings/lexems.csv', 'r')
parser = Parser(lex_file)

syntax_file = open('syntax/settings/syntax.json', 'r')
syntax = json.load(syntax_file)
syntax_file.close()

control_table = syntax["control"]
end_map = syntax["endMap"]


def pop_n(stack, n):
    arr = []
    for _ in range(n):
        arr.append(stack.pop())
    return arr


buff = [Leaf("nabla", [], None)]

lexem = parser.next_lexem()
last_known_line = 0
while buff[-1].value != "PROGRAM":
    if lexem.line is not None:
        last_known_line = lexem.line
    last = buff[-1].value

    if (lexem.term not in control_table) or (last not in control_table[lexem.term]):
        raise Exception("Error in line: " + str(last_known_line))
    action = control_table[lexem.term][last]
    if action == 'shift':
        buff.append(Leaf(lexem.term, [], lexem.value))
        lexem = parser.next_lexem()
    elif action == 'reduce':
        rules = end_map[last]
        for rule in rules:
            right = rule["right"]
            left = rule["left"]
            if list(map(lambda l: l.value, buff[-len(right):])) == right:
                buff.append(Leaf(left, pop_n(buff, len(right)), lexem.value))
    else:
        raise Exception("Error in line: " + str(last_known_line))

graph = pydot.Dot(graph_type='graph')
visit(buff[-1], graph=graph)
graph.write_png('tree.png')


lex_file.close()
