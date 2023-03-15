import simpy
import random

class Node(object) :
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
                print('message')
    
    def wait(self,duration):
        yield self.env.timeout(duration)
    