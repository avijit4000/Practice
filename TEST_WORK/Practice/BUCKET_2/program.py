# print("Avijit")
# def pe(a):
#     if len(a)<=1:
#         return a
#     ie=a[len(a)//2]
#     lef=[x for x in a if x<ie]
#     rig=[x for x in a if x<ie]
#     return pe(lef)+[ie]+pe(rig)
# if __name__=="__main__":
#     a=[10,2,5,6,99,63,549,25,6,55,84,15,47]
#     print(pe(a))

# print([x for x in range(10) if x%2!=0])
# import random as re
# print(re.choice([x for x in range(0,11) if x%2==0]))
# print([x for x in range(0,11) if x%2==0])
# print(re.choice([2,5,6,9]))
#
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(10))

# class Person:
#     name="Avijit"
#     def __init__(self,name=None):
#         self.name=name
# jeffrey=Person("Biswas")


# def add_matrices(matrix1, matrix2):
#     result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
#     for i in range(3):
#         for j in range(3):
#             result[i][j] = matrix1[i][j] + matrix2[i][j]
#
#     return result
#
# # Function to multiply two matrices
# def multiply_matrices(matrix1, matrix2):
#     result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 result[i][j] += matrix1[i][k] * matrix2[k][j]
#
#     return result
#
# # Input two 3x3 matrices from the user
# print("Enter elements of the first 3x3 matrix:")
# matrix1 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(3)] for i in range(3)]
#
# print("Enter elements of the second 3x3 matrix:")
# matrix2 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(3)] for i in range(3)]
#
# # Call the functions to perform addition and multiplication
# addition_result = add_matrices(matrix1, matrix2)
# multiplication_result = multiply_matrices(matrix1, matrix2)
#
# # Display the results
# print("\nAddition Result:")
# for row in addition_result:
#     print(row)
#
# print("\nMultiplication Result:")
# for row in multiplication_result:
#     print(row)


# print([[int(input()) for j in range(3)] for i in range(3)])
# def add_(m1,m2):
#     result=[[0,0,0],[0,0,0],[0,0,0]]
#     for i in range(3):
#         for j in range(3):
#             result[i][j]=m1[i][j]+m2[i][j]
#     return result
m1=[[2,5,6],[6,5,8],[4,7,9]]
m2=[[5,6,9],[8,7,9],[8,1,9]]
# print(add_(m1,m2))


# [[int(input("enger:  ")) for j in range(3)] for i in range(3)]

# def multp(m1,m2):
print(m1)
print(m2)

