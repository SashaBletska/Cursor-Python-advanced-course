"""3. Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
Override a printable string representation of Profile class and return: list of the params mentioned above"""


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def info(self):
        return list(self.__dict__.values())


p = Profile("Tom", "Hanks", "134059384", "UA str,1", "tom@gmail.com",
            "05.10.1991", "30", "male")
print(p.info())
