

import random

names = ["John Doe", "Jane Smith", "William Johnson", "Emily Williams", "James Brown", "Olivia Jones", "Alexander Garcia", "Sophia Miller", "Michael Davis", "Abigail Rodriguez", "Benjamin Martinez", "Chloe Gonzalez", "David Hernandez", "Ella Lopez", "Richard Perez", "Ava Gomez", "Christopher Sanchez", "Natalie Moore", "Matthew Anderson", "Isabella Taylor"]

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
