class Node:
    def __init__(self, label):
        self.label = label
        self.next = None
        
    def getLabel(self):
        return self.label
        
    def getNext(self):
        return self.next