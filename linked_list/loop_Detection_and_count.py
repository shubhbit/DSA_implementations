from node_insertion_singly_ll import CRUDLinkedList
from singly_ll_with_3_nodes import Node

class LoopDetection(CRUDLinkedList):
    def __init__(self):
        super().__init__()

    def detect_loop_floyds_algo(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return slow_p
    def get_length_of_loop(self, common_ptr):
        count = 0
        temp = common_ptr
        print("val: ", common_ptr.value)
        print("")
        while 1:
            temp = temp.next
            count +=1
            if temp == common_ptr:
                return count
        


if __name__ == "__main__":
    elems = [12, 34, 90, 23, 76]
    linked_list = LoopDetection()
    linked_list.head = Node(elems[0])
    node_2 = Node(elems[1])
    node_3 = Node(elems[2])
    node_4 = Node(elems[3])
    node_5 = Node(elems[4])
    linked_list.head.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_3

    # for elem in elems:
    #     print(f"adding {elem}")
    #     linked_list.insert_a_node_at_end(elem)
    #
    # print("printing list after adding 5 elements")
    # linked_list.traverse_list()
    print("Detecting a loop in linkedin: ")
    common_ptr = linked_list.detect_loop_floyds_algo()
    print("lenght of loop: ", linked_list.get_length_of_loop(common_ptr))