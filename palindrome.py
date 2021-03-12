
# Exercice Nro. 1

value= input('Enter a string:')

def is_palindrome():
   w=''
   for i in value:
       w =  i + w

   if (value == w):
     print('Word is Palindrome')
   else:
     print('Word is not Palindrome')


is_palindrome()

