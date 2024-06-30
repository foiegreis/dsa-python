from singly_linked_list import SinglyLinkedList, Node

"""Remove the nth node from end of linked list"""

def remove_nth_node_from_end(self, n):
    size = self.get_size()
    if size < n:
        print("The value n is outside the linked list range")
        return

    # Step 2: Edge case when n is equal to the length of the list
    if n == size:
        self.head = self.head.next
        return

    # Step 3: Find the (length - n)th node from the beginning
    prev = None
    current = self.head
    count = 0
    while current:
        if count == size - n:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            break
        prev = current
        current = current.next
        count += 1


# Add method to SinglyLinkedList
SinglyLinkedList.remove_nth_node_from_end = remove_nth_node_from_end


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(4)
    list1.append(5)
    list1.append(6)
    print("List: ")
    print(list1)

    n = 3
    list1.remove_nth_node_from_end(n)
    print("\nResulting linked list after removing the nth node from end:")
    print(list1)

