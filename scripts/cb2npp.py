# encoding=utf-8
# Stored in %APPDATA%\Notepad++\plugins\Config\PythonScript\scripts

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

editor.replace("·\r\n","\r\n")   # end of line
editor.replace("»\r\n","_\r\n")  # output command
editor.replace("‡","->")         # assignment arrow
editor.replace("î","=>")         # jump command

editor.replace("Ð","r")          # r
editor.replace("–","o")          # theta
editor.replace("¸","i")          # i

editor.replace("¯",">=")         # greater than or equal to
editor.replace("®","<=")         # less than or equal to
editor.replace("¬","<>")         # not equal

editor.replace("£","*")          # multiplication
editor.replace("¤","/")          # division
editor.replace("ƒ","!")          # factorial

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()