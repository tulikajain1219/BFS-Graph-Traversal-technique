import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
node_dict={0:[1,2,7,8],1:[3,5],2:[4,6]}
BFS=[]
BFS_collection=[]

for i in node_dict:
    connection=[]
    BFS_collection.append(i)
    connection=node_dict[i]
    if len(connection)==1:
        BFS_collection.append(connection[0])
        G.add_edge(i, connection[0])
    else:
        for j in connection:
            BFS_collection.append(j)
            G.add_edge(i, j)

for i in BFS_collection:
    if i not in BFS:
        BFS.append(i)

print(BFS)
    
nx.draw(G,with_labels=1)
plt.savefig("simple_path_1.png") # save as png
plt.show() # display



