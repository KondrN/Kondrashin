melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455, 'Si': 1415, 'Be': 1287}
print("Введите первый элемент")
one_el= str(input())
print("Введите второй элемент")
two_el= str(input())
print(melt[one_el]-melt[two_el])