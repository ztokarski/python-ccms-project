from ui import *
from open import *
from login import *



def main():
    while True:
        print(Ui.START_MAIN)
        Login().login_check()

if __name__ == '__main__':
    main()