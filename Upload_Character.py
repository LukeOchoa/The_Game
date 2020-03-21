def insert_character(kharacter):
    for i in kharacters['Blake'].all_information:
        for j in kharacters['Blake'].all_information[i]:
            if j != 'key':
                for k in kharacters['Blake'].all_information[i][j]:
                    print(kharacters['Blake'].all_information[i][j][k])
                    print(k, "kei")
                    define_spaces(1)
                    # table,column,   values,
                    print(i, j, k)
                    sql_insert = "INSERT INTO {} {} VALUES {}".format(replace(i, ' ', '_'), str(j), k)
                    print(sql_insert)
                    fetch_commit(sql_insert)

