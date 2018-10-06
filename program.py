aliens = 2
password = "aliens"

print("Quickly! aliens are invading the planet")
print("You need to activate the global defence platforms")
print("Hope you know the password")
print()
print("----------------------------------------")
print("WELCOME TO THE THE GLOBAL DEFENCE NETWORK")
print("----------------------------------------")
print("")



guess = raw_input("Please enter the password:" ).upper()

while guess != password:
    print()
    print("INCORRECT PASSWORD")
    print()
    aliens = aliens ** 2
    print("There", aliens, "aliens now on the Earth, try again")
    if aliens > 7400000000:
        break
    print()
    print("Password hint: the things that are attacking us.")
    print()
    guess = raw_input("Quick! Please enter the password: ").upper()




if aliens > 7400000000:
    print("Nooo! The aliens have outnumbered us. All is lost." )
else:
    print("Hooray! We won the flight and word is alive")
