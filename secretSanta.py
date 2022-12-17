

import random

names = ["Harsha Ahmed", "Arav Kewalia", "Arya Vaidya", "Lingesh Sashi Kumar", "Nan Singh", "Abby Mathew", "Rohan Gali", "Pranav Karra", "Riya Shenvi","Arul Nangla" , "Claire Zhu", "Andrew Thoms", "Aritra Banerjee", "Rohit Mudduluru","Mayur Kashyap", "Aarav Sureban", "Shivani Swarnakar", "Liana Wowk", "Ayush Singhal","Alan Jiang", "Harini Sivakumar", "Anya Goel", "Joon Young Doh", "Sahel Abraham", "Nandika Nambiar", "Eric Shao", "Jiya Mody", "Hershey Saran", "Manav Paul", "Armaan Kabra", "Arjun Agarwala", "Shrey Agarwal"]

# create a dictionary to store each person's wishlist
wishlists = {}

# ask each person to create their wishlist
for name in names:
  wishlist = input(f"{name}, please enter your wishlist: \n")
  wishlists[name] = wishlist

# create a list of remaining names that still need to be matched
remaining_names = names.copy()

# create a dictionary to store the secret santa matches
secret_santa_matches = {}

# match each person with another person on the list
while len(remaining_names) > 0:
  # get the current person's name
  current_name = remaining_names[0]

  # create a list of possible matches (excluding the current person and anyone they have already been matched with)
  possible_matches = [name for name in remaining_names if name != current_name and name not in secret_santa_matches.values()]

  # choose a random match from the list of possible matches
  match_name = random.choice(possible_matches)

  # add the match to the secret santa matches dictionary
  secret_santa_matches[current_name] = match_name

  # remove the current person and their match from the remaining names list
  remaining_names.remove(current_name)
  remaining_names.remove(match_name)

# print the secret santa matches
for name, match in secret_santa_matches.items():
  print(f" \n {name}'s secret santa match is {match}\n")
