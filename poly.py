# A simple Python function to demonstrate
# Polymorphism
'''
def add(x, y, z = 0):
	return x + y+ z
'''
# Driver code

class Numbers:

    def __init__(self,operation  ,  a = 0 , b =0, c =0):
        self.operation = operation
        self.a = a
        self.b = b
        self.c = c


    def cal(self):
        if self.operation == '+':
            result = self.a + self.b + self.c
        elif self.operation == '-':
            result = self.a - self.b
        else:
            result = self.a * self.b
        return result





a1 = Numbers('*',5,6)
result = a1.cal()
print(result)




