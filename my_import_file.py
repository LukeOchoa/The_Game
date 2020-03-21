import copy
import sqlite3


def return_index_location(sentence_a, find_item, switch):
    is_location = 0
    index_location = 0
    if switch:
        is_location = True

    for p in range(len(sentence_a)):
        if alpha[p] == find_item:
            index_location = p
            is_location = True
            break
        is_location = False
    if switch:
        return [index_location, is_location]
    else:
        return index_location


def fetch_commit(sqline):
    results = cursor1.execute(sqline)
    r = results.fetchall()
    connection.commit()
    return r


def define_spaces(amount):
    for i in range(amount):
        print()
    return amount


def print_lines_dict(item):
    item = dreturn_keys_values(item)
    for i in range(len(item["key"])):
        print("key=({}) --- value=({})".format(item["key"][i], item["value"][i]))


def print_lines(item):
    for i in range(len(item)):
        print(item[i])


def replace(item, old_item, new_item):
    l_item = list(item)
    cnt = 0
    for i in l_item:
        if i == old_item:
            l_item[cnt] = new_item
        cnt += 1
    item = "".join(l_item)
    return item


def return_keys_values(dictionary):
    memory = []
    key_slot = []
    value_slot = []
    for key, value in dictionary.items():
        key_slot.append(key)
        value_slot.append(value)
    memory.append(copy.deepcopy(key_slot))
    memory.append(copy.deepcopy(value_slot))
    return copy.deepcopy(memory)


def dreturn_keys_values(dictionary):
    memory = {
        "key": "key",
        "value": "value"
    }
    key_slot = []
    value_slot = []
    for key, value in dictionary.items():
        key_slot.append(key)
        value_slot.append(value)
    memory["key"] = copy.deepcopy(key_slot)
    memory["value"] = copy.deepcopy(value_slot)
    return copy.deepcopy(memory)

##############################


class Character:
    def __init__(self, free):
        self.all_information = free
        self.action_stats = free
        self.character_stats = free
        self.character = free
        self.dodge = free
        self.language_items = free
        self.move = free
        self.skills = free
        self.social_information = free


def init_character(char_obj):
    char_obj.all_information = {}
    char_obj.action_stats = []
    char_obj.character_stats = []
    char_obj.character = []
    char_obj.dodge = []
    char_obj.language_items = []
    char_obj.move = []
    char_obj.skills = []
    char_obj.social_information = []


rkvd = dreturn_keys_values


##############################


menu = ["action stats",
        "character stats",
        "characters",
        "dodge",
        "language items",
        "move",
        "personal information",
        "skills",
        "social information"
        ]
action_stats = {
    "ID": "blank",
    "basic move": "blank",
    "basic_lift": "blank",
    "basic speed": "blank",
    "damage_thrust": "blank",
    "damage_swing": "blank",
    "encumbrance_level": "blank",
    "move": "blank",
    "dodge": "blank",
    "damage resistance": "blank",
    "parry": "blank",
    "block": "blank",
    "character name": "blank"
}
character_stats = {
    "ID": "blank",
    "strength": "blank",
    "dexterity": "blank",
    "intelligence": "blank",
    "health": "blank",
    "hit points": "blank",
    "will": "blank",
    "perception": "blank",
    "fatigue points": "blank",
    "character name": "blank"
}
characters = {
    "ID": "blank",
    "character name": "blank"
}
dodge = {
    "ID": "blank",
    "dodge1": "blank",
    "dodge2": "blank",
    "dodge3": "blank",
    "dodge4": "blank",
    "character_name": "blank"
}
language_items = {
    "ID": "blank",
    "spoken": "blank",
    "speech level": "blank",
    "written": "blank",
    "written level": "blank",
    "point cost": "blank",
    "language name": "blank",
    "character name": "blank"
}
move = {
    "ID": "blank",
    "bmx1": "blank",
    "bmxdot8": "blank",
    "bmxdot6": "blank",
    "bmxdot4": "blank",
    "bmxdot2": "blank",
    "character name": "blank"
}
personal_information = {
    "ID": "blank",
    "name": "blank",
    "player": "blank",
    "height": "blank",
    "weight": "blank",
    "size modifier": "blank",
    "age": "blank",
    "point total": "blank",
    "unspent points": "blank",
    "appearance": "blank",
    "character name": "blank"
}
skills = {
    "ID": "blank",
    "name": "blank",
    "level": "blank",
    "relative_level": "blank",
    "character name": "blank",
}
social_information = {
    "ID": "blank",
    "technology level": "blank",
    "cultural familiarities": "blank",
    "reaction modifiers": "blank",
    "languages": "blank",  # should be language items, switch when necessary
    "character name": "blank",
    "mother tongue": "blank"
}
tables = {
    "action stats": {"key": action_stats},
    "character stats": {"key": character_stats},
    "characters": {"key": characters},
    "dodge": {"key": dodge},
    "language items": {"key": language_items},
    "move": {"key": move},
    "personal information": {"key": personal_information},
    "skills": {"key": skills},
    "social information": {"key": social_information}
}


#######################################################


connection = sqlite3.connect('/home/luke/PycharmProjects/The_Game/Databases/db.Character_Data')

connection.execute("PRAGMA foreign_keys = ON")

cursor1 = connection.cursor()