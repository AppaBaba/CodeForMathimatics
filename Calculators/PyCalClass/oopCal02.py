class oopCal:
   def add(self, n1, n2):
       answer = n1 + n2
       return answer
    
   def sub(self, n1, n2):
       answer = n1 - n2
       return answer
    

   def mul(self, n1, n2):
       answer = n1 * n2
       return answer
    

   def div(self, n1, n2):      
       if (n2 == 0):
           answer = "Can't divide by zero!"
       else:
           answer = n1 / n2 
    
       return answer
      
   def input2num(self):
       n1 = int(input("First number: "))
       n2 = int(input("Second number: "))
       return (n1, n2)

   def menu(self):
      print("Press key -\n"
            "add to Add\n"
            "sub to Subtract\n"
            "mul to Multiply\n" 
	    "dev to Divide\n"
            "exit to Exit\n")
      # Take input from the user
      select = input("Select operation:")

      if select == 'add':
         (n1, n2) = self.input2num()
         print(n1, "+", n2, "=", self.add(n1, n2))
         status = 0
         return status
      elif select == 'sub':
         (n1, n2) = self.input2num()
         print(n1, "-", n2, "=", self.sub(n1, n2))
         status = 0
         return status
      elif select == 'mul':
         (n1, n2) = self.input2num()
         print(n1, "*", n2, "=", self.mul(n1, n2))
         status = 0
         return status
      elif select == 'div':
         (n1, n2) = self.input2num()
         print(n1, "/", n2, "=", self.div(n1, n2))
         status = 0
         return status
      elif select == 'exit':
         status = 1
         return status
      else:
         print("Invalid input")
         status = 0
         return status


status = 0
cal = oopCal()
while status == 0:
   status = cal.menu()
   print()
if status == 1:
    print()
print("Good Stuff")

