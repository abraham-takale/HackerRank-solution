def count_substring(string, sub_string):
    s = len(string)
    su = len(sub_string)
    split_string = []
    coun = 0

    for i in range(s - su + 1):
        split_string.append(string[i:i+su])

    for item in split_string:
        if item == sub_string:
            coun += 1
    return coun

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
