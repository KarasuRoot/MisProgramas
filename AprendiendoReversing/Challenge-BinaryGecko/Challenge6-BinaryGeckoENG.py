import os
import struct
import sys
destination_directory = r"C:\Users\Administrador\Desktop\BinaryGecko"
filename = "licencia.enc"
pathcomplete = os.path.join(destination_directory, filename)
head = struct.pack("<I", 1279869765) 
substring1 = b"BinaryGeck0\x00" 
stuffed = b"\x00\x00\x00\x00" 
substring2 = b"9898\x00" 
final = head + substring1 + stuffed + substring2

try:
    os.makedirs(destination_directory, exist_ok=True)
    with open(pathcomplete, "wb") as f:
        f.write(final)

    print(f"    Success! File '{filename}' generated.")
    print(f"   Size: {len(final)} bytes")
    print(f"   Save path: {pathcomplete}")

except PermissionError:
    print(f" Permissions error: Could not write to path '{destination_directory}'.", file=sys.stderr)
    print("   Make sure you run the script with sufficient permissions.", file=sys.stderr)
except Exception as e:
    print(f"    Unexpected error while writing file: {e}", file=sys.stderr)