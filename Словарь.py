from string import punctuation, whitespace, digits

SET_SYMBOLS_NOT_LETTERS = set(punctuation + whitespace + digits)


class Person:
    def __init__(self, name, surname, phone, city, email):
        self._name = name
        self._surname = surname
        self._phone = phone
        self._city = city
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(set(name).intersection(SET_SYMBOLS_NOT_LETTERS)) != 0:
            raise ValueError()
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if len(set(surname).intersection(SET_SYMBOLS_NOT_LETTERS)) != 0:
            raise ValueError()
        self._surname = surname

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if len(set(phone).intersection(set(digits + '+'))) == 0:
            raise ValueError()
        self._phone = phone

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if len(set(city).intersection(SET_SYMBOLS_NOT_LETTERS)) != 0:
            raise ValueError()
        self._city = city

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if len(set(email).intersection(set('@.'))) == 0:
            raise ValueError()
        self._email = email

    def __eq__(self, other):
        if type(other) != Person:
            raise ValueError
        return self._name == other.name and \
            self._surname == other.surname and \
            self._phone == other.phone and \
            self._city == other.city and \
            self._email == other.email

    def __str__(self):
        return f'Person(' \
               f'name={self._name}, ' \
               f'surname={self._surname}, ' \
               f'phone={self._phone}, ' \
               f'city={self._city}, ' \
               f'email={self._email})'


class Directory:
    def __init__(self):
        self._dict_persons = dict()

    def add_person(self, person):
        if type(person) != Person:
            raise ValueError()

        if person.email in self._dict_persons:
            raise ValueError()

        self._dict_persons[person.email] = person

    def get_person_by_email(self, email):
        if type(email) != str:
            raise ValueError()

        try:
            return self._dict_persons[email]
        except KeyError:
            raise KeyError(f'There is not such person with email `{email}`!')

    def del_person(self, person):
        if type(person) != Person:
            raise ValueError()

        try:
            self._dict_persons.pop(person.email)
        except KeyError:
            raise KeyError()

    def del_person_by_email(self, email):
        if type(email) != str:
            raise ValueError()

        try:
            self._dict_persons.pop(email)
        except KeyError:
            raise KeyError()

    def __str__(self):
        return '\n'.join(str(person) for person in self._dict_persons.values())



def main():
    directory = Directory()
    directory.add_person(Person('a', 'A', '+71', 'aaa', 'kaka1@yandex.ru'))
    directory.add_person(Person('b', 'B', '+72', 'bbb', 'kaka2@yandex.ru'))
    directory.add_person(Person('c', 'C', '+73', 'ccc', 'kaka3@yandex.ru'))
    directory.add_person(Person('d', 'D', '+74', 'ddd', 'kaka4@yandex.ru'))
    print(directory)

    print('=' * 40)
    directory.get_person_by_email('kaka2@yandex.ru').name = 'akaki'
    print(directory)


if __name__ == '__main__':
    main()
