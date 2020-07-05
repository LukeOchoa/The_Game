import sqlite3
from my_import_file import *

character_name_global = "Blake"

# kharacter is a dictionary that will be initialized to be a class Character
# we create/add a item in the dictionary with the name/key from character_name_global(which is a global var import)
# the kharacters variable .all_information will receive a deepcopy of every table and data structure for
# # a character from the global import variable tables
kharacters = {}
kharacters[character_name_global] = Character
kharacters[character_name_global].all_information = copy.deepcopy(tables)
staging_kharacters = copy.deepcopy(kharacters)  # This is the area that will house all changes and the base name "kharacters" dictionary will be the old version of the items.
# when something is deleted or changed, at least one previous version of this information will persist by being saving in the "old information" aka kharacters and not staging_kharacters


# this is a very simple function that collects all table names from the database and returns it as an array
# gtn means get table name
def get_table_names():
    sqline_1 = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name ASC"
    results_gtn = fetch_commit(sqline_1)
    all_sql_table_names = []
    for i in range(len(results_gtn)):
        all_sql_table_names.append(results_gtn[i][0])
    return all_sql_table_names


# get_table_keys gets two(2) variables tables_gtk(all sql tables) and character name(character name global)
# [keyword gtk==func name]
# This function attains the ids from all tables in the database. i refer to these as "keys" because in the
# # program data structure all ids are represented as a "key" in the dictionaries
# in the forloop we format a string with the character name and the table names,,, pass that to and sql function
# ## which returns an id and we increment of each table and pass the sql function again and again... etc.
# # Every pass on the loop we check if there is a id belonging to a certain character name
# # (aka kharacter["insert key name here"]) then we append it to an array. when the loop finishes, we return that array
def get_table_keys(tables_gtk, character_name_gtk):
    s = 'character_name'
    r2 = []
    for i in range(len(tables_gtk)):
        sqline_2 = "SELECT ID FROM {} WHERE {}='{}'".format(tables_gtk[i], s, character_name_gtk)
        r2.append(fetch_commit(sqline_2))
    return r2


def sql_line_maker(column, table, qualifier, qualifier2, qualifier3,
                   qualifier4):  # qualifer='ID'(unless otherwise specificed), qualifer2=(value corresponding to q), qualifier3 =character_name(unless otherwise specified), qualifier4 = corresponding value
    sql_line_1 = "SELECT {} FROM {} WHERE {}='{}' AND {}='{}'".format(column, table, qualifier, qualifier2, qualifier3,
                                                                      qualifier4)
    return sql_line_1


# load keys assigns all "key"s(or technically sql IDs) from the the previous get_table_keys() to the character of our choosing
# First) we get all dictionary keys/values with rkvd() from -kharacter_lk[character_name_lk].all_information-
# Second) loop through the length of keys(The length is the same length as the entire amount of tables in our db) then we
# # we start a second loop that goes through every "key"/ID that was a match to our character. This a nested array within
# # the keys variable
# Third) we choose a table from rkvd_tables every loop pass and index each table at "key" keys[i][j][0].
# # For each key we find in there we copy an entirely new blank data structure of the table we found at that ID location to a new dictionary entry.
# # Example: If we found a "key"/ID for table skills, the function would CREATE a new dictionary entry in the class Character
# # kharacter[character_name_global].all_information[The_current_table_in_loop][the_current_key_in_loop]. This entry and
# # "key"/ID are unique to our character_name(example: Blake)
# Then we simply repeat this for all keys for this character
# # # VARIABLE == # # #
# |kharacter_lk == kharacters|, |keys == table_keys FROM get_table_keys == all_sql_tables FROM get_table_names()|, |character_name_lk == character_name_global|

def load_keys(kharacter_lk, keys, character_name_lk):
    rkvd_tables = rkvd(kharacter_lk[character_name_lk].all_information)
    for i in range(len(keys)):
        for j in range(len(keys[i])):
            # print(str(keys[i][j][0]))
            # kharacter_lk[character_name_lk].all_information[rkvd_tables['key'][i]][str(keys[i][j][0])] = \
            #     copy.deepcopy(kharacter_lk[character_name_lk].all_information[rkvd_tables['key'][i]]['key'])  # key is variable is in a tuple?
            kharacter_lk[character_name_lk].all_information[rkvd_tables['key'][i]][keys[i][j][0]] = \
                copy.deepcopy(kharacter_lk[character_name_lk].all_information[rkvd_tables['key'][i]]['key'])
            # kharacter_lk[character_name_lk].all_information[rkvd_tables['key'][i]] = \
            #     copy.deepcopy(kharacter_lk[character_name_lk].all_information[rkvd_tables['key'][i]]['key'])


# key_storage.append(dreturn_keys_values(karacter['Blake'].all_information[args_dict['table']][args_dict['qualifier2']][args_dict['column']]))
#
def get_sql_arguments(karacter, character_name_gsa):
    args_dict = {
        "column": "",
        "table": "",
        "qualifier": "ID",
        "qualifier2": ""
    }
    sql_args = []
    key_storage = [0, 1, 2]
    key_storage[0] = dreturn_keys_values(karacter[character_name_gsa].all_information) # key_storage is a dictionary of all table names

    for i in range(len(key_storage[0]['key'])):  # all tables
        args_dict['table'] = key_storage[0]['key'][i]  # get a table name(string) from key_storage, [0] is the index where it is stored, ['key'] is a dictionary index to attain the table name. We only store one table name but key_storage houses all of them
        key_storage[1] = dreturn_keys_values(karacter[character_name_gsa].all_information[args_dict['table']])

        for j in range(len(key_storage[1]['key'])):  # version of a table
            args_dict['qualifier2'] = key_storage[1]['key'][j]  # get a "key" name, rinse and repeat
            key_storage[2] = dreturn_keys_values(
                karacter[character_name_gsa].all_information[args_dict['table']][args_dict['qualifier2']])  # assign key_storage[2] a key/value==(dictionary) pair, it attains the "key" dictionary. The previous key_storage contained all "key"s to a specific table(aka an array of "key"s)
                                                                                                            # this key_storage will attain only one of those values
            for ij in range(len(key_storage[2]['key'])):  # values in table
                args_dict['column'] = key_storage[2]['key'][ij]  # get a column name from the values in key_storage. rinse and repeat
                sql_args.append(copy.deepcopy(args_dict))   # now we take all of the previously gained arg_dict values PLUS the newly acquired 'column' value and we append that to a slot in the array
    return sql_args


def load_character(base_item, sub_item, arg3):
    base_item[arg3['table']][arg3['qualifier2']][arg3['column']] = sub_item


def activate_Load_Character():
    all_sql_tables = get_table_names()
    table_keys = get_table_keys(all_sql_tables, character_name_global)
    load_keys(staging_kharacters, table_keys, character_name_global)
    sql_arguments = get_sql_arguments(staging_kharacters, character_name_global)

    for i in range(len(sql_arguments)):
        change_me_later = 'character_name'
        arg = sql_arguments[i]
        arg_alter = copy.deepcopy(sql_arguments[i])
        arg['table'] = replace(arg['table'], ' ', '_')
        arg['column'] = replace(arg['column'], ' ', '_')
        if arg['qualifier2'] != 'key':  # key
            sq_line_1 = sql_line_maker(arg['column'], arg['table'], arg['qualifier'], arg['qualifier2'],
                                       change_me_later, character_name_global)
            result = fetch_commit(sq_line_1)
            load_character(staging_kharacters[character_name_global].all_information, result[0][0], arg_alter)

