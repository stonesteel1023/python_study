my_english_dict = {}

print("\n================= add_to_dict ====================\n")

def add_to_dict(x=dict, y="", z=str):
    if type(x) is not dict:
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif type(z) is not str :
        print("You need to send a word and a definition.")
    elif y in x.keys() :
        print(y + " is already on the dictionary. Won't add.")
    else :
        x[y] = z
        print(y + " has been added.")

print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")

print("\n===================== END ========================\n")

print("\n\n================= get_from_dict ====================\n")

def get_from_dict(x=dict, y=str):
  if y in x :
      print(y + ": " + x.get(y))
  else :
    if (y not in x) and (type(x) is dict) and (type(y) is str):
      print(y + " was not found in this dict.")
    elif type(x) is not dict :
      print("You need to send a dictionary. You sent: <class 'str'>")
    elif type(y) is not str :
      print("You need to send a word to search for.")  

print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n==================== END =========================\n")

print("\n\n================= update_word ====================\n")

def update_word(x=dict, y="", z=""):
    if type(x) is not dict :
        print("You need to send a dictionary. You sent: ", type(x))
    elif y =="" or z =="" :
        print("You need to send a word and a definition to update.")
    else :
        if y not in x :
            print(y + " is not on the dict. Can't update non-existing word.")
        else :
            x[y] = z
            print(y + " has been updated to: " + x.get(y))

print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n======================= END ==========================\n")

print("\n\n================= delete_from_dict ====================\n")

def delete_from_dict(x=dict, y=str):
  if type(x) is not dict :
    print("You need to send a dictionary. You sent: <class 'str'>")
  elif type(y) is not str :
    print("You need to specify a word to delete.")
  elif (y not in x) and (type(x) is dict) and (type(y) is str):
    print(y + " is not in this dict. Won't delete.")
  else :
    del x[y]
    print(y + " has been deleted.")
    
    my_english_dict = {}

print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n======================= END ==========================\n")
