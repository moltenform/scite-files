
[back to "adding scite features with lua"](adding_scite_features_with_lua.md)

## API 

API for [downpoured_scite_utils.lua](https://raw.githubusercontent.com/moltenjs/scite-files/master/files/files/helpers/downpoured_scite_utils.lua), by Ben Fisher.

| ScApp methods |  |
| ------------- | ------------- |
| ScApp:Trace(s) | Print to the output pane |
| ScApp:OpenFile(filename) | Open a file (will reset lua's state, remember to require() dependencies again) |
| ScApp:GetProperty(propname) | Returns value of property |
| ScApp:SetProperty(propname, val) | Set value of property |
| ScApp:UnsetProperty(propname) | Unset property |
| ScApp:GetFilePath() | Returns full file path |
| ScApp:GetFileName() | Returns file name |
| ScApp:GetFileDirectory() | Returns directory of file |
| ScApp:GetSciteDirectory() | Returns SciTE location |
| ScApp:GetSciteUserDirectory() | Returns SciTE user dir location |
| ScApp:RunToolCmd(n) | Run a command |
| ScApp:MakeColor(r,g,b) | Pack colors into an integer, to use with ScEditor:methods that use an integer to represent color |
| ScApp:GetColor(n) | Returns tuple r,g,b. Unpack colors from an integer, to use with ScEditor:methods that use an integer to represent color |
| ScApp:abbrev() | Expand Abbreviation | 
| ScApp:about() | About SciTE | 
| ScApp:activate() | Activate | 
| ScApp:allowaccess() |  | 
| ScApp:block_comment() | Block Comment or Uncomment | 
| ScApp:bookmark_clearall() | Clear All Bookmarks | 
| ScApp:bookmark_next() |  | 
| ScApp:bookmark_next_select() | Select to next bookmark | 
| ScApp:bookmark_prev() |  | 
| ScApp:bookmark_prev_select() | Select to prev bookmark | 
| ScApp:bookmark_select_all() |  | 
| ScApp:bookmark_toggle() |  | 
| ScApp:box_comment() | Box Comment | 
| ScApp:buffer() |  | 
| ScApp:buffersep() |  | 
| ScApp:build() |  | 
| ScApp:clean() |  | 
| ScApp:clear() |  | 
| ScApp:clearoutput() |  | 
| ScApp:close() |  | 
| ScApp:closeall() |  | 
| ScApp:compile() |  | 
| ScApp:complete() | Complete Symbol | 
| ScApp:completeword() | Complete Word | 
| ScApp:copy() |  | 
| ScApp:copyasrtf() |  | 
| ScApp:copypath() |  | 
| ScApp:cut() |  | 
| ScApp:directiondown() |  | 
| ScApp:directionup() |  | 
| ScApp:duplicate() |  | 
| ScApp:encoding_default() | Code Page Property | 
| ScApp:encoding_ucookie() | UTF-8 | 
| ScApp:encoding_ucs2be() | UTF-16 Big Endian | 
| ScApp:encoding_ucs2le() | UTF-16 Little Endian | 
| ScApp:encoding_utf8() | UTF-8 with BOM | 
| ScApp:enterselection() |  | 
| ScApp:eol_convert() | Convert Line End Characters | 
| ScApp:eol_cr() |  | 
| ScApp:eol_crlf() |  | 
| ScApp:eol_lf() |  | 
| ScApp:expand() | Toggle current fold | 
| ScApp:expand_ensurechildrenvisible() | Ensure children visible | 
| ScApp:filer() |  | 
| ScApp:find() |  | 
| ScApp:findinfiles() |  | 
| ScApp:findnext() |  | 
| ScApp:findnextback() |  | 
| ScApp:findnextbacksel() | Find prev and select what is found | 
| ScApp:findnextsel() | Find next and select what is found | 
| ScApp:finishedexecute() |  | 
| ScApp:foldmargin() |  | 
| ScApp:fullscreen() |  | 
| ScApp:go() |  | 
| ScApp:dlg_goto() |  | 
| ScApp:help() | Help | 
| ScApp:help_scite() | SciTE Help | 
| ScApp:import() |  | 
| ScApp:incsearch() |  | 
| ScApp:ins_abbrev() | Insert Abbreviation | 
| ScApp:join() |  | 
| ScApp:language() |  | 
| ScApp:linenumbermargin() |  | 
| ScApp:linereverse() |  | 
| ScApp:loadsession() |  | 
| ScApp:lwrcase() | Make Selection Lowercase | 
| ScApp:matchbrace() |  | 
| ScApp:matchcase() |  | 
| ScApp:monofont() | Use Monospaced Font | 
| ScApp:movetableft() |  | 
| ScApp:movetabright() |  | 
| ScApp:mrufile() |  | 
| ScApp:mru_sep() |  | 
| ScApp:mru_sub() |  | 
| ScApp:menunew() |  | 
| ScApp:nextfile() |  | 
| ScApp:nextfilestack() |  | 
| ScApp:nextmatchppc() | Go to next preprocessor section | 
| ScApp:nextmsg() |  | 
| ScApp:ontop() | Always On Top | 
| ScApp:open() |  | 
| ScApp:openabbrevproperties() | Open Abbreviations File | 
| ScApp:opendirectoryproperties() | Open Directory Options File | 
| ScApp:openfileshere() | Open Files Here | 
| ScApp:openglobalproperties() | Open Global Options File | 
| ScApp:openlocalproperties() | Open Local Options File | 
| ScApp:openluaexternalfile() | Open Lua Startup Script | 
| ScApp:openselected() | Open Selected Filename | 
| ScApp:openuserproperties() | Open User Options File | 
| ScApp:paste() |  | 
| ScApp:pasteanddown() |  | 
| ScApp:prevfile() |  | 
| ScApp:prevfilestack() |  | 
| ScApp:prevmatchppc() | Go to prev preprocessor section | 
| ScApp:prevmsg() | Previous Message in output pane | 
| ScApp:menuprint() |  | 
| ScApp:printsetup() |  | 
| ScApp:quit() |  | 
| ScApp:readonly() |  | 
| ScApp:redo() |  | 
| ScApp:regexp() |  | 
| ScApp:replace() |  | 
| ScApp:revert() |  | 
| ScApp:runwin() |  | 
| ScApp:save() |  | 
| ScApp:saveacopy() |  | 
| ScApp:saveall() |  | 
| ScApp:saveas() |  | 
| ScApp:saveashtml() |  | 
| ScApp:saveaspdf() |  | 
| ScApp:saveasrtf() |  | 
| ScApp:saveastex() |  | 
| ScApp:saveasxml() |  | 
| ScApp:savesession() |  | 
| ScApp:selectall() |  | 
| ScApp:selectionaddeach() |  | 
| ScApp:selectionaddnext() |  | 
| ScApp:selection_for_find() |  | 
| ScApp:selecttobrace() |  | 
| ScApp:selecttonextmatchppc() |  | 
| ScApp:selecttoprevmatchppc() |  | 
| ScApp:selmargin() |  | 
| ScApp:showcalltip() |  | 
| ScApp:split() |  | 
| ScApp:splitvertical() |  | 
| ScApp:srcwin() |  | 
| ScApp:statuswin() |  | 
| ScApp:stopexecute() |  | 
| ScApp:stream_comment() |  | 
| ScApp:switchpane() |  | 
| ScApp:tabsize() |  | 
| ScApp:tabwin() |  | 
| ScApp:toggleoutput() |  | 
| ScApp:toggleparameters() |  | 
| ScApp:toggle_foldall() |  | 
| ScApp:toggle_foldrecursive() |  | 
| ScApp:tools() |  | 
| ScApp:toolwin() |  | 
| ScApp:undo() |  | 
| ScApp:unslash() |  | 
| ScApp:uprcase() | Make Selection Uppercase | 
| ScApp:vieweol() | View End of Line | 
| ScApp:viewguides() |  | 
| ScApp:viewspace() |  | 
| ScApp:viewstatusbar() |  | 
| ScApp:viewtabbar() |  | 
| ScApp:viewtoolbar() |  | 
| ScApp:wholeword() |  | 
| ScApp:wrap() |  | 
| ScApp:wraparound() |  | 
| ScApp:wrapoutput() |  | 

| User strip api | |
| ------------- | ------------- |
| see the example near the end of the document [here](adding_scite_features_with_lua.md) | |

ScOutput can also be used in place of ScEditor:for any of the following, if you want the action to take place on the output pane.

| Basics  |  |
| ------------- | ------------- |
| ScEditor:PaneWrite(string txt, int pos=None) | Write text at the current position, and update selection. Typically the most useful method. |
| string ScEditor:Utils.GetEolCharacter() | Return current EOL character, e.g. \\r\\n |
| ScEditor:PaneInsertText(string txt, int pos) | Insert text, without changing selection |
| ScEditor:PaneAppend(string txt) | Append text |
| ScEditor:PaneRemoveText(int pos1, int pos2) | Remove text between these positions |
| ScEditor:PaneGetTextRange(int pos1, int pos2) | Get text between these positions |
| int,int ScEditor:PaneFindText(string s, int pos1=0, int pos2=-1, wholeWord=False, matchCase=False, regExp=False, flags=0) | Find text |
| string ScEditor:GetLineText(int line) | Returns text of specified line |
| string ScEditor:GetSelectedText() | Returns selected text |


| Text retrieval and modification  |  |
| ------------- | ------------- |
| ScEditor:AddText(string text) | Add text to the document at current position. |
| ScEditor:Allocate(int bytes) | Enlarge the document to a particular size of text bytes. |
| int ScEditor:AllocateExtendedStyles(int numberStyles) | Allocate some extended (&gt;255) style numbers and return the start of the range |
| ScEditor:AppendText(string text) | Append a string to the end of the document without changing the selection. |
| ScEditor:ChangeInsertion(string text) | Change the text that is being inserted in response to SC\_MOD\_INSERTCHECK |
| ScEditor:ClearAll() | Delete all text in the document. |
| ScEditor:ClearDocumentStyle() | Set all style bytes to 0, remove all folding information. |
| ScEditor:DeleteRange(int pos, int deleteLength) | Delete a range of text in the document. |
| string,int ScEditor:EncodedFromUTF8(string utf8) | Translates a UTF8 string into the document encoding. Return the length of the result in bytes. On error return 0. |
| int ScEditor:GetCharAt(int pos) |  Returns the character byte at the position. |
| string ScEditor:GetCurrentLineText() | Returns text of current line |
| string,int ScEditor:GetLine(int line) | Retrieve the contents of a line. Returns the length of the line. |
| bool ScEditor:GetReadOnly() |  In read-only mode? |
| int ScEditor:GetStyleAt(int pos) |  Returns the style byte at the position. |
| string,int ScEditor:GetText() | Retrieve all the text in the document. Returns number of characters retrieved.  |
| ScEditor:InsertText(int pos, string text) | Insert string at a position. |
| string ScEditor:PaneGetText(int pos1, int pos2) | Get text between these positions |
| ScEditor:ReleaseAllExtendedStyles() | Release all extended (&gt;255) style numbers |
| ScEditor:ReplaceSel(string text) | Replace the selected text with the argument text. |
| ScEditor:SetLengthForEncode(int bytes) | Set the length of the utf8 argument for calling EncodedFromUTF8. Set to -1 and the string will be measured to the first nul. |
| ScEditor:SetReadOnly(bool value) |  Set to read only or read write. |
| ScEditor:SetSavePoint() | Remember the current position in the undo history as the position at which the document was saved. |
| ScEditor:SetText(string text) | Replace the contents of the document with the argument text. |
| string,int ScEditor:TargetAsUTF8() | Returns the target converted to UTF8. Return the length in bytes. |


| Searching  |  |
| ------------- | ------------- |
| int ScEditor:GetSearchFlags() |  Get the search flags used by SearchInTarget. |
| string ScEditor:GetTag(int tagNumber) |  Retrieve the value of a tag from a regular expression search.  |
| int ScEditor:GetTargetEnd() |  Get the position that ends the target. |
| int ScEditor:GetTargetStart() |  Get the position that starts the target. |
| string ScEditor:GetTargetText() |  Retrieve the text in the target. |
| int ScEditor:ReplaceTarget(string text) | Replace the target text with the argument text. Text is counted so it can contain NULs. Returns the length of the replacement text. |
| int ScEditor:ReplaceTargetRE(string text) | Replace the target text with the argument text after \\d processing. Text is counted so it can contain NULs. Looks for \\d where d is between 1 and 9 and replaces these with the strings matched in the last search operation which were surrounded by \\( and \\). Returns the length of the replacement text including any change caused by processing the \\d patterns. |
| ScEditor:SearchAnchor() | Sets the current caret position to be the search anchor. |
| int ScEditor:SearchInTarget(string text) | Search for a counted string in the target and set the target to the found range. Text is counted so it can contain NULs. Returns length of range or -1 for failure in which case target is not moved. |
| int ScEditor:SearchNext(int flags, string text) | Find some text starting at the search anchor. Does not ensure the selection is visible. |
| int ScEditor:SearchPrev(int flags, string text) | Find some text starting at the search anchor and moving backwards. Does not ensure the selection is visible. |
| ScEditor:SetSearchFlags(int value) |  Set the search flags used by SearchInTarget. |
| ScEditor:SetTargetEnd(int value) |  Sets the position that ends the target which is used for updating the document without affecting the scroll position. |
| ScEditor:SetTargetRange(int start, int end) | Sets both the start and end of the target in one call. |
| ScEditor:SetTargetStart(int value) |  Sets the position that starts the target which is used for updating the document without affecting the scroll position. |
| ScEditor:TargetFromSelection() | Make the target range start and end be the same as the selection range start and end. |
| ScEditor:TargetWholeDocument() | Sets the target to the whole document. |


| Overtype  |  |
| ------------- | ------------- |
| bool ScEditor:GetOvertype() |  Returns true if overtype mode is active otherwise false is returned. |
| ScEditor:SetOvertype(bool value) |  Set to overtype (true) or insert mode. |


| Cut, copy and paste  |  |
| ------------- | ------------- |
| bool ScEditor:CanPaste() | Will a paste succeed? |
| ScEditor:Clear() | Clear the selection. |
| ScEditor:Copy() | Copy the selection to the clipboard. |
| ScEditor:CopyAllowLine() | Copy the selection, if selection empty copy the line with the caret |
| ScEditor:CopyRange(int start, int end) | Copy a range of text to the clipboard. Positions are clipped into the document. |
| ScEditor:CopyText(string text) | Copy argument text to the clipboard. |
| ScEditor:Cut() | Cut the selection to the clipboard. |
| bool ScEditor:GetPasteConvertEndings() |  Get convert-on-paste setting |
| ScEditor:Paste() | Paste the contents of the clipboard into the document replacing the selection. |
| ScEditor:SetPasteConvertEndings(bool value) |  Enable/Disable convert-on-paste for line endings |
| string ScEditor:Utils.GetClipboardText() | Get clipboard text (not available on all platforms) |
| ScEditor:Utils.SetClipboardText(s) | Set clipboard text |


| Undo and Redo  |  |
| ------------- | ------------- |
| ScEditor:AddUndoAction(int token, int flags) | Add a container action to the undo stack |
| ScEditor:BeginUndoAction() | Start a sequence of actions that is undone and redone as a unit. May be nested. |
| bool ScEditor:CanRedo() | Are there any redoable actions in the undo history? |
| bool ScEditor:CanUndo() | Are there any undoable actions in the undo history? |
| ScEditor:EmptyUndoBuffer() | Delete the undo history. |
| ScEditor:EndUndoAction() | End a sequence of actions that is undone and redone as a unit. |
| bool ScEditor:GetUndoCollection() |  Is undo history being collected? |
| ScEditor:Redo() | Redoes the next action on the undo history. |
| ScEditor:SetUndoCollection(bool value) |  Choose between collecting actions into the undo history and discarding them. |
| ScEditor:Undo() | Undo one action in the undo history. |


| Selection and information  |  |
| ------------- | ------------- |
| int ScEditor:CharPositionFromPoint(int x, int y) | Find the position of a character from a point within the window. |
| int ScEditor:CharPositionFromPointClose(int x, int y) | Find the position of a character from a point within the window. Return INVALID\_POSITION if not close to text. |
| ScEditor:ChooseCaretX() | Set the last x chosen value to be the caret x position. |
| int ScEditor:CountCharacters(int startPos, int endPos) | Count characters between two positions. |
| int ScEditor:FindColumn(int line, int column) | Find the position of a column on a line taking into account tabs and multi-byte characters. If beyond end of line, return line end position. |
| int ScEditor:GetAnchor() |  Returns the position of the opposite end of the selection to the caret. |
| int ScEditor:GetColumn(int pos) |  Retrieve the column number of a position, taking tab width into account. |
| string,int ScEditor:GetCurLine() | Retrieve the text of the line containing the caret. Returns the index of the caret on the line.  |
| int ScEditor:GetCurrentPos() |  Returns the position of the caret. |
| int ScEditor:GetLength() |  Returns the number of bytes in the document. |
| int ScEditor:GetLineCount() |  Returns the number of lines in the document. There is always at least one. |
| int ScEditor:GetLineEndPosition(int line) |  Get the position after the last visible characters on a line. |
| int ScEditor:GetLineSelEndPosition(int line) | Retrieve the position of the end of the selection at the given line (INVALID\_POSITION if no selection on this line). |
| int ScEditor:GetLineSelStartPosition(int line) | Retrieve the position of the start of the selection at the given line (INVALID\_POSITION if no selection on this line). |
| int ScEditor:GetLinesOnScreen() |  Retrieves the number of lines completely visible. |
| bool ScEditor:GetModify() |  Is the document different from when it was last saved? |
| bool ScEditor:GetMouseSelectionRectangularSwitch() |  Whether switching to rectangular mode while selecting with the mouse is allowed. |
| string,int ScEditor:GetSelText() | Retrieve the selected text. Return the length of the text.  |
| int ScEditor:GetSelectionEnd() |  Returns the position at the end of the selection. |
| bool ScEditor:GetSelectionIsRectangle() |  Is the selection rectangular? The alternative is the more common stream selection. |
| int ScEditor:GetSelectionMode() |  Get the mode of the current selection. |
| int ScEditor:GetSelectionStart() |  Returns the position at the start of the selection. |
| int ScEditor:GetTextLength() |  Retrieve the number of characters in the document. |
| ScEditor:GotoLine(int line) | Set caret to start of a line and ensure it is visible. |
| ScEditor:GotoPos(int pos) | Set caret to a position and ensure it is visible. |
| ScEditor:HideSelection(bool normal) | Draw the selection in normal style or with selection highlighted. |
| bool ScEditor:IsRangeWord(int start, int end) | Is the range start..end considered a word? |
| int ScEditor:LineFromPosition(int pos) | Retrieve the line containing a position. |
| int ScEditor:LineLength(int line) | How many characters are on a line, including end of line characters? |
| ScEditor:MoveCaretInsideView() | Move the caret inside current view if it's not there already. |
| ScEditor:MoveSelectedLinesDown() | Move the selected lines down one line, shifting the line below before the selection |
| ScEditor:MoveSelectedLinesUp() | Move the selected lines up one line, shifting the line above after the selection |
| int ScEditor:PointXFromPosition(int pos) | Retrieve the x value of the point in the window where a position is displayed. |
| int ScEditor:PointYFromPosition(int pos) | Retrieve the y value of the point in the window where a position is displayed. |
| int ScEditor:PositionAfter(int pos) | Given a valid document position, return the next position taking code page into account. Maximum value returned is the last position in the document. |
| int ScEditor:PositionBefore(int pos) | Given a valid document position, return the previous position taking code page into account. Returns 0 if passed 0. |
| int ScEditor:PositionFromLine(int line) | Retrieve the position at the start of a line. |
| int ScEditor:PositionFromPoint(int x, int y) | Find the position from a point within the window. |
| int ScEditor:PositionFromPointClose(int x, int y) | Find the position from a point within the window but return INVALID\_POSITION if not close to text. |
| int ScEditor:PositionRelative(int pos, int relative) | Given a valid document position, return a position that differs in a number of characters. Returned value is always between 0 and last position in document. |
| ScEditor:SelectAll() | Select all the text in the document. |
| ScEditor:SetAnchor(int value) |  Set the selection anchor to a position. The anchor is the opposite end of the selection from the caret. |
| ScEditor:SetCurrentPos(int value) |  Sets the position of the caret. |
| ScEditor:SetEmptySelection(int pos) | Set caret to a position, while removing any existing selection. |
| ScEditor:SetMouseSelectionRectangularSwitch(bool value) |  Set whether switching to rectangular mode while selecting with the mouse is allowed. |
| ScEditor:SetSel(int start, int end) | Select a range of text. |
| ScEditor:SetSelectionEnd(int value) |  Sets the position that ends the selection - this becomes the currentPosition. |
| ScEditor:SetSelectionMode(int value) |  Set the selection mode to stream (SC\_SEL\_STREAM) or rectangular (SC\_SEL\_RECTANGLE/SC\_SEL\_THIN) or by lines (SC\_SEL\_LINES). |
| ScEditor:SetSelectionStart(int value) |  Sets the position that starts the selection - this becomes the anchor. |
| int ScEditor:TextHeight(int line) | Retrieve the height of a particular line of text in pixels. |
| int ScEditor:TextWidth(int style, string text) | Measure the pixel width of some text in a particular style.  Does not handle tab or control characters. |
| ScEditor:Utils.ExpandSelectionToIncludeEntireLines() | Ensure entire lines are selected |
| int ScEditor:WordEndPosition(int pos, bool onlyWordCharacters) | Get position of end of word. |
| int ScEditor:WordStartPosition(int pos, bool onlyWordCharacters) | Get position of start of word. |


| Multiple Selection and Virtual Space  |  |
| ------------- | ------------- |
| int ScEditor:AddSelection(int caret, int anchor) | Add a selection |
| ScEditor:ClearSelections() | Clear selections to a single empty stream selection |
| ScEditor:DropSelectionN(int selection) | Drop one selection |
| colour ScEditor:GetAdditionalCaretFore() |  Get the foreground colour of additional carets. |
| bool ScEditor:GetAdditionalCaretsBlink() |  Whether additional carets will blink |
| bool ScEditor:GetAdditionalCaretsVisible() |  Whether additional carets are visible |
| int ScEditor:GetAdditionalSelAlpha() |  Get the alpha of the selection. |
| bool ScEditor:GetAdditionalSelectionTyping() |  Whether typing can be performed into multiple selections |
| int ScEditor:GetMainSelection() |  Which selection is the main selection |
| int ScEditor:GetMultiPaste() |  Retrieve the effect of pasting when there are multiple selections. |
| bool ScEditor:GetMultipleSelection() |  Whether multiple selections can be made |
| int ScEditor:GetRectangularSelectionAnchor() |  Returns the position at the end of the selection. |
| int ScEditor:GetRectangularSelectionAnchorVirtualSpace() |  Returns the position at the end of the selection. |
| int ScEditor:GetRectangularSelectionCaret() |  Returns the position at the end of the selection. |
| int ScEditor:GetRectangularSelectionCaretVirtualSpace() |  Returns the position at the end of the selection. |
| int ScEditor:GetRectangularSelectionModifier() |  Get the modifier key used for rectangular selection. |
| bool ScEditor:GetSelectionEmpty() |  Is every selected range empty? |
| int ScEditor:GetSelectionNAnchor(int selection) |  Which selection is the main selection |
| int ScEditor:GetSelectionNAnchorVirtualSpace(int selection) |  Which selection is the main selection |
| int ScEditor:GetSelectionNCaret(int selection) |  Which selection is the main selection |
| int ScEditor:GetSelectionNCaretVirtualSpace(int selection) |  Which selection is the main selection |
| int ScEditor:GetSelectionNEnd(int selection) |  Returns the position at the end of the selection. |
| int ScEditor:GetSelectionNStart(int selection) |  Returns the position at the start of the selection. |
| int ScEditor:GetSelections() |  How many selections are there? |
| int ScEditor:GetVirtualSpaceOptions() |  Returns the position at the end of the selection. |
| ScEditor:MultipleSelectAddEach() | Add each occurrence of the main selection in the target to the set of selections. If the current selection is empty then select word around caret. |
| ScEditor:MultipleSelectAddNext() | Add the next occurrence of the main selection to the set of selections as main. If the current selection is empty then select word around caret. |
| ScEditor:RotateSelection() | Set the main selection to the next selection. |
| ScEditor:SetAdditionalCaretFore(colour value) |  Set the foreground colour of additional carets. |
| ScEditor:SetAdditionalCaretsBlink(bool value) |  Set whether additional carets will blink |
| ScEditor:SetAdditionalCaretsVisible(bool value) |  Set whether additional carets are visible |
| ScEditor:SetAdditionalSelAlpha(int value) |  Set the alpha of the selection. |
| ScEditor:SetAdditionalSelBack(colour value) |  Set the background colour of additional selections. Must have previously called SetSelBack with non-zero first argument for this to have an effect. |
| ScEditor:SetAdditionalSelFore(colour value) |  Set the foreground colour of additional selections. Must have previously called SetSelFore with non-zero first argument for this to have an effect. |
| ScEditor:SetAdditionalSelectionTyping(bool value) |  Set whether typing can be performed into multiple selections |
| ScEditor:SetMainSelection(int value) |  Set the main selection |
| ScEditor:SetMultiPaste(int value) |  Change the effect of pasting when there are multiple selections. |
| ScEditor:SetMultipleSelection(bool value) |  Set whether multiple selections can be made |
| ScEditor:SetRectangularSelectionAnchor(int value) |  Returns the position at the end of the selection. |
| ScEditor:SetRectangularSelectionAnchorVirtualSpace(int value) |  Returns the position at the end of the selection. |
| ScEditor:SetRectangularSelectionCaret(int value) |  Returns the position at the end of the selection. |
| ScEditor:SetRectangularSelectionCaretVirtualSpace(int value) |  Returns the position at the end of the selection. |
| ScEditor:SetRectangularSelectionModifier(int value) |  On GTK+, allow selecting the modifier key to use for mouse-based rectangular selection. Often the window manager requires Alt+Mouse Drag for moving windows. Valid values are SCMOD\_CTRL(default), SCMOD\_ALT, or SCMOD\_SUPER. |
| int ScEditor:SetSelection(int caret, int anchor) | Set a simple selection |
| ScEditor:SetSelectionNAnchor(int selection, int value) |  Which selection is the main selection |
| ScEditor:SetSelectionNAnchorVirtualSpace(int selection, int value) |  Which selection is the main selection |
| ScEditor:SetSelectionNCaret(int selection, int value) |  Which selection is the main selection |
| ScEditor:SetSelectionNCaretVirtualSpace(int selection, int value) |  Which selection is the main selection |
| ScEditor:SetSelectionNEnd(int selection, int value) |  Sets the position that ends the selection - this becomes the currentPosition. |
| ScEditor:SetSelectionNStart(int selection, int value) |  Sets the position that starts the selection - this becomes the anchor. |
| ScEditor:SetVirtualSpaceOptions(int value) |  Returns the position at the end of the selection. |
| ScEditor:SwapMainAnchorCaret() | Swap that caret and anchor of the main selection. |


| Scrolling and automatic scrolling  |  |
| ------------- | ------------- |
| bool ScEditor:GetEndAtLastLine() |  Retrieve whether the maximum scroll position has the last line at the bottom of the view. |
| int ScEditor:GetFirstVisibleLine() |  Retrieve the display line at the top of the display. |
| bool ScEditor:GetHScrollBar() |  Is the horizontal scroll bar visible? |
| int ScEditor:GetScrollWidth() |  Retrieve the document width assumed for scrolling. |
| bool ScEditor:GetScrollWidthTracking() |  Retrieve whether the scroll width tracks wide lines. |
| bool ScEditor:GetVScrollBar() |  Is the vertical scroll bar visible? |
| int ScEditor:GetXOffset() |  Get and Set the xOffset (ie, horizontal scroll position). |
| ScEditor:LineScroll(int columns, int lines) | Scroll horizontally and vertically. |
| ScEditor:ScrollCaret() | Ensure the caret is visible. |
| ScEditor:ScrollRange(int secondary, int primary) | Scroll the argument positions and the range between them into view giving priority to the primary position then the secondary position. This may be used to make a search match visible. |
| ScEditor:SetEndAtLastLine(bool value) |  Sets the scroll range so that maximum scroll position has the last line at the bottom of the view (default). Setting this to false allows scrolling one page below the last line. |
| ScEditor:SetFirstVisibleLine(int value) |  Scroll so that a display line is at the top of the display. |
| ScEditor:SetHScrollBar(bool value) |  Show or hide the horizontal scroll bar. |
| ScEditor:SetScrollWidth(int value) |  Sets the document width assumed for scrolling. |
| ScEditor:SetScrollWidthTracking(bool value) |  Sets whether the maximum width line displayed is used to set scroll width. |
| ScEditor:SetVScrollBar(bool value) |  Show or hide the vertical scroll bar. |
| ScEditor:SetVisiblePolicy(int visiblePolicy, int visibleSlop) | Set the way the display area is determined when a particular line is to be moved to by Find, FindNext, GotoLine, etc. |
| ScEditor:SetXCaretPolicy(int caretPolicy, int caretSlop) | Set the way the caret is kept visible when going sideways. The exclusion zone is given in pixels. |
| ScEditor:SetXOffset(int value) |  Get and Set the xOffset (ie, horizontal scroll position). |
| ScEditor:SetYCaretPolicy(int caretPolicy, int caretSlop) | Set the way the line the caret is on is kept visible. The exclusion zone is given in lines. |


| White space  |  |
| ------------- | ------------- |
| int ScEditor:GetExtraAscent() |  Get extra ascent for each line |
| int ScEditor:GetExtraDescent() |  Get extra descent for each line |
| int ScEditor:GetViewWS() |  Are white space characters currently visible? Returns one of SCWS\_\* constants. |
| int ScEditor:GetWhitespaceSize() |  Get the size of the dots used to mark space characters. |
| ScEditor:SetExtraAscent(int value) |  Set extra ascent for each line |
| ScEditor:SetExtraDescent(int value) |  Set extra descent for each line |
| ScEditor:SetViewWS(int value) |  Make white space characters invisible, always visible or visible outside indentation. |
| ScEditor:SetWhitespaceBack(bool useSetting, colour back) | Set the background colour of all whitespace and whether to use this setting. |
| ScEditor:SetWhitespaceFore(bool useSetting, colour fore) | Set the foreground colour of all whitespace and whether to use this setting. |
| ScEditor:SetWhitespaceSize(int value) |  Set the size of the dots used to mark space characters. |


| Cursor  |  |
| ------------- | ------------- |
| int ScEditor:GetCursor() |  Get cursor type. |
| ScEditor:SetCursor(int value) |  Sets the cursor to one of the SC\_CURSOR\* values. |


| Line endings  |  |
| ------------- | ------------- |
| ScEditor:ConvertEOLs(int eolMode) | Convert all line endings in the document to one mode. |
| int ScEditor:GetEOLMode() |  Retrieve the current end of line mode - one of CRLF, CR, or LF. |
| int ScEditor:GetLineEndTypesActive() |  Get the line end types currently recognised. May be a subset of the allowed types due to lexer limitation. |
| int ScEditor:GetLineEndTypesAllowed() |  Get the line end types currently allowed. |
| int ScEditor:GetLineEndTypesSupported() |  Bit set of LineEndType enumertion for which line ends beyond the standard LF, CR, and CRLF are supported by the lexer. |
| bool ScEditor:GetViewEOL() |  Are the end of line characters visible? |
| ScEditor:SetEOLMode(int value) |  Set the current end of line mode. |
| ScEditor:SetLineEndTypesAllowed(int value) |  Set the line end types that the application wants to use. May not be used if incompatible with lexer or encoding. |
| ScEditor:SetViewEOL(bool value) |  Make the end of line characters visible or invisible. |


| Styling  |  |
| ------------- | ------------- |
| int ScEditor:GetEndStyled() |  Retrieve the position of the last correctly styled character. |
| int ScEditor:GetIdleStyling() |  Retrieve the limits to idle styling. |
| int ScEditor:GetLineState(int line) |  Retrieve the extra styling information for a line. |
| int ScEditor:GetMaxLineState() |  Retrieve the last line number that has line state. |
| ScEditor:SetIdleStyling(int value) |  Sets limits to idle styling. |
| ScEditor:SetLineState(int line, int value) |  Used to hold extra styling information for each line. |
| ScEditor:SetStyling(int length, int style) | Change style from current styling position for length characters to a style and move the current styling position to after this newly styled segment. |
| ScEditor:SetStylingEx(string styles) | Set the styles for a segment of the document. |
| ScEditor:StartStyling(int pos, int mask) | Set the current styling position to pos and the styling mask to mask. The styling mask can be used to protect some bits in each styling byte from modification. |


| Style definition  |  |
| ------------- | ------------- |
| colour ScEditor:GetStyleBack(int style) |  Get the background colour of a style. |
| bool ScEditor:GetStyleBold(int style) |  Get is a style bold or not. |
| int ScEditor:GetStyleCase(int style) |  Get is a style mixed case, or to force upper or lower case. |
| bool ScEditor:GetStyleChangeable(int style) |  Get is a style changeable or not (read only). Experimental feature, currently buggy. |
| int ScEditor:GetStyleCharacterSet(int style) |  Get the character get of the font in a style. |
| bool ScEditor:GetStyleEOLFilled(int style) |  Get is a style to have its end of line filled or not. |
| string ScEditor:GetStyleFont(int style) |  Get the font of a style. Returns the length of the fontName  |
| colour ScEditor:GetStyleFore(int style) |  Get the foreground colour of a style. |
| bool ScEditor:GetStyleHotSpot(int style) |  Get is a style a hotspot or not. |
| bool ScEditor:GetStyleItalic(int style) |  Get is a style italic or not. |
| int ScEditor:GetStyleSize(int style) |  Get the size of characters of a style. |
| int ScEditor:GetStyleSizeFractional(int style) |  Get the size of characters of a style in points multiplied by 100 |
| bool ScEditor:GetStyleUnderline(int style) |  Get is a style underlined or not. |
| bool ScEditor:GetStyleVisible(int style) |  Get is a style visible or not. |
| int ScEditor:GetStyleWeight(int style) |  Get the weight of characters of a style. |
| ScEditor:SetStyleBack(int style, colour value) |  Set the background colour of a style. |
| ScEditor:SetStyleBold(int style, bool value) |  Set a style to be bold or not. |
| ScEditor:SetStyleCase(int style, int value) |  Set a style to be mixed case, or to force upper or lower case. |
| ScEditor:SetStyleChangeable(int style, bool value) |  Set a style to be changeable or not (read only). Experimental feature, currently buggy. |
| ScEditor:SetStyleCharacterSet(int style, int value) |  Set the character set of the font in a style. |
| ScEditor:SetStyleEOLFilled(int style, bool value) |  Set a style to have its end of line filled or not. |
| ScEditor:SetStyleFont(int style, string value) |  Set the font of a style. |
| ScEditor:SetStyleFore(int style, colour value) |  Set the foreground colour of a style. |
| ScEditor:SetStyleHotSpot(int style, bool value) |  Set a style to be a hotspot or not. |
| ScEditor:SetStyleItalic(int style, bool value) |  Set a style to be italic or not. |
| ScEditor:SetStyleSize(int style, int value) |  Set the size of characters of a style. |
| ScEditor:SetStyleSizeFractional(int style, int value) |  Set the size of characters of a style. Size is in points multiplied by 100. |
| ScEditor:SetStyleUnderline(int style, bool value) |  Set a style to be underlined or not. |
| ScEditor:SetStyleVisible(int style, bool value) |  Set a style to be visible or not. |
| ScEditor:SetStyleWeight(int style, int value) |  Set the weight of characters of a style. |
| ScEditor:StyleClearAll() | Clear all the styles and make equivalent to the global default style. |
| ScEditor:StyleResetDefault() | Reset the default style to its state at startup |


| Caret, selection, and hotspot styles  |  |
| ------------- | ------------- |
| colour ScEditor:GetCaretFore() |  Get the foreground colour of the caret. |
| colour ScEditor:GetCaretLineBack() |  Get the colour of the background of the line containing the caret. |
| int ScEditor:GetCaretLineBackAlpha() |  Get the background alpha of the caret line. |
| bool ScEditor:GetCaretLineVisible() |  Is the background of the line containing the caret in a different colour? |
| bool ScEditor:GetCaretLineVisibleAlways() |  Is the caret line always visible? |
| int ScEditor:GetCaretPeriod() |  Get the time in milliseconds that the caret is on and off. |
| int ScEditor:GetCaretSticky() |  Can the caret preferred x position only be changed by explicit movement commands? |
| int ScEditor:GetCaretStyle() |  Returns the current style of the caret. |
| int ScEditor:GetCaretWidth() |  Returns the width of the insert mode caret. |
| colour ScEditor:GetHotspotActiveBack() | Get the back colour for active hotspots. |
| colour ScEditor:GetHotspotActiveFore() | Get the fore colour for active hotspots. |
| bool ScEditor:GetHotspotActiveUnderline() |  Get whether underlining for active hotspots. |
| bool ScEditor:GetHotspotSingleLine() |  Get the HotspotSingleLine property |
| int ScEditor:GetSelAlpha() |  Get the alpha of the selection. |
| bool ScEditor:GetSelEOLFilled() |  Is the selection end of line filled? |
| ScEditor:SetCaretFore(colour value) |  Set the foreground colour of the caret. |
| ScEditor:SetCaretLineBack(colour value) |  Set the colour of the background of the line containing the caret. |
| ScEditor:SetCaretLineBackAlpha(int value) |  Set background alpha of the caret line. |
| ScEditor:SetCaretLineVisible(bool value) |  Display the background of the line containing the caret in a different colour. |
| ScEditor:SetCaretLineVisibleAlways(bool value) |  Sets the caret line to always visible. |
| ScEditor:SetCaretPeriod(int value) |  Get the time in milliseconds that the caret is on and off. 0 = steady on. |
| ScEditor:SetCaretSticky(int value) |  Stop the caret preferred x position changing when the user types. |
| ScEditor:SetCaretStyle(int value) |  Set the style of the caret to be drawn. |
| ScEditor:SetCaretWidth(int value) |  Set the width of the insert mode caret. |
| ScEditor:SetHotspotActiveBack(bool useSetting, colour back) | Set a back colour for active hotspots. |
| ScEditor:SetHotspotActiveFore(bool useSetting, colour fore) | Set a fore colour for active hotspots. |
| ScEditor:SetHotspotActiveUnderline(bool value) |  Enable / Disable underlining active hotspots. |
| ScEditor:SetHotspotSingleLine(bool value) |  Limit hotspots to single line so hotspots on two lines don't merge. |
| ScEditor:SetSelAlpha(int value) |  Set the alpha of the selection. |
| ScEditor:SetSelBack(bool useSetting, colour back) | Set the background colour of the main and additional selections and whether to use this setting. |
| ScEditor:SetSelEOLFilled(bool value) |  Set the selection to have its end of line filled or not. |
| ScEditor:SetSelFore(bool useSetting, colour fore) | Set the foreground colour of the main and additional selections and whether to use this setting. |
| ScEditor:ToggleCaretSticky() | Switch between sticky and non-sticky: meant to be bound to a key. |


| Character representations  |  |
| ------------- | ------------- |
| ScEditor:ClearRepresentation(string encodedCharacter) | Remove a character representation. |
| int ScEditor:GetControlCharSymbol() |  Get the way control characters are displayed. |
| string ScEditor:GetRepresentation(string encodedCharacter) |  Set the way a character is drawn.  |
| ScEditor:SetControlCharSymbol(int value) |  Change the way control characters are displayed: If symbol is &lt; 32, keep the drawn way, else, use the given character. |
| ScEditor:SetRepresentation(string encodedCharacter, string value) |  Set the way a character is drawn. |


| Margins  |  |
| ------------- | ------------- |
| int ScEditor:GetMarginCursorN(int margin) |  Retrieve the cursor shown in a margin. |
| int ScEditor:GetMarginLeft() |  Returns the size in pixels of the left margin. |
| int ScEditor:GetMarginMaskN(int margin) |  Retrieve the marker mask of a margin. |
| int ScEditor:GetMarginOptions() |  Get the margin options. |
| int ScEditor:GetMarginRight() |  Returns the size in pixels of the right margin. |
| bool ScEditor:GetMarginSensitiveN(int margin) |  Retrieve the mouse click sensitivity of a margin. |
| int ScEditor:GetMarginStyle(int line) |  Get the style number for the text margin for a line |
| int ScEditor:GetMarginStyleOffset() |  Get the start of the range of style numbers used for margin text |
| string ScEditor:GetMarginStyles(int line) |  Get the styles in the text margin for a line |
| string ScEditor:GetMarginText(int line) |  Get the text in the text margin for a line |
| int ScEditor:GetMarginTypeN(int margin) |  Retrieve the type of a margin. |
| int ScEditor:GetMarginWidthN(int margin) |  Retrieve the width of a margin in pixels. |
| ScEditor:MarginTextClearAll() | Clear the margin text on all lines |
| ScEditor:SetFoldMarginColour(bool useSetting, colour back) | Set the colours used as a chequerboard pattern in the fold margin |
| ScEditor:SetFoldMarginHiColour(bool useSetting, colour fore) | Set the colours used as a chequerboard pattern in the fold margin |
| ScEditor:SetMarginCursorN(int margin, int value) |  Set the cursor shown when the mouse is inside a margin. |
| ScEditor:SetMarginLeft(int value) |  Sets the size in pixels of the left margin. |
| ScEditor:SetMarginMaskN(int margin, int value) |  Set a mask that determines which markers are displayed in a margin. |
| ScEditor:SetMarginOptions(int value) |  Set the margin options. |
| ScEditor:SetMarginRight(int value) |  Sets the size in pixels of the right margin. |
| ScEditor:SetMarginSensitiveN(int margin, bool value) |  Make a margin sensitive or insensitive to mouse clicks. |
| ScEditor:SetMarginStyle(int line, int value) |  Set the style number for the text margin for a line |
| ScEditor:SetMarginStyleOffset(int value) |  Get the start of the range of style numbers used for margin text |
| ScEditor:SetMarginStyles(int line, string value) |  Set the style in the text margin for a line |
| ScEditor:SetMarginText(int line, string value) |  Set the text in the text margin for a line |
| ScEditor:SetMarginTypeN(int margin, int value) |  Set a margin to be either numeric or symbolic. |
| ScEditor:SetMarginWidthN(int margin, int value) |  Set the width of a margin to a width expressed in pixels. |


| Annotations  |  |
| ------------- | ------------- |
| ScEditor:AnnotationClearAll() | Clear the annotations from all lines |
| int ScEditor:GetAnnotationLines(int line) |  Get the number of annotation lines for a line |
| int ScEditor:GetAnnotationStyle(int line) |  Get the style number for the annotations for a line |
| int ScEditor:GetAnnotationStyleOffset() |  Get the start of the range of style numbers used for annotations |
| string ScEditor:GetAnnotationStyles(int line) |  Get the annotation styles for a line |
| string ScEditor:GetAnnotationText(int line) |  Get the annotation text for a line |
| int ScEditor:GetAnnotationVisible() |  Get the visibility for the annotations for a view |
| ScEditor:SetAnnotationStyle(int line, int value) |  Set the style number for the annotations for a line |
| ScEditor:SetAnnotationStyleOffset(int value) |  Get the start of the range of style numbers used for annotations |
| ScEditor:SetAnnotationStyles(int line, string value) |  Set the annotation styles for a line |
| ScEditor:SetAnnotationText(int line, string value) |  Set the annotation text for a line |
| ScEditor:SetAnnotationVisible(int value) |  Set the visibility for the annotations for a view |


| Other settings  |  |
| ------------- | ------------- |
| bool ScEditor:GetBufferedDraw() |  Is drawing done first into a buffer or direct to the screen? |
| int ScEditor:GetCodePage() |  Get the code page used to interpret the bytes of the document as characters. |
| bool ScEditor:GetFocus() |  Get internal focus flag. |
| int ScEditor:GetFontQuality() |  Retrieve the quality level for text. |
| int ScEditor:GetIMEInteraction() |  Is the IME displayed in a window or inline? |
| int ScEditor:GetPhasesDraw() |  How many phases is drawing done in? |
| string ScEditor:GetPunctuationChars() |  Get the set of characters making up punctuation characters |
| int ScEditor:GetTechnology() |  Get the tech. |
| bool ScEditor:GetTwoPhaseDraw() |  Is drawing done in two phases with backgrounds drawn before foregrounds? |
| string ScEditor:GetWhitespaceChars() |  Get the set of characters making up whitespace for when moving or selecting by word. |
| string ScEditor:GetWordChars() |  Get the set of characters making up words for when moving or selecting by word. Returns the number of characters |
| ScEditor:GrabFocus() | Set the focus to this Scintilla widget. |
| ScEditor:SetBufferedDraw(bool value) |  If drawing is buffered then each line of text is drawn into a bitmap buffer before drawing it to the screen to avoid flicker. |
| ScEditor:SetCharsDefault() | Reset the set of characters for whitespace and word characters to the defaults. |
| ScEditor:SetCodePage(int value) |  Set the code page used to interpret the bytes of the document as characters. The SC\_CP\_UTF8 value can be used to enter Unicode mode. |
| ScEditor:SetFocus(bool value) |  Change internal focus flag. |
| ScEditor:SetFontQuality(int value) |  Choose the quality level for text from the FontQuality enumeration. |
| ScEditor:SetIMEInteraction(int value) |  Choose to display the the IME in a winow or inline. |
| ScEditor:SetPhasesDraw(int value) |  In one phase draw, text is drawn in a series of rectangular blocks with no overlap. In two phase draw, text is drawn in a series of lines allowing runs to overlap horizontally. In multiple phase draw, each element is drawn over the whole drawing area, allowing text to overlap from one line to the next. |
| ScEditor:SetPunctuationChars(string value) |  Set the set of characters making up punctuation characters Should be called after SetWordChars. |
| ScEditor:SetTechnology(int value) |  Set the technology used. |
| ScEditor:SetTwoPhaseDraw(bool value) |  In twoPhaseDraw mode, drawing is performed in two phases, first the background and then the foreground. This avoids chopping off characters that overlap the next run. |
| ScEditor:SetWhitespaceChars(string value) |  Set the set of characters making up whitespace for when moving or selecting by word. Should be called after SetWordChars. |
| ScEditor:SetWordChars(string value) |  Set the set of characters making up words for when moving or selecting by word. First sets defaults like SetCharsDefault. |


| Brace highlighting  |  |
| ------------- | ------------- |
| ScEditor:BraceBadLight(int pos) | Highlight the character at a position indicating there is no matching brace. |
| ScEditor:BraceBadLightIndicator(bool useBraceBadLightIndicator, int indicator) | Use specified indicator to highlight non matching brace instead of changing its style. |
| ScEditor:BraceHighlight(int pos1, int pos2) | Highlight the characters at two positions. |
| ScEditor:BraceHighlightIndicator(bool useBraceHighlightIndicator, int indicator) | Use specified indicator to highlight matching braces instead of changing their style. |
| int ScEditor:BraceMatch(int pos) | Find the position of a matching brace or INVALID\_POSITION if no match. |


| Tabs and Indentation Guides  |  |
| ------------- | ------------- |
| ScEditor:AddTabStop(int line, int x) | Add an explicit tab stop for a line. |
| ScEditor:ClearTabStops(int line) | Clear explicit tabstops on a line. |
| bool ScEditor:GetBackSpaceUnIndents() |  Does a backspace pressed when caret is within indentation unindent? |
| int ScEditor:GetHighlightGuide() |  Get the highlighted indentation guide column. |
| int ScEditor:GetIndent() |  Retrieve indentation size. |
| int ScEditor:GetIndentationGuides() |  Are the indentation guides visible? |
| int ScEditor:GetLineIndentPosition(int line) |  Retrieve the position before the first non indentation character on a line. |
| int ScEditor:GetLineIndentation(int line) |  Retrieve the number of columns that a line is indented. |
| int ScEditor:GetNextTabStop(int line, int x) | Find the next explicit tab stop position on a line after a position. |
| bool ScEditor:GetTabIndents() |  Does a tab pressed when caret is within indentation indent? |
| int ScEditor:GetTabWidth() |  Retrieve the visible size of a tab. |
| bool ScEditor:GetUseTabs() |  Retrieve whether tabs will be used in indentation. |
| ScEditor:SetBackSpaceUnIndents(bool value) |  Sets whether a backspace pressed when caret is within indentation unindents. |
| ScEditor:SetHighlightGuide(int value) |  Set the highlighted indentation guide column. 0 = no highlighted guide. |
| ScEditor:SetIndent(int value) |  Set the number of spaces used for one level of indentation. |
| ScEditor:SetIndentationGuides(int value) |  Show or hide indentation guides. |
| ScEditor:SetLineIndentation(int line, int value) |  Change the indentation of a line to a number of columns. |
| ScEditor:SetTabIndents(bool value) |  Sets whether a tab pressed when caret is within indentation indents. |
| ScEditor:SetTabWidth(int value) |  Change the visible size of a tab to be a multiple of the width of a space character. |
| ScEditor:SetUseTabs(bool value) |  Indentation will only use space characters if useTabs is false, otherwise it will use a combination of tabs and spaces. |


| Markers  |  |
| ------------- | ------------- |
| int ScEditor:MarkerAdd(int line, int markerNumber) | Add a marker to a line, returning an ID which can be used to find or delete the marker. |
| ScEditor:MarkerAddSet(int line, int set) | Add a set of markers to a line. |
| ScEditor:MarkerDefine(int markerNumber, int markerSymbol) | Set the symbol used for a particular marker number. |
| ScEditor:MarkerDefinePixmap(int markerNumber, string pixmap) | Define a marker from a pixmap. |
| ScEditor:MarkerDefineRGBAImage(int markerNumber, string pixels) | Define a marker from RGBA data. It has the width and height from RGBAImageSetWidth/Height |
| ScEditor:MarkerDelete(int line, int markerNumber) | Delete a marker from a line. |
| ScEditor:MarkerDeleteAll(int markerNumber) | Delete all markers with a particular number from all lines. |
| ScEditor:MarkerDeleteHandle(int handle) | Delete a marker. |
| ScEditor:MarkerEnableHighlight(bool enabled) | Enable/disable highlight for current folding bloc (smallest one that contains the caret) |
| int ScEditor:MarkerGet(int line) | Get a bit mask of all the markers set on a line. |
| int ScEditor:MarkerLineFromHandle(int handle) | Retrieve the line number at which a particular marker is located. |
| int ScEditor:MarkerNext(int lineStart, int markerMask) | Find the next line at or after lineStart that includes a marker in mask. Return -1 when no more lines. |
| int ScEditor:MarkerPrevious(int lineStart, int markerMask) | Find the previous line before lineStart that includes a marker in mask. |
| int ScEditor:MarkerSymbolDefined(int markerNumber) | Which symbol was defined for markerNumber with MarkerDefine |
| ScEditor:SetMarkerAlpha(int markerNumber, int value) |  Set the alpha used for a marker that is drawn in the text area, not the margin. |
| ScEditor:SetMarkerBack(int markerNumber, colour value) |  Set the background colour used for a particular marker number. |
| ScEditor:SetMarkerBackSelected(int markerNumber, colour value) |  Set the background colour used for a particular marker number when its folding block is selected. |
| ScEditor:SetMarkerFore(int markerNumber, colour value) |  Set the foreground colour used for a particular marker number. |
| ScEditor:SetRGBAImageHeight(int value) |  Set the height for future RGBA image data. |
| ScEditor:SetRGBAImageScale(int value) |  Set the scale factor in percent for future RGBA image data. |
| ScEditor:SetRGBAImageWidth(int value) |  Set the width for future RGBA image data. |


| Indicators  |  |
| ------------- | ------------- |
| ScEditor:FindIndicatorFlash(int start, int end) | On OS X, flash a find indicator, then fade out. |
| ScEditor:FindIndicatorHide() | On OS X, hide the find indicator. |
| ScEditor:FindIndicatorShow(int start, int end) | On OS X, show a find indicator. |
| int ScEditor:GetIndicAlpha(int indicator) |  Get the alpha fill colour of the given indicator. |
| int ScEditor:GetIndicFlags(int indic) |  Retrieve the attributes of an indicator. |
| colour ScEditor:GetIndicFore(int indic) |  Retrieve the foreground colour of an indicator. |
| colour ScEditor:GetIndicHoverFore(int indic) |  Retrieve the foreground hover colour of an indicator. |
| int ScEditor:GetIndicHoverStyle(int indic) |  Retrieve the hover style of an indicator. |
| int ScEditor:GetIndicOutlineAlpha(int indicator) |  Get the alpha outline colour of the given indicator. |
| int ScEditor:GetIndicStyle(int indic) |  Retrieve the style of an indicator. |
| bool ScEditor:GetIndicUnder(int indic) |  Retrieve whether indicator drawn under or over text. |
| int ScEditor:GetIndicatorCurrent() |  Get the current indicator |
| int ScEditor:GetIndicatorValue() |  Get the current indicator value |
| int ScEditor:IndicatorAllOnFor(int int) | Are any indicators present at position? |
| ScEditor:IndicatorClearRange(int int, int clearLength) | Turn a indicator off over a range. |
| int ScEditor:IndicatorEnd(int indicator, int int) | Where does a particular indicator end? |
| ScEditor:IndicatorFillRange(int int, int fillLength) | Turn a indicator on over a range. |
| int ScEditor:IndicatorStart(int indicator, int int) | Where does a particular indicator start? |
| int ScEditor:IndicatorValueAt(int indicator, int int) | What value does a particular indicator have at at a position? |
| ScEditor:SetIndicAlpha(int indicator, int value) |  Set the alpha fill colour of the given indicator. |
| ScEditor:SetIndicFlags(int indic, int value) |  Set the attributes of an indicator. |
| ScEditor:SetIndicFore(int indic, colour value) |  Set the foreground colour of an indicator. |
| ScEditor:SetIndicHoverFore(int indic, colour value) |  Set the foreground hover colour of an indicator. |
| ScEditor:SetIndicHoverStyle(int indic, int value) |  Set a hover indicator to plain, squiggle or TT. |
| ScEditor:SetIndicOutlineAlpha(int indicator, int value) |  Set the alpha outline colour of the given indicator. |
| ScEditor:SetIndicStyle(int indic, int value) |  Set an indicator to plain, squiggle or TT. |
| ScEditor:SetIndicUnder(int indic, bool value) |  Set an indicator to draw under text or over(default). |
| ScEditor:SetIndicatorCurrent(int value) |  Set the indicator used for IndicatorFillRange and IndicatorClearRange |
| ScEditor:SetIndicatorValue(int value) |  Set the value used for IndicatorFillRange |


| Autocompletion  |  |
| ------------- | ------------- |
| bool ScEditor:AutoCActive() | Is there an auto-completion list visible? |
| ScEditor:AutoCCancel() | Remove the auto-completion list from the screen. |
| ScEditor:AutoCComplete() | User has selected an item so remove the list and insert the selection. |
| int ScEditor:AutoCPosStart() | Retrieve the position of the caret when the auto-completion list was displayed. |
| ScEditor:AutoCSelect(string text) | Select the item in the auto-completion list that starts with a string. |
| ScEditor:AutoCShow(int lenEntered, string itemList) | Display a auto-completion list. The lenEntered parameter indicates how many characters before the caret should be used to provide context. |
| ScEditor:AutoCStops(string characterSet) | Define a set of character that when typed cancel the auto-completion list. |
| ScEditor:ClearRegisteredImages() | Clear all the registered XPM images. |
| bool ScEditor:GetAutoCAutoHide() |  Retrieve whether or not autocompletion is hidden automatically when nothing matches. |
| bool ScEditor:GetAutoCCancelAtStart() |  Retrieve whether auto-completion cancelled by backspacing before start. |
| int ScEditor:GetAutoCCaseInsensitiveBehaviour() |  Get auto-completion case insensitive behaviour. |
| bool ScEditor:GetAutoCChooseSingle() |  Retrieve whether a single item auto-completion list automatically choose the item. |
| int ScEditor:GetAutoCCurrent() |  Get currently selected item position in the auto-completion list |
| string ScEditor:GetAutoCCurrentText() |  Get currently selected item text in the auto-completion list Returns the length of the item text  |
| bool ScEditor:GetAutoCDropRestOfWord() |  Retrieve whether or not autocompletion deletes any word characters after the inserted text upon completion. |
| bool ScEditor:GetAutoCIgnoreCase() |  Retrieve state of ignore case flag. |
| int ScEditor:GetAutoCMaxHeight() |  Set the maximum height, in rows, of auto-completion and user lists. |
| int ScEditor:GetAutoCMaxWidth() |  Get the maximum width, in characters, of auto-completion and user lists. |
| int ScEditor:GetAutoCMulti() |  Retrieve the effect of autocompleting when there are multiple selections. |
| int ScEditor:GetAutoCOrder() |  Get the way autocompletion lists are ordered. |
| int ScEditor:GetAutoCSeparator() |  Retrieve the auto-completion list separator character. |
| int ScEditor:GetAutoCTypeSeparator() |  Retrieve the auto-completion list type-separator character. |
| ScEditor:RegisterImage(int type, string xpmData) | Register an XPM image for use in autocompletion lists. |
| ScEditor:RegisterRGBAImage(int type, string pixels) | Register an RGBA image for use in autocompletion lists. It has the width and height from RGBAImageSetWidth/Height |
| ScEditor:SetAutoCAutoHide(bool value) |  Set whether or not autocompletion is hidden automatically when nothing matches. |
| ScEditor:SetAutoCCancelAtStart(bool value) |  Should the auto-completion list be cancelled if the user backspaces to a position before where the box was created. |
| ScEditor:SetAutoCCaseInsensitiveBehaviour(int value) |  Set auto-completion case insensitive behaviour to either prefer case-sensitive matches or have no preference. |
| ScEditor:SetAutoCChooseSingle(bool value) |  Should a single item auto-completion list automatically choose the item. |
| ScEditor:SetAutoCDropRestOfWord(bool value) |  Set whether or not autocompletion deletes any word characters after the inserted text upon completion. |
| ScEditor:SetAutoCFillUps(string value) |  Define a set of characters that when typed will cause the autocompletion to choose the selected item. |
| ScEditor:SetAutoCIgnoreCase(bool value) |  Set whether case is significant when performing auto-completion searches. |
| ScEditor:SetAutoCMaxHeight(int value) |  Set the maximum height, in rows, of auto-completion and user lists. The default is 5 rows. |
| ScEditor:SetAutoCMaxWidth(int value) |  Set the maximum width, in characters, of auto-completion and user lists. Set to 0 to autosize to fit longest item, which is the default. |
| ScEditor:SetAutoCMulti(int value) |  Change the effect of autocompleting when there are multiple selections. |
| ScEditor:SetAutoCOrder(int value) |  Set the way autocompletion lists are ordered. |
| ScEditor:SetAutoCSeparator(int value) |  Change the separator character in the string setting up an auto-completion list. Default is space but can be changed if items contain space. |
| ScEditor:SetAutoCTypeSeparator(int value) |  Change the type-separator character in the string setting up an auto-completion list. Default is '?' but can be changed if items contain '?'. |


| User lists  |  |
| ------------- | ------------- |
| ScEditor:UserListShow(int listType, string itemList) | Display a list of strings and send notification when user chooses one. |


| Call tips  |  |
| ------------- | ------------- |
| bool ScEditor:CallTipActive() | Is there an active call tip? |
| ScEditor:CallTipCancel() | Remove the call tip from the screen. |
| int ScEditor:CallTipPosStart() | Retrieve the position where the caret was before displaying the call tip. |
| ScEditor:CallTipSetHlt(int start, int end) | Highlight a segment of the definition. |
| ScEditor:CallTipShow(int pos, string definition) | Show a call tip containing a definition near position pos. |
| ScEditor:SetCallTipBack(colour value) |  Set the background colour for the call tip. |
| ScEditor:SetCallTipFore(colour value) |  Set the foreground colour for the call tip. |
| ScEditor:SetCallTipForeHlt(colour value) |  Set the foreground colour for the highlighted part of the call tip. |
| ScEditor:SetCallTipPosStart(int value) |  Set the start position in order to change when backspacing removes the calltip. |
| ScEditor:SetCallTipPosition(bool value) |  Set position of calltip, above or below text. |
| ScEditor:SetCallTipUseStyle(int value) |  Enable use of STYLE\_CALLTIP and set call tip tab size in pixels. |


| Printing  |  |
| ------------- | ------------- |
| int ScEditor:GetPrintColourMode() |  Returns the print colour mode. |
| int ScEditor:GetPrintMagnification() |  Returns the print magnification. |
| int ScEditor:GetPrintWrapMode() |  Is printing line wrapped? |
| ScEditor:SetPrintColourMode(int value) |  Modify colours when printing for clearer printed text. |
| ScEditor:SetPrintMagnification(int value) |  Sets the print magnification added to the point size of each style for printing. |
| ScEditor:SetPrintWrapMode(int value) |  Set printing to line wrapped (SC\_WRAP\_WORD) or not line wrapped (SC\_WRAP\_NONE). |


| Folding  |  |
| ------------- | ------------- |
| int ScEditor:ContractedFoldNext(int lineStart) | Find the next line at or after lineStart that is a contracted fold header line. Return -1 when no more lines. |
| int ScEditor:DocLineFromVisible(int lineDisplay) | Find the document line of a display line taking hidden lines into account. |
| ScEditor:EnsureVisible(int line) | Ensure a particular line is visible by expanding any header line hiding it. |
| ScEditor:EnsureVisibleEnforcePolicy(int line) | Ensure a particular line is visible by expanding any header line hiding it. Use the currently set visibility policy to determine which range to display. |
| ScEditor:ExpandChildren(int line, int level) | Expand a fold header and all children. Use the level argument instead of the line's current level. |
| ScEditor:FoldAll(int action) | Expand or contract all fold headers. |
| ScEditor:FoldChildren(int line, int action) | Expand or contract a fold header and its children. |
| ScEditor:FoldLine(int line, int action) | Expand or contract a fold header. |
| bool ScEditor:GetAllLinesVisible() |  Are all lines visible? |
| int ScEditor:GetAutomaticFold() |  Get automatic folding behaviours. |
| bool ScEditor:GetFoldExpanded(int line) |  Is a header line expanded? |
| int ScEditor:GetFoldLevel(int line) |  Retrieve the fold level of a line. |
| int ScEditor:GetFoldParent(int line) |  Find the parent line of a child line. |
| int ScEditor:GetLastChild(int line, int level) | Find the last child line of a header line. |
| bool ScEditor:GetLineVisible(int line) |  Is a line visible? |
| ScEditor:HideLines(int lineStart, int lineEnd) | Make a range of lines invisible. |
| ScEditor:SetAutomaticFold(int value) |  Set automatic folding behaviours. |
| ScEditor:SetFoldExpanded(int line, bool value) |  Show the children of a header line. |
| ScEditor:SetFoldFlags(int value) |  Set some style options for folding. |
| ScEditor:SetFoldLevel(int line, int value) |  Set the fold level of a line. This encodes an integer level along with flags indicating whether the line is a header and whether it is effectively white space. |
| ScEditor:ShowLines(int lineStart, int lineEnd) | Make a range of lines visible. |
| ScEditor:ToggleFold(int line) | Switch a header line between expanded and contracted. |
| int ScEditor:VisibleFromDocLine(int line) | Find the display line of a document line taking hidden lines into account. |


| Line wrapping  |  |
| ------------- | ------------- |
| int ScEditor:GetLayoutCache() |  Retrieve the degree of caching of layout information. |
| int ScEditor:GetPositionCache() |  How many entries are allocated to the position cache? |
| int ScEditor:GetWrapIndentMode() |  Retrieve how wrapped sublines are placed. Default is fixed. |
| int ScEditor:GetWrapMode() |  Retrieve whether text is word wrapped. |
| int ScEditor:GetWrapStartIndent() |  Retrive the start indent for wrapped lines. |
| int ScEditor:GetWrapVisualFlags() |  Retrive the display mode of visual flags for wrapped lines. |
| int ScEditor:GetWrapVisualFlagsLocation() |  Retrive the location of visual flags for wrapped lines. |
| ScEditor:LinesJoin() | Join the lines in the target. |
| ScEditor:LinesSplit(int pixelWidth) | Split the lines in the target into lines that are less wide than pixelWidth where possible. |
| ScEditor:SetLayoutCache(int value) |  Sets the degree of caching of layout information. |
| ScEditor:SetPositionCache(int value) |  Set number of entries in position cache |
| ScEditor:SetWrapIndentMode(int value) |  Sets how wrapped sublines are placed. Default is fixed. |
| ScEditor:SetWrapMode(int value) |  Sets whether text is word wrapped. |
| ScEditor:SetWrapStartIndent(int value) |  Set the start indent for wrapped lines. |
| ScEditor:SetWrapVisualFlags(int value) |  Set the display mode of visual flags for wrapped lines. |
| ScEditor:SetWrapVisualFlagsLocation(int value) |  Set the location of visual flags for wrapped lines. |
| int ScEditor:WrapCount(int line) | The number of display lines needed to wrap a document line |


| Zooming  |  |
| ------------- | ------------- |
| int ScEditor:GetZoom() |  Retrieve the zoom level. |
| ScEditor:SetZoom(int value) |  Set the zoom level. This number of points is added to the size of all fonts. It may be positive to magnify or negative to reduce. |
| ScEditor:ZoomIn() | Magnify the displayed text by increasing the sizes by 1 point. |
| ScEditor:ZoomOut() | Make the displayed text smaller by decreasing the sizes by 1 point. |


| Long lines  |  |
| ------------- | ------------- |
| colour ScEditor:GetEdgeColour() |  Retrieve the colour used in edge indication. |
| int ScEditor:GetEdgeColumn() |  Retrieve the column number which text should be kept within. |
| int ScEditor:GetEdgeMode() |  Retrieve the edge highlight mode. |
| ScEditor:SetEdgeColour(colour value) |  Change the colour used in edge indication. |
| ScEditor:SetEdgeColumn(int value) |  Set the column number of the edge. If text goes past the edge then it is highlighted. |
| ScEditor:SetEdgeMode(int value) |  The edge may be displayed by a line (EDGE\_LINE) or by highlighting text that goes beyond it (EDGE\_BACKGROUND) or not displayed at all (EDGE\_NONE). |


| Lexer  |  |
| ------------- | ------------- |
| int ScEditor:AllocateSubStyles(int styleBase, int numberStyles) | Allocate a set of sub styles for a particular base style, returning start of range |
| int ScEditor:ChangeLexerState(int start, int end) | Indicate that the internal state of a lexer has changed over a range and therefore there may be a need to redraw. |
| ScEditor:Colourise(int start, int end) | Colourise a segment of the document using the current lexing language. |
| string,int ScEditor:DescribeKeyWordSets() | Retrieve a '\\n' separated list of descriptions of the keyword sets understood by the current lexer.  |
| string,int ScEditor:DescribeProperty(string name) | Describe a property.  |
| ScEditor:FreeSubStyles() | Free allocated sub styles |
| int ScEditor:GetDistanceToSecondaryStyles() |  Where styles are duplicated by a feature such as active/inactive code return the distance between the two types. |
| int ScEditor:GetLexer() |  Retrieve the lexing language of the document. |
| string ScEditor:GetLexerLanguage() |  Retrieve the name of the lexer. Return the length of the text.  |
| int ScEditor:GetPrimaryStyleFromStyle(int style) |  For a secondary style, return the primary style, else return the argument. |
| string ScEditor:GetProperty(string key) |  Retrieve a &quot;property&quot; value previously set with SetProperty.  |
| string ScEditor:GetPropertyExpanded(string key) |  Retrieve a &quot;property&quot; value previously set with SetProperty, with &quot;$()&quot; variable replacement on returned buffer.  |
| int ScEditor:GetPropertyInt(string key) |  Retrieve a &quot;property&quot; value previously set with SetProperty, interpreted as an int AFTER any &quot;$()&quot; variable replacement. |
| int ScEditor:GetStyleFromSubStyle(int subStyle) |  For a sub style, return the base style, else return the argument. |
| string ScEditor:GetSubStyleBases() |  Get the set of base styles that can be extended with sub styles  |
| int ScEditor:GetSubStylesLength(int styleBase) |  The number of sub styles associated with a base style |
| int ScEditor:GetSubStylesStart(int styleBase) |  The starting style number for the sub styles associated with a base style |
| ScEditor:LoadLexerLibrary(string path) | Load a lexer library (dll / so). |
| string,int ScEditor:PropertyNames() | Retrieve a '\\n' separated list of properties understood by the current lexer.  |
| int ScEditor:PropertyType(string name) | Retrieve the type of a property. |
| ScEditor:SetIdentifiers(int style, string value) |  Set the identifiers that are shown in a particular style |
| ScEditor:SetKeyWords(int keywordSet, string value) |  Set up the key words used by the lexer. |
| ScEditor:SetLexer(int value) |  Set the lexing language of the document. |
| ScEditor:SetLexerLanguage(string value) |  Set the lexing language of the document based on string name. |
| ScEditor:SetProperty(string key, string value) |  Set up a value that may be used by a lexer for some optional feature. |


| Commands typically bound to key presses  |  |
| ------------- | ------------- |
| ScEditor:BackTab() | Dedent the selected lines. |
| ScEditor:Cancel() | Cancel any modes such as call tip or auto-completion list display. |
| ScEditor:CharLeft() | Move caret left one character. |
| ScEditor:CharLeftExtend() | Move caret left one character extending selection to new caret position. |
| ScEditor:CharLeftRectExtend() | Move caret left one character, extending rectangular selection to new caret position. |
| ScEditor:CharRight() | Move caret right one character. |
| ScEditor:CharRightExtend() | Move caret right one character extending selection to new caret position. |
| ScEditor:CharRightRectExtend() | Move caret right one character, extending rectangular selection to new caret position. |
| ScEditor:DelWordLeft() | Delete the word to the left of the caret. |
| ScEditor:DelWordRight() | Delete the word to the right of the caret. |
| ScEditor:DelWordRightEnd() | Delete the word to the right of the caret, but not the trailing non-word characters. |
| ScEditor:DeleteBack() | Delete the selection or if no selection, the character before the caret. |
| ScEditor:DocumentEnd() | Move caret to last position in document. |
| ScEditor:DocumentEndExtend() | Move caret to last position in document extending selection to new caret position. |
| ScEditor:DocumentStart() | Move caret to first position in document. |
| ScEditor:DocumentStartExtend() | Move caret to first position in document extending selection to new caret position. |
| ScEditor:Home() | Move caret to first position on line. |
| ScEditor:HomeExtend() | Move caret to first position on line extending selection to new caret position. |
| ScEditor:HomeRectExtend() | Move caret to first position on line, extending rectangular selection to new caret position. |
| ScEditor:HomeWrap() | These are like their namesakes Home(Extend)?, LineEnd(Extend)?, VCHome(Extend)? except they behave differently when word-wrap is enabled: They go first to the start / end of the display line, like (Home\|LineEnd)Display The difference is that, the cursor is already at the point, it goes on to the start or end of the document line, as appropriate for (Home\|LineEnd\|VCHome)(Extend)?. |
| ScEditor:HomeWrapExtend() | These are like their namesakes Home(Extend)?, LineEnd(Extend)?, VCHome(Extend)? except they behave differently when word-wrap is enabled: They go first to the start / end of the display line, like (Home\|LineEnd)Display The difference is that, the cursor is already at the point, it goes on to the start or end of the document line, as appropriate for (Home\|LineEnd\|VCHome)(Extend)?. |
| ScEditor:LineCopy() | Copy the line containing the caret. |
| ScEditor:LineCut() | Cut the line containing the caret. |
| ScEditor:LineDelete() | Delete the line containing the caret. |
| ScEditor:LineDown() | Move caret down one line. |
| ScEditor:LineDownExtend() | Move caret down one line extending selection to new caret position. |
| ScEditor:LineDownRectExtend() | Move caret down one line, extending rectangular selection to new caret position. |
| ScEditor:LineDuplicate() | Duplicate the current line. |
| ScEditor:LineEnd() | Move caret to last position on line. |
| ScEditor:LineEndDisplay() | Move caret to last position on display line. |
| ScEditor:LineEndDisplayExtend() | Move caret to last position on display line extending selection to new caret position. |
| ScEditor:LineEndExtend() | Move caret to last position on line extending selection to new caret position. |
| ScEditor:LineEndRectExtend() | Move caret to last position on line, extending rectangular selection to new caret position. |
| ScEditor:LineEndWrap() | These are like their namesakes Home(Extend)?, LineEnd(Extend)?, VCHome(Extend)? except they behave differently when word-wrap is enabled: They go first to the start / end of the display line, like (Home\|LineEnd)Display The difference is that, the cursor is already at the point, it goes on to the start or end of the document line, as appropriate for (Home\|LineEnd\|VCHome)(Extend)?. |
| ScEditor:LineEndWrapExtend() | These are like their namesakes Home(Extend)?, LineEnd(Extend)?, VCHome(Extend)? except they behave differently when word-wrap is enabled: They go first to the start / end of the display line, like (Home\|LineEnd)Display The difference is that, the cursor is already at the point, it goes on to the start or end of the document line, as appropriate for (Home\|LineEnd\|VCHome)(Extend)?. |
| ScEditor:LineScrollDown() | Scroll the document down, keeping the caret visible. |
| ScEditor:LineScrollUp() | Scroll the document up, keeping the caret visible. |
| ScEditor:LineTranspose() | Switch the current line with the previous. |
| ScEditor:LineUp() | Move caret up one line. |
| ScEditor:LineUpExtend() | Move caret up one line extending selection to new caret position. |
| ScEditor:LineUpRectExtend() | Move caret up one line, extending rectangular selection to new caret position. |
| ScEditor:LowerCase() | Transform the selection to lower case. |
| ScEditor:NewLine() | Insert a new line, may use a CRLF, CR or LF depending on EOL mode. |
| ScEditor:PageDown() | Move caret one page down. |
| ScEditor:PageDownExtend() | Move caret one page down extending selection to new caret position. |
| ScEditor:PageDownRectExtend() | Move caret one page down, extending rectangular selection to new caret position. |
| ScEditor:PageUp() | Move caret one page up. |
| ScEditor:PageUpExtend() | Move caret one page up extending selection to new caret position. |
| ScEditor:PageUpRectExtend() | Move caret one page up, extending rectangular selection to new caret position. |
| ScEditor:ParaDown() | Move caret between paragraphs (delimited by empty lines). |
| ScEditor:ParaDownExtend() | Move caret between paragraphs (delimited by empty lines). |
| ScEditor:ParaUp() | Move caret between paragraphs (delimited by empty lines). |
| ScEditor:ParaUpExtend() | Move caret between paragraphs (delimited by empty lines). |
| int ScEditor:PrivateLexerCall(int operation, int pointer) | For private communication between an application and a known lexer. |
| ScEditor:ScrollToEnd() | Scroll to end of document. |
| ScEditor:ScrollToStart() | Scroll to start of document. |
| ScEditor:SelectionDuplicate() | Duplicate the selection. If selection empty duplicate the line containing the caret. |
| ScEditor:Tab() | If selection is empty or all on one line replace the selection with a tab character. If more than one line selected, indent the lines. |
| ScEditor:UpperCase() | Transform the selection to upper case. |
| ScEditor:VCHome() | Move caret to before first visible character on line. If already there move to first character on line. |
| ScEditor:VCHomeDisplay() | Move caret to before first visible character on display line. If already there move to first character on display line. |
| ScEditor:VCHomeDisplayExtend() | Like VCHomeDisplay but extending selection to new caret position. |
| ScEditor:VCHomeExtend() | Like VCHome but extending selection to new caret position. |
| ScEditor:VCHomeRectExtend() | Move caret to before first visible character on line. If already there move to first character on line. In either case, extend rectangular selection to new caret position. |
| ScEditor:VCHomeWrap() | These are like their namesakes Home(Extend)?, LineEnd(Extend)?, VCHome(Extend)? except they behave differently when word-wrap is enabled: They go first to the start / end of the display line, like (Home\|LineEnd)Display The difference is that, the cursor is already at the point, it goes on to the start or end of the document line, as appropriate for (Home\|LineEnd\|VCHome)(Extend)?. |
| ScEditor:VCHomeWrapExtend() | These are like their namesakes Home(Extend)?, LineEnd(Extend)?, VCHome(Extend)? except they behave differently when word-wrap is enabled: They go first to the start / end of the display line, like (Home\|LineEnd)Display The difference is that, the cursor is already at the point, it goes on to the start or end of the document line, as appropriate for (Home\|LineEnd\|VCHome)(Extend)?. |
| ScEditor:WordLeft() | Move caret left one word. |
| ScEditor:WordLeftEnd() | Move caret left one word, position cursor at end of word. |
| ScEditor:WordLeftEndExtend() | Move caret left one word, position cursor at end of word, extending selection to new caret position. |
| ScEditor:WordLeftExtend() | Move caret left one word extending selection to new caret position. |
| ScEditor:WordPartLeft() | Move to the previous change in capitalisation. |
| ScEditor:WordPartLeftExtend() | Move to the previous change in capitalisation extending selection to new caret position. |
| ScEditor:WordPartRight() | Move to the change next in capitalisation. |
| ScEditor:WordPartRightExtend() | Move to the next change in capitalisation extending selection to new caret position. |
| ScEditor:WordRight() | Move caret right one word. |
| ScEditor:WordRightEnd() | Move caret right one word, position cursor at end of word. |
| ScEditor:WordRightEndExtend() | Move caret right one word, position cursor at end of word, extending selection to new caret position. |
| ScEditor:WordRightExtend() | Move caret right one word extending selection to new caret position. |

The following constants are defined,

| Constants | 
| ------------- | 
| ANNOTATION\_BOXED | 
| ANNOTATION\_HIDDEN | 
| ANNOTATION\_INDENTED | 
| ANNOTATION\_STANDARD | 
| CARETSTYLE\_BLOCK | 
| CARETSTYLE\_INVISIBLE | 
| CARETSTYLE\_LINE | 
| CARET\_EVEN | 
| CARET\_JUMPS | 
| CARET\_SLOP | 
| CARET\_STRICT | 
| EDGE\_BACKGROUND | 
| EDGE\_LINE | 
| EDGE\_NONE | 
| INDIC0\_MASK | 
| INDIC1\_MASK | 
| INDIC2\_MASK | 
| INDICS\_MASK | 
| INDIC\_BOX | 
| INDIC\_COMPOSITIONTHICK | 
| INDIC\_COMPOSITIONTHIN | 
| INDIC\_CONTAINER | 
| INDIC\_DASH | 
| INDIC\_DIAGONAL | 
| INDIC\_DOTBOX | 
| INDIC\_DOTS | 
| INDIC\_FULLBOX | 
| INDIC\_HIDDEN | 
| INDIC\_IME | 
| INDIC\_IME\_MAX | 
| INDIC\_MAX | 
| INDIC\_PLAIN | 
| INDIC\_ROUNDBOX | 
| INDIC\_SQUIGGLE | 
| INDIC\_SQUIGGLELOW | 
| INDIC\_SQUIGGLEPIXMAP | 
| INDIC\_STRAIGHTBOX | 
| INDIC\_STRIKE | 
| INDIC\_TEXTFORE | 
| INDIC\_TT | 
| INVALID\_POSITION | 
| KEYWORDSET\_MAX | 
| MARKER\_MAX | 
| SCEN\_CHANGE | 
| SCEN\_KILLFOCUS | 
| SCEN\_SETFOCUS | 
| SCFIND\_CXX11REGEX | 
| SCFIND\_MATCHCASE | 
| SCFIND\_POSIX | 
| SCFIND\_REGEXP | 
| SCFIND\_WHOLEWORD | 
| SCFIND\_WORDSTART | 
| SCMOD\_ALT | 
| SCMOD\_CTRL | 
| SCMOD\_META | 
| SCMOD\_NORM | 
| SCMOD\_SHIFT | 
| SCMOD\_SUPER | 
| SCVS\_NONE | 
| SCVS\_RECTANGULARSELECTION | 
| SCVS\_USERACCESSIBLE | 
| SCWS\_INVISIBLE | 
| SCWS\_VISIBLEAFTERINDENT | 
| SCWS\_VISIBLEALWAYS | 
| SCWS\_VISIBLEONLYININDENT | 
| SC\_ALPHA\_NOALPHA | 
| SC\_ALPHA\_OPAQUE | 
| SC\_ALPHA\_TRANSPARENT | 
| SC\_AUTOMATICFOLD\_CHANGE | 
| SC\_AUTOMATICFOLD\_CLICK | 
| SC\_AUTOMATICFOLD\_SHOW | 
| SC\_CACHE\_CARET | 
| SC\_CACHE\_DOCUMENT | 
| SC\_CACHE\_NONE | 
| SC\_CACHE\_PAGE | 
| SC\_CARETSTICKY\_OFF | 
| SC\_CARETSTICKY\_ON | 
| SC\_CARETSTICKY\_WHITESPACE | 
| SC\_CASEINSENSITIVEBEHAVIOUR\_IGNORECASE | 
| SC\_CASEINSENSITIVEBEHAVIOUR\_RESPECTCASE | 
| SC\_CASE\_CAMEL | 
| SC\_CASE\_LOWER | 
| SC\_CASE\_MIXED | 
| SC\_CASE\_UPPER | 
| SC\_CHARSET\_8859\_15 | 
| SC\_CHARSET\_ANSI | 
| SC\_CHARSET\_ARABIC | 
| SC\_CHARSET\_BALTIC | 
| SC\_CHARSET\_CHINESEBIG5 | 
| SC\_CHARSET\_CYRILLIC | 
| SC\_CHARSET\_DEFAULT | 
| SC\_CHARSET\_EASTEUROPE | 
| SC\_CHARSET\_GB2312 | 
| SC\_CHARSET\_GREEK | 
| SC\_CHARSET\_HANGUL | 
| SC\_CHARSET\_HEBREW | 
| SC\_CHARSET\_JOHAB | 
| SC\_CHARSET\_MAC | 
| SC\_CHARSET\_OEM | 
| SC\_CHARSET\_OEM866 | 
| SC\_CHARSET\_RUSSIAN | 
| SC\_CHARSET\_SHIFTJIS | 
| SC\_CHARSET\_SYMBOL | 
| SC\_CHARSET\_THAI | 
| SC\_CHARSET\_TURKISH | 
| SC\_CHARSET\_VIETNAMESE | 
| SC\_CP\_UTF8 | 
| SC\_CURSORARROW | 
| SC\_CURSORNORMAL | 
| SC\_CURSORREVERSEARROW | 
| SC\_CURSORWAIT | 
| SC\_EFF\_QUALITY\_ANTIALIASED | 
| SC\_EFF\_QUALITY\_DEFAULT | 
| SC\_EFF\_QUALITY\_LCD\_OPTIMIZED | 
| SC\_EFF\_QUALITY\_MASK | 
| SC\_EFF\_QUALITY\_NON\_ANTIALIASED | 
| SC\_EOL\_CR | 
| SC\_EOL\_CRLF | 
| SC\_EOL\_LF | 
| SC\_FOLDACTION\_CONTRACT | 
| SC\_FOLDACTION\_EXPAND | 
| SC\_FOLDACTION\_TOGGLE | 
| SC\_FOLDLEVELBASE | 
| SC\_FOLDLEVELHEADERFLAG | 
| SC\_FOLDLEVELNUMBERMASK | 
| SC\_FOLDLEVELWHITEFLAG | 
| SC\_FONT\_SIZE\_MULTIPLIER | 
| SC\_IDLESTYLING\_AFTERVISIBLE | 
| SC\_IDLESTYLING\_ALL | 
| SC\_IDLESTYLING\_NONE | 
| SC\_IDLESTYLING\_TOVISIBLE | 
| SC\_IME\_INLINE | 
| SC\_IME\_WINDOWED | 
| SC\_INDICFLAG\_VALUEFORE | 
| SC\_INDICVALUEBIT | 
| SC\_INDICVALUEMASK | 
| SC\_IV\_LOOKBOTH | 
| SC\_IV\_LOOKFORWARD | 
| SC\_IV\_NONE | 
| SC\_IV\_REAL | 
| SC\_LINE\_END\_TYPE\_DEFAULT | 
| SC\_LINE\_END\_TYPE\_UNICODE | 
| SC\_MARGINOPTION\_NONE | 
| SC\_MARGINOPTION\_SUBLINESELECT | 
| SC\_MARGIN\_BACK | 
| SC\_MARGIN\_FORE | 
| SC\_MARGIN\_NUMBER | 
| SC\_MARGIN\_RTEXT | 
| SC\_MARGIN\_SYMBOL | 
| SC\_MARGIN\_TEXT | 
| SC\_MASK\_FOLDERS | 
| SC\_MAX\_MARGIN | 
| SC\_MULTIAUTOC\_EACH | 
| SC\_MULTIAUTOC\_ONCE | 
| SC\_MULTIPASTE\_EACH | 
| SC\_MULTIPASTE\_ONCE | 
| SC\_ORDER\_CUSTOM | 
| SC\_ORDER\_PERFORMSORT | 
| SC\_ORDER\_PRESORTED | 
| SC\_PHASES\_MULTIPLE | 
| SC\_PHASES\_ONE | 
| SC\_PHASES\_TWO | 
| SC\_PRINT\_BLACKONWHITE | 
| SC\_PRINT\_COLOURONWHITE | 
| SC\_PRINT\_COLOURONWHITEDEFAULTBG | 
| SC\_PRINT\_INVERTLIGHT | 
| SC\_PRINT\_NORMAL | 
| SC\_SEL\_LINES | 
| SC\_SEL\_RECTANGLE | 
| SC\_SEL\_STREAM | 
| SC\_SEL\_THIN | 
| SC\_STATUS\_BADALLOC | 
| SC\_STATUS\_FAILURE | 
| SC\_STATUS\_OK | 
| SC\_STATUS\_WARN\_REGEX | 
| SC\_STATUS\_WARN\_START | 
| SC\_TECHNOLOGY\_DEFAULT | 
| SC\_TECHNOLOGY\_DIRECTWRITE | 
| SC\_TECHNOLOGY\_DIRECTWRITEDC | 
| SC\_TECHNOLOGY\_DIRECTWRITERETAIN | 
| SC\_TIME\_FOREVER | 
| SC\_TYPE\_BOOLEAN | 
| SC\_TYPE\_INTEGER | 
| SC\_TYPE\_STRING | 
| SC\_WEIGHT\_BOLD | 
| SC\_WEIGHT\_NORMAL | 
| SC\_WEIGHT\_SEMIBOLD | 
| SC\_WRAPINDENT\_FIXED | 
| SC\_WRAPINDENT\_INDENT | 
| SC\_WRAPINDENT\_SAME | 
| SC\_WRAPVISUALFLAGLOC\_DEFAULT | 
| SC\_WRAPVISUALFLAGLOC\_END\_BY\_TEXT | 
| SC\_WRAPVISUALFLAGLOC\_START\_BY\_TEXT | 
| SC\_WRAPVISUALFLAG\_END | 
| SC\_WRAPVISUALFLAG\_MARGIN | 
| SC\_WRAPVISUALFLAG\_NONE | 
| SC\_WRAPVISUALFLAG\_START | 
| SC\_WRAP\_CHAR | 
| SC\_WRAP\_NONE | 
| SC\_WRAP\_WHITESPACE | 
| SC\_WRAP\_WORD | 
| STYLE\_BRACEBAD | 
| STYLE\_BRACELIGHT | 
| STYLE\_CALLTIP | 
| STYLE\_CONTROLCHAR | 
| STYLE\_DEFAULT | 
| STYLE\_INDENTGUIDE | 
| STYLE\_LASTPREDEFINED | 
| STYLE\_LINENUMBER | 
| STYLE\_MAX | 
| UNDO\_MAY\_COALESCE | 
| VISIBLE\_SLOP | 
| VISIBLE\_STRICT | 


More information is available in the [official documentation](http://www.scintilla.org/ScintillaDoc.html).
