from faker import Faker

fake = Faker("ru_Ru")


class UserData:
    def __init__(self, login, password, first_name, last_name, zip_code):
        self.login = login
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code

    @staticmethod
    def random():
        return UserData(
            login=fake.email(),
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            zip_code=fake.postcode(),
        )
