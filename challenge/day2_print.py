days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# function is_on_list
def is_on_list(x : list, y : str):
  str1 = ""
  for st in x :
    if st == y :
      str1 = "True"
      break
    else : 
      str1 = "False"
      continue
  return str1

# function get_x
def get_x(x : list, y : int) :
  return(x[y])

# function add_x
def add_x(x : list, y : str) :
  # x.append(x[5])
  for st in x :
    if st == y :
      x.append(st)
      break

# function remove_x
def remove_x(x : list, y : str) :
  # x.remove(x[0])
  for st in x :
    if st == y :
      x.remove(st)
      break

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)