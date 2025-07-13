class MyCollection:
  def __len__(self):
      return 42 

coll = MyCollection()
s = len(coll)
print(str(s))
