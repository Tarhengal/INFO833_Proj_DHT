import matplotlib.pyplot as plt
import networkx as nwx

def createGraph(listeNodeID,listeNode):

    G1 = nwx.Graph()
    #noeuds=[i for i in range (10)]
    for i in listeNodeID:
        G1.add_node(i)

    def createListeLiens(listeNode):
        listeLiens=[]
        for node in listeNode:
            listeLiens.append((node.l_n.id,node.r_n.id))
        return(listeLiens)

    def addedges(G1,listenodeID,listeLiens):
        for i in range (len(listenodeID)):
            G1.add_edge(listenodeID[i],listeLiens[i][0])
            G1.add_edge(listenodeID[i],listeLiens[i][1])
        return(G1)
    

    listeLiens = createListeLiens(listeNode)
    G1=addedges(G1,listeNodeID,listeLiens)

    nwx.draw(G1,with_labels=True)  

    plt.show() 