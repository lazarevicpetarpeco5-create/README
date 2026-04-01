print("Welcome to the Calculator")


 

while True: #start of the loop



   print("\nchoose 2 numbers")
   num1 = float(input())
   num2 = float(input())
  

   op = input("Choose(+, -, *, /) or type `exit` to quit:")

   if  op == "exit":
    break #stops the loop

   elif op == "+":

    print(num1 + num2)

   elif op == "-":
    print(num1 - num2)

   elif op == "*":

    print(num1 * num2)

   elif op == "/":

    print(num1 / num2)





