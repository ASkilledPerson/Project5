from Queue import LinkedQueue
from QuickSort import quick_sort

from QuickSort import pick_pivot

# queue = LinkedQueue()
# print(queue.is_empty())
#
# queue.enqueue(1)
# queue.enqueue(7)
# print(queue)
# queue.enqueue(5)
# queue.enqueue(54)
# queue.enqueue(22)
# queue.enqueue(4)
# queue.enqueue(57)
# queue.enqueue(56)
# queue.enqueue(55)
# queue.enqueue(53)
# queue.enqueue(51)
#
#
# # print(queue.dequeue())
# print(queue.get_middle())
# print("kk")
# print(queue)
#
# quick_sort(queue)
# print("lll",queue)
# print("@@@", pick_pivot(queue))


def AddValues(queue, fp):
    '''
    :param queue: queue to add values to
    :param fp: file pointer to read from
    :return:  None
    '''
    for num in fp:
        queue.enqueue(num)



if __name__ == '__main__':
    fp = open(input("Please Enter File Name: "), "r")
    queue = LinkedQueue()

    AddValues(queue, fp)
    fp.close()

    quick_sort(queue)
    print(queue)
