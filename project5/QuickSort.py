from Queue import Node
from Queue import LinkedQueue

def insertion_sort(queue):
    """
    If the size of the queue is less than 10.
    :param queue: type: LinkedQueue less than 10 elements
    :return: None
    """
    if queue.head == None:
        return None
    sorted_list = queue.head
    queue.head = queue.head.next
    sorted_list.next = None
    while queue.head is not None:
        temp_node = queue.head
        queue.head = queue.head.next
        if temp_node < sorted_list:
            temp_node.next = sorted_list
            sorted_list = temp_node
        else:
            search_index = sorted_list
            while search_index.next is not None and search_index.next < temp_node:
                search_index = search_index.next
            temp_node.next = search_index.next
            search_index.next = temp_node
    queue.head = sorted_list

def pick_pivot(queue):
    """
    :param queue: Type LinkedQueue queue
    :return: Pivot element Type: Node.val
    """
    new_queue = LinkedQueue()
    new_queue.enqueue(queue.head.val)
    new_queue.enqueue(queue.tail.val)
    new_queue.enqueue(queue.get_middle())
    insertion_sort(new_queue)
    return new_queue.head.val


def quick_sort(queue):
    """

    :param queue:
    :return:
    """
    size = len(queue)
    if size <=10:
        insertion_sort(queue)
    else:
        p = pick_pivot(queue)
        lesser_list = LinkedQueue()
        greater_list = LinkedQueue()
        equal_list = LinkedQueue()

        while not queue.is_empty():
            if queue.head.val < p:
                lesser_list.enqueue(queue.dequeue())
            elif queue.head.val > p:
                greater_list.enqueue(queue.dequeue())
            else:
                equal_list.enqueue(queue.dequeue())
        quick_sort(lesser_list)
        quick_sort(greater_list)

        while not lesser_list.is_empty():
            queue.enqueue(lesser_list.dequeue())

        while not equal_list.is_empty():
            queue.enqueue(equal_list.dequeue())

        while not greater_list.is_empty():
            queue.enqueue(greater_list.dequeue())