from singly_linked_list import SinglyLinkedList, Node

""" Checks if singly linked list is palindrome. Uses the slow fast pointer approach"""

def is_palindrome(self) -> bool:
    slow = self.head
    fast = self.head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast: #Skip the middle element if the length is odd
        slow = slow.next

    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next

    return True

# Add method to SinglyLinkedList
SinglyLinkedList.is_palindrome = is_palindrome


if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(2)
    list1.append(1)
    print("List: ")
    print(list1)

    palindrome = list1.is_palindrome()
    print("\nLinked List is a palindrome: ", palindrome)

