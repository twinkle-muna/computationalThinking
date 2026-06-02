c = {1,2,3}
d = {3, 4, 5}

try:
  print(c+d)
except TypeError:
  print("왜 일까? \"print(c + d) \" 뭘 고쳐야 할까?")
  print(c | d)
