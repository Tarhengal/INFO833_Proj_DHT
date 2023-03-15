import simpy
from node import Node
from pipe import Pipe

env = simpy.Environment()
node_1 = Node(1,env)
node_2 = Node(2,env)
pipe = Pipe(env)

def comunication(node_1, node_2, content, env):
    yield pipe.send(node_1, node_2, content, env) 
    node_1.action.interrupt()
    node_2.action.interrupt()
   
env.process(comunication(node_1, node_2, 'Ping', env))   
env.run(until=40)