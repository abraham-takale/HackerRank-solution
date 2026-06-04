PhoneBook={}
n=int(input())
for i in range(n):
    name,phone=input().split()
    PhoneBook[name]=phone
try:        
    while True:
        name=input()
        if name in PhoneBook:
            print(name+ "="+PhoneBook[name])
        else:
            print("Not found")
except EOFError:
    pass
