
-- from the Scite-ru project, https://bitbucket.org/scite-ru/scite-ru.bitbucket.org/wiki/Home

function move_or_copy_lines(action, direction)
	editor:BeginUndoAction()
	local start_line = editor:LineFromPosition(editor.SelectionStart)
	local end_line = editor:LineFromPosition(editor.SelectionEnd)
	local start_pos = editor:PositionFromLine(start_line)
	local end_pos = editor:PositionFromLine(end_line) + editor:LineLength(end_line)
	editor:SetSel(start_pos, end_pos)
	local text, length = editor:GetSelText()
	local target_line = nil
	if action == 'move' then
		if direction == 'up' then
			target_line = start_line - 2 -- move up
		else -- direction == 'down'
			target_line = start_line -- move down
		end
	else -- action == 'copy'
		if direction == 'up' then
			target_line = start_line - 1 -- copy up
		else -- direction == 'down'
			target_line = start_line + (end_line - start_line) -- copy down
		end
	end
	if action == 'move' then
		editor:DeleteBack()
	end
	local target_pos = editor:PositionFromLine(target_line) + editor:LineLength(target_line)
	editor:InsertText(target_pos, text)
	editor:SetSel(target_pos, target_pos + length - 2)

	-- set indention
	start_line = editor:LineFromPosition(editor.SelectionStart)
	end_line = editor:LineFromPosition(editor.SelectionEnd)
	local min_indention = math.huge
	local indention_table = {}
	local i = 1
	local indention = nil
	for line = start_line, end_line, 1 do
		indention = editor.LineIndentation[line]
		min_indention = math.min(min_indention, indention)
		indention_table[i] = indention
		i = i + 1
	end
	for i,v in pairs(indention_table) do
		indention_table[i] = v - min_indention
	end
	i = 1
	indention = math.max(
		editor.LineIndentation[start_line - 1], editor.LineIndentation[end_line + 1])
	for line = start_line, end_line, 1 do
		editor.LineIndentation[line] = indention + indention_table[i]
		i = i + 1
	end
	editor:EndUndoAction()

end

function move_lines_up()
	move_or_copy_lines('move', 'up')
end

function move_lines_down()
	move_or_copy_lines('move', 'down')
end

function copy_lines_up()
	move_or_copy_lines('copy', 'up')
end

function copy_lines_down()
	move_or_copy_lines('copy', 'down')
end


--~ scite_Command 'Move lines up|move_lines_up|Alt+Up'
--~ scite_Command 'Move lines down|move_lines_down|Alt+Down'
--~ scite_Command 'Copy lines up|copy_lines_up|Ctrl+Alt+Up'
--~ scite_Command 'Copy lines down|copy_lines_down|Ctrl+Alt+Down'
