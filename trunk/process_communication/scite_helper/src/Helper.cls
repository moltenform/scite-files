VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Helper"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = True
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = True
'---------------------------------------------------------------------
Option Explicit
Private hSciteWind As Long
Private hScintillaWnd As Long
Private hDirectorWnd As Long
Private SDI As Long
Dim rec As RECT
'---------------------------------------------------------------------

Public Property Get Left() As Long
    Left = rec.Left
End Property
'---------------------------------------------------------------------

Public Property Get Top() As Long
    Top = rec.Top
End Property
'---------------------------------------------------------------------

Public Property Get Width() As Long
    Width = rec.Right - rec.Left
End Property
'---------------------------------------------------------------------

Public Property Get Height() As Long
    Height = rec.Bottom - rec.Top
End Property
'---------------------------------------------------------------------

Public Sub OnTop(WindowName As String, OnTop As Boolean)
    Const SWP_NOMOVE = 2
    Const SWP_NOSIZE = 1
    Const HWND_TOPMOST = -1
    Const HWND_NOTOPMOST = -2
    Dim hFormWind As Long
    
    hFormWind = FindWindow(vbNullString, WindowName)
    If OnTop = True Then
        SetWindowPos hFormWind, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE Or SWP_NOSIZE
    Else
        SetWindowPos hFormWind, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOMOVE Or SWP_NOSIZE
    End If
End Sub
'---------------------------------------------------------------------

Public Sub Focus()
    SetForegroundWindow hSciteWind
End Sub
'=====================================================================

Public Function Send(Data As String) As String
    Dim sString As String
    Dim cds As COPYDATASTRUCT
    Dim buf() As Byte
    Dim BufSize As Long
    Const SMTO_NORMAL = &H0
    Const S_ALERT = "SciTE window not found!"
    
    sString = Text2String(Trim$(Data))
    If sString = "" Then Exit Function
    If hDirectorWnd = 0 Then
        If Left$(Data, 9) <> "identity:" Then
            MsgBox S_ALERT, vbCritical, App.FileDescription
        End If
        Send = ""
        Exit Function
    Else
        BufSize = Len(sString)
        ReDim buf(1 To BufSize) As Byte
        Call CopyMemory(buf(1), ByVal sString, BufSize)
        With cds
            .dwData = 0
            .cbData = Len(sString) ' + 1 !!! В доке написано, что завершающий нуль не нужен!
            If .cbData > UBound(buf) Then .cbData = UBound(buf)
            .lpData = VarPtr(buf(1))
        End With
        
        Call SendMessageTimeout(hDirectorWnd, SDI, 0&, 0&, SMTO_NORMAL, 1000&, 0&)
        Call SendMessage(hDirectorWnd, WM_COPYDATA, Result.hwnd, cds)
        Send = String2Text(Result.txtResult.text)
    End If
End Function
'---------------------------------------------------------------------

Public Function LUA(Command As String) As String
    Const TMP = "$$$"
    Send "extender:dostring props[" & Chr$(39) & TMP & Chr$(39) & "]=" & Command
    LUA = Props(TMP)
End Function
'---------------------------------------------------------------------

Public Property Get GetText() As String
    GetText = LUA("editor:GetText()")
End Property
'---------------------------------------------------------------------

Public Property Get GetSelText() As String
    Dim text As String
    text = Send("askproperty:CurrentSelection")
    GetSelText = Mid$(text, 18)
End Property
'---------------------------------------------------------------------

Public Sub ReplaceSel(ReplaceText As String)
    Send "insert:" & ReplaceText
End Sub
'---------------------------------------------------------------------

Public Sub menucommand(IDM_Command As String)
    Send "menucommand:" & IDM_Command
End Sub
'---------------------------------------------------------------------

Public Property Let Props(Key As String, Value As String)
    Send "property:" & Key & "=" & Value
End Property
'---------------------------------------------------------------------

Public Property Let WindowID(Value As Long)
    hDirectorWnd = Value
    RegisterSDI
End Property
'---------------------------------------------------------------------

Public Property Get WindowID() As Long
    WindowID = hDirectorWnd
End Property
'---------------------------------------------------------------------

Public Property Get Props(Key As String) As String
    Dim ret As String
    ret = Send("askproperty:" & Key)
    Props = Mid$(ret, 18)
End Property
'---------------------------------------------------------------------

Public Sub Trace(Data As String)
    Send "extender:dostring trace(" & Chr$(39) & Data & Chr$(39) & ")"
End Sub
'---------------------------------------------------------------------

Public Sub About()
    Dim soautors As String
    soautors = "Alexander Asyabrik aka Shura"
    MsgBox App.FileDescription & " " & App.Major & "." & App.Minor & " beta" & vbNewLine & vbNewLine & "Copyleft  " & App.LegalCopyright & "  and" & vbNewLine & soautors, vbInformation, App.FileDescription
End Sub
'=====================================================================

Private Function ClassName(hWind As Long) As String
    'Извлекает имя класса окна
    Dim ret As Long
    Dim sText As String

    sText = String$(255, Chr$(0))
    ret = GetClassName(hWind, sText, 255)
    ClassName = Left$(sText, ret)
End Function
'---------------------------------------------------------------------

Private Sub RegisterSDI()
    'Регистрируем SciTEDirectorInterface (для метода Send)
    SDI = RegisterWindowMessage("SciTEDirectorInterface")
   
    ' Суб-классим форму, чтобы получать сообщения
    SetWindowLongA Result.hwnd, -4, AddressOf Window_Proc
    ' Объясняем SciTE какому окну слать ответы
    Call Send("identity:" & Format(Result.hwnd))
End Sub
'---------------------------------------------------------------------

Private Function FindScintillaWindow() As Long
    Dim cn As String
    Dim ChldWnd As Long
    Const GW_CHILD = 5
    Const GW_HWNDNEXT = 2
    Dim GW_CMD As Long
    GW_CMD = GW_CHILD

    ChldWnd = GetWindow(hSciteWind, GW_CMD)
    Do
        ChldWnd = GetWindow(ChldWnd, GW_CMD)
        cn = ClassName(ChldWnd)
        GW_CMD = GW_HWNDNEXT
    Loop While cn <> "Scintilla" And ChldWnd <> 0
    FindScintillaWindow = ChldWnd
End Function
'---------------------------------------------------------------------

Private Function FindDirectorWindow() As Long
    Dim cn As String
    Dim ChldWnd As Long
    Const GW_CHILD = 5
    Const GW_HWNDNEXT = 2
    Dim SciTEProcID As Long
    Dim ChldProcID As Long
    
    Call GetWindowThreadProcessId(hSciteWind, SciTEProcID)
    ChldWnd = GetWindow(GetDesktopWindow(), GW_CHILD)
    Do
        ChldWnd = GetWindow(ChldWnd, GW_HWNDNEXT)
        cn = ClassName(ChldWnd)
        Call GetWindowThreadProcessId(ChldWnd, ChldProcID)
    Loop While (cn <> "DirectorExtension" Or ChldProcID <> SciTEProcID) And ChldWnd <> 0
    FindDirectorWindow = ChldWnd
End Function
'---------------------------------------------------------------------

Private Sub Class_Initialize()
    'Находим окно SciTE
    hSciteWind = FindWindow("SciTEWindow", vbNullString)
'MsgBox "hSciteWind:" & hSciteWind
    
    'Находим размеры окна SciTE (для методов Left, Top, Width, Height)
    Call GetWindowRect(hSciteWind, rec)
    
    'Находим окно Scintilla (для метода Focus)
    hScintillaWnd = FindScintillaWindow()
'MsgBox "hScintillaWnd:" & hScintillaWnd

    hDirectorWnd = FindDirectorWindow()
'MsgBox "hDirectorWnd:" & hDirectorWnd
    RegisterSDI
End Sub
'---------------------------------------------------------------------

Private Sub Class_Terminate()
   ' Снимаем суб-классинг с формы
   SetWindowLongA Result.hwnd, -4, GetClassLongA(Result.hwnd, -24)
End Sub
'---------------------------------------------------------------------

Private Function Text2String(text As String) As String
    Dim i As Long
    Dim Char As String
    Dim strOut As String
    strOut = ""
    For i = 1 To Len(text)
        Char = Mid$(text, i, 1)
        Select Case Asc(Char)
        Case 7
            Char = "\a"
        Case 8
            Char = "\b"
        Case 9
            Char = "\t"
        Case 10
            Char = "\n"
        Case 11
            Char = "\v"
        Case 12
            Char = "\f"
        Case 13
            Char = "\r"
        Case 92
            Char = "\\"
        End Select
        strOut = strOut + Char
    Next i
    Text2String = strOut
End Function
'---------------------------------------------------------------------

Private Function String2Text(str As String) As String
    Dim i As Long
    Dim Char As String
    Dim strOut As String
    Dim esc As Boolean
    strOut = ""
    esc = False
    For i = 1 To Len(str)
        Char = Mid$(str, i, 1)
        If (Not esc) And (Char = "\") Then
            esc = True
        Else
            If esc Then
                Select Case Char
                Case "a"
                    Char = Chr$(7)
                Case "b"
                    Char = Chr$(8)
                Case "t"
                    Char = Chr$(9)
                Case "n"
                    Char = Chr$(10)
                Case "v"
                    Char = Chr$(11)
                Case "f"
                    Char = Chr$(12)
                Case "r"
                    Char = Chr$(13)
                Case "\"
                    Char = Chr$(92)
                End Select
                esc = False
            End If
            strOut = strOut + Char
        End If
    Next i
    String2Text = strOut
End Function


