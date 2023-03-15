import simpy
import random

class Pipe(object):
    
    def __init__(self, env, capacity=simpy.core.Infinity):
        self.env = env
        self.capacity = capacity
        self.pipes = []

    def message_generator(sender_id, reciever_id, content, env, self):
        yield env.timeout(random.randint(6, 10))
        date = self.env.now
        msg = (date,sender_id, reciever_id, content, env)
        self.put(msg)    

    def send(sender, reciever, content, env, self):
        '''
        while True :
            with message.request() as req :
                yield req
                print('%s envoyé à %d' % (content,env.now))
            yield env.timeout(0)
        '''
        self.env.process(self.message_generator(sender.id, reciever.id, content, env))
        self.env.process(self.receive(env))

    def receive(self, env):
        msg = yield self.get()
        #self.messages.append((msg.date, msg.reciever_id, msg.sender_id, msg.content))
        print('At time %d: Node %s received message : %s from Node %s' % (msg.date, msg.reciver_id, msg.content, msg.sender.id))
        yield env.timeout(random.randint(4, 8))

    '''
    def put(self, value):
        if not self.pipes:
            raise RuntimeError('There are no output pipes.')
        events = [store.put(value) for store in self.pipes]
        return self.env.all_of(events)  # Condition event for all "events"
    
    def get_output_conn(self):
        pipe = simpy.Store(self.env, capacity=self.capacity)
        self.pipes.append(pipe)
        return pipe
    
    def message_generator(node_id, env, out_pipe):
        while True:
            yield env.timeout(random.randint(6, 10))
            msg = (env.now, '%s says hello at %d' % (node_id, env.now))
            out_pipe.put(msg)

    def message_consumer(node_id, env, in_pipe):
        while True:
            msg = yield in_pipe.get()
            
            if msg[0] < env.now:
                print('LATE Getting Message: at time %d: %s received message: %s' %
                    (env.now, node_id, msg[1]))

            else:
                print('at time %d: %s received message: %s.' %
                    (env.now, node_id, msg[1]))

    '''    
    