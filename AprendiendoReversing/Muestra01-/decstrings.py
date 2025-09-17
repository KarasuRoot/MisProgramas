import base64
import sys
import clr

clr.AddReference("dnlib")

import dnlib
from dnlib.DotNet import *
from dnlib.DotNet.Emit import OpCodes

def xor(string, key):
    for i in range(len(string)):
        string[i] ^= key[i % len(key)];
        
    return string
    
def get_strings(module):
    strings = []
    for type in module.GetTypes():
        for method in type.Methods:
            try:
                for instr in method.Body.Instructions:
                    if instr.OpCode == OpCodes.Ldstr:
                        strings.append(instr.Operand)
            except Exception as e:
                #print(f"[!] {str(e)}")
                continue
                
    return strings

if __name__ == '__main__':
    key = bytearray([159, 116, 197, 16, 133, 107, 140, 151, 14, 105])
    
    module = dnlib.DotNet.ModuleDefMD.Load("Chrome.pif")
    strings = get_strings(module)
    
    for string in strings:
        if string:
            old = string
            try:
                string = bytearray(base64.b64decode(string))
                dec = xor(string, key)
                print(f"[+] {old} <-----------> {dec.decode()}")
            except Exception as e:
                print(f"[!] {old} <-----------> {str(e)}")