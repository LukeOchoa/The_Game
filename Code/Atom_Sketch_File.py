from my_import_file import *


# def return_index_location(sentence_a, find_item, switch):
#     is_location = 0
#     index_location = 0
#     if switch:
#         is_location = True
#
#     for p in range(len(sentence_a)):
#         if alpha[p] == find_item:
#             index_location = p
#             is_location = True
#             break
#         is_location = False
#     if switch:
#         return [index_location, is_location]
#     else:
#         return index_location
#
#
# def if_space(item_a, sentence):
#     item_location = ril(sentence, item_a, False)
#     if sentence[item_location - 1] != ' ' and sentence[item_location + 1] != ' ':
#         return True
#     else:
#         return False
#
#
# class Template:
#     def __init__(self, free):
#         self.template = ""
#
#     def load_commands(self, fv):
#         self.template.display = '{} {}- {}#'.format(
#     def load_write():


# format_a = {
#     ':': ['', False],  # write or display
#     '-': ['', False],  # table
#     '#': ['', False],  # key
#     '.': ['', False]  # column
# }
# for i, j in format_a.items():
#     print(j)


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


#
#
#
# format_a = {
#     ':': ['display:', True],  # write or display
#     '-': ['table', True],  # table
#     '#': ['key', True],  # key
#     '.': ['column', True]  # column
# }
#
# fa = format_a
#
# print(command_rules(fa))


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


print(command_checker(input()))

# display: table- key# column.
