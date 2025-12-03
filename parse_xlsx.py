import openpyxl

def custom_sequence(start_num):
    num = start_num
    while True:
        yield num
        num += 3


def find_itog_indexes(col):
    itog_indexes = []
    for cell in col[5:]:
        if cell.value == 'ИТОГ:':
            itog_indexes.append(cell.row - 1)
    return itog_indexes


def find_product_indexs(col):
    indexes = []
    for cell in col:
        if cell.value == 'продукт':
            indexes.append(cell.row - 1)
    return indexes


def cut_by_indexes(col, indexes):
    new_col = []
    for cut in indexes:
        new_col += col[cut[0]:cut[1]]
    return new_col


def parse_xlsx(table_name, sheet_name, amount_of_days=5, file_name=None):
    if file_name:
        file = open(file_name, 'w', encoding='utf-8')
    else:
        file = None
    # Создаем генератор для последовательности
    name_idx_gen = custom_sequence(1)
    norma_idx_gen = custom_sequence(2)
    wb = openpyxl.load_workbook(table_name)
    ws = wb[sheet_name]
    col_list = [col for col in ws.columns]
    name_indexes = [next(name_idx_gen) for _ in range(amount_of_days)]
    norma_indexes = [next(norma_idx_gen) for _ in range(amount_of_days)]
    itog_counter = 0 # сколько раз встретилось слово итог
    itog_indexes = find_itog_indexes(col_list[1])
    product_indexes = find_product_indexs(col_list[1])
    cut_indexes = [[product, itog] for product, itog in zip(product_indexes, itog_indexes)]
    for nameIdx, normIdx in zip(name_indexes, norma_indexes):
        colName, colNorm = col_list[nameIdx], col_list[normIdx]
        colName = cut_by_indexes(colName, cut_indexes)
        colNorm = cut_by_indexes(colNorm, cut_indexes)
        if file_name:
            for cell1, cell2 in zip(colName, colNorm):
                if cell1.value == 'продукт':
                    print(file=file)
                elif cell1.value and cell2.value:
                    print(cell1.value, cell2.value, file=file)
            print(file=file)
        else:
            for cell1, cell2 in zip(colName, colNorm):
                if cell1.value == 'продукт':
                    print()
                elif cell1.value and cell2.value:
                    print(cell1.value, cell2.value)
            print()
    if file_name:
        file.close()

# парсер тригериться на фразы продукт и итог. обрабатывает только два столбца. продукт и норма
# в столбце со словом "продукт" должно быть слово "ИТОГ:" написание должно быть такое.
# парсер вырезает два столбца между этими словами и генерит файл раскладки в формате
# Прием пищи(на каждой строке продукт и норма). пустая строка. Прием пищи и тд. пока не
# закончаться приемы пищи в одном дне. дальше две пусых строки. и новый день. Чето не работает проверь формат.
#
#
# Внимание на таблицу Архыз. Формат должен совпадать В одном столбце указаны приемы пищи в день.
# В переменной amount_of_days указывается количество дней в цикле раскладки. По умолчанию 5 дней.
# table_name - путь к таблице. sheet_name - имя листа. file_name - имя файла распарсеной таблицы.
#
#
#
#
#
#
#
#
#
#