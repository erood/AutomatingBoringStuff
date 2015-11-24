#! python3.4
# add_bullets_to_do_wiki_markup.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.
import pyperclip

__author__ = 'm'

def main():
    text = pyperclip.paste()
    lines = text.split("\n")

    for i in range(len(lines)):
        lines[i] = "*" + lines[i]

    text = '\n'.join(lines)
    pyperclip.copy(text)

if __name__ == "__main__":
    main()
