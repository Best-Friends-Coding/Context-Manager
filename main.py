import time
while True:
  with open("C:/Users/satya/OneDrive/Shreyas/CodeCamp/Python Projects/Context Manager/file.txt", "r") as txt_file:
    reader = txt_file.read()
    c_word = input("Which word do you want to find? \n")
    time.sleep(1)
    print("Reading...")
    time.sleep(1)
    lister = reader.split()
    if c_word in reader:
          op1 = f"Yes, the word '{c_word}' present in the file..."
          time.sleep(1)
          print("Parsing...")
          time.sleep(1)          
          counter = reader.upper().count(c_word.upper())
          op2 = f"The count of '{c_word}'s is '{counter}'"
          print("Locating the words..This might take some time")
          time.sleep(1)
          indices=[]  
          c_word = c_word.lower()        
          for i in range(len(lister)):
            if (lister[i].lower().find(c_word)) != -1:
              f = i
              f+=1
              indices.append(f"{f}:{lister[i]}")
          op3 = indices

    else:
      print("This word isn't present in the file, please try again.")
    
    with open("C:/Users/satya/OneDrive/Shreyas/CodeCamp/Python Projects/Context Manager/output.txt", "a+") as output:
      output.write("\n \n \n")
      output.write(f"Output for {c_word}:\n")
      output.write(op1 + "\n")  
      output.write(op2 + "\n")
      output.write(str(op3) + "\n")


    y_n = input("Do you want to continue? ")
    y_n = y_n.lower()
    if y_n == "yes":
      print("Starting again")
    elif y_n == "no":
      print("Quitting...")
      print("Your output has been printed in output.txt")
      break                                  