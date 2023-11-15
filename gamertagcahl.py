
while True:
    gamertag = input("Enter a gamertag: ")
    if len(gamertag) <= 15:
        break
    else:
        print("Gamertag must be 15 characters or less. Please try again.")

print("Valid gamertag entered:", gamertag)
