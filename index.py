class Stack: 
	
	def __init__(self):
		self.stack = []
		
	def push(self, obj):
		self.stack.append(obj)
		
	def pop(self):
		if self.isEmpty():
			return "The stack is empty"
		return self.stack.pop()

	def isEmpty(self):
		return len(self.stack) == 0
	
	def peek(self):
		if self.isEmpty():
			return "The stack is empty"
		return self.stack[-1]
	
	def size(self):
		return len(self.stack)

#create a stack object

p1 = Stack()

#add something into the stack

p1.push(1)
p1.push(2)
p1.push(3)


#print the stack 

print(p1.stack)

#pop the stack 

print(p1.pop())

print(p1.stack)

#peak the stack

print(p1.peek())

print(p1.size())


class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None

class NodeStack:
	def __init__(self):
		self.head = None 
		self.size = 0 

	def push(self, value):
		if self.head:
			current = self.head
			while current: 
				if current.next == None: 
					current.next = Node(value)
					self.size = self.size + 1
					return
				current = current.next
			
		else:
			self.head = Node(value)
			self.size = 1

	def pop(self):
		if self.size == 0:
			return "Empty Stack"

		if self.size == 1: 
			data = self.head.data
			self.head = None
			self.size = 0

			return data
		
		else:
			current = self.head

			while current.next.next: 
				current = current.next

			popped_value = current.next
			current.next = None
			self.size -= 1
			return popped_value
			

			

	
	def traverseAndPrint(self):
		current = self.head 
		while current:
			print(current.data, end = ", ")
			current = current.next
		print("none")

	def printFirstNode(self):
		print(self.head, "lol")


myStack = NodeStack()

myStack.push("A")
myStack.push("B")
myStack.push("C")

myStack.traverseAndPrint()
print(myStack.size)

#myStack.printFirstNode()

myStack.pop()
myStack.traverseAndPrint()