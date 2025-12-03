import help
import parse_xlsx
import raskladka
import menu
import os

os.system('color')



class Params:
    def __init__(self, table_name, sheet_name, amount_of_days, raskladka_file_name, bzukk_table_name, log_file_name, cycle_amount, amount_of_people=14):
        self.table_name = table_name
        self.sheet_name = sheet_name
        self.amount_of_days = amount_of_days
        self.raskladka_file_name = raskladka_file_name
        self.bzukk_table_name = bzukk_table_name
        self.log_file_name = log_file_name
        self.cycle_amount = cycle_amount
        self.amount_of_people = amount_of_people

    def __str__(self):
        return f'table_name: {self.table_name}\nsheet_name: {self.sheet_name}\namount_of_days: {self.amount_of_days}\n' \
               f'raskladka_file_name: {self.raskladka_file_name}\nbzukk_table_name: {self.bzukk_table_name}\n' \
               f'log_file_name: {self.log_file_name}\ncycle_amount: {self.cycle_amount}\namount_of_people: {self.amount_of_people}'

# table_name = 'Архыз.xlsx'
table_name = 'Рыбоков.xlsx'
sheet_name = 'Раскладка'
raskladka_file_name = 'raskladka.txt'
bzukk_table_name = 'bzukk.csv'
log_file_name = 'log.txt'
amount_of_days = 2
cycle_amount = 1
pars = Params(table_name, sheet_name, amount_of_days, raskladka_file_name, bzukk_table_name, log_file_name, cycle_amount)

is_calc = False
print("\033[47m\033[30m")
os.system('cls')
while True:

    menu.print_menu()
    inp = input()

    if inp == 'q':
        break
    try:
        code = int(inp)
    except ValueError:
        print('Некорректные данные')
        continue

    if code == 1:
        raskladka.raskladka(raskladka_file_name, bzukk_table_name)
        is_calc = True
    elif code == 2:
        parse_xlsx.parse_xlsx(table_name, sheet_name, amount_of_days, raskladka_file_name)
        print('Загружено')
    elif code == 3:
        help.is_rask_calc(is_calc, bzukk_table_name)
        raskladka.print_products_bzukk(raskladka.products_bzukk)
    elif code == 4:
        if not is_calc:
            print('Раскладка не расчитана')
            continue
        print('Количество людей:', pars.amount_of_people)
        print('Количество циклов:', pars.cycle_amount)
        raskladka.print_zakupka(raskladka.productsAmount, pars.amount_of_people, pars.cycle_amount)
    elif code == 5:
        if not is_calc:
            print('Раскладка не расчитана')
            continue
        raskladka.print_zakupka(raskladka.productsAmount, pars.amount_of_people, pars.cycle_amount, log_file_name)
        print('Выведено')
    elif code == 6:
        help.is_rask_calc(is_calc, bzukk_table_name)
        help.add_new_product(bzukk_table_name)
        print('Добавлено')
    elif code == 7:
        help.is_rask_calc(is_calc, bzukk_table_name)
        help.remove_from_count(bzukk_table_name)
        print('Удалено')
    elif code == 8:
        help.is_rask_calc(is_calc, bzukk_table_name)
        help.add_to_count(bzukk_table_name)
        print('Добавлено')
    elif code == 9:
        help.delete_product(bzukk_table_name)
        print('Удалено')
    elif code == 10:
        menu.print_par(pars)
    elif code == 11:
        pars = help.change_pars(pars)
    elif code == 12:
        raskladka.raskladka(raskladka_file_name, bzukk_table_name, log_file_name)
        print('Рассчитано')
    elif code == 13:
        os.system('cls')
        print('До свидания')
        break

print("\033[0m")