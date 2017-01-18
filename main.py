import os
from ui import *
from open_list import *
from login import *



def main():
    while True:
        print("{:^250}".format(Ui.START_MAIN))
        Login().login_check()
os.system("printf '\033c'")
if __name__ == '__main__':
    main()
