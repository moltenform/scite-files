VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Helper"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = True
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = True
Option Explicit
Private hSciteWind As Long
Private SDI  As Long
Private hScintillaWnd As Long
Private hDirectorWnd   As Long

Const S_ALERT = "SciTE window not found!"

Private Function ClassName(hWind As Long) As String
    'Извлекает имя класса окна
    Dim ret As Long
    Dim sText As String

    sText = String$(255, Chr$(0))
    ret = GetClassName(hWind, sText, 255)
    ClassName = Left$(sText, ret)
End Function

Private Function FindChildWindowByClassName(hScintillaWnd As Long, sClassName As String) As Long
    Dim cn As String
    Dim ChldWnd As Long
    Const GW_CHILD = 5
    Const GW_HWNDNEXT = 2
    Dim GW_CMD As Long
    GW_CMD = GW_CHILD

    ChldWnd = GetWindow(hScintillaWnd, GW_CMD)
    Do
        ChldWnd = GetWindow(ChldWnd, GW_CMD)
        cn = ClassName(ChldWnd)
        GW_CMD = GW_HWNDNEXT
    Loop While cn <> sClassName And ChldWnd <> 0
    FindChildWindowByClassName = ChldWnd
End Function

'====================================================================================

Public Function GetText() As String
    Dim GetSel As Long
    Dim Text As String
    Dim Textlen As Long
    Const WM_GETTEXT = &HD                   'Getting text of child window
    Const WM_GETTEXTLENGTH = &HE
    
    If hScintillaWnd = 0 Then
        MsgBox S_ALERT, vbCritical, App.FileDescription
        Exit Function
    Else
        Textlen = SendMessage(hScintillaWnd, WM_GETTEXTLENGTH, 0, 0)
        If Textlen = 0 Then
            GetText = ""
            Exit Function
        End If
        Text = String$(Textlen, Chr$(0))
        Textlen = SendMessage(hScintillaWnd, WM_GETTEXT, Textlen, ByVal Text)
        GetText = Left(Text, Textlen)
    End If
End Function

Public Function GetSelText() As String
    Dim Text As String
    Dim startpos As Long   ' начало выделенного текста
    Dim endpos As Long    ' конец выделенного текста
    Dim retval As Long    ' возвращаемое значение
    Const EM_GETSEL = &HB0
    If hScintillaWnd = 0 Then
        MsgBox S_ALERT, vbCritical, App.FileDescription
        Exit Function
    Else
        retval = SendMessage(hScintillaWnd, EM_GETSEL, 0&, 0&)
        startpos = retval And 65535
        endpos = (retval And &HFFFF0000) / &H10000
        GetSelText = Mid(GetText(), startpos + 1, endpos - startpos)
    End If
End Function

Public Function ReplaceSel(sReplaceText As String) As Long
    Const EM_REPLACESEL = &HC2
    If hScintillaWnd = 0 Then
        MsgBox S_ALERT, vbCritical, App.FileDescription
        Exit Function
    Else
        ReplaceSel = SendMessage(hScintillaWnd, EM_REPLACESEL, 1&, ByVal sReplaceText)
    End If
End Function

Public Function About() As Long
    Dim soautors As String
    soautors = "Alexander Asyabrik aka Shura"
    MsgBox App.FileDescription & " " & App.Major & "." & App.Minor & " beta" & vbNewLine & vbNewLine & "Copyleft  " & App.LegalCopyright & "  and" & vbNewLine & soautors, vbInformation, App.FileDescription
End Function

Public Function Command(IDM_Command As Long) As Long
    Const WM_COMMAND = &H111
    If hSciteWind <> 0 And IDM_Command > 1 Then
        'Посылаем окну команду
        Command = PostMessage(ByVal hSciteWind, WM_COMMAND, IDM_Command, 0&)
    End If
End Function

Public Function Send(Data As String) As String
    Dim sString As String
    Dim cds     As COPYDATASTRUCT
    Dim buf(1 To 255) As Byte
    Const SMTO_NORMAL = &H0
    
    sString = Trim$(Data)
    If sString = "" Then Exit Function
    
    If hDirectorWnd = 0 Then
        If Left$(Data, 9) <> "identity:" Then
            MsgBox S_ALERT, vbCritical, App.FileDescription
        End If
        Send = ""
        Exit Function
    Else
        Call CopyMemory(buf(1), ByVal sString, Len(sString))
        With cds
            .dwData = 0
            .cbData = Len(sString) ' + 1 !!! В доке написано, что завершающий нуль не нужен!
            .lpData = VarPtr(buf(1))
        End With
        
        Call SendMessageTimeout(hDirectorWnd, SDI, 0&, 0&, SMTO_NORMAL, 1000&, 0&)
        Call SendMessage(hDirectorWnd, WM_COPYDATA, Result.hwnd, cds)
        
        Send = Result.txtResult.Text
    End If
End Function

Private Sub Class_Initialize()
    'Находим окно SciTE (для метода Command)
    hSciteWind = FindWindow("SciTEWindow", vbNullString)
    
    'Находим окно Scintilla (для методов GetText, GetSelText, ReplaceSel)
    hScintillaWnd = FindChildWindowByClassName(hSciteWind, "Scintilla")
    
    'Регистрируем SciTEDirectorInterface (для метода Send)
    SDI = RegisterWindowMessage("SciTEDirectorInterface")
    hDirectorWnd = FindWindow("DirectorExtension", "DirectorExtension")
   
    ' Суб-классим форму, чтобы получать сообщения
    SetWindowLongA Result.hwnd, -4, AddressOf Window_Proc
    ' Объясняем SciTE какому окну слать ответы
    Call Send("identity:" & Format(Result.hwnd))
End Sub

Private Sub Class_Terminate()
   ' Снимаем суб-классинг с формы
   SetWindowLongA Result.hwnd, -4, GetClassLongA(Result.hwnd, -24)
End Sub
