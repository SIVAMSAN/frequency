def most_frequent(string):
    frequency = {}

    for letter in string:
        frequency[letter] = frequency.get(letter, 0) + 1

    sorted_letters = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)

    for letter in sorted_letters:
        print(letter ,frequency[letter] ,sep= str ("="))

most_frequent("MISSISSIPPI")
