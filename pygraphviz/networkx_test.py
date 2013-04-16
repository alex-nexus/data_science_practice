import networkx as nx
import pygraphviz as pgv
import matplotlib.pyplot as ppt

edgelist = [(1,2),(1,9),(3,2),(3,9),(4,5),(4,6),(4,9),(5,9),(7,8),(7,9)]

nxd = nx.DiGraph()
nxu = nx.Graph()
gvd = pgv.AGraph(directed=True)
gvu = pgv.AGraph()

nxd.add_edges_from(edgelist)
nxu.add_edges_from(edgelist)
gvd.add_edges_from(edgelist)
gvu.add_edges_from(edgelist)

pos1 = nx.spring_layout(nxd)
nx.draw_networkx(nxd,pos1)
ppt.savefig('1_networkx_directed.png')
ppt.clf()

pos2 = nx.spring_layout(nxu)
nx.draw_networkx(nxu,pos2)
ppt.savefig('2_networkx_undirected.png')
ppt.clf()

gvd.layout(prog='neato')
gvd.draw('3_pygraphviz_directed.png')

gvu.layout(prog='neato')
gvu.draw('4_pygraphviz_undirected.png')
