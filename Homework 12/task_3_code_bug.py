from datetime import datetime
import faker


class Student():
    birth_date = faker.Faker().date_of_birth(minimum_age=16, maximum_age=60)
    is_birthday = 0

    def age(self):
        if self.birth_date:
            return datetime.now().year - self.birth_date.year

    def exact_age(self):
        if self.birth_date:
            bd = self.birth_date
            if not datetime(datetime.now().year, bd.month, bd.day) < datetime.now():
                self.is_birthday = 1
            return datetime.now().year - self.birth_date.year - self.is_birthday


student = Student()

print(student.birth_date)
print(f"{student.age() = }")
print(f"{student.exact_age() = }")
