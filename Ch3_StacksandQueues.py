class StackNode(object):
	def __init__(self, data=None, next_node=None):
		self.data=data
		self.next_node=next_node

	def get_data(self):
		return self.data

	def set_data(self, val):
		self.data=val

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node=new_next

	def print_node(self):
		print self.data

class Stack(object):
	def __init__(self, head=None):
		self.head = head

	def push(self, data):
		new_node = StackNode(data)
		new_node.set_next(self.head) 
		self.head = new_node

	def pop(self):
		val = self.head.get_data()
		self.head=self.head.get_next()
		return val

	def peek(self):
		return self.head.get_data()

	def print_stack(self):
		current = self.head
		while current:
			print current.get_data()
			current = current.get_next()

	def is_empty(self):
		if self.head is None:
			return True
		else:
			return False

	def size(self):
		i=0
		current = self.head
		while current: 
			i+=1
			current=current.get_next()
		return i



# stack1 = Stack(StackNode(10))
# stack1.push(20)
# print stack1.peek()
# stack1.print_stack()

# print stack1.is_empty()
# stack1.pop()
# stack1.pop()
# stack1.print_stack()

class Queue(object):
	def __init__(self, head=None, tail=None):
		self.head = head
		if tail is None: 
			self.tail = head
		else: 
			self.tail = tail

	def add(self, data):
		new_node=StackNode(data)
		self.tail.set_next(new_node)
		self.tail=new_node

	def remove(self):
		val = self.head.get_data()
		self.head=self.head.get_next()
		return val

	def peek(self):
		return self.head.get_data()

	def print_queue(self):
		current = self.head
		while current:
			print current.get_data()
			current = current.get_next()

	def is_empty(self):
		if self.head is None:
			return True
		else:
			return False

	def size(self):
		i=0
		current = self.head
		while current: 
			i+=1
			current=current.get_next()
		return i

queue1 = Queue(StackNode(5))
queue1.add(4)
queue1.add(6)
queue1.add(8)

queue1.print_queue()

queue1.remove()
queue1.remove()

queue1.print_queue()