import simpy
import random
from pipe import Pipe

class Node() :
    def __init__(self, id, env):
        self.id = id
        self.env = env

    def message(self,env,node_1,node_2,info,case):
        """
        info : liste des nouveaux voisins exemple : ["salurt a tous",3]  
        voisin droite = 5 pour noeud.id=1 et voisin gauche = 5 pour noeud.id =50

        """
        bc_pipe = Pipe(env)
        if case == 2:
            env.process(Pipe.message_generator(self, env, bc_pipe,info))
            env.process(Pipe.message_consumer(node_1, env, bc_pipe.get_output_conn()))
            env.process(Pipe.message_consumer(node_2, env, bc_pipe.get_output_conn()))
        if case ==1:
            env.process(Pipe.message_generator(self, env, bc_pipe,info))
            env.process(Pipe.message_consumer(node_1, env, bc_pipe.get_output_conn()))
    
    def setNeighbors(self,info):
        self.l_n=info[0]
        self.r_n=info[1]

    def setNeighborsR(self,node):
        self.r_n=node
    def setNeighborsL(self,node):
        self.l_n=node

    def delete(self,env):
        self.message(env,self.l_n,self.r_n,[self.l_n,self.r_n,4],2)


    def add(self,liste,env):
        node=random.randint(0,len(liste)-1)
        self.verification(liste[node],env)
    
    def verification(self,node,env):

        if node.l_n.id < self.id and self.id < node.id:
            self.r_n = node
            self.l_n = node.l_n
            self.message(env,node.l_n,node,[node.l_n.id,node.id,"R","L",self,1],2)


        elif node.id < self.id and self.id < node.r_n.id:
            self.r_n = node.r_n
            self.l_n = node
            self.message(env,node.r_n,node,[node.id,node.r_n.id,"R","L",self,1],2)
        

        else:
            if node.id < self.id:
                node.message(env,self,node.r_n,[self,node.r_n,env,2],1)
            
            if self.id < node.id:
                node.message(env,self,node.l_n,[self,node.l_n,env,2],1)
                
        
    def checkNeighbors(self):
        print("L : "+str(self.l_n.id) + " R : "+str(self.r_n.id))

    def wait(self,duration):
        yield self.env.timeout(duration)