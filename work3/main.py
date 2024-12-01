import sys
from pathlib import Path
#from colorama import Fore

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

def view_directory(directory, indent=0):
    path = Path(directory)
    print()
    pass

view_directory('path')