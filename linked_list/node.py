class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, element=None, next=None):
        self.elem = element
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        if self.elem == other.elem:
            return True
        return False 

    def __repr__(self):
        return self.elem