# encoding=utf-8

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

editor.replace("\r\n","·\r\n")   # end of line
editor.replace("_\r\n","»\r\n")  # output command
editor.replace("->","‡")         # assignment arrow

editor.rereplace(r"\br\b","Ð")    # r
editor.rereplace(r"\bo\b","–")    # theta
editor.rereplace(r"\bi\b","¸")    # i

editor.replace(">=","¯")         # greater than or equal to
editor.replace("<=","®")         # less than or equal to
editor.replace("<>","¬")         # not equal

editor.replace("*","£")          # multiplication
editor.replace("/","¤")          # division
editor.replace("!","ƒ")          # factorial

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()