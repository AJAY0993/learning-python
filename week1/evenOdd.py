def main():
    num = int(input("Your number is? "))

    if isEven(num):
        print('Even')
    else: 
        print('Odd')

def isEven(n):
   return n%2 == 0
         
main()