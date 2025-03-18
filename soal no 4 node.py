class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List kosong.")

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def insert_at(self, position, value):
        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            current_position = 0
            while current and current_position < position - 1:
                current = current.next
                current_position += 1

            if not current:
                print("Posisi melebihi panjang list.")
                return

            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Sebelum insert:")
linked_list.display()  

linked_list.insert_at(1, 50)

print("Setelah insert:")
linked_list.display() 

linked_list.insert_at(0, 100)

print("Setelah insert di awal:")
linked_list.display() 

linked_list.insert_at(10, 200)
