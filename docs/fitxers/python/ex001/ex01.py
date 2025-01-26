# try:
#     with open("fitxer02.txt") as f:
#         print(f.read())
# except Exception as e:
#     print("Error:", e)

try:
    f = open("fitxer01.txt")
    for linia in f:
        print(linia, end="")
except Exception as e:
    print("Error:", e)