import os
import sys

# LBYL = Look Before You Leap
# EAFP = Easy to Ask Forgiveness than Permission

try:
    print("O arquivo existe")
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"[Error] {str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
# else: # Quando não ocorre a exceção.
    # print("Sucesso!!") 
# Finally
    #print("Executa isso sempre")
try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)

