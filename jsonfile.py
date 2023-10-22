import json

if (box_type == "Clothes"):
    new_user_values = {user_email:[box_size, "Clothes", key_words, measurements]}
elif (box_type == "Accessories"):
    new_user_values = {user_email:[box_size, "Accessories", colour, key_words]}
elif (box_type == "Shoes"):
    new_user_values = {user_email:[box_size, "Shoes", shoe_type, sex, shoe_size]}
    


with open("swapPartyUsers.json", 'w') as file:
    json.dump(new_user, file)

data[user_email]= new_user_values

with open('swapPartyUsers.json', 'w') as file:
    json.dump(data, file, ident=4)