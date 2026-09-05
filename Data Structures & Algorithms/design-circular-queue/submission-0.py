class MyCircularQueue:

    def __init__(self, k: int):
        self.k =k
        self.front = 0
        self.rear = -1
        self.store = 0
        self.arr =[0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.k
        self.arr[self.rear] = value
        self.store +=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) %self.k
        self.store -=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.store ==0

    def isFull(self) -> bool:
        return self.k == self.store


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()