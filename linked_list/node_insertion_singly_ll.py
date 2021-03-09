from singly_ll_with_3_nodes import Node, LinkedList

class CRUDLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def insert_a_node_at(self, value, location):
        if self.head:
            init_location = 1
            temp = self.head
            while init_location < location-1:
                temp = temp.next
                init_location += 1
            if temp:
                temp2 = temp.next
                temp.next = Node(value)
                temp.next.next = temp2
                print(f"Node added at location: {location}")
        else:
            print("Linked list is empty")

    def insert_a_node_at_start(self, value):
        if self.head:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            print("New Node added at the start")
        else:
            self.head = Node(value)

    def insert_a_node_at_end(self, value):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
        else:
            self.head = Node(value)
        print("Node added at the end")



if __name__ == "__main__":
    elems = [12, 34, 90, 23, 76]
    linked_list = CRUDLinkedList()
    print("length of linked_list: ", linked_list.length_iterative_way())

    print("printing empty list")
    linked_list.traverse_list()
    for elem in elems:
        print(f"adding {elem}")
        linked_list.insert_a_node_at_end(elem)
    print("printing list after adding 4 elements")
    print("length of linked_list: ", linked_list.length_iterative_way())
    linked_list.traverse_list()
    print("Inserting 100 at the start")
    linked_list.insert_a_node_at_start(100)
    print("length of linked_list: ", linked_list.length_iterative_way())
    print("printing list after adding new element at start")
    linked_list.traverse_list()

    print("Inserting 500 at the 3rd")
    linked_list.insert_a_node_at(500, 3)
    print("length of linked_list: ", linked_list.length_iterative_way())
    print("printing list after adding new element at 3rd")
    linked_list.traverse_list()
    print("printing length of linked list recursive way: ", linked_list.length_recursive_way(linked_list.head))



