def print_data(name, surname, birthday, city, email, phone):
    return f' Surname - {surname}, name - {name}, birthday - {birthday}, city - {city},' \
           f'email - {email}, phone - {phone}'


print(print_data(name='Фредрик', surname='Бакман', birthday='1996', city='Стокгольм', email='Bakman@mail.ru',
                 phone='8-800-800-80-80'))