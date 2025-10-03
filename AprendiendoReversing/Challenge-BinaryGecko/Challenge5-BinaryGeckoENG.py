import socket
import getpass
import pyperclip  

namepccomplete = socket.gethostname()

if '-' in namepccomplete:
    namesegment = namepccomplete.split('-')[-1]
else:
    namesegment = namepccomplete
namesegment = namesegment.upper()
username = getpass.getuser()
basestrings = namesegment + "-" + username + "-REV"
try:
    pyperclip.copy(basestrings)
    print("\n=== Chain Generation Simulator (FINAL) ===")
    print(f"Team Name (Segment, Capital Letters): {namesegment}")
    print(f"Username (Case-Sensitive): {username}")
    print("------------------------------------------")
    print(f" The string has been copied to the clipboard: {basestrings}")
    print("------------------------------------------")
except pyperclip.PyperclipException as e:
    
    print("\nERROR: Could not access clipboard.")
    print("Make sure you have a graphical environment or the necessary dependencies (e.g. xclip/xsel on Linux).")
    print(f"The generated string is: {basestrings}")
    print(f"Error details: {e}")