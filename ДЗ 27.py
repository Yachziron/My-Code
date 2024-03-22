import math
class Pendulum:
   g = 10
   pi = 3.14

   @classmethod
   def calculate_period(cls, length):
       return 2 * Pendulum.pi * math.sqrt(length/Pendulum.g)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)