
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        
        self.head = None
    
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
            result += str(current.data) + " -> "
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
    
    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size
    
    def prepend(self, data:int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node, data) ->None:
        if not prev_node:
            print("Previous node cannot be null")
            return 
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_by_key(self, key) -> None:
        tmp = self.head
        prev = None

        if tmp and tmp.data == key:
            print("Key found at head position")
            self.head = tmp.next
            del tmp
            return
        
        while tmp and tmp.data != key:
            prev = tmp
            tmp = tmp.next
        
        if not tmp:
            print(f"Key {key} not found in linked list")
            return
        
        print(f"Key {key} found in linked list")
        del tmp

    



if __name__=="__main__":
    list = SinglyLinkedList()

    list.append(1)
    list.append(2)
    list.append(3)
    list.prepend(0)
    print(list)
