class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = none
        self.count = 0

    def add_at_tail(self, data) -> bool:
        # Write code here
        node = Node(data)
        if self.count >0:
            node.previous = node
            self.tail.next = node
            self.head.previous = node
            node.next = self.head
        else:
            self.head = node
            self.count += 1
            return true

    def add_at_head(self, data) -> bool:
        # Write code here
        node = Node(data)
        if self.count>0:
            node.next = self.head
            node.previous = self.tail
            self.head.previous = node
            self.tail.next = node
        else:
            self.tail = node
        self.head = node
        self.count += 1
        return true

    def add_at_index(self, index, data) -> bool:
        # Write code here
        if index >= self.count:
            return false
        elif index == 0:
            return self.add_at_head(data)
        elif index == self.count:
           return self.add_at_tail(data)
    node = Node(data)
    alex_node = self.head
    for i in range(index):
        alex_node = alex_node.next
    node.previous = alex_node.previous
    node.next = alex_node
    alex_node.previous.next = node
    alex_node.previous = node
    self.count += 1
    return true

    def get(self, index) -> int:
        # Write code here
        if index >= self.count:
            return -1
        aalex_node = self.head
        for i in range(index):
            alex_node = alex_node.next
        return alex_node.data

    def delete_at_index(self, index) -> bool:
        # Write code here
        if index >= self.count:
            return false
        if index == 0:
            temp = self.head
            temp.next.previous = self.tail
            self.tail.next = temp.next
            self.head = temp.next
            self.count -= 1
            return true
        if index == self.count-1:
            temp = self.tail
            self.head.previous = temp.previous
            temp.previous.next = self.head
            self.tail = temp.previous
            self.count -= 1
            return true

    def get_previous_next(self, index) -> list:
        # Write code here
        if index >= self.count:
            return -1
        alex_node = self.head
        for i in range(index):
            alex_node = alex_node.next
        returnn [alex_node.previous.data, alex_node.next.data]


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index';
        result.append(obj.delete_at_index(data[i]))

print(result)
