# class Register:
#     def __init__(self, email, password):
#         self.email_ = email
#         self.password_ = password

#     def Info(self):
#         print(self.email_)
#         print(self.password_)


# p1 = Register("xyz@go.com", "test123")
# p2 = Register("zoom@go.com", "test123")

# p1.Info()
# p2.Info()

# public, private, and protected
class Circle:
    def __init__(self, r):
        # self.r_ = r # public
        self.__r_ = r # private

c1 = Circle(10)
# print(c1.r_)
# print(c1.__r_) # AttributeError: 'Circle' object has no attribute '__r_'
# Name mangling
# Syntax: _ClassName__variableName
# print(c1._Circle__r_)