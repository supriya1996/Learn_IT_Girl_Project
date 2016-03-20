class Queue(object):
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.n = 0
        self.l = []
    
    def enqueue(self, element):
       
        self.l.append(element)
        self.tail += 1
        self.n += 1
    
    def dequeue(self):
        if self.n == 0: return None
        e = self.l[self.head]
        self.head += 1
        self.n -= 1
        return e
        
    def size(self):
        return self.n
    
    def elements(self):
        return [self.l[i] for i in xrange(self.head, self.tail)]
		
if __name__ == "__main__":
    q = Queue()
    
    assert None == q.dequeue()
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert 1 == q.dequeue()
    assert 2 == q.dequeue()
    assert 3 == q.dequeue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    
    assert 1 == q.dequeue()
    assert 2 == q.dequeue()
    assert 3 == q.dequeue()
    assert 4 == q.dequeue()
    assert 5 == q.dequeue()