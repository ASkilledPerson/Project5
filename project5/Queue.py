class Node:
    """Lightweight, nonpublic class for storing a singly linked node.
    should only be called within the LinkedQueue class definition """

    __slots__ = 'val', 'next'  # streamline memory usage

    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __lt__(self, other):
        ''' assumes other is of same type, invoked with "<" '''
        return self.val <= other.val

    def __le__(self, other):
        ''' assumes other is of same type, invoked with "<=" '''
        return self.val <= other.val


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        ''' string implementation of current elements in queue '''
        head = self.head
        values = list()
        while head:
            values.append(str(head.val))
            head = head.next

        return ", ".join(values)

    __repr__ = __str__

    ################## start modifying below this line ######################
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def dequeue(self):
        """
        removes and returns the first val
        :return: Node.val
        """
        store_val = None
        if not self.is_empty():
            if self.size == 1:
                store_val = self.head.val
                self.head.val = None
                self.tail.val = None

            else:
                store_val = self.head.val
                self.head.val = None
                self.head = self.head.next
            self.size -= 1
        return store_val

    def enqueue(self, element):
        """
        Adds a node to the queue at the end
        :param element: adds a node with element as the val
        :return: None
        """
        add_val = Node(element, None)
        if self.is_empty():
            add_val = Node(element, None)
            self.tail = add_val
            self.head = self.tail
        else:
            self.tail.next = add_val
            self.tail = add_val
        self.size += 1


    def get_middle(self):
        """
        return the element at the position self.size//2
        :return: Node.val
        """
        node = self.head
        mid_val = None
        mid_val_index = self.size//2
        for i in range(mid_val_index+1):
            mid_val = node.val
            node = node.next
        return mid_val