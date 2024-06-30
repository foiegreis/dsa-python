from doubly_linked_list import DoublyLinkedList

""" Removes duplicates from linked list"""

def remove_duplicates(self):
    if not self.head:
        return
    current = self.head
    while current and current.next:
        if current.data == current.next.data:
            temp = current.next
            current.next = current.next.next
            if current.next:
                current.next.prev = current
            del temp
        else:
            current = current.next


# Add method to SinglyLinkedList
DoublyLinkedList.remove_duplicates = remove_duplicates


if __name__ == "__main__":
    list = DoublyLinkedList()
    list.append(1)
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(3)
    list.append(4)

    print("List: ")
    print(list)

    list.remove_duplicates()
    print("List after removing duplicates:")
    print(list)
