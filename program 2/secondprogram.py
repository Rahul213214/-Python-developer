class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def find_middle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer.data if slow_pointer else None

if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)

    middle_element = linked_list.find_middle()
    print(f"The middle element is: {middle_element}")
