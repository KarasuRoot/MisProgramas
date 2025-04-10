def xor_strings_with_details(str1, str2):
  """Realiza la operación XOR byte a byte entre dos cadenas y muestra los detalles de cada operación, incluyendo el carácter ASCII resultante y la cadena final.

  Args:
    str1: La primera cadena.
    str2: La segunda cadena.
  """

  bytes1 = bytes(str1, 'utf-8')
  bytes2 = bytes.fromhex(str2)

  result_bytes = bytearray()
  for i, (b1, b2) in enumerate(zip(bytes1, bytes2)):
      result_byte = b1 ^ b2
      result_char = chr(result_byte)
      result_bytes.append(result_byte)
      print(f"{i}: {hex(b1)[2:]} XOR {hex(b2)} = {hex(result_byte)[2:]} ({result_char})")

  result_string = bytes(result_bytes).decode('utf-8')
  print(f"La cadena resultante es: {result_string}")

# Datos de entrada
string1 = "Messing_in_bytes"
hex_string = "1F 2C 37 36 3B 3d 28 19 3D 26 1A 31 2D 3B 37 3E"

# Realizar la operación XOR y mostrar los detalles
xor_strings_with_details(string1, hex_string)