"""
list.head            second                last node
    |                   |                    |
    |                   |                    |
+---+------+      +-----+-------+      +-----+-----+  ----------- 
|  1|  o--------->| 2   |  o---------> | 3   | None
+---+------+      +-----+-------+      +-----+-----+  -----------

"""
# three steps to create linked list
# 1- create head and tail inialize with null
# 2- create ablank node and assigne a value to it and reference to null
# 3- link Head and tial with these node
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode


# ++++++++++++++++++++++++++++++++++++++++++
single_linked_list = SLinkedList()
single_linked_list.insertSLL(1, 1)
single_linked_list.insertSLL(2, 1)
single_linked_list.insertSLL(3, 1)
single_linked_list.insertSLL(4, 1)


# inset in the begining
single_linked_list.insertSLL(0, 0)

# inset in the middel
single_linked_list.insertSLL(33, 3)

print([node.value for node in single_linked_list])
