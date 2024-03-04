class calc :
    def sum(self, a, b):
        return a+b

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


a=calc()
result = a.sum(3, 4 )
print(result)

result = a.sub(4,5)
print(result)