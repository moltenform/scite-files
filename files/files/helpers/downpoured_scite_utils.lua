-- downpoured_scite_utils.lua
-- by Ben Fisher, 2018
-- instructions + examples:
-- https://github.com/downpoured/scite-files/tree/master/files/files/helpers/adding_scite_features_with_lua.md
-- list of available methods+documentation:
-- https://github.com/downpoured/scite-files/tree/master/files/files/helpers/downpoured_scite_utils_api.md

----------------------------------------------------------------------
-- inheritsFrom
-- http://lua-users.org/wiki/InheritanceTutorial
----------------------------------------------------------------------
function inheritsFrom(baseClass)
    local new_class = {}
    local class_mt = { __index = new_class }
    function new_class:create()
        local newinst = {}
        setmetatable( newinst, class_mt )
        return newinst
    end
    if nil ~= baseClass then
        setmetatable( new_class, { __index = baseClass } )
    end

    -- Return the class object of the instance
    function new_class:class()
        return new_class
    end

    -- Return the super class object of the instance
    function new_class:superClass()
        return baseClass
    end
    
    -- Return true if the caller is an instance of theClass
    function new_class:isa( theClass )
        local b_isa = false
        local cur_class = new_class
        while ( nil ~= cur_class ) and ( false == b_isa ) do
            if cur_class == theClass then
                b_isa = true
            else
                cur_class = cur_class:superClass()
            end
        end

        return b_isa
    end

    return new_class
end

----------------------------------------------------------------------
-- ScAppClass
-- I've gathered all the common commands that act on
-- the scite application into this class
----------------------------------------------------------------------
local ScAppClass = inheritsFrom(nil)
function ScAppClass:Init(s)
end

function ScAppClass:Trace(s)
    trace(s)
end

function ScAppClass:OpenFile(s)
    scite.Open(s)
end

function ScAppClass:GetProperty(s)
    return props[s]
end

function ScAppClass:SetProperty(s, v)
    props[s] = v
end

function ScAppClass:UnsetProperty(s, v)
    props[s] = nil
end

function ScAppClass:UpdateStatusBar(updateSlowData)
    if updateSlowData == nil then updateSlowData = false end
    scite.UpdateStatusBar(updateSlowData)
end

function ScAppClass:GetFilePath(cannotBeUntitled)
    if cannotBeUntitled == nil then cannotBeUntitled = true end
    if cannotBeUntitled then
        -- we usually don't want untitled documents to look like they have a path
        if self:GetProperty('FilePath') ~= nil and self:GetProperty('FilePath'):len() > 0 then
            return self:GetProperty('FilePath')
        else
            return ''
        end
    else
        return self:GetProperty('FilePath')
    end
end

function ScAppClass:GetFileName()
    return self:GetProperty('FileNameExt')
end

function ScAppClass:GetFileDirectory()
    return self:GetProperty('FileDir')
end

function ScAppClass:GetSciteDirectory()
    return self:GetProperty('SciteDefaultHome')
end

function ScAppClass:GetSciteUserDirectory()
    return self:GetProperty('SciteUserHome')
end

function ScAppClass:RunToolCmd(n)
    return scite.MenuCommand(1100+n)
end

-- constants like SCMOD_SHIFT are placed in global scope, so no need for a function. 
-- no need for MakeKeymod, lua extension has special logic for iface_keymod and takes 2 integers

function ScAppClass:MakeColor(red, green, blue)
        assert((0 <= red) and (red <= 255))
        assert((0 <= green) and (green <= 255))
        assert((0 <= blue) and (blue<= 255))
        return red + (green << 8) + (blue << 16)
end

function ScAppClass:GetColor(val)
        local red = val & 0x000000ff
        local green = (val & 0x0000ff00) >> 8
        local blue = (val & 0x000ff0000) >> 16
        return red, green, blue
end

function ScAppClass:abbrev() return scite.MenuCommand(242) end
function ScAppClass:about() return scite.MenuCommand(902) end
function ScAppClass:activate() return scite.MenuCommand(320) end
function ScAppClass:allowaccess() return scite.MenuCommand(119) end
function ScAppClass:block_comment() return scite.MenuCommand(243) end
function ScAppClass:bookmark_clearall() return scite.MenuCommand(224) end
function ScAppClass:bookmark_next() return scite.MenuCommand(221) end
function ScAppClass:bookmark_next_select() return scite.MenuCommand(225) end
function ScAppClass:bookmark_prev() return scite.MenuCommand(223) end
function ScAppClass:bookmark_prev_select() return scite.MenuCommand(226) end
function ScAppClass:bookmark_select_all() return scite.MenuCommand(227) end
function ScAppClass:bookmark_toggle() return scite.MenuCommand(222) end
function ScAppClass:box_comment() return scite.MenuCommand(246) end
function ScAppClass:buffer() return scite.MenuCommand(1200) end
function ScAppClass:buffersep() return scite.MenuCommand(505) end
function ScAppClass:build() return scite.MenuCommand(302) end
function ScAppClass:clean() return scite.MenuCommand(308) end
function ScAppClass:clear() return scite.MenuCommand(206) end
function ScAppClass:clearoutput() return scite.MenuCommand(420) end
function ScAppClass:close() return scite.MenuCommand(105) end
function ScAppClass:closeall() return scite.MenuCommand(503) end
function ScAppClass:compile() return scite.MenuCommand(301) end
function ScAppClass:complete() return scite.MenuCommand(233) end
function ScAppClass:completeword() return scite.MenuCommand(234) end
function ScAppClass:copy() return scite.MenuCommand(204) end
function ScAppClass:copyasrtf() return scite.MenuCommand(245) end
function ScAppClass:copypath() return scite.MenuCommand(118) end
function ScAppClass:cut() return scite.MenuCommand(203) end
function ScAppClass:directiondown() return scite.MenuCommand(806) end
function ScAppClass:directionup() return scite.MenuCommand(805) end
function ScAppClass:duplicate() return scite.MenuCommand(250) end
function ScAppClass:encoding_default() return scite.MenuCommand(150) end
function ScAppClass:encoding_ucookie() return scite.MenuCommand(154) end
function ScAppClass:encoding_ucs2be() return scite.MenuCommand(151) end
function ScAppClass:encoding_ucs2le() return scite.MenuCommand(152) end
function ScAppClass:encoding_utf8() return scite.MenuCommand(153) end
function ScAppClass:enterselection() return scite.MenuCommand(256) end
function ScAppClass:eol_convert() return scite.MenuCommand(433) end
function ScAppClass:eol_cr() return scite.MenuCommand(431) end
function ScAppClass:eol_crlf() return scite.MenuCommand(430) end
function ScAppClass:eol_lf() return scite.MenuCommand(432) end
function ScAppClass:expand() return scite.MenuCommand(235) end
function ScAppClass:expand_ensurechildrenvisible() return scite.MenuCommand(238) end
function ScAppClass:filer() return scite.MenuCommand(114) end
function ScAppClass:find() return scite.MenuCommand(210) end
function ScAppClass:findinfiles() return scite.MenuCommand(215) end
function ScAppClass:findnext() return scite.MenuCommand(211) end
function ScAppClass:findnextback() return scite.MenuCommand(212) end
function ScAppClass:findnextbacksel() return scite.MenuCommand(214) end
function ScAppClass:findnextsel() return scite.MenuCommand(213) end
function ScAppClass:finishedexecute() return scite.MenuCommand(305) end
function ScAppClass:foldmargin() return scite.MenuCommand(406) end
function ScAppClass:fullscreen() return scite.MenuCommand(961) end
function ScAppClass:go() return scite.MenuCommand(303) end
function ScAppClass:dlg_goto() return scite.MenuCommand(220) end
function ScAppClass:help() return scite.MenuCommand(901) end
function ScAppClass:help_scite() return scite.MenuCommand(903) end
function ScAppClass:import() return scite.MenuCommand(1300) end
function ScAppClass:incsearch() return scite.MenuCommand(252) end
function ScAppClass:ins_abbrev() return scite.MenuCommand(247) end
function ScAppClass:join() return scite.MenuCommand(248) end
function ScAppClass:language() return scite.MenuCommand(1400) end
function ScAppClass:linenumbermargin() return scite.MenuCommand(407) end
function ScAppClass:linereverse() return scite.MenuCommand(218) end
function ScAppClass:loadsession() return scite.MenuCommand(132) end
function ScAppClass:lwrcase() return scite.MenuCommand(241) end
function ScAppClass:macrolist() return scite.MenuCommand(314) end
function ScAppClass:macroplay() return scite.MenuCommand(313) end
function ScAppClass:macrorecord() return scite.MenuCommand(311) end
function ScAppClass:macrostoprecord() return scite.MenuCommand(312) end
function ScAppClass:macro_sep() return scite.MenuCommand(310) end
function ScAppClass:matchbrace() return scite.MenuCommand(230) end
function ScAppClass:matchcase() return scite.MenuCommand(801) end
function ScAppClass:monofont() return scite.MenuCommand(450) end
function ScAppClass:movetableft() return scite.MenuCommand(509) end
function ScAppClass:movetabright() return scite.MenuCommand(508) end
function ScAppClass:mrufile() return scite.MenuCommand(1000) end
function ScAppClass:mru_sep() return scite.MenuCommand(120) end
function ScAppClass:mru_sub() return scite.MenuCommand(121) end
function ScAppClass:menunew() return scite.MenuCommand(101) end
function ScAppClass:nextfile() return scite.MenuCommand(502) end
function ScAppClass:nextfilestack() return scite.MenuCommand(507) end
function ScAppClass:nextmatchppc() return scite.MenuCommand(262) end
function ScAppClass:nextmsg() return scite.MenuCommand(306) end
function ScAppClass:ontop() return scite.MenuCommand(960) end
function ScAppClass:open() return scite.MenuCommand(102) end
function ScAppClass:openabbrevproperties() return scite.MenuCommand(463) end
function ScAppClass:opendirectoryproperties() return scite.MenuCommand(465) end
function ScAppClass:openfileshere() return scite.MenuCommand(413) end
function ScAppClass:openglobalproperties() return scite.MenuCommand(462) end
function ScAppClass:openlocalproperties() return scite.MenuCommand(460) end
function ScAppClass:openluaexternalfile() return scite.MenuCommand(464) end
function ScAppClass:openselected() return scite.MenuCommand(103) end
function ScAppClass:openuserproperties() return scite.MenuCommand(461) end
function ScAppClass:paste() return scite.MenuCommand(205) end
function ScAppClass:pasteanddown() return scite.MenuCommand(208) end
function ScAppClass:prevfile() return scite.MenuCommand(501) end
function ScAppClass:prevfilestack() return scite.MenuCommand(506) end
function ScAppClass:prevmatchppc() return scite.MenuCommand(260) end
function ScAppClass:prevmsg() return scite.MenuCommand(307) end
function ScAppClass:menuprint() return scite.MenuCommand(131) end
function ScAppClass:printsetup() return scite.MenuCommand(130) end
function ScAppClass:quit() return scite.MenuCommand(140) end
function ScAppClass:readonly() return scite.MenuCommand(416) end
function ScAppClass:redo() return scite.MenuCommand(202) end
function ScAppClass:regexp() return scite.MenuCommand(802) end
function ScAppClass:replace() return scite.MenuCommand(216) end
function ScAppClass:revert() return scite.MenuCommand(104) end
function ScAppClass:runwin() return scite.MenuCommand(351) end
function ScAppClass:save() return scite.MenuCommand(106) end
function ScAppClass:saveacopy() return scite.MenuCommand(116) end
function ScAppClass:saveall() return scite.MenuCommand(504) end
function ScAppClass:saveas() return scite.MenuCommand(110) end
function ScAppClass:saveashtml() return scite.MenuCommand(111) end
function ScAppClass:saveaspdf() return scite.MenuCommand(113) end
function ScAppClass:saveasrtf() return scite.MenuCommand(112) end
function ScAppClass:saveastex() return scite.MenuCommand(115) end
function ScAppClass:saveasxml() return scite.MenuCommand(117) end
function ScAppClass:savesession() return scite.MenuCommand(133) end
function ScAppClass:selectall() return scite.MenuCommand(207) end
function ScAppClass:selectionaddeach() return scite.MenuCommand(258) end
function ScAppClass:selectionaddnext() return scite.MenuCommand(257) end
function ScAppClass:selection_for_find() return scite.MenuCommand(217) end
function ScAppClass:selecttobrace() return scite.MenuCommand(231) end
function ScAppClass:selecttonextmatchppc() return scite.MenuCommand(263) end
function ScAppClass:selecttoprevmatchppc() return scite.MenuCommand(261) end
function ScAppClass:selmargin() return scite.MenuCommand(405) end
function ScAppClass:showcalltip() return scite.MenuCommand(232) end
function ScAppClass:split() return scite.MenuCommand(249) end
function ScAppClass:splitvertical() return scite.MenuCommand(401) end
function ScAppClass:srcwin() return scite.MenuCommand(350) end
function ScAppClass:statuswin() return scite.MenuCommand(353) end
function ScAppClass:stopexecute() return scite.MenuCommand(304) end
function ScAppClass:stream_comment() return scite.MenuCommand(244) end
function ScAppClass:switchpane() return scite.MenuCommand(421) end
function ScAppClass:tabsize() return scite.MenuCommand(440) end
function ScAppClass:tabwin() return scite.MenuCommand(354) end
function ScAppClass:toggleoutput() return scite.MenuCommand(409) end
function ScAppClass:toggleparameters() return scite.MenuCommand(412) end
function ScAppClass:toggle_foldall() return scite.MenuCommand(236) end
function ScAppClass:toggle_foldrecursive() return scite.MenuCommand(237) end
function ScAppClass:tools() return scite.MenuCommand(1100) end
function ScAppClass:toolwin() return scite.MenuCommand(352) end
function ScAppClass:undo() return scite.MenuCommand(201) end
function ScAppClass:unslash() return scite.MenuCommand(804) end
function ScAppClass:uprcase() return scite.MenuCommand(240) end
function ScAppClass:vieweol() return scite.MenuCommand(403) end
function ScAppClass:viewguides() return scite.MenuCommand(404) end
function ScAppClass:viewspace() return scite.MenuCommand(402) end
function ScAppClass:viewstatusbar() return scite.MenuCommand(411) end
function ScAppClass:viewtabbar() return scite.MenuCommand(410) end
function ScAppClass:viewtoolbar() return scite.MenuCommand(408) end
function ScAppClass:wholeword() return scite.MenuCommand(800) end
function ScAppClass:wrap() return scite.MenuCommand(414) end
function ScAppClass:wraparound() return scite.MenuCommand(803) end
function ScAppClass:wrapoutput() return scite.MenuCommand(415) end
ScApp = ScAppClass:create()
ScApp:Init()

----------------------------------------------------------------------
-- ScToolUIManagerClass
-- wrapper for showing custom ui in a strip
-- you should create an instance of ScToolUIBase and pass it in as toolUI
-- refer to https://github.com/downpoured/scite-files/tree/master/files/files/helpers/adding_scite_features_with_lua.md
----------------------------------------------------------------------
local ScToolUIManagerClass = inheritsFrom(nil)
function ScToolUIManagerClass:Init()
    self.currentUserStrip = nil
    self.eventIsRegisteredWithExtman = false
end

function ScToolUIManagerClass:UserStripSet(toolUI, control, value)
    -- toolUI should be an instance of ScToolUIBase
    self:EnsureActive(toolUI)
    return scite.StripSet(control, value)
end

function ScToolUIManagerClass:UserStripSetList(toolUI, control, value)
    self:EnsureActive(toolUI)
    return scite.StripSetList(control, value)
end

function ScToolUIManagerClass:UserStripGetValue(toolUI, control)
    self:EnsureActive(toolUI)
    return scite.StripValue(control)
end

function ScToolUIManagerClass:OnUserStrip(control, eventType)
    if self.currentUserStrip then
        self.currentUserStrip:OnRawEvent(control, eventType)
    end
end

function ScToolUIManagerClass:Show(toolUI)
    if toolUI.spec then
        scite.StripShow(toolUI.spec)
    else
        scite.StripShow('')
    end
    self.currentUserStrip = toolUI
end

function ScToolUIManagerClass:EnsureActive(toolUI)
    if toolUI then
        if not toolUI.isScToolUIBase then
            assert(false, 'param toolUI should be an instance of ScToolUIBase')
        end
    end
    if self.currentUserStrip ~= toolUI then
        assert(false, 'the UI object is no longer active')
    end
end

function ScToolUIManagerClass:RegisterEventWithExtman()
    -- I'd do this automatically, but that would create a hard dependency on extman,
    -- and it'd be better if people could use this script without needing extman.
    if self.eventIsRegisteredWithExtman then
    else
        scite_OnUserStrip(
            function(a,b) self:OnUserStrip(a,b) end
        )
        self.eventIsRegisteredWithExtman = true
    end
end

ScToolUIManager = ScToolUIManagerClass:create()
ScToolUIManager:Init()

-- to use ScToolUIManager, you will need to add the following lines to at least one of your scripts:
-- require('path/to/extman')
-- ScToolUIManager:RegisterEventWithExtman()

----------------------------------------------------------------------
-- ScToolUIBase
-- you can use a class derived from ScToolUIBase to draw a strip dialog ui
-- refer to https://github.com/downpoured/scite-files/tree/master/files/files/helpers/adding_scite_features_with_lua.md
----------------------------------------------------------------------
ScToolUIBase = inheritsFrom(nil)
function ScToolUIBase:Init()
    self.isScToolUIBase = true
    self.spec=''
    self.currentNumber = 0
    self.callbackOnClick = {}
    
    self.currentlyBuilding = true
    self:AddControls()
    self.currentlyBuilding = false
    
    -- define constants
    self.eventTypeUnknown = 0
    self.eventTypeClicked = 1
    self.eventTypeChange = 2
    self.eventTypeFocusIn = 3
    self.eventTypeFocusOut = 4
end

function ScToolUIBase:Show()
    ScToolUIManager:Show(self)
    self:OnOpen()
end
    
function ScToolUIBase:Close()
    ScToolUIManager:Show(nil)
end
    
function ScToolUIBase:AddLabel(text)
    return self:_add(text, "'", "'")
end
    
function ScToolUIBase:AddButton(text, callback, closes, default)
    if callback == nil then callback = nil end
    if closes == nil then closes = false end
    if defaultbtn == nil then defaultbtn = false end
    if defaultbtn then
        return self:_add(text, '((', '))', callback, closes)
    else
        return self:_add(text, '(', ')', callback, closes)
    end
end
    
function ScToolUIBase:AddCombo()
    return self:_add('', '{', '}')
end
    
function ScToolUIBase:AddEntry(text)
    return self:_add(text, '[', ']')
end
    
function ScToolUIBase:AddRow()
    return self:_add('\n', '', '', nil, nil, true)
end
    
function ScToolUIBase:_add(text, start, paramend, callback, closes, noNumber)
    if callback == nil then callback = nil end
    if closes == nil then closes = false end
    if noNumber == nil then noNumber = false end
    assert(self.currentlyBuilding, 'Controls can only be added within AddControls().')
    self.spec = self.spec .. start .. text .. paramend
    
    self.callbackOnClick[self.currentNumber] = {callback, closes}
    local ret = self.currentNumber
    if not noNumber then
        self.currentNumber = self.currentNumber + 1
    end
    return ret
end

function ScToolUIBase:OnRawEvent(control, eventType)
    -- if the implementation class wants, it can see the raw event too
    local res = self:OnEvent(control, eventType)
    if res then
        return nil
    end
    
    if eventType == self.eventTypeClicked then
        local foundcallback = nil
        local foundcloses = nil
        for index, value in ipairs(self.callbackOnClick) do
            if index == control then
                foundcallback = value[1]
                foundcloses = value[2]
                break
            end
        end
    
        if foundcallback then
            foundcallback()
        end
        if foundcloses then
            self:Close()
        end
    end
end

function ScToolUIBase:Get(control)
    return ScToolUIManager:UserStripGetValue(self, control)
end

function ScToolUIBase:Set(control, val)
    return ScToolUIManager:UserStripSet(self, control, val)
end
    
function ScToolUIBase:SetList(control, val)
    -- val delimited by \n newlines
    return ScToolUIManager:UserStripSetList(self, control, val)
end

-- for the implementation class to override
function ScToolUIBase:AddControls()
    print('please implement AddControls in your child class')
end
    
function ScToolUIBase:OnOpen()
    print('please implement OnOpen in your child class')
end
    
function ScToolUIBase:OnEvent(control, eventType)
    -- implement, if desired, in a child class
end

function stringstartswith(s,start)
   return string.sub(s,1,start:len())==start
end

function stringendswith(str, ending)
   return ending == "" or str:sub(-#ending) == ending
end

----------------------------------------------------------------------
-- ScEditor and ScOutput
-- I've gathered all the common commands that act on
-- editing or output panes into this class
----------------------------------------------------------------------
local function isAScintillaFunction(pane, key)
    local closure = nil
    local status, err = pcall(function() closure = pane[key] end)
    if not status then
         if tostring(err):find("Pane function / readable property") then
            return nil
        else
            assert(false, 'error ' .. tostring(err))
        end
    end
    return closure
end

function makePanelObj(paneImpl, paneNum)
    local ret = {}
    ret.pane = paneImpl
    ret.paneNum = paneNum
    ret.PaneAppend = function(self, txt)
        -- Append text
        return self.pane:append(txt)
    end
    
    ret.GetEolCharacter = function(self)
        -- Return current EOL character, e.g. \r\n
        local n = self:GetEOLMode()
        if n == 0 then
            return '\r\n'
        elseif n == 1 then
            return '\r'
        else
            return '\n'
        end
    end
    
    ret.PaneInsertText = function(self, txt, pos)
        -- Insert text, without changing selection
        return self.pane:insert(pos, txt)
    end
        
    ret.PaneWrite = function(self, txt, pos)
        -- Insert text, and update selection as if the text was typed in
        if not pos then
            pos = self.pane.CurrentPos
        end
        
        self.pane:insert(pos, txt)
        self.pane:GotoPos(pos + txt:len())
    end
    
    ret.PaneRemoveText = function(self, npos1, npos2)
        -- Remove text between these positions
        return self.pane:remove(npos1, npos2)
    end
        
    ret.PaneGetTextRange = function(self, n1, n2)
        -- Get text between these positions
        return self.pane:textrange(n1, n2)
    end

    ret.PaneFindText = function(self, s, pos1, pos2, wholeWord, matchCase, regExp, flags)
        if pos1 == nil then pos1 = 0 end
        if pos2 == nil then pos2 = -1 end
        if wholeWord == nil then wholeWord = false end
        if matchCase == nil then matchCase = false end
        if regExp == nil then regExp = false end
        if flags == nil then flags = 0 end
        
        -- Find text
        if wholeWord then
            flags = flags|SCFIND_WHOLEWORD
        end
        if matchCase then
            flags = flags|SCFIND_MATCHCASE
        end
        if regExp then
            flags = flags|SCFIND_REGEXP
        end
            
        return self.pane:findtext(s, flags, pos1, pos2)
    end
    
    -- helpers where the Scintilla version is less convenient to use
    ret.GetLineText = function(self, line)
        -- Returns text of specified line
        return self:GetLine(line)
    end

    ret.GetSelectedText = function(self)
        -- Returns selected text
        return self:GetSelText()
    end
        
    ret.GetCurrentLineText = function(self)
        -- Returns text of current line
        return self:GetCurLine()
    end
    
    local mt = {
    __index = function(self, key)
        -- in my opinion, the Scintilla api is a bit harder to use
        -- because when retrieving info, sometimes you have to say
        -- a = editor.Foo
        -- and other times
        -- a = editor:GetBar()
        -- and also,
        -- editor.Foo = 2
        -- and other times
        -- editor.SetBar(2)
        -- with this wrapper,
        -- the syntax is always :GetBar() and :SetBar(2)
        
        -- is it a function?
        local closure = isAScintillaFunction(self.pane, key)
        if closure then
            return closure
        end
        
        -- is it a property?
        if stringstartswith(key, 'Get') then
            shortkey = key:sub(4, -1)
            return function()
                return self.pane[shortkey]
            end
        elseif stringstartswith(key, 'Set') then
            shortkey = key:sub(4, -1)
            return function(slf, v)
                self.pane[shortkey] = v
            end
        end
    
        -- unknown method
        assert(false, 'unknown method '..key)
    end,
    
    __newindex = function (t,k,v)
        assert(false, 'use a "set" method instead, tried to modify '..k)
    end
    }
    
    setmetatable(ret, mt)
    return ret
end

ScEditor = makePanelObj(editor, 0)
ScOutput = makePanelObj(output, 1)

-- Credit: scite-ru
-- https://bitbucket.org/scite-ru/scite-ru.bitbucket.org/src
-- is the position part of a comment
function IsComment(pos)
    local style = editor.StyleAt[pos]
    local lexer = props['Language']
    local comment = {
        abap = {1, 2},
        ada = {10},
        asm = {1, 11},
        au3 = {1, 2},
        baan = {1, 2},
        bullant = {1, 2, 3},
        caml = {12, 13, 14, 15},
        cpp = {1, 2, 3, 15, 17, 18},
        csound = {1, 9},
        css = {9},
        d = {1, 2, 3, 4, 15, 16, 17},
        escript = {1, 2, 3},
        euphoria = {1, 18},
        flagship = {1, 2, 3, 4, 5, 6},
        forth = {1, 2, 3},
        gap = {9},
        hypertext = {9, 20, 29, 42, 43, 44, 57, 58, 59, 72, 82, 92, 107, 124, 125},
        xml = {9, 29},
        inno = {1, 7},
        latex = {4},
        lua = {1, 2, 3},
        script_lua = {4, 5},
        mmixal = {1, 17},
        nsis = {1, 18},
        opal = {1, 2},
        pascal = {2, 3, 4},
        perl = {2},
        bash = {2},
        pov = {1, 2},
        ps = {1, 2, 3},
        python = {1, 12},
        rebol = {1, 2},
        ruby = {2},
        scriptol = {2, 3, 4, 5},
        smalltalk = {3},
        specman = {2, 3},
        spice = {8},
        sql = {1, 2, 3, 13, 15, 17, 18},
        tcl = {1, 2, 20, 21},
        verilog = {1, 2, 3},
        vhdl = {1, 2}
    }

    for l,ts in pairs(comment) do
        if l == lexer then
            for _,s in pairs(ts) do
                if s == style then
                    return true
                end
            end
            return false
        end
    end
    -- asn1, ave, blitzbasic, cmake, conf, eiffel, eiffelkw, erlang, euphoria, fortran, f77, freebasic, kix, lisp, lout, octave, matlab, metapost, nncrontab, props, batch, makefile, diff, purebasic, vb, yaml
    if style == 1 then return true end
    return false
end

function printTable(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. printTable(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end


