import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
from matplotlib.widgets import Button
from algorithm import reweight,Dijkstras
import numpy as np

#run the algowrihm in advancee
G1 = {
    0:{1:-2},
    1:{2:-1},
    2:{0:4,3:2,4:-3},
    3:{},
    4:{},
    5:{3:1,4:-4}
}
V1=[0,1,2,3,4,5]
Gw=reweight(G1,V1)
Paths = []
Records=[]
for v in V1:
    out = Dijkstras(Gw,V1,v)
    Paths.append(out[2])
    Records.append(out[3])


class GraphVisualize:
    def __init__(self):
        self.G = nx.DiGraph(directed=True)
        self.G.add_nodes_from([(0, {'name': 0}),
                          (1, {'name': 1}),
                          (2, {'name': 2}),
                          (3, {'name': 3}),
                          (4, {'name': 4}),
                          (5, {'name': 5})])

        self.G.add_edges_from([(0, 1, {'weight': -2}),
                          (1, 2, {'weight': -1}),
                          (2, 0, {'weight': 4}),
                          (2, 3, {'weight': 2}),
                          (2, 4, {'weight': -3}),
                          (5, 3, {'weight': 1}),
                          (5, 4, {'weight': -4})])
        self.pos = nx.spring_layout(self.G)
        self.source_node=0
        self.step=0

        self.running=False
        self.if_reweighted=False
        self.fig, self.ax=plt.subplots(figsize=(10,10))
        self.anim = matplotlib.animation.FuncAnimation(self.fig, self.update, frames=6, interval=1000, repeat=True)

    def updateGraphWeights(self,graph,weights):
        for key in weights:
            adj = weights[key]
            for k in adj:
                start=int(key)
                end=int(k)
                dis=adj[k]
                self.G[start][end]['weight']=dis


    def update(self,num):
        self.ax.clear()
        self.node_labels = nx.get_node_attributes(self.G, 'name')
        self.edge_labels = nx.get_edge_attributes(self.G, 'weight')
        if self.if_reweighted == True:
            print("hello")
            for node in self.node_labels:
                print("hello")


        #print(type(self.node_labels[0]))
        # print(edge_labels)
        #if self.if_reweighted == True:

        nx.draw_networkx_edges(self.G,pos=self.pos,ax=self.ax,arrowsize=20)
        nx.draw_networkx_edge_labels(self.G,self.pos,edge_labels=self.edge_labels)
        nx.draw_networkx_nodes(self.G,self.pos,node_color='g',ax=self.ax,node_size=500, alpha=0.9)
        nx.draw_networkx_labels(self.G,self.pos,self.node_labels,16)
        if self.if_reweighted == False:
            self.updateGraphWeights(self.G,Gw)

    def _pause(self,event):
        if self.running==True:
            self.anim.event_source.stop()
            self.running = False
        else:
            self.anim.event_source.start()
            self.runnning = True

    def animate(self):
        #pause_ax = self.fig.add_axes([0.9, 0.025, 0.1, 0.04])
        #pause_button = Button(pause_ax,'pause')
        #pause_button.on_clicked(self._pause)

        plt.show()



#nx.draw_networkx_edges(G,pos=pos,ax=ax,arrowsize=12)
#nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
#nx.draw_networkx_nodes(G,pos,node_color='g',ax=ax,nodesize=500,alpha=0.9)
#nx.draw_networkx_labels(G,pos,node_labels,16)

vis = GraphVisualize()
vis.animate()