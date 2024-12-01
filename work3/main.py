import sys
from pathlib import Path
from colorama import Fore, Back, Style


def view_directory(directory, indent=0):
    print(f"==>> directory: {directory}")
    p = Path(directory)
    
    for x in p.iterdir():
        if x.is_dir():
            print(Fore.BLUE, " " * indent, "📂 Folder --> " + str(x))
            view_directory(x, indent + 2)
        elif x.is_file():
            print(Fore.YELLOW, " " * indent, "📄 File --> " + str(x))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Back.RED + "Потрібно передати шлях до директорії як аргумент!" + Style.RESET_ALL)
        sys.exit(1)

    directory = sys.argv[1]
    p = Path(directory)


    if not p.exists():
        print(Back.RED + f"Помилка: Шлях '{directory}' не існує!" + Style.RESET_ALL)
        sys.exit(1)

    if not p.is_dir():
        print(Back.RED + f"Помилка: Шлях '{directory}' не є директорією!" + Style.RESET_ALL)
        sys.exit(1)

    try:
        view_directory(directory)
    except Exception as e:
        print(Back.RED + f"Сталася помилка: {e}" + Style.RESET_ALL)
        sys.exit(1)
