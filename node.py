import simpy
from pipe import Pipe

class Node() :
    def __init__(self, id, env):
        self.id = id
        self.env = env

    def message(self,env,node_2): 
        bc_pipe = Pipe(env)
        env.process(Pipe.message_generator(self.id, env, bc_pipe))
        env.process(Pipe.message_consumer(self.id, env, bc_pipe.get_output_conn()))
        env.process(Pipe.message_consumer(node_2.id, env, bc_pipe.get_output_conn()))


    def wait(self,duration):
        yield self.env.timeout(duration)

env = simpy.Environment()
node_1 = Node(1,env)
node_2 = Node(2,env)

node_1.message(env,node_2)

env.run(until=15)
    