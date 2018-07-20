
## How to add SciTE features with Lua

by Ben Fisher, 2018. First, here is a step-by-step guide to get started.

* download SciTE

* open the directory that contains SciTE. In Linux, this is typically /usr/bin/scite

* create a subdirectory called "scripts"

* create a new file in the "scripts" directory called "example.lua"

* enter the following text into example.lua,

```
print('moving to the start')
editor:GotoPos(0)
```

* open SciTE

* from the Options menu, choose open User Options File, this will open a file called SciTEUser.properties

* add the following lines to SciTEUser.properties

```
command.name.9.*=my lua example
command.mode.9.*=subsystem:lua,savebefore:no
command.9.*=dofile $(SciteDefaultHome)/scripts/example.lua
```

* create a new file in SciTE and type a few words. In the Tools menu, you should now see "my lua example". If you click "my lua example" from the Tools menu, it will run our lua script. The text "moving to the start" will show in the output pane on the right, and the current position will be sent back to the beginning of the document, as if you had hit the Home key, because our script told SciTE to `GotoPos` 0.

## More info about .properties files

In a .properties file, you can specify a "command". A command can run a program, open a file, or in our case, run a lua script.

In the line

```
command.name.9.*=my lua example
```

The \* symbol represents which file extension(s) that the command applies to. If the lines were changed to command.9.\*.py, then the command would only be active when SciTE was editing a .py file. A plain \* means that the command is active for every file type.

The number 9 represents the command number. For example, if you were to add a new script, you could add lines in the form `command.name.8.*=...` or `command.name.10.*=...` as long as you aren't using 9 again.

If the command is between 1 and 9, command 1 can be started by pressing Ctrl-1, 2 by Ctrl-2, and so on. So, we can run our example by pressing Ctrl-9.

You can also specify your own keyboard shortcut for the command, for example by adding the line: `command.shortcut.9.*=Ctrl+Shift+J`

You can add a command to the context menu (the menu that appears on right-click) by adding a line like the following: `user.context.menu=my lua example|1109|` (We type 1109 because this is the sum of 1100 (the first tool command) and 9 (the tool command number we want to run)).

## Installing someone else's Lua script

How to install a Lua script, for example, one of the scripts listed on the [helpers](../../helpers.md) page. In this example we are setting up gusnan's switch-from-cpp-to-header script.

* perform the steps in the first section above to set up "my lua example".

* download [swapheader.lua](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/swapheader.lua)

* place `swapheader.lua` into the `scripts` directory mentioned earlier.

* from the Options menu, choose open User Options File, this will open a file called SciTEUser.properties

* add the following lines to SciTEUser.properties

```
command.name.20.*=Swap C / Header
command.20.*=dofile $(SciteDefaultHome)/scripts/swapheader.lua
command.subsystem.20.*=3
command.mode.20.*=savebefore:no
command.shortcut.20.*=F11
```

* Now, if you are writing C code, you can press F11 to switch between myfile.c and myfile.h

(Some scripts use "extman" to register for events. Or, if the script has code like `AddEventHandler('OnOpen', ...)`, this can be replaced with `require('extman') ... scite_OnOpen(...)` Refer to the "Register for events" section below.)


## Writing Lua code

Scripts are written in the Lua language. 

I've written a small wrapper script to make it easier to direct SciTE from Lua. 

* perform the steps in the first section above to set up "my lua example".

* download [downpoured_scite_utils.lua](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/downpoured_scite_utils.lua)

* place `downpoured_scite_utils.lua` into the `scripts` directory mentioned earlier.

* Open the `example.lua` file that was created earlier, and change it to read

```
require('scripts/downpoured_scite_utils')

-- printing to the output pane without a newline
ScApp:Trace('a')
ScApp:Trace('b')
ScOutput:PaneAppend('a')
ScOutput:PaneAppend('b')

-- getting/setting SciTE properties
print('\n current value of find.use.strip = '..ScApp:GetProperty('find.use.strip'))
ScApp:SetProperty('find.use.strip', '0')

-- opening a new document
ScApp:menunew()
require('scripts/downpoured_scite_utils') -- remember to re-import after changing document

-- adding text to the document
ScEditor:PaneWrite('abcdefg')

-- set selection
ScEditor:SetSel(2,5)
print('sel starts at ' .. ScEditor:GetSelectionStart())
print('sel ends at ' .. ScEditor:GetSelectionEnd())
print('selected text is ' .. tostring(ScEditor:GetSelText()))
print('length of this line is ' .. ScEditor:LineLength(0))
ScEditor:DocumentEnd()

-- highlight chars 2 to 5
local red_underline = 2
local prev_indic = ScEditor:GetIndicatorCurrent()
ScEditor:SetIndicatorCurrent(red_underline)
ScEditor:IndicatorFillRange(2, 3)
ScEditor:SetIndicatorCurrent(prev_indic)

```

Open SciTE, go the Tools menu, and choose "my lua example", and the code will run. Some of the letters will now have a red underline, as an example of what scripts can do.

[Full api for downpoured_scite_utils](downpoured_scite_utils_api.md)

Note that whenever a different document is opened, lua's global state is reset. This is why after any call to `ScApp:OpenFile` or `ScApp:menunew`, you need to `require` all script dependencies again.

Lua's builtin `os.execute` function can be used to run an external program. (In Windows, though, os.execute sometimes briefly shows a flash of cmd.exe instance on the screen, which looks distracting. A solution to this is the [scite_lua_startprocess](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_lua_startprocess.zip) helper.) 

Lua's standard library is limited. One way to add features is to write a C extension, like the aforementioned lua\_startprocess. Another option is to use my fork of SciTE, [SciTE-with-Python](https://github.com/downpoured/scite-with-python), that uses Python in place of Lua because of Python's much larger standard library and ecosystem, and comes with many [plugins](https://github.com/downpoured/scite-with-python/wiki/Features). Lua code can be run when SciTE starts up by adding code to the 'lua startup script'; see the next example.

## Register for events

A lua script can also listen for events in SciTE and run code when the event is triggered. Here is an example of how to configure this:

* perform the steps in the "Writing Lua code" section above.

* download [extman](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/extman.zip), unzip it, and place extman.lua into the "scripts" directory that you created earlier. (unlike other extman scripts, this version of extman won't automatically search for and run all lua scripts).

* from the Options menu, choose open User Options File, this will open a file called SciTEUser.properties

* add the following line to SciTEUser.properties

```
ext.lua.startup.script=$(SciteDefaultHome)/scripts/startup.lua
```

* save changes to SciTEUser.properties and restart SciTE. from the Options menu, choose open User Options File, choose "Open lua startup script". This will make a file called startup.lua.

* add the following lines to startup.lua

```
require('scripts/extman')
require('scripts/downpoured_scite_utils')

local function notifyWhenTextFileOpened(filename)
    if stringendswith(filename, '.txt') then
        print('opening a text file ' .. filename)
    end
end

local function typingCapitalWTypesAnAInstead(key, shift, ctrl, alt)
    if key == string.byte('W') and shift and not ctrl and not alt then
        ScEditor:PaneWrite('A')
        return true -- stop normal handling
    end
end

scite_OnOpen(notifyWhenTextFileOpened)
scite_OnKey(typingCapitalWTypesAnAInstead)
```

* Save changes to startup.lua and restart SciTE

* Now, when you open a \.txt file, you'll see the message, and when you type W, it makes an A instead.

* Note that the line `return true` is what causes the normal event handling to be stopped; without this line, the W might still appear.

(What does "extman" do? SciTE only allows one handler for a lua event, extman dispatches the event to any number of callers, allowing different lua scripts to both be notified of the same event.) Other events that can be registered in extman are:

| function to register for an event |  |
| ------------- | ------------- |
| scite_OnMarginClick(fn) | provide a callback function that recieves no parameters  |
| scite_OnDoubleClick(fn) | provide a callback function that recieves no parameters  |
| scite_OnSavePointLeft(fn) | provide a callback function that recieves no parameters  |
| scite_OnSavePointReached(fn) | provide a callback function that recieves no parameters  |
| scite_OnChar(fn) | provide a callback function that one parameter "char"  |
| scite_OnSave(fn) | provide a callback function that one parameter "filename"  |
| scite_OnBeforeSave(fn) | provide a callback function that one parameter "filename"  |
| scite_OnSwitchFile(fn) | provide a callback function that one parameter "filename"  |
| scite_OnOpen(fn) | provide a callback function that one parameter "filename"  |
| scite_OnUpdateUI(fn) | provide a callback function that recieves no parameters  |
| scite_OnKey(fn) | provide a callback function that recieves 4 parameters (key,shift,ctrl,alt) |
| scite_OnDwellStart(fn) | provide a callback function that recieves 2 parameters (pos,string) |
| scite_OnClose(fn) | provide a callback function that recieves no parameters  |
| scite_OnStyle(fn) | provide a callback function that recieves one parameter  |
| scite_OnStrip(fn) | provide a callback function that recieves 2 parameters (controlNum, eventType)  |

## Adding a UI ("user strip") for your lua script

* perform the steps in the "Register for events" section above

* open SciTE

* from the Options menu, choose open User Options File, this will open a file called SciTEUser.properties

* add the following lines to SciTEUser.properties

```
command.name.8.*=my gui example
command.mode.8.*=subsystem:lua,savebefore:no
command.8.*=dofile $(SciteDefaultHome)/scripts/userstrip_example.lua
```

* create a file in the `scripts` directory called `userstrip_example.lua`, and add the following code:

```
require('scripts/extman')
require('scripts/downpoured_scite_utils')
ScToolUIManager:RegisterEventWithExtman()

ExampleUIClass = inheritsFrom(ScToolUIBase)
function ExampleUIClass:AddControls()
    local callbackOk = function() self:OnOK() end
    local callbackGo = function() self:OnGo() end
    self:AddLabel('A label')
    self.idCombo = self:AddCombo()
    self.idBtnGo = self:AddButton('Go', callbackGo)
    self:AddRow()
    self:AddLabel('Name:')
    self.idEntry = self:AddEntry('default name')
    self:AddButton('OK', callbackOk, true, true)
    self:AddButton('Cancel', nil, true, false)
end

function ExampleUIClass:OnOpen()
    self:SetList(self.idCombo, 'pear\nlemon\norange')
    self:Set(self.idEntry, 'default name')
    self:Set(self.idCombo, 'default food')
end
    
function ExampleUIClass:OnGo()
    print('clicked Go, val='.. self:Get(self.idCombo) ..', entry='.. self:Get(self.idEntry))
end
    
function ExampleUIClass:OnOK()
    print('clicked OK, val='.. self:Get(self.idCombo) ..', entry='.. self:Get(self.idEntry))
end

local instance = ExampleUIClass:create()
instance:Init()
instance:Show()

```

* Save and restart SciTE

* create a new file in SciTE and type a few words. In the Tools menu, you should now see "my gui example". If you click "my gui example" from the Tools menu, the user strip ui should appear at the bottom of the window, and you can now interact by clicking the buttons.

* if you click ok or cancel, the ui will close.

Further documentation for user strip: To use downpoured_scite_utils to show user strip UI, create a class that inherits from ScToolUIBase, as seen in the example. Then, the following methods are available:

| Method |  |
| ------------- | ------------- |
| instance:Show() | show the user strip  |
| instance:Close() | close the user strip  |
| instance:AddControls() | override this method to draw your ui  |
| instance:OnOpen() | override this method to do setup, e.g. setting default values |
| instance:AddLabel(text) | add a label. returns id for this control; should only be called inside the AddControls() method.  |
| instance:AddButton(text, callback, closes, default) | add a button, and callback when button is clicked. if `closes` is true, button will close the user strip. if `default` is true, the button will have a "default" style with thicker border. returns id for this control; should only be called inside the AddControls() method. |
| instance:AddCombo() | add a combo box. use setlist() at a later time to fill with content. returns id for this control; should only be called inside the AddControls() method. |
| instance:AddEntry() | add a text entry box. use set() at a later time to fill with content. returns id for this control; should only be called inside the AddControls() method. |
| instance:AddRow() | add new row. |
| instance:Get(controlId) | get current value inside a combo box or text entry box  |
| instance:Set(controlId, val) | set current value inside a combo box or text entry box  |
| instance:SetList(controlId, val) | set options in a combo box, value delimited by \n newlines  |
| instance:OnEvent(controlId, eventType) | (optional) you can override this method to receive low-level events. eventType is usually one of the following: self.eventTypeClicked, self.eventTypeChange, self.eventTypeFocusIn, or self.eventTypeFocusOut  |

(If you have questions or comments about the information here, I can be contacted at scitewiki at gmail dot com.)

