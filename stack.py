class Stack:
	
	def __init__(self):
		self.stack = []
    #insere na pilha
	def push(self, e):
		self.stack.append(e)

    #remove ultimo elemento
	def pop(self):
		if not self.empty():
			self.stack.pop(len(self.stack) - 1)

    #retorna ultimo elemento
	def top(self):
		if not self.empty():
			return self.stack[-1]
		return None

    #verifica se a pilha esta vazia
	def empty(self):
		if (len(self.stack) == 0):
			return True
		return False
    #
	def length(self):
		return len(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
#print(s.top())
s.pop()
#print(s.top())
s.pop()
print(s.length())