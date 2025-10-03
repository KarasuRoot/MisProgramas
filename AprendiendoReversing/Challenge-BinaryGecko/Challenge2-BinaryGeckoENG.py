user_name = input("Insert your name: ")
intermediate_key = []
for char in user_name:
    new_char_code = ord(char) + 3
    new_char = chr(new_char_code)
    intermediate_key.append(new_char)
ciphered_string = "".join(intermediate_key)
final_key = ciphered_string[::-1]
print("\n--- Result ---")
print(f"Usuario: {user_name}")
print(f"KeyGen: {final_key}")
print("-----------------")