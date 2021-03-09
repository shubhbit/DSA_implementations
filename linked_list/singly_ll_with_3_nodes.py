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



if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(23)
    second = Node(12)
    third = Node(89)
    ll.head.next = second
    second.next = third
    ll.traverse_list()

