#CALCULATOR PROGRAM
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            print("Division by zero")
            return -1
        else:
            return a / b

    def expo(self, a, b):
        return a ** b

    def run_calculator(self):
        while True:
            a = float(input("Enter number 1:"))
            b = float(input("Enter number 2:"))
            choice = int(input("Enter the choice\n1: Addition\n2: Subtraction\n3: Multiplication\n4: Division\n5: Exponent\n6: Exit\n"))

            if choice == 1:
                result = self.add(a, b)
            elif choice == 2:
                result = self.sub(a, b)
            elif choice == 3:
                result = self.mul(a, b)
            elif choice == 4:
                result = self.div(a, b)
                if result == -1:
                    continue
            elif choice == 5:
                result = self.expo(a, b)
            elif choice == 6:
                print("Exit")
                break
            else:
                print("Wrong choice")
                continue

            print("Result:", result)

if __name__ == "__main__":
    calc = Calculator()
    calc.run_calculator()
    
    
    
#CALCULATOR PROGRAM
# class Calc:
#     def add(a,b):
#         return a+b;
#     def sub(a,b):
#         return a-b;
#     def mul(a,b):
#         return a*b;
#     def div(a,b):
#         if b==0:
#             print("Division by zero");
#             return -1;
#         else:
#             return a/b;
#     def expo(a,b):
#         return a**b
# 
#     def calculator(self):
#         while(True):
#             a=float(input("Enter number 1:"))
#             b=float(input("Enter number 2:"))
#             cases=int(input("Enter the choice \n 1:Addition \n 2:Subtraction \n 3:Multiplication \n 4:Division \n 5:Exponent \n 6:Exit \n"))
#             if cases==1:
#                 x=self.add(a,b)
#             elif cases==2:
#                 x=self.sub(a,b)
#             elif cases==3:
#                 x=self.mul(a,b)
#             elif cases==4:
#                 x=self.div(a,b)
#                 if x==-1:
#                     continue
#             elif cases==5:
#                 x=self.expo(a,b)
#             elif cases==6:
#                 print()
#                 break
#             else:
#                 print("Wrong choice")
#             print(x)
#         
# p=Calc()

