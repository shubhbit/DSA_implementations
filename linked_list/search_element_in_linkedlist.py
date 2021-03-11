from node_insertion_singly_ll import CRUDLinkedList

class SearchElement(object):
    def __init__(self, head):
        self.head = head

    def search_element_iteratively(self, item):
        temp = self.head
        while temp:
            if temp.value == item:
                return True
            temp = temp.next
        return False

    def search_element_recursively(self, head, item):
        if not head:
            print("head empty")
            return False
        elif head.value == item:
            print("Matched")
            return True
        else:
            print("calling again")
            return self.search_element_recursively(head.next, item)

    def get_nth_element(self, index):
        init_index = 1
        temp = self.head
        while init_index < index and temp:
            init_index +=1
            temp = temp.next
        if temp:
            return temp.value
        else:
            return 0



if __name__ == "__main__":
    elems = [12, 34, 90, 23, 76]
    linked_list = CRUDLinkedList()
    print("length of linked_list: ", linked_list.length_iterative_way())
    for elem in elems:
        print(f"adding {elem}")
        linked_list.insert_a_node_at_end(elem)
    print("printing list after adding 5 elements")
    print("length of linked_list: ", linked_list.length_iterative_way())
    linked_list.traverse_list()
    search = SearchElement(linked_list.head)
    search_elem = 90
    print(f"Searching for item:{search_elem} in linked_list")
    print(f"Found: {search.search_element_iteratively(search_elem)}")
    linked_list.traverse_list()
    for search_elem in [12, 34, 90, 23, 76, 50000]:
        print(f"Searching for item recursively:{search_elem} in linked_list")
        print(f"Found: {search.search_element_recursively(search.head, search_elem)}")

    linked_list.traverse_list()

    n = -1
    print(f"Fining {n}th element")
    print(search.get_nth_element(n))