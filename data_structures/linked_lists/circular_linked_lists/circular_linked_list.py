""" Class to create circular linked list """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Point to itself to form circular structure
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(" (Head)")

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail


if __name__ == "__main__":
    # Create a circular linked list
    cll = CircularLinkedList()

    # Append nodes
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)
    cll.append(5)

    # Print the circular linked list
    cll.print_list()

    # Access head and tail
    head = cll.get_head()
    tail = cll.get_tail()
    print(f"Head: {head.data}")
    print(f"Tail: {tail.data}")
