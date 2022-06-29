import sys

# Parent index = floor((index - 1) / 2)
# left child = 2 * index + 1
# right child = 2 * index + 2
# Inserting: insert at end at heapify up
# Removing min: swap value at end with min value, and heapifyDown

class MinHeap:
    def __init__(self, capacity):
        minVal = sys.maxsize * -1
        self.heap = [minVal] * capacity
        self.capacity = capacity
        self.size = 0
    
    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.heap[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity
    
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def insert(self, data):
        if self.isFull():
            raise("Heap is full")
        self.heap[self.size] = data
        self.size += 1

        self.heapifyUp()

    def insertRecursive(self, data):
        if self.isFull():
            raise("Heap is full")
        self.heap[self.size] = data
        self.size += 1

        self.heapifyUp(self.size - 1)

    def heapifyUp(self, index=None):
        if index != None: # Recursive method
            index = self.size - 1
            if self.hasParent(index) and self.parent(index) > self.heap[index]:
                index = self.heapifySwap(index)

        else: # Iterative method
            index = self.size - 1
            while self.hasParent(index) and self.parent(index) > self.heap[index]:
                index = self.heapifySwap(index)

    def heapifySwap(self, index):
        self.swap(self.getParentIndex(index), index)
        return self.getParentIndex(index)

    def removeMin(self):
        if self.size == 0:
            raise "Empty Heap"
        data = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data

    def removeMinRecursive(self):
        if self.size == 0:
            raise "Empty Heap"
        data = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data
    
    def heapifyDown(self, index = None):
        if index: # Recursive method
            smallest = index
            if self.hasLeftChild(index) and self.heap[smallest] > self.leftChild(index):
                smallest = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.heap[smallest] > self.rightChild(index):
                smallest = self.getRightChildIndex(index)
            if smallest != index:  # Swap if either left or right child is smaller than value at heap[index]
                self.swap(index, smallest)  
                self.heapifyDown(smallest)
        else: # Iterative method
            index = 0
            while self.hasLeftChild(index):  # Only need to check left child since heaps MUST be filled left to right
                smallerChildIndex = self.getLeftChildIndex(index)
                if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                    smallerChildIndex = self.getRightChildIndex(index)
                if self.heap[index] < self.heap[smallerChildIndex]:
                    break
                else:
                    self.swap(index, smallerChildIndex)
                index = smallerChildIndex

    def getHeap(self):
        return self.heap[0: self.size ]

heap = MinHeap(7)
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.removeMin()
heap.removeMin()


print(heap.getHeap())