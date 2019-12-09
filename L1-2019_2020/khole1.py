def capslow(phrase):
    caps = 0
    low = 0
    for letter in phrase:
        if letter.isupper():
            caps += 1
        elif letter.islower():
            low += 1
    
    print("There are", caps, "upper letters and", low, "lower letters in:\n", phrase, "\n\n")
    
capslow("Bonjour, je représente la RATP et la SNCF.")
