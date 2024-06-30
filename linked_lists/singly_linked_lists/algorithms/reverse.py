from singly_linked_list import SinglyLinkedList

def reverse_list(self):
    prev = None
    current = self.head
    next = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    self.head = prev

#Add method to SinglyLinkedList
SinglyLinkedList.reverse_list = reverse_list


if __name__ == "__main__":
    list = SinglyLinkedList()

    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    print(list)

    list.reverse_list()
    print(list)
