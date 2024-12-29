class Netflix:
    name= ''
    email= ''
    password= None
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def print_details(self):
        print(self.name)
        print(self.email)
        print(self.password)


user1 = Netflix("karan", "karan@123", "1234")   
user1.print_details()