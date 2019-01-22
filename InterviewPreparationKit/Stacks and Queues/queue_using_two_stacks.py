class MyQueue(object):
    def __init__(self):
        self.inst = []
        self.outst = []
    def peek(self):
        if len(self.outst) == 0:
            while len(self.inst) != 0:
                a = self.inst.pop()
                self.outst.append(a)
        return self.outst[len(self.outst) - 1]
        
    def pop(self):
        if len(self.outst) == 0:
            while len(self.inst) != 0:
                a = self.inst.pop()
                self.outst.append(a)
        return self.outst.pop()        
        
    def put(self, value):
        self.inst.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
