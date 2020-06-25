#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

bettermcbShelf = shelve.open('bettermcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        bettermcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del bettermcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:

  # List keywords and load content.
    if sys.argv[1].lower() == 'list':
      pyperclip.copy(str(list(bettermcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
      thing = list(bettermcbShelf.keys())
      for i in thing:
        del bettermcbShelf[i]
        
    elif sys.argv[1] in bettermcbShelf:
      pyperclip.copy(bettermcbShelf[sys.argv[1]])

bettermcbShelf.close()