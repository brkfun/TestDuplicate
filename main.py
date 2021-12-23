import os
import re


def linux_command():
    print('Linux command use: cut -d: -f2 passwd | sort | uniq -d')
    cmd = 'cut -d: -f2 passwd | sort | uniq -d'
    os.system(cmd)


def array_value_counter(array, max_duplicate):
    response = []
    for i in array.items():
        if len(i[1]) >= max_duplicate:
            response.append({i[0]: i[1]})
    return response


def python_section():
    print('Python command use: ')
    file_path = input('file path:[default : ./passwd]') or "passwd"
    file_reader = open(file_path, "r")
    regex = re.findall(r"(.*):(.*):(.*)", file_reader.read(), re.MULTILINE)
    intension = {}
    for i in regex:
        if i[1] in intension:
            intension[i[1]].append(i[0])
            continue
        intension.update({i[1]: [i[0]]})
    print(intension)
    print("all values by key to dictionary")
    print(array_value_counter(intension, 2))


if __name__ == '__main__':
    print('Developed on pyCharm with venv')
    sel = input('Select your style: \r\n [1]: Python \r\n [Anything Else]: Linux \n') or "1"
    if sel == "1":
        python_section()
    else:
        linux_command()
