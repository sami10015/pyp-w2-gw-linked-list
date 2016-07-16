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
        if self.start is None and self.end is None:
            return '[]'
        return_str = '['
        for elem in self:
            if elem == self.end.elem:
                return_str += str(elem) + ']'
                break
            return_str += str(elem) + ', '
        return return_str

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
        #While aux exists
        while aux:
            #Return and hold the element under that node, and move it to the next one
            yield aux.elem
            aux = aux.next
        #When done, raise a StopIteration error 
        raise StopIteration   
            
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('list indices must be integers, not str')
        elif index >= len(self):
            raise IndexError('list index out of range')
            
        for i, elem in enumerate(self):
            if i == index:
                return elem
        raise KeyError #If nothing was found, raise a KeyError

    def __add__(self, other):
        aux_list = LinkedList()
        for node in self:
            aux_list.append(node)
            
        for node in other:
            aux_list.append(node)
        return aux_list

    def __iadd__(self, other):
        for node in other:
            self.append(node)
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for index, elem in enumerate(self):
            if elem != other[index]:
                return False
        return True
        
    def __ne__(self, other):
        return not self.__eq__(other)

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
        previous = self.start
        
        if len(self) == 0 or index >= len(self):
            raise IndexError
            
        if index is None:
            index = len(self) - 1
        
        if index == 0:
            return_elem = self.start.elem
            self.start = self.start.next
            return return_elem
            
        for i in range(index - 1):
            previous = previous.next
            
        if previous.next:
            return_elem = previous.next.elem
            previous.next = previous.next.next
            return return_elem
        else:
            return_elem = previous.elem
            self.start = None
            return return_elem