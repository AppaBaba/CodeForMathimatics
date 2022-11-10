import math

class oopCal:
   def add(self, n1, n2):
       return n1 + n2
   def sub(self, n1, n2):
       return n1 - n2
   def mul(self, n1, n2):
       return n1 * n2
   def div(self, n1, n2):      
       if (n2 == 0):
           return "Can't divide by zero!"
       else:
           return n1 / n2
   def sq(self, n):
      return n**2
   def sqr(self, n):
      return math.sqrt(n)
   def log(self, n):
      return math.log(n)
   def exp(self, n1, n2):
      return n1**n2
   def sinr(self,n):
        return math.sin(n)
   def cosr(self,n):
        return math.cos(n)
   def inputnum(self):
      n = int(input("Number: "))
      return n
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
            "squ for Square\n"
            "sqr for Squareroot\n"
            "log for log\n"
            "exp for Exponentiate\n"
            "sin for Sine\n"
            "cos for Cosine\n"
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
      elif select == 'squ':
         n = self.inputnum()
         print(" ", self.sq(n))
         status = 0
         return status
      elif select == 'sqr':
         n = self.inputnum()
         print(" ", self.sqr(n))
         status = 0
         return status
      elif select == 'log':
         n = self.inputnum()
         print("log(",n,") = ", self.log(n))
         status = 0
         return status
      elif select == 'exp':
         (n1, n2) = self.input2num()
         print(" ", self.exp(n1, n2))
         status = 0
         return status
      elif select == 'sin':
         n = self.inputnum()
         print (self.sinr(n))
         status = 0
         return status
      elif select == 'cos':
         n = self.inputnum()
         print (self.cosr(n))
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

