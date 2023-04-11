from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding= 'utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def change_info(info):
    info[0][0], info[0][2] = info[0][2], info[0][0]

    find_phone_pattern = r"(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?([доб. ]*)(\d*)\)?"
    change_phone_pattern = r'+7(\2)\3-\4-\5 \6\7'
    find_name_pattern = r'(\w+)\s(\w+)\s?(\w+)?'
    change_pattern_surname = r'\1'
    change_pattern_firstname = r'\2'
    change_pattern_lastname = r'\3'

    for i in info:
        result = re.sub(find_phone_pattern, change_phone_pattern, i[5])
        i[5] = result
        i[0] = i[0] + ' ' + i[1] + ' ' + i[2]
        i[2] = (re.sub(find_name_pattern, change_pattern_lastname, i[0]).strip())
        i[1] = (re.sub(find_name_pattern, change_pattern_firstname, i[0]).strip())
        i[0] = (re.sub(find_name_pattern, change_pattern_surname, i[0]).strip())
    return info

def delete_dupe(changed_info):
    changed_info.sort()
    total_info = []
    check_name = ''
    for i, person in enumerate(changed_info):
        if check_name != person[0] + person[1]:
            total_info.append(person)
        else:
            if total_info[-1][2] == '':
                total_info[-1][2] = changed_info[i][2]
            if total_info[-1][3] == '':
                total_info[-1][3] = changed_info[i][3]
            if total_info[-1][4] == '':
                total_info[-1][4] = changed_info[i][4]
            if total_info[-1][5] == '':
                total_info[-1][5] = changed_info[i][5]
            if total_info[-1][6] == '':
                total_info[-1][6] = changed_info[i][6]

        check_name = person[0] + person[1]
    return total_info


if __name__ == '__main__':
    res = change_info(contacts_list)
    total_res = delete_dupe(res)



with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    datawriter.writerows(total_res)