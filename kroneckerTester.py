from KroneckerInitMatrix import InitMatrix
import KroneckerGenerator
import numpy as np
import networkx as nx
import testgg as test
import matplotlib.pyplot as plt

def get_graph(nxgraph):
    
    x = nxgraph
    cc_conn = nx.connected_components(x)
    num_cc = nx.number_connected_components(x)
    #largest_cc = len(cc_conn[0])

    return x, cc_conn, num_cc #, largest_cc

def create_graph_stats(nxgraph):
    (x, cc_conn, num_cc) = get_graph(nxgraph) #, largest_cc
    cc = nx.closeness_centrality(x)
    bc = nx.betweenness_centrality(x)
    deg = nx.degree_centrality(x)
    dens = nx.density(x)

    stats = {'cc':cc, 'bc':bc, 'deg':deg, \
             'num_cc':num_cc, 'dens':dens}#, 'largest_cc':largest_cc}

    return stats #conn,

#above are methods to make input for histogram

nodes = 2

init = InitMatrix(nodes)
init.make()

#Alpha Beta Method of Testing
init.addEdge(0, 1)
init.addSelfEdges()
init.makeStochasticAB(0.4, 0.2)

#Custom Method of Testing
#p = 15
#c = 6
#probArr = np.array([1, c*p, p/c, 0, 0, c*p, 1, p/c, 0, 0, p/c, p/c, 1, p/c, p/c, 0, 0, p/c, 1, c*p, 0, 0, p/c, c*p, 1])
#init.makeStochasticCustom(probArr) 

#Networkx Graph Gen as Seed, Alpha Beta after Testing
#G = nx.watts_strogatz_graph(5, 2, 0.1)
#nx.draw(G)
#plt.show() # if you want to visualize your seed graph first
#init = InitMatrix(nodes)
#init = init.makeStochasticABFromNetworkxGraph(G, 0.75, 0.5)

#Networkx Graph Gen as Seed Testing, not Stochastic after
#G = nx.watts_strogatz_graph(5, 3, 0.1)
#G = nx.hypercube_graph(3)
#nx.draw(G)
#plt.show() # if you want to visualize your seed graph first
#init = InitMatrix(nodes)
#init = init.makeFromNetworkxGraph(G)
#init.addSelfEdges() # if you want to ensure self edges for Kronecker

k = 5
print "Seed Matrix Nodes:"
print nodes
print "Kronecker Iterations:"
print k
nxgraph = KroneckerGenerator.generateStochasticKron(init, k, True)
#for line in nx.generate_edgelist(nxgraph, data=False):
 #   print(line)
print "Done Creating Network!"

is_bipart = nx.is_bipartite(nxgraph)
print "is_bipart:"
print is_bipart
is_conn = nx.is_connected(nxgraph)
print "is_conn:"
print is_conn #test

#print "Exporting to GML File"
#nx.write_gml(nxgraph,"KronSeed1_75a5b.gml") #export to gml file for gephi

#nx.draw(nxgraph, pos=nx.spring_layout(nxgraph))
#plt.show()

#print "Printing Statistics..."
#stats = create_graph_stats(nxgraph)
#print "Density: "
#print stats['dens']

#print "Creating Histogram..."
#histogramInput = create_graph_stats(nxgraph)
#test.histogram(histogramInput, 30)
