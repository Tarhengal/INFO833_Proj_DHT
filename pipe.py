import simpy
import random

class Pipe(object):
    
    def __init__(self, env, capacity=simpy.core.Infinity):
        self.env = env
        self.capacity = capacity
        self.pipes = []
        
    def put(self, value):
        if not self.pipes:
            raise RuntimeError('There are no output pipes.')
        events = [store.put(value) for store in self.pipes]
        return self.env.all_of(events)  # Condition event for all "events"
    
    def message_generator(node_id, env, out_pipe):
    
        while True:
            yield env.timeout(random.randint(6, 10))
            msg = (env.now, '%s says hello at %d' % (node_id, env.now))
            out_pipe.put(msg)

    def get_output_conn(self):
        pipe = simpy.Store(self.env, capacity=self.capacity)
        self.pipes.append(pipe)
        return pipe

    def message_consumer(node_id, env, in_pipe):
        while True:
            msg = yield in_pipe.get()
            
            if msg[0] < env.now:
                print('LATE Getting Message: at time %d: %s received message: %s' %
                    (env.now, node_id, msg[1]))

            else:
                print('at time %d: %s received message: %s.' %
                    (env.now, node_id, msg[1]))

            yield env.timeout(random.randint(4, 8))