from doubly_linked_list import DoublyLinkedList


def reverse_list(self):
    if not self.head or not self.head.next:
        return

    current = self.head
    prev_node = None

    while current:
        next_node = current.next
        current.next = prev_node
        current.prev = next_node
        prev_node = current
        current = next_node

    self.head = prev_node


# Add method to SinglyLinkedList
DoublyLinkedList.reverse_list = reverse_list


if __name__ == "__main__":
    list = DoublyLinkedList()

    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    print(list)

    list.reverse_list()
    print(list)
