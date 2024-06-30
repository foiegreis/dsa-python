
"""Flattens multilevel Doubly linked List"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __del__(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node

    def __repr__(self) -> str:
        current = self.head
        if not current:
            return "The list is empty"
        result = ""
        while current:
            result += str(current.data) + " <--> "
            current = current.next
        return result + "None"

    def get_head(self):
        return self.head

    def get_tail(self):
        if not self.head:
            return None

        current = self.head
        while current.next:
            current = current.next

        return current

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Print multilevel doubly linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            if current.child:
                print("(", end="")
                self.print_child_list(current.child)
                print(")", end="")
            current = current.next
        print("None")

    # Helper function to print multilevel doubly linked list
    def print_child_list(self, child_head):
        current = child_head
        while current:
            print(current.data, end=" <-> ")
            if current.child:
                print("(", end="")
                self.print_child_list(current.child)
                print(")", end="")
            current = current.next

    # Flatten doubly linked list
    def flatten(self):
        current = self.head
        while current:
            if current.child:
                # Flatten child list
                self.tail.next = current.child
                current.child.prev = self.tail

                # Update tail to the end of child list
                child_tail = current.child
                while child_tail.next:
                    child_tail = child_tail.next
                self.tail = child_tail

                # Remove child link
                current.child = None

            current = current.next


if __name__ == "__main__":
    # Create a doubly linked list
    list1 = DoublyLinkedList()

    # Append nodes
    list1.append(1)
    list1.append(2)
    list1.append(3)

    # Adding a child list
    list1.head.child = Node(4)
    list1.head.child.next = Node(5)
    list1.head.child.next.prev = list1.head.child
    list1.head.child.next.child = Node(6)

    # Print the list with children
    print("Original Doubly Linked List:")
    list1.print_list()

    # Flatten the list
    list1.flatten()

    # Print the flattened list
    print("\nFlattened Doubly Linked List:")
    list1.print_list()
