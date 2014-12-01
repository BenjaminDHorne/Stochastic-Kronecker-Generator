
import GraphGen as gg
import matplotlib.pyplot as plt

def histogram(stats, numbins=10):
    x = range(numbins+1) ##0-0.1, 0.1-0.2, etc.
    xvals = []
    for val in x:
        xvals.append( float(val)/numbins )
    plt.figure()    
    i = 0
    for title in ['cc','deg','bc']:
        hist = {}
        vals = stats[title].values()
        for val in x:
            hist[val] = 0.01
        for val in vals:
            z = int(val*numbins)
            hist[z] += 1
        y = []
        for key in x:
            y.append(hist[key])
        plt.subplot(3, 1, i + 1)
        plt.title(title)
        plt.xticks(x)
        plt.bar(x, y, 1, color='r')
        i += 1
    plt.show()


if __name__ =="__main__":
    p = {}
    gtypes = [('erdos_renyi_graph', 20, 0.15, 3)]
    #gtypes = [('random', 20, 0.15, 3), \
              #('random', 200, 0.03, 3), \
              #('watts_strogatz_graph', 20, 0.1, 5), \
              #('watts_strogatz_graph', 200, 0.01, 8), \
              #('barabasi_albert_graph', 20, 0.1, 10), \
              #('barabasi_albert_graph', 200, 0.01, 20), \
    #]

    #gtypes = [('watts_strogatz_graph', 40, 0.1, 3), \
              #('watts_strogatz_graph', 40, 0.1, 8), \
              #('watts_strogatz_graph', 40, 0.1, 15), \
    #]

    for (g,x,y,z) in gtypes:
        p['graph_type'] = g
        p['num_agents'] = x
        p['connection_probability'] = y
        p['num_nodes_to_attach'] = z


        ag = range(p['num_agents'])

        (conn, stats) = gg.create_graph_type(ag,p)
        print p
        print "Connected components:", stats['num_cc']
        histogram(stats, 20*(1+int(p['num_agents']/60)))

