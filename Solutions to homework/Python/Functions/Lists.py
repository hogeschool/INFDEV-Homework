class Empty:
  def __init__(self):
    self.IsEmpty = True

class Node:
  def __init__(self,head,tail):
    self.IsEmpty = False
    self.Head = head
    self.Tail = tail

def printAll(l):
  while not l.IsEmpty:
    print(l.Head)
    l = l.Tail

def printAllLists(ll):
  while not ll.IsEmpty:
    l = ll.Head
    while not l.IsEmpty:
      print(l.Head, end="\t")
      l = l.Tail
    print()
    ll = ll.Tail

def printAllRec(l):
  if not l.IsEmpty:
    print(l.Head)
    printAllRec(l.Tail)

def interval(l,u):
  i = Empty()
  while l <= u:
    i = Node(u,i)
    u = u - 1
  return i

def intervalRec(l,u):
  if l > u:
    return Empty()
  else:
    return Node(l, intervalRec(l+1,u))

def evens(l,u):
  i = Empty()
  while l <= u:
    if u % 2 == 0:
      i = Node(u,i)
    u = u - 1
  return i

def evensRec(l,u):
  if l > u:
    return Empty()
  else:
    if l % 2 == 0:
      return Node(l, evensRec(l+1,u))
    else:
      return evensRec(l+1,u)

def odds(l,u):
  i = Empty()
  while l <= u:
    if u % 2 == 1:
      i = Node(u,i)
    u = u - 1
  return i

def oddsRec(l,u):
  if l > u:
    return Empty()
  else:
    if l % 2 == 1:
      return Node(l, oddsRec(l+1,u))
    else:
      return oddsRec(l+1,u)

def multiplicationRow(r,i):
  if i > 10:
    return Empty()
  else:
    return Node(i * r, multiplicationRow(r,i+1))

def multiplicationTable(r):
  if r > 10:
    return Empty()
  else:
    return Node(multiplicationRow(r,1), multiplicationTable(r+1))

printAllLists(multiplicationTable(1))
