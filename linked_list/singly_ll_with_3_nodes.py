class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def traverse_list(self):
        """
        method to traverse a list
        :param list: list to be travered
        :return: None
        """
        temp = self.head
        while temp:
            print(f"Node: {temp.value}")
            temp = temp.next

    def length_iterative_way(self):
        """
        iteratively finds length of a linked list
        :return: int: length of linked list
        """
        length = 0
        if self.head:
            temp = self.head
            length += 1
            while temp.next:
                length += 1
                temp = temp.next
        return length

    def length_recursive_way(self, node):
        if not node:
            return 0
        else:
            return 1+ self.length_recursive_way(node.next)

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(23)
    second = Node(12)
    third = Node(89)
    ll.head.next = second
    second.next = third
    ll.traverse_list()

