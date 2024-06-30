from doubly_linked_list import DoublyLinkedList

"""Uses the Floyd's Cycle-Finding Algorithm = slow and fast pointers method"""


def detect_cycle(self):
    if not self.head or not self.head.next:
        return False

    slow = self.head
    fast = self.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Add method to SinglyLinkedList
DoublyLinkedList.detect_cycle = detect_cycle


if __name__ == "__main__":
    list = DoublyLinkedList()

    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)

    # Create cycle for the example
    tail = list.get_tail()
    if tail:
        tail.next = list.get_head().next.next

    # NB: do not print or it will iterate forever

    #TODO controlla perche finisce in loop
    if list.detect_cycle():
        print("Cycle detected")
    else:
        print("No cycle detected")