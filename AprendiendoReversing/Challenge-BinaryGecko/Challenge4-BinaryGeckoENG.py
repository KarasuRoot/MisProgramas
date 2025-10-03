valid_entry = False
while not valid_entry:
    entrynum = input("Enter a 4-digit number (ej: 1933): ")
    if len(entrynum) == 4 and entrynum.isdigit():
        valid_entry = True
    else:
        print("Error: Please enter exactly 4 digits. Please try again.")
pair1_str = entrynum[0:2]
pair2_str = entrynum[2:4]
pair1 = int(pair1_str)
pair2 = int(pair2_str)
sum = pair1 + pair2
keyfinal = sum * 2
keyfinal = "KEY" + str(keyfinal)
print("\n--- CALCULATION DETAILS ---")
print(f"Number entered: {entrynum}")
print(f"   - First Pair: {pair1}")
print(f"   - Second Pair: {pair2}")
print(f"   - Addition: {pair1} + {pair2} = {sum}")
print(f"   - Result: {sum} x 2 = {keyfinal}")
print(f"\nThe generated key is: {keyfinal}")