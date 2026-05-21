def findRedundantBrackets(s:str):
	expressions=['(', ')', '+', '-', '*', '/']
	stack=[]
	for char in s:
		if char in expressions and char!=')':
			stack.append(char)
		if char==')':
			no_of_expressions=0
			while True:
				top=stack.pop()
				if top=='(':
					break
				else:
					no_of_expressions+=1
			if no_of_expressions<1:
				return True
	return False

s=input()
print("Yes" if findRedundantBrackets(s) else "No")