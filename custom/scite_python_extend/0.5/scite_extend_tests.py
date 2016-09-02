# SciTE Python Extension
# Ben Fisher, 2011

import CScite
from CScite import ScEditor, ScOutput, ScApp
import exceptions
import sys

CurrentPane = ScEditor # press Ctrl+' to switch
winNewLines = True


def test_0_0():
	import base64 #try importing a nontrivial library, loads from python25.zip
	import ctypes #try importing a nontrivial library, loads from python25.zip and _ctypes

	ScApp.MsgBox('Test:MessageBox')
	ScApp.Trace('Test:')
	ScApp.Trace('Tracing')

def test_0_1():
	ScOutput.ClearAll()
	ScApp.Trace('abc')
	expectEqual(ScOutput.GetAllText(), 'abc')
	ScOutput.ClearAll()
	expectEqual(ScOutput.GetAllText(), '')
	ScOutput.ClearAll()
	ScApp.Trace('AA'); ScApp.Trace('BB'); ScApp.Trace('CC')
	expectEqual(ScOutput.GetAllText(), 'AABBCC')
	
	expectEqual(ScApp.GetProperty('tabbar.visible') , '1')
	expectEqual(ScApp.GetProperty('margin.width') , '16')
	expectEqual(ScApp.GetProperty('a.new.prop') , '')
	for prop in ('tabbar.visible', 'margin.width', 'a.new.prop'):
		print '%s=%s'%(prop, ScApp.GetProperty(prop))
	ScApp.SetProperty('a.new.prop', 'abc')
	expectEqual(ScApp.GetProperty('a.new.prop') , 'abc')
	ScApp.SetProperty('a.new.prop', 'def')
	expectEqual(ScApp.GetProperty('a.new.prop') , 'def')
	ScApp.UnsetProperty('a.new.prop')
	expectEqual(ScApp.GetProperty('a.new.prop') , '')
	
	expectThrow( (lambda: ScApp._specialatt), '', exceptions.AttributeError)
	expectThrow( (lambda: ScApp.nonExist()), 'Could not find command')
	expectThrow( (lambda: ScApp.nonExist(1)), 'takes no arguments', exceptions.TypeError )
	expectThrow( (lambda: ScApp.NON_EXIST), 'Could not find constant')
	expectThrow( (lambda: ScApp.NON_EXIST(1)), 'Could not find constant')
	expectThrow( (lambda: ScApp.Close(1)), 'takes no arguments', exceptions.TypeError )
	
	# test constants
	expectEqual(ScApp.SCFIND_WHOLEWORD, 2)
	expectEqual(ScApp.SCFIND_MATCHCASE, 4)
	expectEqual(ScApp.SCFIND_WORDSTART, 0x00100000)
	expectEqual(ScApp.SCFIND_REGEXP, 0x00200000)
	expectEqual(ScApp.SCFIND_POSIX, 0x00400000)
	expectEqual(ScApp.SC_CHARSET_CHINESEBIG5, 136)
	expectEqual(ScApp.SC_MOD_INSERTTEXT, 1)
	
	# not sure how to test this, but at least it shouldn't throw an error
	ScApp.UpdateStatusBar()
	ScApp.UpdateStatusBar(True)
	ScApp.UpdateStatusBar(False)
	
	# test commands that can be verified by script
	ScApp.Trace('abc')
	ScApp.ClearOutput()
	expectEqual(ScOutput.GetAllText(), '')
	
	ScEditor.ClearAll()
	ScEditor.Write('h')
	ScApp.Duplicate()
	expectEqual(ScEditor.GetAllText(), 'h\r\nh' if winNewLines else 'h\nh')
	
	ScEditor.ClearAll()
	ScEditor.Write('ABCabcABC')
	ScApp.SelectAll()
	ScApp.LwrCase()
	expectEqual(ScEditor.GetAllText(), 'abcabcabc')
	
	ScEditor.ClearAll()
	ScEditor.Write('qq')
	ScApp.SelectAll()
	ScApp.Cut()
	ScApp.Paste()
	ScApp.Paste()
	ScApp.Paste()
	expectEqual(ScEditor.GetAllText(), 'qqqqqq')
	
	ScEditor.ClearAll()
	ScEditor.Write('g')
	ScApp.SelectAll()
	ScApp.UprCase()
	ScApp.Copy()
	ScApp.Paste() #replaces selection
	ScApp.Paste()
	expectEqual(ScEditor.GetAllText(), 'GG')
	
	ScApp.CopyPath()

def test_0_2():
	print 'Goto'
	ScApp.Goto()
	print 'About'
	ScApp.About()
	print 'SaveSession...'
	ScApp.SaveSession()
	
	ScApp.OpenFile('nonexist.test')
	ScApp.MsgBox( 'Opened.')
	ScApp.Close()
	ScApp.MsgBox( 'Closed.')
	
	toggles = ((ScApp.SelMargin, 'SelMargin'),(ScApp.ToggleOutput, 'ToggleOutput'),
		(ScApp.ToggleParameters, 'ToggleParameters'),(ScApp.Find, 'Find'),(ScApp.FindInFiles, 'FindInFiles'))
	for fn, name in toggles:
		fn(); ScApp.MsgBox( 'Starting '+name)
		fn(); ScApp.MsgBox( 'Stopping '+name)
	
	ScEditor.ClearAll()
	ScEditor.Write('bookmark on this line')
	ScApp.BookmarkToggle()
	ScApp.ViewEol()
	ScEditor.Write('\ncan see the LF character')
	ScEditor.Write(' wrap a long string '*40)
	ScApp.Wrap()
	
	# to address later:
	ScApp.Fullscreen() #does not work in this release
	ScApp.Tools() #not sure of effect, but test that it does not throw
	ScApp.ToolWin() #not sure of effect, but test that it does not throw
	
	
# testing the current pane.
def test_1_1():
	CurrentPane.ClearAll()
	expectEqual(CurrentPane.GetAllText(), '')
	CurrentPane.Write('ab'); CurrentPane.Write('bc')
	expectEqual(CurrentPane.GetAllText(), 'abbc')
	
	# append not affected by position
	CurrentPane.ClearAll()
	CurrentPane.Append('123'); CurrentPane.GotoPos(1); CurrentPane.Append('456')
	expectEqual(CurrentPane.GetAllText(), '123456')
	
	# Write -is- affected by position
	CurrentPane.ClearAll()
	CurrentPane.Write('ABC'); CurrentPane.GotoPos(1); CurrentPane.Write('DEF')
	expectEqual(CurrentPane.GetAllText(), 'ADEFBC')
	
	CurrentPane.ClearAll()
	CurrentPane.Write('aaaa'); CurrentPane.InsertText('bb',2); CurrentPane.InsertText('cc',3)
	expectEqual(CurrentPane.GetAllText(), 'aabccbaa')
	
	CurrentPane.ClearAll()
	CurrentPane.Write('123456789'); CurrentPane.Remove(1,1); CurrentPane.Remove(3,5)
	expectEqual(CurrentPane.GetAllText(), '134789')
	
	CurrentPane.ClearAll()
	CurrentPane.Write('123456789');
	expectEqual(CurrentPane.Textrange(1,1), ''); expectEqual(CurrentPane.Textrange(1,2), '2')
	expectEqual(CurrentPane.Textrange(1,3), '23'); expectEqual(CurrentPane.Textrange(2,5), '345')
	
	CurrentPane.ClearAll()
	CurrentPane.Write('a teststringnotwhole teststring testStringnotwhole testString end');
	expectEqual( CurrentPane.FindText('testString',wholeWord=True, matchCase=True), (51,61))
	expectEqual( CurrentPane.FindText('testString',matchCase=True), (32,42))
	expectEqual( CurrentPane.FindText('testString',wholeWord=True), (21,31))
	expectEqual( CurrentPane.FindText('testString'), (2,12))
	
	expectThrow( (lambda:CScite.pane_ScintillaFn(3, 'a', ('b','C'))), 'Invalid pane')
	expectThrow( (lambda:CurrentPane.NotAValid()), 'Could not find fn.')
	expectThrow( (lambda:CurrentPane.SetNotAValid('f')), 'Could not find prop.')
	expectThrow( (lambda:CurrentPane.GetNotAValid()), 'Could not find prop.')
	
	# scintilla fns
	expectThrow( (lambda:CurrentPane.ClearAll(1)), 'Wrong # of args')
	expectThrow( (lambda:CurrentPane.SetWhitespaceBack(1,1,1)), 'Wrong # of args')
	expectThrow( (lambda:CurrentPane.AppendText('a','b','c','d')), 'Wrong # of args')
	expectThrow( (lambda:CurrentPane.AppendText('a','a')), 'int expected')
	expectThrow( (lambda:CurrentPane.AppendText(False,False)), 'string expected')
	expectThrow( (lambda:CurrentPane.MarkerAdd(1,1,1)), 'Wrong # of args')
	expectThrow( (lambda:CurrentPane.CanRedo(None)), 'Wrong # of args')
	expectThrow( (lambda:CurrentPane.CanRedo(0)), 'Wrong # of args')
	
	# scintilla  get/set
	expectThrow( (lambda:CurrentPane.SetLineCount(4)), 'prop can\'t be set')
	expectThrow( (lambda:CurrentPane.GetWhitespaceChars()), 'prop can\'t be get')
	expectThrow( (lambda:CurrentPane.GetLineCount('a')), 'property does not take params')
	expectThrow( (lambda:CurrentPane.GetLineCount(1)), 'property does not take params')
	expectThrow( (lambda:CurrentPane.GetCharAt()), 'prop needs param')
	expectThrow( (lambda:CurrentPane.GetCharAt('a')), 'Int expected')
	expectThrow( (lambda:CurrentPane.SetStyleBold('a')), 'prop needs param')
	expectThrow( (lambda:CurrentPane.SetStyleBold(True)), 'prop needs param')
	expectThrow( (lambda:CurrentPane.SetViewEOL(1)), 'Bool expected')
	expectThrow( (lambda:CurrentPane.SetViewEOL(True, 45)), 'property does not take params')
	
	
def test_1_2():
	# see what_tested.py for test coverage status
	
	##### CanUndo tests #######
	CurrentPane.BeginUndoAction(); CurrentPane.Write('a'); CurrentPane.EndUndoAction()
	CurrentPane.EmptyUndoBuffer()
	expectEqual(CurrentPane.CanUndo(), False)
	expectEqual(CurrentPane.CanRedo(), False)
	CurrentPane.ClearAll(); CurrentPane.Write('hh')
	CurrentPane.BeginUndoAction()
	CurrentPane.Write('aaaa')
	CurrentPane.EndUndoAction()
	expectEqual(CurrentPane.CanUndo(), True)
	CurrentPane.Undo()
	expectEqual(CurrentPane.CanRedo(), True)
	expectEqual(CurrentPane.GetAllText(), 'hh')
	
	##### FindColumn tests (converts x,y to character, i.e. the 18th char in doc) #######
	sOutputBefore= ScOutput.GetAllText()
	CurrentPane.ClearAll(); CurrentPane.Write('test\na\tb\n\n\n');
	base = 6 
	expectEqual(CurrentPane.FindColumn(1,1), base)
	for i in range(2,2+7):
		expectEqual(CurrentPane.FindColumn(1,i), base+1)
	for i in range(2+7, 30):
		expectEqual(CurrentPane.FindColumn(1,i), base+2)
	ScOutput.ClearAll(); ScOutput.Write(sOutputBefore + 'Pass: FindColumn tests pass\n')
	
	##### character and position tests #######
	CurrentPane.ClearAll(); CurrentPane.Write('0123456789\nabcd\nWXYZ');
	expectEqual(CurrentPane.GetCharAt(1), ord('1'));
	expectEqual(CurrentPane.GetCharAt(5), ord('5'));
	expectEqual(CurrentPane.GetLineCount(), 3);
	
	
	CurrentPane.ClearAll(); CurrentPane.Write('0123456789')
	CurrentPane.SetSelection(1,3)
	expectEqual(CurrentPane.GetSelText(), '12');
	CurrentPane.Copy(); CurrentPane.Paste(); CurrentPane.Paste()
	expectEqual(CurrentPane.GetAllText(), '012123456789');
	CurrentPane.ClearAll(); CurrentPane.Write('0123456789')
	# another way of setting selection
	CurrentPane.ClearAll(); CurrentPane.Write('0123456789')
	CurrentPane.SetSelectionStart(1); expectEqual(CurrentPane.GetAnchor(), 1);expectEqual(CurrentPane.GetSelectionStart(), 1);
	CurrentPane.SetSelectionEnd(3); expectEqual(CurrentPane.GetCurrentPos(), 3);expectEqual(CurrentPane.GetSelectionEnd(), 3);
	expectEqual(CurrentPane.GetSelText(), '12');
	CurrentPane.Cut(); CurrentPane.GotoPos(5); CurrentPane.Paste()
	expectEqual(CurrentPane.GetAllText(), '0345612789');
	# another way of setting selection
	CurrentPane.ClearAll(); CurrentPane.Write('0123456789')
	CurrentPane.SetAnchor(1); expectEqual(CurrentPane.GetSelectionStart(), 1);expectEqual(CurrentPane.GetAnchor(), 1);
	CurrentPane.SetCurrentPos(3); expectEqual(CurrentPane.GetSelectionEnd(), 3);expectEqual(CurrentPane.GetCurrentPos(), 3);
	expectEqual(CurrentPane.GetSelText(), '12');
	CurrentPane.Cut(); CurrentPane.GotoPos(5); CurrentPane.Paste()
	expectEqual(CurrentPane.GetAllText(), '0345612789');
	
	CurrentPane.ClearAll(); CurrentPane.Write('qwert')
	expectEqual(CurrentPane.GetTextLength(), 5);
	
	########marker tests########
	CurrentPane.ClearAll(); CurrentPane.Write('L0\nL1\nL2\nL3\nL4\nL5\n')
	expectEqual(CurrentPane.MarkerGet(1), 0)
	CurrentPane.MarkerAdd(1,3); expectEqual(CurrentPane.MarkerGet(1), 1<<3)
	CurrentPane.MarkerAdd(2,4); expectEqual(CurrentPane.MarkerGet(2), 1<<4)
	CurrentPane.MarkerAdd(3,3); expectEqual(CurrentPane.MarkerGet(3), 1<<3)
	expectEqual(CurrentPane.MarkerGet(4), 0)
	expectEqual(CurrentPane.MarkerNext(0, 1<<4), 2) #next 4mark start line 0
	expectEqual(CurrentPane.MarkerNext(3, 1<<4), -1)
	CurrentPane.MarkerDelete(2,4); expectEqual(CurrentPane.MarkerGet(2), 0)
	CurrentPane.MarkerDeleteAll(3); 
	expectEqual(CurrentPane.MarkerGet(1), 0); expectEqual(CurrentPane.MarkerGet(3), 0)
	
	
	CurrentPane.GetCharAt #{"CharAt", 2007, 0, iface_int, iface_position},
	CurrentPane.GetCaretWidth #{"CaretWidth", 2189, 2188, iface_int, iface_void},
	CurrentPane.GetCurrentPos #{"CurrentPos", 2008, 2141, iface_position, iface_void},
	CurrentPane.GetUseTabs #{"UseTabs", 2125, 2124, iface_bool, iface_void},
	CurrentPane.GetStyleAt #{"StyleAt", 2010, 0, iface_int, iface_position},
	CurrentPane.GetStyleBold #{"StyleBold", 2483, 2053, iface_bool, iface_int},
	CurrentPane.GetViewEOL #{"ViewEOL", 2355, 2356, iface_bool, iface_void},
	
	
	
def test_1_3():
	# rough visual test to confirm some properties
	CurrentPane.ClearAll()
	CurrentPane.Write('some sample text. Expect: caret is now very wide!')
	CurrentPane.SetCaretWidth(3); expectEqual(CurrentPane.GetCaretWidth() , 3)
	
	#~ nStyle = CurrentPane.GetStyleAt(2) #broken??
	nStyle=11
	prevsize = CurrentPane.GetStyleSize(nStyle)
	print CurrentPane.GetStyleSize(nStyle)
	
	expectEqual(CurrentPane.GetStyleBold(nStyle), False);
	expectEqual(CurrentPane.GetStyleItalic(nStyle), False);
	
	CurrentPane.SetStyleBold(nStyle, True); expectEqual(CurrentPane.GetStyleBold(nStyle), True)
	ScApp.MsgBox('Text is now bold')
	CurrentPane.SetStyleBold(nStyle, False)
	CurrentPane.SetStyleItalic(nStyle, True); expectEqual(CurrentPane.GetStyleItalic(nStyle), True)
	ScApp.MsgBox('Text is now italic')
	CurrentPane.SetStyleItalic(nStyle, False)
	CurrentPane.SetStyleSize(nStyle, 22); expectEqual(CurrentPane.GetStyleSize(nStyle), 22)
	ScApp.MsgBox('Text is now big')
	CurrentPane.SetStyleSize(nStyle, prevsize)
	ScApp.MsgBox('Text is now normal')
	print CurrentPane.GetStyleSize(nStyle)
	
	CurrentPane.SetStyleFore(nStyle, CurrentPane.MakeColor(200, 100, 5))
	expectEqual(CurrentPane.GetColor(CurrentPane.GetStyleFore(nStyle)), (200,100,5))
	ScApp.MsgBox('Text is now orange')
	CurrentPane.SetStyleFore(nStyle, CurrentPane.MakeColor(0, 0, 0))
	ScApp.MsgBox('Text is now black')
	
	CurrentPane.Write('\nother line (where marker added)\nother.')
	expectEqual(CurrentPane.GetViewEOL(), False); 
	CurrentPane.SetViewEOL(True); expectEqual(CurrentPane.GetViewEOL(), True);
	CurrentPane.MarkerAdd(1,3)
	CurrentPane.MarkerSetFore(3, CurrentPane.MakeColor(50, 200, 50))
	CurrentPane.MarkerSetBack(3, CurrentPane.MakeColor(50, 200, 50))
	ScApp.MsgBox('See eol and green bookmark on line 2')
	
	print CurrentPane.GetViewEOL()
	a=CurrentPane.GetViewEOL()
	CurrentPane.SetViewEOL(False); expectEqual(CurrentPane.GetViewEOL(), False);
	ScEditor.MarkerDelete(1,3)
	ScApp.MsgBox('Marker and EOL gone')
	# test the ones that are overridden
	
	#~ print CurrentPane.GetMarginLeft()
	#~ print CurrentPane.GetMarginRight()
	#~ CurrentPane.SetMarginLeft(None,5)
	#~ CurrentPane.SetMarginLeft(80)
	#~ CurrentPane.SetMarginRight(80)
	#~ CurrentPane.SetZoom(CurrentPane.GetZoom()+1)
	
	
def test_1_4():
	# very slightly verify
	print 'GetHotspotActiveFore', CurrentPane.GetHotspotActiveFore()
	print 'GetHotspotActiveBack', CurrentPane.GetHotspotActiveBack()
	expectNotEqual(CurrentPane.GetHotspotActiveFore(), 0)
	expectNotEqual(CurrentPane.GetHotspotActiveBack(), 0)
	
	print 'GetLexer', CurrentPane.GetLexer()
	expectNotEqual(CurrentPane.GetLexer(), 0)
	print 'GetLexerLanguage', CurrentPane.GetLexerLanguage()
	expectNotEqual(CurrentPane.GetLexerLanguage(), 0)
	
	
##################################

testLevel = 0
def RunTestSet( keycode, fShift, fCtrl, fAlt):
	global testLevel
	if keycode==ord("K") and fCtrl and not fShift and not fAlt:
		ScApp.MsgBox('switching pane')
		SwitchOutput()
		return False
	
	if not (keycode>=ord('0') and keycode<=ord('9')):
		return True
	
	if fCtrl and fShift and not fAlt:
		ScOutput.ClearAll()
		print 'setting testlevel to '+str(keycode-ord('0'))
		testLevel = keycode-ord('0')
		return False
	elif fCtrl and not fShift and not fAlt:
		ScEditor.ClearAll()
		ScOutput.ClearAll()
		s = 'test_' + str(testLevel) + '_' + str(keycode-ord('0')) + '()'
		print s
		#could try, catch NameError name 'test_0_5' is not defined
		exec s
		return False


##################################

def expectThrow(fn, sExpectedError, TypeException=exceptions.RuntimeError):
	try:
		fn()
	except TypeException,e:
		sError = str(e).split('\n')[-1]
		if sExpectedError.lower() in sError.lower():
			print 'Pass:',sExpectedError, ' == ', sError
		elif TypeException==True:
			print 'Pass:',' ', sError
		else:
			print 'Fail: expected msg',sExpectedError,'got',sError
	else:
		print 'Fail: expected to throw! '+sExpectedError

def expectEqual(v, vExpected):
	if v != vExpected:
		print 'Fail: Expected '+str(vExpected) + ' but got '+str(v)
		raise exceptions.RuntimeError, 'stop'
	else:
		print 'Pass: '+str(vExpected) + ' == '+str(v)

def expectNotEqual(v, vExpected):
	if v == vExpected:
		print 'Fail: Expected '+str(vExpected) + ' not to equal '+str(v)
		raise exceptions.RuntimeError, 'stop'
	else:
		print 'Pass: '+str(vExpected) + ' != '+str(v)


class PrintToEditor():
	def __init__(self): pass
	def write(self, s): ScEditor.Write(s)
	def close(self): pass

sys.stdoutOut = sys.stdout
sys.stdoutEdit = PrintToEditor()

def SwitchOutput():
	global CurrentPane
	if CurrentPane==ScEditor:
		sys.stdout = sys.stdoutEdit
		CurrentPane = ScOutput
	else:
		sys.stdout = sys.stdoutOut
		CurrentPane = ScEditor

def printclear():
	if CurrentPane == ScOutput:
		ScEditor.ClearAll()
	else:
		ScOutput.ClearAll()
	
	
