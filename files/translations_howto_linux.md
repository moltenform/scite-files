
<a name="how_to_install_translation_linux"></a>
### How to install a translation (Linux)

* View the list of translations [here](translations_list.md).

* Right-click one of the links and choose "Save link as..." or "Save target as..."

    * <a href="#">![Screenshot right-click link](https://raw.githubusercontent.com/moltenjs/scite-files/master/files/translations_install_linux_right.png)</a>

* Save to a writable directory, such as ~/Downloads.

    * <a href="#">![Screenshot save to downloads](https://raw.githubusercontent.com/moltenjs/scite-files/master/files/translations_install_linux_path.png)</a>

* Open a terminal, and using sudo, move the file to `/usr/share/scite/locale.properties`

    * <a href="#">![Screenshot save to downloads](https://raw.githubusercontent.com/moltenjs/scite-files/master/files/translations_install_linux_terminal.png)</a>

* (Note that the destination filename is locale.properties). If `/usr/share/scite` does not exist, try `/usr/local/share/scite`. 

* Re-open SciTE, and the menus and dialogs will show translated text

* (In summary, the name of the file must be locale.properties and should be placed in the same directory as SciTEGlobal.properties)

[back](translations.md)
