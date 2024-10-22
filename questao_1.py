num = int(input("Qual o números de termos você deseja? "))

n1 = 0
n2 = 1
n3 = 0

for _ in range(0, num):
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
