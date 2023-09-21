# casio-programs
Programs for Casio CFX-9850G graphing calculator

My repository of Casio CFX-9850G programs. Some of these I wrote when I first got this calculator, when I was in seventh or eighth grade.

## Editor
I used the Casio FA-124 program (linked below) and a serial cable to copy these programs from the calculator to my computer. After that, I copied the text from FA-124 to Notepad++. Notepad++ does not support the character set that the Casio does, so I created two scripts (located in the scripts folder) that will convert the code from the Casio character set to characters that make more sense for coding, and vice versa. You will need the Python Script plugin for Notepad++ to run these scripts.

The following characters get converted (So far. I'm sure more will need to be added):

| Casio Character | Description              | How it's displayed in Npp | Substitution |
| :-------------: | -----------              | :-----------------------: | :----------: |
| `↵`             | end of line              | `·`                       | `\r\n`       |
| `◢`             | output command           | `»`                       | `_\r\n`      |
| `→`             | assignment               | `‡`                       | `->`         |
| `⇒`             | jump command             | `î`                       | `=>`         |
| `r`             | r                        | `Ð`                       | `r`          |
| `θ`             | theta                    | `–`                       | `o`          |
| `i`             | i                        | `¸`                       | `i`          |
| `≥`             | greater than or equal to | `¯`                       | `>=`         |
| `≤`             | less than or equal to    | `®`                       | `<=`         |
| `≠`             | not equal to             | `¬`                       | `<>`         |
| `×`             | multiplication           | `£`                       | `*`          |
| `÷`             | division                 | `¤`                       | `/`          |
| `!`             | factorial                | `ƒ`                       | `!`          |

So when editing programs with Notepad++, use the substituted characters. Then before transferring to the calculator, run the npp2cb script to convert back.

## Resources
* [Casio FA-124](https://edu.casio.com/forteachers/er/software/)
* [Casio CFX-9850G Manual](https://support.casio.com/en/manual/manualfile.php?cid=004008001)
* [Notepad++](https://notepad-plus-plus.org/downloads/)
* [Python Script Plugin](https://npppythonscript.sourceforge.net/)  <--- You can just install this through the Plugins Admin in Notepad++. No need to download it manually.
