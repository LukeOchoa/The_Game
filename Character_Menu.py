from my_import_file import *
from Load_Character import *


ril = return_index_location


def display_command(commands_dc):
    if validate_commands_against_dictionary(commands_dc):
        print_lines_dict(staging_kharacters[character_name_global].all_information[commands_dc["-"][2]][commands_dc['#'][2]])


def write_command(commands_wc):
    print("please choose what you want to write now: ")
    if validate_commands_against_dictionary(commands_wc):
        staging_kharacters[character_name_global].all_information[commands_wc["-"][2]][commands_wc['#'][2]][commands_wc['.'][2]] = input()


def dictionary_query(commands_dq):

    dkv_tables = dreturn_keys_values(staging_kharacters[character_name_global].all_information)
    if commands_dq['-'][2] in dkv_tables['key']:
        dkv_keys = dreturn_keys_values(staging_kharacters[character_name_global].all_information[commands_dq["-"][2]])
        if commands_dq["#"][2] in dkv_keys['key']:
            dkv_columns = dreturn_keys_values(staging_kharacters[character_name_global].all_information[commands_dq["-"][2]][commands_dq["#"][2]])
            if commands_dq[":"][2] == 'write':
                if commands_dq["."][2] in dkv_columns['key']:
                    return True
                else:
                    print(f'Invalid Column==({commands_dq["."][2]})')
                    return False
            return True
        else:
            print(type(commands_dq["#"][2]), "  |   ", staging_kharacters[character_name_global].all_information[commands_dq["-"][2]])
            print(f'Invalid Key==({commands_dq["#"][2]})')
            return False
    else:
        print(f'Invalid Table==({commands_dq["-"][2]})')
        return False


def validate_commands_against_dictionary(commands_vcad):
    command_markers = [
        ':',  # write or display
        '-',  # table
        '#',  # key
        '.'  # column
    ]

    def clean_commands():
        x = 1
        if commands_vcad[":"][0] == 'display:':
            x = 1
        if commands_vcad[":"][0] == 'write:':
            x = 0
        cm = command_markers
        for i in range(len(commands_vcad) - x):
            commands_vcad[cm[i]][2].pop()
            commands_vcad[cm[i]][2] = ("".join(commands_vcad[cm[i]][2]))

        if commands_vcad["#"][2].isdigit():
            commands_vcad["#"][2] = int(commands_vcad["#"][2])

        return commands_vcad

    return dictionary_query(clean_commands())


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
            write_command(commands_a)
            return True
        elif commands_a[':'][0] == command_options[1]:
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

while True:

    user_command = input()

    print(command_checker(user_command))
