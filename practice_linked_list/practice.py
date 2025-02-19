class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print("None")


list1 = linked_list()
list1.append(1)
list1.append(2)
list1.append(3)
list1.printList()
