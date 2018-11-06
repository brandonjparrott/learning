"""
    Doubly Linked List

    Main Questions / Objectives:

        - Reverse a linked list
        - Detect a loop cycle in a linked list
        - Return the nth node from the end of a linked list
        - Remove duplicates from a linked list

    Main Methods to implement:

        - addToStart - done
        - addToEnd - done
        - isEmpty - done
        - remove - done
        - insert (at a specific position)
        - reverse - done
        - removeDuplicates - Done
        - display - done
"""


class MyNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def addToStart(self, data):
        if self.head is None:
            self.head = MyNode(data)
            return
        node = MyNode(data)
        node.next = self.head
        self.head = node
        return

    def addToEnd(self, data):
        if self.head is None:
            self.head = MyNode(data)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = MyNode(data)

    def isEmpty(self):
        return self.head is None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        node = self.head
        prev = None
        while node is not None:
            if node.data == data:
                break
            prev = node
            node = node.next
        if node is None:
            return
        prev.next = node.next

    def removeDuplicates(self):
        current = second = self.head
        while current is not None:
            while second.next is not None:
                if second.next.data == current.data:
                    second.next = second.next.next
                else:
                    second = second.next
            current = second = current.next

    def display(self):
        if self.head is None:
            print("List is empty!")
        node = self.head
        while node is not None:
            print(str(node.data))
            node = node.next


"""
    Test one:
    
    Make sure we are appending and prepending correctly...
"""
# MyList = MyLinkedList()
# MyList.addToStart("I")
# MyList.addToEnd("am")
# MyList.addToEnd("brandon")
# MyList.display()
#
# MyList = MyLinkedList()
# MyList.addToEnd("am")
# MyList.addToEnd("brandon")
# MyList.addToStart("I")
# MyList.display()


"""
    Test Two:
    
    Reverse a linked list
"""
# MyList = MyLinkedList()
# MyList.addToStart("am")
# MyList.addToEnd("brandon")
# MyList.addToStart("I")
# MyList.reverse()
# MyList.display()


"""
    Test Three:
    
    Remove a node
"""
# MyList = MyLinkedList()
# MyList.addToStart("I")
# MyList.addToEnd("am")
# MyList.addToEnd("brandon")
# MyList.remove("am")
# MyList.display()

"""
    Test Four:
    
    remove duplicates
"""
# MyList = MyLinkedList()
# MyList.addToStart("I")
# MyList.addToEnd("am")
# MyList.addToEnd("am")
# MyList.addToEnd("brandon")
# MyList.addToEnd("brandon")
# MyList.addToEnd("brandon")
# MyList.removeDuplicates()
# MyList.display()

