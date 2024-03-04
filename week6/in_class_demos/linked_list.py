class Node:
    def __init__(self, data):
        self.data = data
        # When we create a node set its next value to none so no node is linked to it
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # This only intiatates at the start of the list creation creating a head node in our list
        if self.head is None:
            self.head = new_node
            return
        # Sets the last node to the node at the start of the list
        last_node = self.head
        # Loops through from the first node checking the node for a next (linked) value
        while last_node.next:
            last_node = last_node.next
        # stos when no next(linked) value is found and sets the next(linked) value to the node just created
        last_node.next = new_node

    def getItem(self, index):
        # go to the start of the linkedlist
        current_node = self.head
        # use a count to find the item in the linked list by index once reached
        count = 0
        while current_node:
            if count == index:
                return current_node.data
            count += 1
            # move onto the next node using the linked list 
            current_node = current_node.next
        raise IndexError("Index out of range")

    def setItem(self, index, data):
        # go to the start of the linkedlist
        current_node = self.head
        # use a count to set the item data in the linked list by index once reached
        count = 0
        while current_node:
            if count == index:
                current_node.data = data
                return
            count += 1
            # move onto the next node using the linked list 
            current_node = current_node.next
        raise IndexError("Index out of range")
    
    def display(self):
        # go to the start of the linkedlist
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            # move onto the next node using the linked list 
            current_node = current_node.next
        print()
    
# Example usage:
my_list = LinkedList()
my_list.append("0x1001")
my_list.append("0x1002")
my_list.append("0x1003")

print("Initial list:")
my_list.display()

print("Item at index 1:", my_list.getItem(1))

my_list.setItem(1, "0x2005")
print("Updated list after setting item at index 1 to 0x2005:")
my_list.display()