Attribute VB_Name = "Public"
'---------------------------------------------------------------------
Declare Function GetClassName Lib "user32" Alias "GetClassNameA" (ByVal hwnd As Long, ByVal lpClassName As String, ByVal nMaxCount As Long) As Long
Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Long
Declare Function SendMessage Lib "user32" Alias "SendMessageA" (ByVal hwnd As Long, ByVal wMsg As Long, ByVal wParam As Long, lParam As Any) As Long
Declare Function GetWindow Lib "user32" (ByVal hwnd As Long, ByVal wCmd As Long) As Long
Declare Sub CopyMemory Lib "kernel32" Alias "RtlMoveMemory" (hpvDest As Any, hpvSource As Any, ByVal cbCopy As Long)
Declare Function GetClassLongA Lib "user32" (ByVal hwnd As Long, ByVal nParam As Long) As Long
Declare Function SetWindowLongA Lib "user32" (ByVal hwnd As Long, ByVal nParam As Long, ByVal dwNewValue As Long) As Long
Declare Function CallWindowProcA Lib "user32" (ByVal lpPrevProc As Long, ByVal hwnd As Long, ByVal uMsg As Long, ByVal wParam As Long, ByVal lParam As Long) As Long
Public Declare Function RegisterWindowMessage Lib "user32" Alias "RegisterWindowMessageA" (ByVal lpString As String) As Long
Public Declare Function SendMessageTimeout Lib "user32" Alias "SendMessageTimeoutA" (ByVal hwnd As Long, ByVal msg As Long, ByVal wParam As Long, ByVal lParam As Long, ByVal fuFlags As Long, ByVal uTimeout As Long, lpdwResult As Long) As Long
Public Declare Function GetWindowRect Lib "user32" (ByVal hwnd As Long, lpRect As RECT) As Long
Public Declare Function SetWindowPos Lib "user32" (ByVal hwnd As Long, ByVal hWndInsertAfter As Long, ByVal x As Long, ByVal y As Long, ByVal cx As Long, ByVal cy As Long, ByVal wFlags As Long) As Long
Public Declare Function GetDesktopWindow& Lib "user32" ()
Public Declare Function GetWindowThreadProcessId Lib "user32" (ByVal hwnd As Long, lpdwProcessId As Long) As Long
Public Declare Function SetForegroundWindow Lib "user32" (ByVal hwnd As Long) As Long
'---------------------------------------------------------------------
Public Const WM_COPYDATA = &H4A
Public Const GW_CHILD = 5
Public Const GW_HWNDNEXT = 2
Public Type COPYDATASTRUCT
    dwData As Long
    cbData As Long
    lpData As Long
End Type

Public Type RECT
        Left As Long
        Top As Long
        Right As Long
        Bottom As Long
End Type
'---------------------------------------------------------------------

Function Window_Proc(ByVal hwnd As Long, ByVal uMsg As Long, ByVal wParam As Long, ByVal lParam As Long) As Long
    Dim cds As COPYDATASTRUCT
    Dim buf() As Byte
    Dim sString As String

   ' Процедура обработки сообщений окна
   Window_Proc = CallWindowProcA(GetClassLongA(hwnd, -24), hwnd, uMsg, wParam, lParam)
   Select Case uMsg
      Case WM_COPYDATA    ' (пришло сообщение WM_COPYDATA)
      ' а тут мы в обратном порядке извлекаем из полученной структуры строку
      Call CopyMemory(cds, ByVal lParam, Len(cds))
      ' Copy the string that was passed into a byte array.
      ReDim buf(1 To cds.cbData)
      Call CopyMemory(buf(1), ByVal cds.lpData, cds.cbData)

      ' Convert the ASCII byte array back to a Unicode string.
      sString = StrConv(buf, vbUnicode)
      
      ' Display the received string.
      Result.txtResult = sString
   End Select
End Function
