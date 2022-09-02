class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def add_at_tail(self, data) -> bool:
        node = Node(data)
        if self.count > 0:
            node.previous = self.tail
            self.tail.next = node
            self.head.previous = node
            node.next = self.head
        else:
            self.head = node
        self.tail = node
        self.count += 1
        return True

    def add_at_head(self, data) -> bool:   
        node = Node(data)
        if self.count > 0:
            node.next = self.head
            node.previous = self.tail
            self.head.previous = node
            self.tail.next = node
        else:
            self.tail = node
        self.head = node
        self.count += 1
        return True
    
    def add_at_index(self, index, data) -> bool:
        if index < 0 or index >= self.count:
            return False
        if index == 0:
            return self.add_at_head(data)
        if index == self.count:
            return self.add_at_tail(data)
        
        node = Node(data)
        alex_node = self.head
        for i in range(index):
            alex_node = alex_node.next
        node.previous = node.previous
        node.next = node
        alex_node.previous.next = node
        alex_node.previous = node
        self.count += 1
        return True        

    def get(self, index) -> int:
        if index < 0 or index >= self.count:
            return -1
        alex_node = self.head
        for i in range(index):
            alex_node = alex_node.next
        return alex_node.data
       
    def delete_at_index(self, index) -> bool:
        if index < 0 or index >= self.count:
            return False
        if index == 0:
            temp = self.head
            temp.next.previous = self.tail
            self.tail.next = temp.next
            self.head = temp.next
            self.count -= 1
            return True
        if index == self.count - 1:
            temp = self.tail
            self.head.previous = temp.previous
            temp.previous.next = self.head
            self.tail = temp.previous
            self.count -= 1
            return True
       
        alex_node = self.head
        for j in range(index):
            alex_node = alex_node.next
        alex_node.previous.next = alex_node.next
        alex_node.next.previous = alex_node.previous
        self.count -= 1
        return True
        

    def get_previous_next(self, index) -> list:
        if index < 0 or index >= self.count:
            return -1
        alex_node = self.head
        for ind in range(index):
            alex_node = alex_node.next
        return [alex_node.previous.data, alex_node.next.data]
        

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
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
