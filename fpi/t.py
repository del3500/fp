from typing import Optional

def get_full_name(first_name: str, last_name: str ):
  full_name = first_name.title() + " " + last_name.title()
  return full_name

def get_name_w_age(name: str, age: int) -> str:
  name_with_age = name + " is this old: " + str(age)
  return name_with_age

def get_items(item_a: str, item_b: int, item_c: bool):
  return item_a, item_b, item_c

def process_items(items: list[str]):
  for item in items:
      print(item)

def process_union(item: int | str):
  print(item)
  return item


#Avoid using Optional for a function where parameter is required,
#use Union instead to avoid confusion when using None

def name_tester(name: str | None) -> str:
  if name is not None:
     print(f"Hey {name}")
     return name
  else:
    print("boo!")

def say_hi(name: Optional[str]):
  print(f"Hey{name}")


