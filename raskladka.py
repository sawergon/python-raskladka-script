# -*- codecs: utf-8 -*-
import csv

WIDTH_TABLE = 10
def get_name_and_norma(string):
    split_string = '\t'.join(string.split(' ')).split('\t')
    name = split_string[0]
    norma = 0
    for word in split_string[1:]:
        try:
            fVal = float(word)
            norma = fVal
        except ValueError:
            name += ' ' + word
    return name, norma

# print(get_name_and_norma(a.strip()))
def get_name_bzukk_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[1]
            try:
                bzukk = [float(val) for val in row[2:]]
            except ValueError:
                continue
            yield name, bzukk
def get_name_bzukk(string):
    split_string = string.split()
    name = split_string[0]
    bzukk = []
    for word in split_string[1:]:
        try:
            fVal = float(word)
            bzukk.append(fVal)
        except ValueError:
            name += ' ' + word
    return name, bzukk

def count_bzukk_by_day(products_list, day_list):
    days_bzu_kk = []
    day_num = 1
    for day in day_list:
        b = 0
        z = 0
        u = 0
        kk = 0
        for product in products_list:
            if product in day and products_list[product][-1]:
                b += products_list[product][0] * day[product] / 100
                z += products_list[product][1] * day[product] / 100
                u += products_list[product][2] * day[product] / 100
                kk += products_list[product][3] * day[product] / 100
        days_bzu_kk.append([day_num, b, z, u, kk])
        day_num += 1
    return days_bzu_kk


def print_bzukk(day, file=None):
    fString = '{:6.2f}|{:6.2f}|{:6.2f}|{:6.2f}'
    if file:
        print('------------------------------------', file=file)
        print('   Б  |   Ж  |   У  |  КК  ', file=file)
        print(fString.format(day[1], day[2], day[3], day[4]), file=file)
    else:
        print('------------------------------------')
        print('   Б  |   Ж  |   У  |  КК  ')
        print(fString.format(day[1], day[2], day[3], day[4]))

def out_red(text):
    print("\033[31m{}\033[30m".format(text))

def out_green(text):
    print("\033[32m{}\033[30m".format(text))

def out_blue(text):
    print("\033[34m{}\033[30m".format(text))

def find_max_len_name(day):
    max_len_name = -1
    for product in day:
        if len(product) > max_len_name:
            max_len_name = len(product)
    return max_len_name
def print_day(day, product_bzukk, day_num, file=None):
    max_name = find_max_len_name(day) + len('продукт')
    fStringMain = '\n' + '-' * 80 + '\n день {}'+ ('\n{:' + str(max_name) + 's}|   норма  |    Б     |     Ж    |     У    |    КК    |  KK/норма').format('продукт')
    split = '-' * 80
    fStringProduct = '{:'+ str(max_name) +'s}|{:10.1f}|{:10.2f}|{:10.2f}|{:10.2f}|{:10.2f}|{:10.2f}'
    if file:
        print(fStringMain.format(day_num), file=file)
        print(split, file=file)
        for product in day:
            if product in product_bzukk:
                bzukk = product_bzukk[product]
            else:
                bzukk = [0, 0, 0, 0]
            print(fStringProduct.format(product, day[product], bzukk[0], bzukk[1], bzukk[2], bzukk[3], bzukk[3] / day[product] / 100), file=file)
    else:
        print(fStringMain.format(day_num))
        print(split)
        for product in day:

            if product in product_bzukk:
                bzukk = product_bzukk[product]
                name = product
                norma = day[product]
                b = bzukk[0]
                z = bzukk[1]
                u = bzukk[2]
                kk = bzukk[3]
                kk_on_norma = bzukk[3] * day[product] / 100
                if product_bzukk[product][-1]:
                    out_green(fStringProduct.format(name, norma, b, z, u, kk, kk_on_norma))
                else:
                    out_red(fStringProduct.format(name, norma, b, z, u, kk, kk_on_norma))
            else:
                bzukk = [0, 0, 0, 0]
                out_blue(fStringProduct.format(product, day[product], bzukk[0], bzukk[1], bzukk[2], bzukk[3], bzukk[3] * day[product] / 100))


def total_norma(day):
    total = 0
    for product in day:
        total += day[product]
    return total


def print_total(day, bzukk, file=None):
    max_name = find_max_len_name(day)
    fString = 'Итого: ' + ' ' * max_name + '|{:10.2f}|{:10.2f}|{:10.2f}|{:10.2f}|{:10.2f}|'
    total_norm = total_norma(day)
    if file:
        print(fString.format(total_norm, bzukk[1], bzukk[2], bzukk[3], bzukk[4]), file=file)
    else:
        print(fString.format(total_norm, bzukk[1], bzukk[2], bzukk[3], bzukk[4]))


def print_products_bzukk(bzukk, file_name=None):
    max_name = find_max_len_name(bzukk)
    fMain = ('\n{:' + str(max_name) + 's}|    Б     |     Ж    |     У    |    КК    ').format('продукт')
    split = '-' * 80

    fString = '{:' + str(max_name) + 's}|{:10.2f}|{:10.2f}|{:10.2f}|{:10.2f}'

    if file_name:
        w_file = open(file_name, 'w', encoding="utf-8")
        print(fMain, file=w_file)
        print(split, file=w_file)
        for product in list(sorted(bzukk)):
            print(fString.format(product, bzukk[product][0], bzukk[product][1], bzukk[product][2], bzukk[product][3]), file=w_file)
    else:
        print(fMain)
        print(split)
        for product in list(sorted(bzukk)):
            print(fString.format(product, bzukk[product][0], bzukk[product][1], bzukk[product][2], bzukk[product][3]))

productsAmount = []
products_bzukk = {}
days_bzukk = []

def print_zakupka(productsAmount, people_amount, cycles_amount, file_name=None):
    global products_bzukk
    max_name = find_max_len_name(products_bzukk)
    fMain = ('\n{:' + str(max_name) + 's}| вес в граммах').format('продукт')
    split = '-' * 80
    fString = '{:' + str(max_name) + 's}|{:10.2f}'
    total_summ = {}
    if file_name:
        w_file = open(file_name, 'w', encoding="utf-8")
        print('Количество людей:', people_amount, file=w_file)
        print('Количество циклов:', cycles_amount, file=w_file)
        print(fMain, file=w_file)
        print(split, file=w_file)
        for day in productsAmount:
            for product in day:
                total_summ[product] = total_summ.get(product, 0) + day[product]
        for product in list(sorted(total_summ)):
            print(fString.format(product, total_summ[product] * people_amount * cycles_amount), file=w_file)

    else:
        print(fMain)
        print(split)
        for day in productsAmount:
            for product in day:
                total_summ[product] = total_summ.get(product, 0) + day[product]
        for product in list(sorted(total_summ)):
            print(fString.format(product, total_summ[product] * people_amount * cycles_amount))


def raskladka(raskladka_table_name, bzukk_table_name, log_file_name=None, dublicate=False):
    """

    :param raskladka_table_name: имя файла с раскладкой
    :param bzukk_table_name: имя файла с бжу
    :param log_file_name: имя файла с логами
    :param dublicate: нужно ли дублировать в консоль
    :return:
    """
    # по дням
    global productsAmount, products_bzukk, days_bzukk
    productsAmount = []
    # один день раскладки
    day = {}
    # считываем раскладку по дням из файла
    # названия продуктов будут уникальные
    raskladka_file = open(raskladka_table_name, 'r', encoding="utf-8")
    empty_string_count = 0
    for line in raskladka_file:
        line = line.strip()
        if line:
            productName, productNorma = get_name_and_norma(line)
            day[productName] = day.get(productName, 0) + productNorma
            empty_string_count = 0
        else:
            empty_string_count += 1
        if empty_string_count == 2:
            productsAmount.append(day.copy())
            day = {}
    productsAmount.append(day.copy())
    raskladka_file.close()

    # все бжу
    products_bzukk = {}
    for name, bzukk in get_name_bzukk_from_file(bzukk_table_name):
        products_bzukk[name] = bzukk

    # расчет бжу по дням с учетом использованных продуктов
    days_bzukk = count_bzukk_by_day(products_bzukk, productsAmount)
    split = '-' * 80
    # вывод
    if log_file_name:
        w_file = open(log_file_name, 'w', encoding="utf-8")
        for i in range(len(days_bzukk)):
            print_day(productsAmount[i], products_bzukk, i + 1, w_file)
            print(split, file=w_file)
            print_total(productsAmount[i], days_bzukk[i], w_file)

        w_file.close()

    if dublicate or not log_file_name:
        for i in range(len(days_bzukk)):
            print_day(productsAmount[i], products_bzukk, i + 1)
            print(split)
            print_total(productsAmount[i], days_bzukk[i])


# зеленый цвет - используется в расчетах
# красный цвет - не используется в расчетах
# синий цвет - не известный продукт
