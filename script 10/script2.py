from script1 import *
# This is not the same as 'import script1'.

def main():
    print("script2 is __main__")
    print("script1 is not __main__")

if __name__ == "__main__":
    main()
    print()
else:
    print(2)