import os

from pyfiglet import Figlet
from colorama import Fore


def clear_screen():
    os.system("clear")


def render_text(text: str):
    figlet = Figlet(font="slant")

    for line in text.splitlines():
        print(Fore.RED + figlet.renderText(line))


def ask_question(question):
    print(Fore.YELLOW + question)
    return input(Fore.GREEN + "Yes or No: ").capitalize()


def main():
    clear_screen()
    render_text("I LOVE YOU !")
    response = ask_question("You love me?")

    if response == "Yes":
        clear_screen()
        render_text("Hehe")
        print(Fore.YELLOW + "<3")
    elif response == "No":
        clear_screen()
        render_text("1000-7?")
    else:
        print(Fore.YELLOW + "I not understand you(")


if __name__ == "__main__":
    main()
