def display():
    print("this is display function! ")

def show():
    print("this show function ! ")

print(__name__)
# display()
# show()

import sys
def syss():
    for p in sys.path:
        print(p)
# syss()

def display():
    print("again display function")  

def main():
    print("main")
    print("function")

if __name__ == '__main__':
    main()