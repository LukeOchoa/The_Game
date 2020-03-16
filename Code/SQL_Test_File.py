import sqlite3
from my_import_file import *

s = 'character_name'
s1 = 's'
kharacters = {}
kharacters["Blake"] = Character
kharacters['Blake'].all_information = copy.deepcopy(tables)


connection = sqlite3.connect('/home/luke/PycharmProjects/The_Game/db.Character_Data')

connection.execute("PRAGMA foreign_keys = ON")

cursor1 = connection.cursor()

line9 = "SELECT * FROM Language_Items WHERE character_name='Blake' AND ID=3"

line1_insert = ""


def fetch_commit(sqline):
    results = cursor1.execute(sqline)
    r = results.fetchall()
    connection.commit()
    return r


def get_table_names():
    sqline_1 = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name ASC"
    results_gtn = fetch_commit(sqline_1)
    all_sql_table_names = []
    for i in range(len(results_gtn)):
        all_sql_table_names.append(results_gtn[i][0])
    return all_sql_table_names


def get_table_keys(tables_gtk):
    r2 = []
    for i in range(len(tables_gtk)):
        if tables_gtk[i] == 'Characters':
            sqline_2 = "SELECT ID FROM {} WHERE {}='Blake'".format(tables_gtk[i], s + s1)
        else:
            sqline_2 = "SELECT ID FROM {} WHERE {}='Blake'".format(tables_gtk[i], s)
        r2.append(fetch_commit(sqline_2))
    return r2


def sql_line_maker(column, table, qualifier, qualifier2, qualifier3,
                   qualifier4):  # qualifer='ID'(unless otherwise specificed), qualifer2=(value corresponding to q), qualifier3 =character_name(unless otherwise specified), qualifier4 = corresponding value
    sql_line_1 = "SELECT {} FROM {} WHERE {}='{}' AND {}='{}'".format(column, table, qualifier, qualifier2, qualifier3,
                                                                      qualifier4)
    return sql_line_1


def load_keys(character_lk, keys):
    rkvd_i = rkvd(character_lk['Blake'].all_information)
    for i in range(len(keys)):
        for j in range(len(keys[i])):
            character_lk['Blake'].all_information[rkvd_i['key'][i]][keys[i][j][0]] = \
                copy.deepcopy(character_lk['Blake'].all_information[rkvd_i['key'][i]]['key'])


# key_storage.append(dreturn_keys_values(karacter['Blake'].all_information[args_dict['table']][args_dict['qualifier2']][args_dict['column']]))
def get_sql_arguments(karacter):
    args_dict = {
        "column": "",
        "table": "",
        "qualifier": "ID",
        "qualifier2": ""
    }
    sql_args = []
    key_storage = [0, 1, 2]
    key_storage[0] = dreturn_keys_values(karacter['Blake'].all_information)

    for i in range(len(key_storage[0]['key'])):  # all tables
        args_dict['table'] = key_storage[0]['key'][i]
        key_storage[1] = dreturn_keys_values(karacter['Blake'].all_information[args_dict['table']])

        for j in range(len(key_storage[1]['key'])):  # version of a table
            args_dict['qualifier2'] = key_storage[1]['key'][j]
            key_storage[2] = dreturn_keys_values(
                karacter['Blake'].all_information[args_dict['table']][args_dict['qualifier2']])

            for ij in range(len(key_storage[2]['key'])):  # values in table
                args_dict['column'] = key_storage[2]['key'][ij]
                sql_args.append(copy.deepcopy(args_dict))
    return sql_args


def load_character(base_item, sub_item, arg3):
    base_item[arg3['table']][arg3['qualifier2']][arg3['column']] = sub_item


all_sql_tables = get_table_names()
table_keys = get_table_keys(all_sql_tables)
load_keys(kharacters, table_keys)
sql_arguments = get_sql_arguments(kharacters)


for i in range(len(sql_arguments)):
    arg = sql_arguments[i]
    arg2 = copy.deepcopy(sql_arguments[i])
    arg['table'] = replace(arg['table'], ' ', '_')
    arg['column'] = replace(arg['column'], ' ', '_')
    if arg['qualifier2'] != 'key':
        if arg['table'] != 'characters':
            sq_line_1 = sql_line_maker(arg['column'], arg['table'], arg['qualifier'], arg['qualifier2'],
                                       'character_name', 'Blake')
            r102 = fetch_commit(sq_line_1)
            load_character(kharacters['Blake'].all_information, r102, arg2)


j_obj = rkvd(kharacters['Blake'].all_information)
for cc in range(len(j_obj['key'])):
    print(j_obj['key'][cc])
    print_lines_dict(kharacters['Blake'].all_information[j_obj['key'][cc]])
    define_spaces(2)
