class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.lenght = 0

    def present(self):
        value = ''
        node = self.head
        while node:
            value += str(node.data) + ", "
            node = node.next
        print("[" + value + "]")

    def prepend(self, data):
        self.head = Node(data, self.head)
        self.lenght+= 1


    # def __iter__(self):
    #
    #     return self
    #
    # def __next__(self):
    #     return self.head.next

    def search(self, data):
        node = self.head
        idx = 0
        while node:
            if node.data == data:
                return idx
            idx += 1
            node = node.next
        return -1


m = LinkedList()
m.prepend(2)
m.prepend(4)
m.prepend(6)
print("m->\n", m)
m.present()
print("--->\n", )
print(m.search(2))
# print("m--->\n", m.head)
# print("m--->\n", m.head.data)
# print("m--->\n", m.lenght)
# print("iterate--->\n", m.__iter__())
