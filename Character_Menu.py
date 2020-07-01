from my_import_file import *

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
    if "".join(commands_dc[":"][2]) == 'display':
        if "".join(commands_dc["-"][2]) in dreturn_keys_values(tables)["key"]:
            if "".join(commands_dc["#"][2]) in dreturn_keys_values(tables["".join(commands_dc["-"][2])]):
                print_lines_dict(tables["".join(commands_dc['-'][2])]["".join(commands_dc["#"][2])])
            else:
                print(f'Invalid Key==({"".join(commands_dc["#"][2])})')
        else:
            print(f'Invalid Table==({"".join(commands_dc["-"][2])})')
    else:
        print(f'Somehow you triggered this and now we are both sad ||| ({"".join(commands_dc[":"][2])})')


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
        # print(commands_a)
        if commands_a[':'][0] == command_options[0]:
            for i, j in commands_a.items():
                if j[0][0] == ' ' or j[0][-1] == ' ' or j[1] is False:
                    return False, 'incorrect word syntax'
            print("write")
            return True
        if commands_a[':'][0] == command_options[1]:
            commands_a['.'][1] = True
            for i, j in commands_a.items():
                define_spaces(1)
                # print("isolate=", j)
                define_spaces(1)
                if i == '.':
                    break
                # print('j1=', j[0][0], " and j", j)
                # print('j2=', j[0][-1], " and j", j)
                # print('j3=', j[1], " and j", j)
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

    user_command_array = [[0]]
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


user_command = input()

print(command_checker(user_command))
