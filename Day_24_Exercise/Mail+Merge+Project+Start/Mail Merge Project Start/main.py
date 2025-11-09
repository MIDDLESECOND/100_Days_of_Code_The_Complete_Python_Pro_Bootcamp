#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# import the letter template
with open("Input/Letters/starting_letter.txt", mode = "r") as file:
    letter_content = file.read()

# import the names as list using readlines
with open("Input/Names/invited_names.txt", mode = "r") as file:
    name_list = file.readlines()

# need to clean each name in the list to drop the '\n'
cleaned_name_list = []
for name in name_list:
    cleaned_name = name.replace("\n", "").strip()
    cleaned_name_list.append(cleaned_name)

# print(cleaned_name_list)
# check to make sure name is really cleaned

# generate the readytosend letters
for cleaned_name in cleaned_name_list:
    txt_name = "letter_for_" + str(cleaned_name) + ".txt"
    new_letter_content = letter_content.replace("[name]", cleaned_name)
    with open(f"Output/ReadyToSend/{txt_name}", mode = "w") as file:
        file.write(new_letter_content)