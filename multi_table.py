def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")

def main():
    x=int(input("Enter the number:"))
    table(x)

main()