# Contact Diary BY Muhammad Hanan Asghar
import os
exit = True
while exit:
  print()
  print(" [+] Contact Diary [+] ")
  print("")
  print(" [1] Add Contact")
  print(" [2] Show Contacts")
  print(" [3] Exit Diary")
  print(" [4] Delete Diary")
  print("")
  inp = int(input(" > "))
  if inp==1:
    name = input(" [+] Enter Contact Name : ")
    phone = str(input(" [+] Enter Contact Number : "))
    if "contacts.txt" in list(os.listdir()):
      with open("contacts.txt","a") as file:
        file.write("Name : {}, Contact : {}\n".format(name,phone))
      file.close()
    else:
      with open("contacts.txt","w") as file:
        file.write("Name : {}, Contact : {}\n".format(name,phone))
      file.close()
  elif inp == 2:
    if "contacts.txt" in list(os.listdir()):
      with open("contacts.txt","r") as file:
        contacts = file.read()
      print("")
      print("Your Contact Diary")
      print("")
      print(contacts)
      file.close()
      continue
    else:
      print("No Contacts Found!")
  elif inp == 3:
    exit = False
  elif inp == 4:
    if "contacts.txt" in list(os.listdir()):
      os.remove("contacts.txt")
    else:
      print("No Diary Found")
  else:
    print("Please Enter Correct Option")
