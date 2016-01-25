def sumTwo(x,y):
  return x + y

def ageDescription(age):
  if age < 3:
    return "nothing"
  elif age >= 3 and age <= 12:
    return "you can shoot semi-automated guns in the USA"
  elif age > 12 and age <= 16:
    return "you can go to high school and think your life is really tough"
  elif age > 16 and age <= 25:
    return "you can go to an HBO and think high school was really easy in comparison"
  elif age > 25 and age <= 65:
    return "you can go to work"
  elif age > 65:
    return "you can retire now"

def interval(l,u):
  while l <= u:
    print(l)
    l = l+1

def intervalRec(l,u):
  if l <= u:
    print(l)
    intervalRec(l+1,u)

def evens(l,u):
  while l <= u:
    if l % 2 == 0:
      print(l)
    l = l+1

def evensRec(l,u):
  if l <= u:
    if l % 2 == 0:
      print(l)
    evensRec(l+1,u)

def odds(l,u):
  while l <= u:
    if l % 2 == 1:
      print(l)
    l = l+1

def oddsRec(l,u):
  if l <= u:
    if l % 2 == 1:
      print(l)
    oddsRec(l+1,u)

def intervalSum(l,u):
  sum = 0
  while (l <= u):
    sum = sum + l
    l = l + 1
  return 6

def intervalSumRec(l,u):
  if (l > u):
    return 0
  else:
    return l + intervalSumRec(l+1,u)
        
#print(sumTwo(10, 100))
#print(ageDescription(15))
#interval(5,10)
#intervalRec(5,10)
#evens(5,10)
#evens(5,10)
#odds(5,10)
#odds(5,10)
#print(intervalSum(1,3))
#print(intervalSumRec(1,3))
