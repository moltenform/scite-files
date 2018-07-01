
[back](api_files.md)

<a name="how_to_install_properties"></a>
### How to install a properties file

* A ".properties" file can change colors and fonts, specify lists of keywords, define what action to take on "Compile" and "Go", map file extensions to a programming language, and more

* If a language doesn't have built-in support from SciTE, you might be able to find a `.properties` file for the language in the list [here](api_files.md)

* In recent versions of SciTE, to install a properties file,

    * In Windows, move the .properties file into the directory that contains SciTE.exe
    * In Linux, move the .properties file into the directory that contains SciTEGlobal.properties. This is typically either `/usr/bin/scite` or `/usr/local/bin/scite`

### Advanced details

```
If you would like to know more details about telling SciTE to load a properties file,
There are two main ways you can tell SciTE which properties files to load.

1) 
# in SciTEGlobal.properties,
imports.exclude=(a list of properties files to skip)
# Import all the language specific properties files in this directory
import *
# (SciTE uses this by default)

2) 
# an explicit list.
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

```

