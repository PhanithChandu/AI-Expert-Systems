import itertools

# Taking input
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

# Collect unique letters
letters = list(set(word1 + word2 + result))

# Check condition
if len(letters) > 10:
    print("Too many letters. Not possible to assign digits.")
else:
    digits = range(10)
    solution_found = False

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # First letter cannot be zero
        if (mapping[word1[0]] == 0 or 
            mapping[word2[0]] == 0 or 
            mapping[result[0]] == 0):
            continue

        # Convert words to numbers
        num1 = int("".join(str(mapping[ch]) for ch in word1))
        num2 = int("".join(str(mapping[ch]) for ch in word2))
        num3 = int("".join(str(mapping[ch]) for ch in result))

        # Check condition
        if num1 + num2 == num3:
            print("\nSolution Found:")
            print(f"{word1} = {num1}")
            print(f"{word2} = {num2}")
            print(f"{result} = {num3}")
            solution_found = True
            break

    if not solution_found:
        print("No solution found.")
