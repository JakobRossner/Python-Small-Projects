import art
import game_data
import random


def make_random_number():
    random_number = random.randint(1, len(game_data.data)-1)
    #print(random_number)
    return random_number

def check_if_person_1_has_more_followers():
  if person_1_follower_count > person_2_follower_count:
    person_1_wins = True
    person_2_wins = False
    #print(f"person 1 has more followers ({person_1_follower_count} vs {person_2_follower_count})")
    return person_1_wins
  elif person_1_follower_count < person_2_follower_count:
    person_1_wins = False
    person_2_wins = True
    #print(f"person 2 has more followers ({person_2_follower_count} vs {person_1_follower_count})")
    return person_1_wins
  else:
    print("ERROR in check_if_person_1_has_more_followers()")


    
def check_user_decision_against_result():
  if user_decision == 1:
    if check_if_person_1_has_more_followers() == True:
      return True
    else:
      return False
  elif user_decision == 2:
    if check_if_person_1_has_more_followers() == False:
      return True
    else:
      return False
  else:
    print("ERROR in check_user_decision_against_result()")


#Put the data in my local array
_the_data = game_data.data
points = 0
game_should_continue = True

print(art.logo)
print("/////////////which person is more popular? Who has more followers (As of 2019)? Guess right/////////////\n\n")
display_followers = False
# INPUT message - display followers ?
user_input_display_followers = input("Do you want to display the follower count? It's like a cheat. Type 'y' or 'n': ")


# A debug feature that allows to display the follower number on screen
if user_input_display_followers == "y":
  display_followers = True
else:
  display_followers = False

# The game loop
while game_should_continue:

  person_1_random_number = make_random_number()
  person_1 = _the_data[person_1_random_number]["name"]
  person_1_profession = _the_data[person_1_random_number]["description"]
  person_1_follower_count = _the_data[person_1_random_number]["follower_count"]
  
  person_2_random_number = make_random_number()
  person_2 = _the_data[person_2_random_number]["name"]
  person_2_profession = _the_data[person_2_random_number]["description"]
  person_2_follower_count = _the_data[person_2_random_number]["follower_count"]
  
  #Failsafe if opponents are similiar
  if person_1_random_number ==  person_2_random_number:
    print(f"BOTH random opponents were similiar!  {person_1_random_number} vs {person_2_random_number} . Changing...")
    person_2_random_number = make_random_number()
    person_2 = _the_data[person_2_random_number]["name"]
    person_2_profession = _the_data[person_2_random_number]["description"]
    person_2_follower_count = _the_data[person_2_random_number]["follower_count"]
  else:
    print("")
  
  vs = art.vs
  
  # VS message
  if display_followers == True:
    message_vs = (f"\n\n{person_1}, {person_1_follower_count}k, {person_1_profession} {vs} \n{person_2}, {person_2_follower_count}k, {person_2_profession} ")
  else:
    message_vs = (f"\n\n{person_1}, {person_1_profession} {vs} \n{person_2}, {person_2_profession} ")

  
  user_decision = 1
  #Print VS message from art.py
  print(message_vs)
  
  
  #user_decision = int(input("\nWho has more followers? Type '1' or '2': "))
  try:
    user_decision = int(input("\nWho has more followers? Type '1' or '2': "))
  except ValueError:
    print("That's not an int!")
    user_decision = 1
    print("Setting decision to '1'")
    
  
  person_1_wins = check_if_person_1_has_more_followers()
  
  user_wins = check_user_decision_against_result()
  
  # future feature : removing entries from dictionary
  def delete_dic_entry():
    del _the_data[person_1_random_number]
  
  if user_wins == True:
    points += 1
    print (f"Points : {points}")
  else:
    print (f"\nGame Over. Final points : {points}")
    game_should_continue = False
