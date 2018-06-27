
[back](api_files.md)

<a name="how_to_install_api"></a>
### How to install an api file and enable calltips + completion

* As an example, let's set up the api file for the C standard library

* Download [c.api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c.api)

* In Windows, move `c.api` into the directory that contains `SciTE.exe`

* In Linux, move `c.api` into the directory that contains `SciTEGlobal.properties`. This is typically either `/usr/bin/scite` or `/usr/local/bin/scite`

* Open SciTE

* From the Options menu, select Open User Options File

* Add the line `api.$(file.patterns.cpp)=$(SciteDefaultHome)/c_withdoc.api`

* Add the line `calltip.cpp.use.escapes=1`

    * This will enable calltips that contain more than one line of information, using \n

* Save this file and restart SciTE

* In SciTE, create and open a new file called "test.c"

* Calltips

    * Type the text "fputs("
    
    * As soon as you press (, a calltip appears, showing a description of fputs
    
* Completion

    * On an empty line, type the text "fp" and press Ctrl+Space
    
    * A listbox appears allowing you to choose between fprintf, fputc, and fputs
    
    * You can use the arrow keys can navigate this box and Enter to choose an item from this box
