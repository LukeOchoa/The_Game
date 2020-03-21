import sqlite3
from my_import_file import *


character_name_global = "Blake"


kharacters = {}
kharacters[character_name_global] = Character
kharacters[character_name_global].all_information = copy.deepcopy(tables)








def get_table_names():
    sqline_1 = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name ASC"
    results_gtn = fetch_commit(sqline_1)
    all_sql_table_names = []
    for i in range(len(results_gtn)):
        all_sql_table_names.append(results_gtn[i][0])
    return all_sql_table_names


def get_table_keys(tables_gtk, character_name_gtk):
    s = 'character_name'
    s1 = 's'
    r2 = []
    for i in range(len(tables_gtk)):
        if tables_gtk[i] == 'Characters':
            sqline_2 = "SELECT ID FROM {} WHERE {}='{}'".format(tables_gtk[i], s + s1, character_name_gtk)
        else:
            sqline_2 = "SELECT ID FROM {} WHERE {}='{}'".format(tables_gtk[i], s, character_name_gtk)
        r2.append(fetch_commit(sqline_2))
    return r2


def sql_line_maker(column, table, qualifier, qualifier2, qualifier3,
                   qualifier4):  # qualifer='ID'(unless otherwise specificed), qualifer2=(value corresponding to q), qualifier3 =character_name(unless otherwise specified), qualifier4 = corresponding value
    sql_line_1 = "SELECT {} FROM {} WHERE {}='{}' AND {}='{}'".format(column, table, qualifier, qualifier2, qualifier3,
                                                                      qualifier4)
    return sql_line_1


def load_keys(character_lk, keys, character_name_lk):
    rkvd_i = rkvd(character_lk[character_name_lk].all_information)
    for i in range(len(keys)):
        for j in range(len(keys[i])):
            character_lk[character_name_lk].all_information[rkvd_i['key'][i]][keys[i][j][0]] = \
                copy.deepcopy(character_lk[character_name_lk].all_information[rkvd_i['key'][i]]['key'])


# key_storage.append(dreturn_keys_values(karacter['Blake'].all_information[args_dict['table']][args_dict['qualifier2']][args_dict['column']]))
def get_sql_arguments(karacter, character_name_gsa):
    args_dict = {
        "column": "",
        "table": "",
        "qualifier": "ID",
        "qualifier2": ""
    }
    sql_args = []
    key_storage = [0, 1, 2]
    key_storage[0] = dreturn_keys_values(karacter[character_name_gsa].all_information)

    for i in range(len(key_storage[0]['key'])):  # all tables
        args_dict['table'] = key_storage[0]['key'][i]
        key_storage[1] = dreturn_keys_values(karacter[character_name_gsa].all_information[args_dict['table']])

        for j in range(len(key_storage[1]['key'])):  # version of a table
            args_dict['qualifier2'] = key_storage[1]['key'][j]
            key_storage[2] = dreturn_keys_values(
                karacter[character_name_gsa].all_information[args_dict['table']][args_dict['qualifier2']])

            for ij in range(len(key_storage[2]['key'])):  # values in table
                args_dict['column'] = key_storage[2]['key'][ij]
                sql_args.append(copy.deepcopy(args_dict))
    return sql_args


def load_character(base_item, sub_item, arg3):
    base_item[arg3['table']][arg3['qualifier2']][arg3['column']] = sub_item


all_sql_tables = get_table_names()
table_keys = get_table_keys(all_sql_tables, character_name_global)
load_keys(kharacters, table_keys, character_name_global)
sql_arguments = get_sql_arguments(kharacters, character_name_global)


for i in range(len(sql_arguments)):
    arg = sql_arguments[i]
    arg2 = copy.deepcopy(sql_arguments[i])
    arg['table'] = replace(arg['table'], ' ', '_')
    arg['column'] = replace(arg['column'], ' ', '_')
    if arg['qualifier2'] != 'key':
        if arg['table'] != 'characters':
            sq_line_1 = sql_line_maker(arg['column'], arg['table'], arg['qualifier'], arg['qualifier2'],
                                       'character_name', character_name_global)
            r102 = fetch_commit(sq_line_1)
            load_character(kharacters[character_name_global].all_information, r102, arg2)


j_obj = rkvd(kharacters[character_name_global].all_information)
for cc in range(len(j_obj['key'])):
    print(j_obj['key'][cc])
    print_lines_dict(kharacters[character_name_global].all_information[j_obj['key'][cc]])
    define_spaces(2)