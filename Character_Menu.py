from my_import_file import *

ril = return_index_location


def display_command():
    pass


def write_command():
    pass


# if_space() examines a character, if it is a space it makes sure adjacent chars are not spaces
def if_space(item_a, sentence):
    if sentence[item_a] == ' ':
        if sentence[item_a - 1] != ' ' or sentence[item_a + 1] != ' ':
            return True
        else:
            return False
    else:
        return True


def command_rules(commands_a):
    command_options = [
        'write:',
        'display:'
    ]
    while True:
        if commands_a[':'][0] == command_options[0]:
            for i, j in commands_a.items():
                if j[0][0] == ' ' or j[0][-1] == ' ' or j[1] is False:
                    return False, 'incorrect word syntax'
            return True
        if commands_a[':'][0] == command_options[1]:
            commands_a['.'][1] = True
            for i, j in commands_a.items():
                if j[0][0] == ' ' or j[0][-1] == ' ' or j[1] is False:
                    return False, 'incorrect word syntax'
            return True
        else:
            return False, 'No commands matched'


def command_checker(user_command_a):
    command_markers = [
        ':',  # write or display
        '-',  # table
        '#',  # key
        '.'  # column
    ]
    format_a = {
        ':': ['', False, []],  # write or display
        '-': ['', False, []],  # table
        '#': ['', False, []],  # key
        '.': ['', False, []]  # column
    }

    ### abbreviations ###
    cm = command_markers
    fa = format_a
    ###               ###

    user_command_array = [[0]]
    j = 0

    for i in range(len(user_command_a)):
        if user_command_a[i] == ' ' and user_command_a[i - 1] == command_markers[j]:
            j = j + 1
        else:
            format_a[cm[j]][2].append(user_command_a[i])
            if not if_space(i, user_command_a):
                return False
            if user_command_a[i] == command_markers[j]:
                format_a[cm[j]][0] = ''.join(format_a[cm[j]][2])
                format_a[cm[j]][1] = True

    return command_rules(format_a)


user_command = input()

print(command_checker(user_command))


