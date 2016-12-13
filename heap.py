import math

class MaxHeap(list):
    def __init__(self, arr):
        super().__init__(arr)
        self.heapSize = self.length = self.__len__()
        for i in range(self.length//2 -1, -1, -1):
            self.maxHeapify(i)

    def parent(self,i):
        return math.ceil(i/2) - 1

    def left(self,i):
        return 2*i+1

    def right(self,i):
        return 2*i+2

    def maxHeapify(self,i):
        l = self.left(i)
        r = self.right(i)

        if l < self.heapSize and self[l] > self[i]:
            largest = l
        else:
            largest = i

        if r < self.heapSize and self[r] > self[largest]:
            largest = r
        
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.maxHeapify(largest)

    def sort(self):
        for i in range(self.length-1, 0, -1):
            # print(i)
            self[0],self[i] = self[i],self[0]
            self.heapSize -= 1
            maxHeapify(self,0)
            print(self)

    def extractMax(self):
        if self.heapSize < 0:
            raise 'empty heap!'

        maximum, self[0] = self[0], self[self.heapSize-1]
        self.maxHeapify(0)
        self.pop(self.heapSize-1)
        self.heapSize -= 1

        return maximum

    def increaseKey(self, i, key):
        if key < self[i]:
            raise "New key is smaller than current key."

        self[i] = key
        while(i>0 and self[self.parent(i)]<self[i]):
            self[self.parent(i)], self[i] = self[i], self[self.parent(i)]
            i = self.parent(i)

    def insertKey(self, key):
        self.heapSize += 1
        self.append(key-1)
        self.increaseKey(self.heapSize-1, key)