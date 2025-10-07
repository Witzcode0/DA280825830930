class Register:
    def __init__(self, email, password):
        self.email_ = email
        self.password_ = password

    def Info(self):
        print(self.email_)
        print(self.password_)


p1 = Register("xyz@go.com", "test123")
p2 = Register("zoom@go.com", "test123")

p1.Info()
p2.Info()