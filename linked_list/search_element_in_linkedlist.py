from node_insertion_singly_ll import CRUDLinkedList

class SearchElement(object):
    def __init__(self, head):
        self.head = head

    def search_element_iteratively(self, item):
        pass

    def search_element_recursively(self, item):
        pass

if __name__ == "__main__":
    linked_list = CRUDLinkedList()
    linked_list.insert_a_node_at_end(90)
    linked_list.insert_a_node_at_end(109)
    linked_list.insert_a_node_at_end(23)
    linked_list.insert_a_node_at_end(900)

    print("Searching for item:{0} in linked_list")
    print()
