from .interface import AbstractLinkedList

from linked_list.node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList interface.
    """
    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        if elements:
            for elem in elements:
                self.append(elem)

                    
    def __str__(self):
        return 

    def __len__(self):
        if self.start is None:
            return 0
            
        length = 1
        aux = self.start
        while aux.next != None:
            aux = aux.next
            length += 1
        return length

    def __iter__(self):
        aux = self.start
        while aux:
            yield aux.elem
            aux = aux.next
        raise StopIteration   
            
    def __getitem__(self, index):
        import ipdb; ipdb.set_trace()
        pass
    # l = [object1,object2,object3]
    
    #have to:
    #enumerate(self)
    #check if index is in any of enumerate(self)'s tuples
    
    # list(enumerate(l))
    # [(0, object1), ... ]
    
    #raise KeyError if index doesn't exist in our object
    
    # IndexError?

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        if len(self) != len(other):
            return False
            
        #for elem in range(len(self)):
        #    if self[elem] 

    def append(self, elem):
        new_node = Node(elem)
        
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def count(self):
        return len(self)

    def pop(self, index=None):
        pass

# l = LinkedList()
# l = LinkedList([1, 5, 10])