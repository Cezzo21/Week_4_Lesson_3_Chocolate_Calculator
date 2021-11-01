#3 things: Ask for your name, "Hello Carol"
#Asks how many friends you have,
#how many chocolates you have
#how many chocolates you need to give to your friends
#how many left
#to yourself

Name = input("Name: ")
name = Name.capitalize()
print("Hello", name)
friends = int(input(f"How many friends do you have, {name}? "))
if friends == 0:
    print("Loser :P"), quit()
choc = int(input("And how many pieces of chocolate do you have, my love? "))
print()
if choc == 0:
    print("Are you stupid?"), quit()

share1 = choc/friends
share = int(share1)
left = round((share1 - share) * friends,ndigits=0)


if share == 1:
    print("You have to give each friend 1 piece of chocolate.")
elif share == 0 and choc != 0:
    print("You cannot share any chocolate with your friends :(, and you get to keep all", choc,"pieces to yourself.")
elif choc != 0:
    print("You have to give each friend", share, "pieces of chocolate.")

if left == 1:
    print("You will have 1 piece of chocolate left to yourself")
elif left == 0 and choc != 0:
    print("You will have no pieces left :'(")
elif share != 0 and choc != 0:
    print("You will have", left, "pieces left to yourself")
