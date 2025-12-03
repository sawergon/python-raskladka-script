import csv
import os
import menu

import raskladka


def add_new_product(file_path):
    with open(file_path, 'r+', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        writer = csv.writer(file)
        name = input('Название продукта: ')
        b = float(input('Б: '))
        z = float(input('Ж: '))
        u = float(input('У: '))
        kk = float(input('КК: '))
        # Создаем список строк файла
        rows = list(reader)
        if name in raskladka.products_bzukk:
            for row in rows[1:]:
                if row[1] == name:
                    row[2] = b
                    row[3] = z
                    row[4] = u
                    row[5] = kk
                    break

            # Перемещаем указатель файла в начало
            file.seek(0)

            # Записываем все строки обратно в файл
            for row in rows:
                writer.writerow(row)

            # Удаляем все остальные строки
            file.truncate()
        else:
            writer.writerow([len(rows) + 1, name, b, z, u, kk])


def delete_product(file_path):
    with open(file_path, 'r+', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        writer = csv.writer(file)
        name = input('Название продукта: ')
        if name not in raskladka.products_bzukk:
            print('Такого продукта нет')
            return
        del raskladka.products_bzukk[name]
        # Создаем список строк файла
        rows = list(reader)
        for row in rows[1:]:
            if row[1] == name:
                rows.remove(row)
                break
        # Перемещаем указатель файла в начало
        file.seek(0)

        # Записываем все строки обратно в файл
        for row in rows:
            writer.writerow(row)

        # Удаляем все остальные строки
        file.truncate()


def change_pars(pars):
    menu.print_change_par(pars)
    print('Для выхода q')
    str = input()
    try:
        name, value = str.split('=')
    except ValueError:
        if str != 'q':
            print('Некорректные данные')
        return pars
    name, value = name.strip(), value.strip()
    if name == 'table_name':
        pars.table_name = value
    elif name == 'sheet_name':
        pars.sheet_name = value
    elif name == 'amount_of_days':
        pars.amount_of_days = int(value)
    elif name == 'raskladka_file_name':
        pars.raskladka_file_name = value
    elif name == 'bzukk_table_name':
        pars.bzukk_table_name = value
    elif name == 'log_file_name':
        pars.log_file_name = value
    elif name == 'cycle_amount':
        pars.cycle_amount = int(value)
    elif name == 'amount_of_people':
        pars.amount_of_people = int(value)
    else:
        print('Нет такого параметра')
        return pars
    print('Параметр изменен')
    return pars


def is_rask_calc(is_calc, bzukk_table_name):
    if not is_calc:
        for name, bzukk in raskladka.get_name_bzukk_from_file(bzukk_table_name):
            raskladka.products_bzukk[name] = bzukk


def remove_from_count(file_path):
    with open(file_path, 'r+', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        writer = csv.writer(file)
        name = input('Название продукта: ')
        if name not in raskladka.products_bzukk:
            print('Такого продукта нет')
            return
        # Создаем список строк файла
        rows = list(reader)
        for row in rows[1:]:
            if row[1] == name:
                row[6] = 0
                break
        # Перемещаем указатель файла в начало
        file.seek(0)

        # Записываем все строки обратно в файл
        for row in rows:
            writer.writerow(row)

        # Удаляем все остальные строки
        file.truncate()


def add_to_count(file_path):
    with open(file_path, 'r+', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        writer = csv.writer(file)
        name = input('Название продукта: ')
        if name not in raskladka.products_bzukk:
            print('Такого продукта нет')
            return
        # Создаем список строк файла
        rows = list(reader)
        for row in rows[1:]:
            if row[1] == name:
                row[6] = 1
                break
        # Перемещаем указатель файла в начало
        file.seek(0)

        # Записываем все строки обратно в файл
        for row in rows:
            writer.writerow(row)

        # Удаляем все остальные строки
        file.truncate()