class Intern:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.address = ""
        self.mobile_number = ""
        self.email = ""

    def getdata(self):
        self.name = input("Введіть ім'я стажера: ")
        self.surname = input("Введіть прізвище стажера: ")
        self.address = input("Введіть адресу стажера: ")
        self.mobile_number = input("Введіть номер мобільного стажера: ")
        self.email = input("Введіть електронну пошту стажера: ")

    def putdata(self):
        print("Ім'я:", self.name)
        print("Прізвище:", self.surname)
        print("Адреса:", self.address)
        print("Номер мобільного:", self.mobile_number)
        print("Електронна пошта:", self.email)

    def __del__(self):
        print("Стажер видалений")


class NewIntern(Intern):
    def show_info(self):
        self.putdata()



intern1 = Intern()
intern1.getdata()
intern1.putdata()


intern2 = NewIntern()
intern2.getdata()
intern2.show_info()


del intern1
del intern2
