from my_import_file import *
from Load_Character import *


ril = return_index_location


def display_command(commands_dc):
    command_markers = [
        ':',  # write or display
        '-',  # table
        '#',  # key
        '.'  # column
    ]

    cm = command_markers
    for i in range(len(commands_dc) - 1):
        commands_dc[cm[i]][2].pop()
        commands_dc[cm[i]][2] = ("".join(commands_dc[cm[i]][2]))

    if commands_dc["#"][2].isdigit():
        commands_dc["#"][2] = int(commands_dc["#"][2])

    if commands_dc[":"][2] == 'display':
        dkv_tables = dreturn_keys_values(kharacters[character_name_global].all_information)
        if commands_dc['-'][2] in dkv_tables['key']:
            dkv_keys = dreturn_keys_values(kharacters[character_name_global].all_information[commands_dc["-"][2]])
            if commands_dc["#"][2] in dkv_keys['key']:
                print_lines_dict(kharacters[character_name_global].all_information[commands_dc["-"][2]][commands_dc['#'][2]])
            else:
                print(type(commands_dc["#"][2]), "  |   ", kharacters[character_name_global].all_information[commands_dc["-"][2]])
                fancy = dreturn_keys_values(kharacters[character_name_global].all_information[commands_dc["-"][2]])
                print(f'Invalid Key==({commands_dc["#"][2]})')
        else:
            print(f'Invalid Table==({commands_dc["-"][2]})')
    else:
        print(f'Somehow you triggered this and now we are both sad ||| ({commands_dc[":"][2]})')


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
            print("write")
            return True
        if commands_a[':'][0] == command_options[1]:
            commands_a['.'][1] = True
            for i, j in commands_a.items():
                if i == '.':
                    break

                if j[0][0] == ' ' or j[0][-1] == ' ' or j[1] is False:
                    return False, 'incorrect word syntax'
            display_command(commands_a)
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
    format_a = {               # format_a is a dictionary (curly braces are hard to see here, uwU!)
        ':': ['', False, []],  # write or display
        '-': ['', False, []],  # table
        '#': ['', False, []],  # key
        '.': ['', False, []]  # column
    }

    ### abbreviations ###
    cm = command_markers
    fa = format_a
    ###               ###

    j = 0
    for i in range(len(user_command_a)):
        if user_command_a[i] == ' ' and user_command_a[i - 1] == command_markers[j]:        # this code basically says loop over each character untill you find a pattern that matches a command pattern
            j = j + 1                                                                       # nd if you do then increment j(which which is used to index the command markers) so you can search for the next pattern
        else:
            format_a[cm[j]][2].append(user_command_a[i])                                    # appends a character to the 3rd index in the fa dictionary, when a valid user command is not found
            if not if_space(i, user_command_a):                                             # if ifspace is not true then return a false
                return False
            if user_command_a[i] == command_markers[j]:
                format_a[cm[j]][0] = ''.join(format_a[cm[j]][2])                            # this creates a string out of a char array from all the collected characters, i think its is creating the commands back together after no more command patterns can be found.
                format_a[cm[j]][1] = True                                                   # i vaguely remember this being a boolean to say whether the command is a valid one or not

    return command_rules(format_a)


activate_Load_Character()

user_command = input()

print(command_checker(user_command))