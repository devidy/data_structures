class Stack:
    	
	def __init__(self):
		self.stack = []
		self.len_stack = 0
    
    #insere na stack
	def push(self, e):
		self.stack.append(e)
		self.len_stack += 1
    
    #remove da stack
	def pop(self):
		if not self.empty():
			self.stack.pop(self.len_stack - 1)
			self.len_stack -= 1
    
    #obtem ultimo elemento da stack
	def top(self):
		if not self.empty():
			return self.stack[-1]
		return None

    #verifica se a pilha esta vazia
	def empty(self):
		if self.len_stack == 0:
			return True
		return False

    #retorna o tamanho da stack
	def length(self):
		return self.len_stack

s = Stack()
s.push(1)
print(s.len_stack)
s.push(2)
print(s.len_stack)
s.push(3)
print(s.len_stack)
s.pop()
print(s.len_stack)
s.pop()
print(s.len_stack)
print(s.length())