# # print('avijit')
# import program
# print(program.add(5,3))
#
a=input("enter number: ")
print("you numebr is:", a)
try:
    b=int(a)*3
    print(b)
    # for i in range(1,11):
    #     print(f'{int(a)} X {i}={int(a)*i}')

except Exception as e:
    print('your exception is: ',e)

print('some inp line of code')
print('end of program')