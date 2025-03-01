from re import A
def diamond(n):

  alphabets = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'

  for i in range(0,n):
    print(' '*(n-i)+alphabets[:i+i+1])

  for i in range(n-2,-1,-1):
    print(' '*(n-i)+alphabets[:i+i+1])



diamond(3)
