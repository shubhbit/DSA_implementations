from singly_ll_with_3_nodes import Node, LinkedList

def remove_duplicates(head):
    temp = head
    print("val: ", temp.value)
    print("next: ", temp.next)
    print("next: ", temp.next)
    while  temp.next:
        if temp.value == temp.next.value:
            if temp.next.next:
                temp.next = temp.next.next
            else:
                temp.next = Node
        temp = temp.next
    return head



if __name__ == "__main__":
    elems = ["1", "2", "2", "2", "10"]
    linked_list = LinkedList()
    linked_list.head = Node(elems[0])
    node_2 = Node(elems[1])
    node_3 = Node(elems[2])
    node_4 = Node(elems[3])
    node_5 = Node(elems[4])
    linked_list.head.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    linked_list.traverse_list()
    print("removing duplicates")
    # print(linked_list.head.next)
    remove_duplicates(linked_list.head)
    linked_list.traverse_list()
