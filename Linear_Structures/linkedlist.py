class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 

	def __repr__(self):
		return str(self.data)

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

class LinkedList:
	def __init__(self, iterator=[]):
		self.head = None
		self.length = 0
		for item in iterator: self.add_head(item)

	""" Overriding built in function that gets called when we use len(LinkedList) 
	function to see the length of the linked list """
	def __len__(self):
		return self.length

	""" Overriding built in function that gets called when we want to search a 
	container for a specific object or data element """
	def __contains__(self, data):
		return self.search(data)

	""" Representation of our linked list class """
	def __repr__(self):
		current, items = self.head, []
		while current:
			items.append(str(current))
			current = current.get_next()
		return '->'.join(items)

	""" Returns the head (first data element) of the linked list """
	def get_head(self):
		return self.head

	""" Returns the last data element of the linked list """
	def get_tail(self):
		current = self.head
		while current.get_next():
			current = current.get_next()
		return current

	""" Add a data element to the front of the linked list """
	def add_head(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		self.length += 1

	""" Search for an element in the linked list """
	def search(self, data):
		current = self.head
		found = False
		while current and not found:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()

		return found, current.get_data()

	""" Remove the last data element from the linked list """
	def pop(self):
		prev = None
		current = self.head
		while current.get_next():
			prev = current
			current = current.get_next()
		prev.set_next(current.get_next())
		current.set_next(None)
		self.length -= 1

	""" Removes a data element from the linked list """
	def remove(self, data):
		if len(self) == 0:
			return "No elements in the list"
		prev = None
		current = self.head
		found = False
		while current and not found:
			if current.get_data() == data:
				found = True
			else:
				prev = current 
				current = current.next
		if found:
			self.length -=1
			if prev == None:
				self.head = self.head.get_next()
			else:
				prev.next = current.get_next()

	""" Reverses the linked list iteratively """
	def reverse(self):
		prev = None
		current = self.head
		while current:
			current.next, current, prev = prev, current.next, current
		self.head = prev
		return self.head




# Some tests for our linked list
if __name__ == "__main__":
	L = LinkedList(range(0, 100, 10))
	print(L)
	print(len(L))
	L.pop()
	print(L)
	L.add_head(23)
	print(23 in L)
	print(L.search(23))
	print(L)
	L.remove(23)
	print(L)
	L.reverse()
	print(L)

	