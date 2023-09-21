# encoding=utf-8

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

editor.replace(u"·\r\n","\r\n")   # end of line
editor.replace(u"»\r\n","_\r\n")  # output command
editor.replace(u"‡","->")         # assignment arrow

editor.replace(u"Ð","r")          # r
editor.replace(u"–","o")          # theta
editor.replace(u"¸","i")          # i

editor.replace(u"¯",">=")         # greater than or equal to
editor.replace(u"®","<=")         # less than or equal to
editor.replace(u"¬","<>")         # not equal

editor.replace(u"£","*")          # multiplication
editor.replace(u"¤","/")          # division
editor.replace(u"ƒ","!")          # factorial

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()