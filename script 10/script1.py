from script2 import *
# This is not the same as 'import script2'.

def main():
    print("script1 is __main__")
    print("script2 is not __main__")

if __name__ == "__main__":
    main()
    print()
else:
    print(1)