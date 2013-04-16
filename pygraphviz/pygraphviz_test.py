import pygraphviz as pgv
G=pgv.AGraph()
G.add_node('a')
G.add_edge('b','c')

print G

G.write("file.dot")

G=pgv.AGraph("file.dot")

G.layout()

G.layout(prog='dot')

G.draw('file.png')

G.draw('file.ps',prog='circo')