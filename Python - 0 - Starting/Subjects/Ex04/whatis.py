import sys

def whatis(arg):
   if len(sys.argv) != 2:
       raise AssertionError("AssertionError: more than one argument is provided")

   try:
       num = int(arg)
       print("I'm Even." if num % 2 == 0 else "I'm Odd.")
   except ValueError:
       raise AssertionError("AssertionError: argument is not an integer")

try:
   if(len(sys.argv) >= 2):
       whatis(sys.argv[1])
   elif(len(sys.argv) < 2):
       sys.exit(1)
except AssertionError as e:
   print(e)
   sys.exit(1)