from singly_linked_list import SinglyLinkedList

""" Rotates linked list by k places to the right"""

def rotate_right_by_k_places(self, k):
    if (not self.head or k == 0):
        return

    # Get length of linked list
    length = 1
    current = self.head
    while current.next:
        current = current.next
        length += 1

    # Make the list circular
    current.next = self.head

    # Find the new head and tail
    k = k % length
    steps_to_new_head = length - k
    new_tail = self.head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    self.head = new_head

# Add method to SinglyLinkedList
SinglyLinkedList.rotate_right_by_k_places = rotate_right_by_k_places


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    print("List: ")
    print(list1)

    list1.rotate_right_by_k_places(2)
    print("List after rotating right by 2:")
    print(list1)
