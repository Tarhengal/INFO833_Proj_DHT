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
    
    def message_generator(node, env, out_pipe,info):
        yield env.timeout(0)
        #random.randint(6, 10)
        msg = (env.now,info,node)
        out_pipe.put(msg)

    def get_output_conn(self):
        pipe = simpy.Store(self.env, capacity=self.capacity)
        self.pipes.append(pipe)
        return pipe

    def message_consumer(node, env, in_pipe):
    
        msg = yield in_pipe.get()
        info = msg[1]
        if info[-1] == 1:  # start insert node 
            if msg[0] < env.now:
                print('LATE Getting Message: at time %d: %s received message: %s' %
                    (env.now, node.id, msg[1]))
            else:
                print('at time %d: %s received message: %s from node :%s.' %
                    (env.now, node.id, msg[1],str(msg[2].id)))
            
            if node.id == info[0]:
                node.setNeighborsR(info[4])
                node.message(env,info[4],node,[node,info[4],3],1)
            if node.id == info[1]:
                node.setNeighborsL(info[4])
                node.message(env,info[4],node,[node,info[4],3],1)

        
        if info[-1]==2: # double it and pass it to the next one
            # stop time interuption
            print("try doing verification %d .verification (%d , env )  "%(info[0].id,info[1].id))
            info[0].verification(info[1],info[2])
        
        if info[-1]==3: # Validation 
            # stop time interuption
            print("Validation from %d to %d " % ( info[0].id ,info[1].id ))

        if info[-1]==4:
            if node.id == info[0].id:
                node.r_n=info[1]
            if node.id == info[1].id:
                node.l_n=info[0]



        
        yield env.timeout(random.randint(4, 8))


            

        