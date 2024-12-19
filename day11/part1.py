class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            new_node.prev = current_node
            current_node.next = new_node

    def blink(self):
        current_node = self.head
        while current_node is not None:
            if current_node.value == '0':
                current_node.value = '1'
            elif len(current_node.value) % 2 != 0: # odd number of digits
                current_node.value = str(int(current_node.value) * 2024)
            else:
                self.split_node(current_node)
    
            current_node = current_node.next

    def split_node(self, current_node):
        new_val = current_node.value[0:len(current_node.value)// 2]
        current_node.value = str(int(current_node.value[len(current_node.value) // 2:])) # Cast to int to remove leading 0's
        
        new_node = Node(new_val)
        new_node.next = current_node # insert new node on the left
        new_node.prev = current_node.prev
        
        if current_node.prev is not None:
            current_node.prev.next = new_node
        else:
            # Current_node is head, update head
            self.head = new_node

        current_node.prev = new_node
    
    def __str__(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.value)
            result.append(' ')
            current_node = current_node.next
        return ''.join(result)

    def print_reverse(self):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.prev

    def __len__(self):
        result = 0
        current_node = self.head
        while current_node is not None:
            result += 1
            current_node = current_node.next
        return result

if __name__ == "__main__":
    with open("day11.txt") as f:
        stones = f.read().split()
    
    stones_list = LinkedList()
    for stone in stones:
        stones_list.insert_at_end(Node(stone))

    for i in range(25):
        stones_list.blink()
    print(f"Total stones after 25 blinks: {len(stones_list)}")




