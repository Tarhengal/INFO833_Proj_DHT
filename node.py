import simpy
from pipe import Pipe

class Node() :
    def __init__(self, id, env):
        self.id = id
        self.env = env
        self.action = env.process(self.run())

    def run(self): 
        while True :
            print('Node %d is alive since %d time units' % (self.id, self.env.now))
            aging = 1
            try :
                yield self.env.process(self.wait(aging))
            except simpy.Interrupt :
                print('message send')
    
    def wait(self,duration):
        yield self.env.timeout(duration)

env = simpy.Environment()
node_1 = Node(1,env)
node_2 = Node(2,env)

def message(env,node_1,node_2):
    bc_pipe = Pipe(env)
    env.process(Pipe.message_generator(node_1.id, env, bc_pipe))
    env.process(Pipe.message_consumer(node_1.id, env, bc_pipe.get_output_conn()))
    env.process(Pipe.message_consumer(node_2.id, env, bc_pipe.get_output_conn()))
    node_1.action.interrupt()
    node_2.action.interrupt()

env.process(message(env, node_1,node_2))
env.run(until=15)
    