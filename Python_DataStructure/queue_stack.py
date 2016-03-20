
# 1. Two stacks s1 & s2
# 2. Enqueue: push to s1
# 3. Dequeue: if s2 not empty pop from s2  
#if s2 empty copy all elements from s1 to s2 and then pop





class Queue(object):
    def __init__(self):
        self.S1 = []
        self.S2 = []
     
    def enqueue(self, data):
        print("inserting data... %d" % (data))
        self.S1.append(data)
    
    def dequeue(self):
        if not self.S2:
            while self.S1:
                self.S2.append(self.S1.pop())
        return self.S2.pop() 
	    
q = Queue()
for i in range(5):
    q.enqueue(i)
for i in range(5):
    print("returning data ...", q.dequeue()) 