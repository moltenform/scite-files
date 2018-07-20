
[back](../../helpers.md)

Open `SciTEGlobal.properties`, and add the following lines,

```
ext.lua.startup.script=$(SciteDefaultHome)/see_ascii_selection.lua

#print selection info
command.33.*=PrintSelectionInfo
command.subsystem.33.*=3
command.mode.33.*=savebefore:no
command.shortcut.33.*=F1

# User defined key commands
user.shortcuts=\
F1|1133|\
Ctrl+Shift+V|IDM_PASTEANDDOWN|\
Ctrl+PageUp|IDM_PREVFILE|\
Ctrl+PageDown|IDM_NEXTFILE|
```

Create a file called `see_ascii_selection.lua` in the SciTE directory with the contents,

```
function PrintSelectionInfo()
   local sel = editor:GetSelText()
   print(#sel..' chars selected')
   print(table.concat({sel:byte(1,-1)},','))
end
```

Now you can press F1 to see ASCII codes of symbols under selection while editing any file in SciTE.

Based on a script by Egor Skriptunoff written [here](https://stackoverflow.com/questions/21603285/scite-lua-scripting-extension-api-beginner).
