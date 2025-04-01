from pymongo import MongoClient
from colorama import Fore, Back, Style

client = MongoClient("mongodb+srv://SaiBadrik:BADRIKTHEGOAT@cluster0.qtfa2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
myDB = client["Badrik"]
collection = myDB.users

def add_user(username, password):
  user = {
    "username": username,
    "password": password
  }
  collection.insert_one(user)
  print(Fore.GREEN+"User added")
  print(Fore.WHITE+"")

def delete_user(username):
  doc = collection.find_one({"username": username})
  if(doc):
    collection.delete_one({"username": username})
    print(Fore.GREEN+"User deleted")
    print(Fore.WHITE+"")
  else:
    print(Fore.RED+"User not found")
    print(Fore.WHITE+"")

def get_user(username):
  doc = collection.find_one({"username": username})
  if(doc):
    print(Fore.CYAN+"User found")
    print(Fore.GREEN+"Username \t Password")
    print(Fore.YELLOW+doc["username"], "\t", doc["password"])
    print(Fore.WHITE+"")
  else:
    print("User not found")

def update_user(username, password):
  doc = collection.find_one({"username": username})
  if(doc):
    collection.update_one({"username": username}, {"$set": {"password": password}})
    print("User updated")
  else:
    print("User not found")

def get_all_users():
  users = collection.find()
  if(users):
    print(Fore.CYAN+"Username \t Password")
    print(Fore.WHITE+"")
    i = 0
    for user in users:
      print(i+1, user["username"], "        \t", user["password"])
      i += 1
      
  else:
    print("No users found")

displayMessage = '''
1. Add User
2. Delete User
3. Get User
4. Update User
5. Get All Users
6. Exit
'''

while True:
  print(displayMessage)
  choice = int(input("Enter your choice: "))
  if(choice == 1):
    username = input("Enter username: ")
    password = input("Enter password: ")
    add_user(username, password)
  elif(choice == 2):
    username = input("Enter username: ")
    delete_user(username)
  elif(choice == 3):
    username = input("Enter username: ")
    get_user(username)
  elif(choice == 4):
    username = input("Enter username: ")
    password = input("Enter new password: ")
    update_user(username, password)
  elif(choice == 5):
    get_all_users()
  elif(choice == 6):
    break
  else:
    print("Invalid choice")
