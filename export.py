def data_add():
    f = open('data.txt', 'a', encoding="utf-8")
    user_list = input('Введите данные через пробел: ')
    f.writelines(f'{user_list}\n')
    f.close()