import simpy
import random
from node import Node
from graph import createGraph


def randomNotInList(liste):
    number = random.randint(liste[0],liste[1])
    if number in liste:
        return(randomNotInList(liste))
    else:
        return(number)

def backgroundCheck(liste):
    print("background check")
    for i in liste:
        print(i.id)
        print("L = "+str(i.l_n.id))
        print("R = "+str(i.r_n.id))
        

def createNode(env,liste,liste_ID,n):
    for i in range(n+1):
        number = randomNotInList(liste_ID)
        print(number)
        node = Node(number,env)
        node.add(liste,env)
        liste.append(node)
        liste_ID.append(number)
        env.run(until=i*10+10)
        backgroundCheck(liste)
        createGraph(liste_ID,liste)
        
    return(liste_ID)



minNode = 1
maxNode = 50


#####################################
############## SET UP ###############
#####################################

env = simpy.Environment()

liste = []

node_1 = Node(minNode,env)
node_max = Node(maxNode,env)

node_1.setNeighbors([node_max,node_max])
node_max.setNeighbors([node_1,node_1])

liste.append(node_1)
liste.append(node_max)


liste_ID =[node_1.id,node_max.id]

createGraph(liste_ID,liste)

#####################################
#####################################






#############################################################
########### Choisir le nombre de noeud voulu ################
## attention max 48, car le plus gros node est défini a 50 ##
createNode(env,liste,liste_ID,9)



