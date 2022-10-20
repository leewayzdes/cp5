def perevod(numb):
    n=numb
    newnumb=''
    while n > 0:
        newnumb = str(n % system) + newnumb
        n = n // system
    return newnumb

numb = int(input("Введите число: "))
system = int(input("Введите целевую систему счисления: "))

if system == 2:
    print(numb, "->", perevod(numb))
elif system == 8:
    print(numb, "->", perevod(numb))
else:
    print("Я могу перести только в двоичную и восмеричную систему счисления!")