from singly_linked_list import SinglyLinkedList

"""Uses the Floyd's Cycle-Finding Algorithm = slow and fast pointers method"""

def find_middle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# Add method to SinglyLinkedList
SinglyLinkedList.find_middle = find_middle


if __name__ == "__main__":
    list = SinglyLinkedList()

    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
    list.append(7)
    print(list)

    middle = list.find_middle()
    print("middle element: ", middle)
