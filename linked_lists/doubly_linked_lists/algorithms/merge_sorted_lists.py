from doubly_linked_list import DoublyLinkedList, Node

"""Merges two sorted linked lists into one sorted linked list"""

def merge_sorted_lists(self, list2):
    dummy = Node(0)
    current = dummy
    list1 = self.head

    # Traverse both lists and compare nodes
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1.prev = current
            list1 = list1.next
        else:
            current.next = list2
            list2.prev = current
            list2 = list2.next

        current = current.next

    # Add remaining nodes
    if list1:
        current.next = list1
        list1.prev = current
    if list2:
        current.next = list2
        list2.prev = current

    self.head = dummy.next
    if self.head:
        self.head.prev = None


# Add method to SinglyLinkedList
DoublyLinkedList.merge_sorted_lists = merge_sorted_lists


if __name__ == "__main__":
    list1 = DoublyLinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    print("List1: ")
    print(list1)

    list2 = DoublyLinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    print("List2: ")
    print(list2)

    list1.merge_sorted_lists(list2.head)
    print("Merged list:")
    print(list1)

