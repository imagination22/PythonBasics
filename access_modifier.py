class Parent:
    __private_name = None
    _protected_class_name = None
    __private_class_name = None

    def __init__(self , name , age , balance):
        self.name = name
        self._age = age
        self.__balance =balance

    def public_member(self):
        print("calling public variable from public member : Parent :", self.name)
        print("calling protected member from public member : Parent :", self._age)
        print("calling private variable from public member : Parent : , ", self.__balance)

    def _protected_member(self):
        print("calling public variable  from _protected_member : Parent :", self.name)
        print("calling protected member from _protected_member : Parent :", self._age)
        print("calling private variable from _protected member : Parent : , ", self.__balance)

    def __private_member(self):
        print("calling public  variable from private member : Parent : ", self.name)
        print("calling protected member from __private_member : Parent :", self._age)
        print("calling private variable from __private member : Parent : , ", self.__balance)

    def __private_member_for_child(self):
        print("calling public  variable from private member : for child : ", self.name)
        print("calling protected member from __private_member : for child :", self._age)
        print("calling private variable from __private member : for child : , ", self.__balance)

    def accessmembers(self):
        self.public_member()
        self._protected_member()
        self.__private_member()
# Derived class


class Child(Parent):
    def __init__(self, name, age, balance):
        Parent.__init__(self, name , age, balance)

    def access_parent_members(self):
        self.public_member()
        self._protected_member()
        #self.__private_member_for_child()  # Failed since cannot access private function form child
        #self.__private_member()  #error expected since private member cannot be accessed


shubham = Parent('shubham',25,100.00)
yash =Child('yash',25,110.00)
shubham.accessmembers()
yash.access_parent_members()