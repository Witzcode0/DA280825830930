# method overloading - static binding - compile time polymorphism

# method overriding - dynamic binding - runtime polymorphism

# person - bus

# class Math:
#     def add(self, a, b):
#         print(a + b)

#     def add(self, a, b, c):
#         print(a + b + c)


# obj = Math()
# obj.add(10, 20)


class A:
    def info(self):
        print("I am from parent class")
class B(A):
    def info(self):
        # print("I am from Child class")
        super().info()

obj = B()
obj.info()