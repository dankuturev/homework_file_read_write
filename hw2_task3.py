def create_new_file():
    filenames = [i+".txt" for i in input().split(',')]  # Ввести 1,2,3
    count_lines = []
    for item in filenames:
        with open(item, encoding='utf-8') as file:
            count = 0
            for line in file:
                print(line)
                count += 1
            count_lines.append(count)
    dict_lenght = dict(zip(count_lines, filenames))
    dict_lenght = dict(sorted(dict_lenght.items(), key=lambda x: x[0]))
    with open('new_file.txt', 'a', encoding='utf-8') as new_file:
        for lenght in dict_lenght:
            with open(dict_lenght[lenght], 'r', encoding='utf-8') as file:
                for line in file:
                    new_file.write(line + '\n')


create_new_file()
