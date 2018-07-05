
[back](api_files.md)

<a name="how_to_install_api"></a>
### How to install an api file and enable calltips + completion

* As an example, let's set up the api file for the C standard library

* Download [c.api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c.api)

* Move `c.api` into the directory that contains SciTE. In Linux this is typically `/usr/bin/scite` or `/usr/local/bin/scite`

* Open SciTE

* From the Options menu, choose Open User Options File

* Add the line `api.$(file.patterns.cpp)=$(SciteDefaultHome)/c.api`

* Add the line `calltip.cpp.use.escapes=1`

* Add the line `calltip.cpp.word.characters=$(chars.alpha)$(chars.numeric)_`

* Save this file and restart SciTE

* In SciTE, start a new file and save it as "test.c"

* Calltips

    * Type the text "fprintf("
    
    * As soon as you press (, a calltip appears, showing documentation for "fprintf"
    
    * You can show the calltip tooltip again by clicking to the right of the ( and pressing Ctrl+Shift+Space
    
* Completion

    * On an empty line, type the text "fp" and press Ctrl+Space
    
    * A listbox appears allowing you to choose between fprintf, fputc, and fputs
    
    * You can use the arrow keys can navigate this box and Enter to choose an item from this box


<a name="how_to_install_properties"></a>
### How to install a properties file

* A .properties file can change colors and fonts, specify lists of keywords, define what action to take on "Compile" and "Go", map file extensions to a programming language, and more

* To install a properties file, simply move the .properties file into the directory that contains SciTE. In Linux this is typically `/usr/bin/scite` or `/usr/local/bin/scite`

* If desired, you can then edit the properties file based on your configuration. For example, you have several different versions of Python installed. You can open SciTE, and from the Options menu choose `Open python.properties`. At the bottom of the file you can see the definitions for `command.go.*.py`. If, say, you wanted to press F5 to have SciTE run a python script in Python 3.7, you could change the line to say `command.go.*.py=C:\python37\pythonw -u "$(FileNameExt)"`

### More details

```
There are two main ways you can tell SciTE which properties files to load.

1) 
# (SciTE uses this by default)
# in SciTEGlobal.properties,
imports.exclude=(a list of properties files to skip)
# Import all the language specific properties files in this directory
import *

2) 
# an explicit list of what to import.
# in SciTEGlobal.properties,
import myprop1
import myprop2
# etc.
# the line import myprop1
# looks for a file named myprop1.properties and loads it
# with this approach, relative directories can be used
# if this approach is used, to install a properties file you'll have to add a line
# import mypropfile
# to begin using the file mypropfile.properties

Here are some examples of how autocomplete and calltip can be configured,

# if you hit ctrl-space and there is only one word that would match,
# should we skip showing the menu and just insert that word?
autocomplete.cpp.choose.single=0

# is matching case sensitive?
autocomplete.cpp.ignorecase=0

# enable calltips that contain more than one line of information, using \n. recommended.
calltip.cpp.use.escapes=1

# automatically start autocompletion when this character is typed, see below
autocomplete.cpp.start.characters=

# which characters can be part of a word?
calltip.cpp.word.characters=$(chars.alpha)$(chars.numeric)_

# which character starts a list of parameters (e.g. what starts a function call)
calltip.cpp.parameters.start=(

# which character separates a list of parameters (e.g. within a function call)
calltip.cpp.parameters.separators=,

# is matching case sensitive?
calltip.cpp.ignorecase=0

# ending character
calltip.cpp.parameters.end=)
calltip.cpp.end.definition=)

# for example, calltips for html and css could be,
autocomplete.hypertext.ignorecase=1
calltip.hypertext.ignorecase=1
calltip.hypertext.word.characters=_$(chars.alpha)$(chars.numeric)$:>
calltip.hypertext.end.definition=) 
calltip.css.word.characters=-$(chars.alpha)$(chars.numeric)
calltip.css.parameters.start=:
calltip.css.parameters.end=
calltip.css.parameters.separators=|

A tip when writing a .api file:
If the language has function calls from a namespace, such as "File.WriteAllText()",
it might be better for the api file to have two entries for each function,
one entry to autocomplete the method,
File.WriteAllText
and another entry for the calltip,
WriteAllText(string path, string contents)\n\tDescription: Creates a new file

You can then set start.characters to ".",
autocomplete.(current lexer).start.characters=.
and then when you type "File.", the suggestions will automatically be shown

You can add more than one .api file at a time, e.g.
api.$(file.patterns.cpp)=/path/to/first.api;/path/to/second.api

```

