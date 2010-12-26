Attribute VB_Name = "Public"
Declare Function PostMessage Lib "user32" Alias "PostMessageA" (ByVal hwnd As Long, ByVal wMsg As Long, ByVal wParam As Long, ByVal lParam As Long) As Long
Declare Function GetClassName Lib "user32" Alias "GetClassNameA" (ByVal hwnd As Long, ByVal lpClassName As String, ByVal nMaxCount As Long) As Long
Declare Function FindWindow Lib "user32" Alias "FindWindowA" (ByVal lpClassName As String, ByVal lpWindowName As String) As Long
Declare Function SendMessage Lib "user32" Alias "SendMessageA" (ByVal hwnd As Long, ByVal wMsg As Long, ByVal wParam As Long, lParam As Any) As Long
Declare Function GetWindow Lib "user32" (ByVal hwnd As Long, ByVal wCmd As Long) As Long
Declare Function GetDesktopWindow Lib "user32" () As Long
Declare Sub CopyMemory Lib "kernel32" Alias "RtlMoveMemory" (hpvDest As Any, hpvSource As Any, ByVal cbCopy As Long)
Declare Function GetClassLongA Lib "user32" (ByVal hwnd As Long, ByVal nParam As Long) As Long
Declare Function GetWindowLongA Lib "user32" (ByVal hwnd As Long, ByVal nParam As Long) As Long
Declare Function SetWindowLongA Lib "user32" (ByVal hwnd As Long, ByVal nParam As Long, ByVal dwNewValue As Long) As Long
Declare Function CallWindowProcA Lib "user32" (ByVal lpPrevProc As Long, ByVal hwnd As Long, ByVal uMsg As Long, ByVal wParam As Long, ByVal lParam As Long) As Long
Public Declare Function RegisterWindowMessage Lib "user32" Alias "RegisterWindowMessageA" (ByVal lpString As String) As Long
Public Declare Function SendMessageTimeout Lib "user32" Alias "SendMessageTimeoutA" (ByVal hwnd As Long, ByVal msg As Long, ByVal wParam As Long, ByVal lParam As Long, ByVal fuFlags As Long, ByVal uTimeout As Long, lpdwResult As Long) As Long

Public Const WM_COPYDATA = &H4A
Public Const GW_CHILD = 5
Public Const GW_HWNDNEXT = 2
Public Type COPYDATASTRUCT
    dwData As Long
    cbData As Long
    lpData As Long
End Type

Dim cds As COPYDATASTRUCT
Dim buf(1 To 255) As Byte, sString As String

Function Window_Proc(ByVal hwnd As Long, ByVal uMsg As Long, ByVal wParam As Long, ByVal lParam As Long) As Long
   ' Процедура обработки сообщений окна
   Window_Proc = CallWindowProcA(GetClassLongA(hwnd, -24), hwnd, uMsg, wParam, lParam)
   Select Case uMsg
      Case WM_COPYDATA    ' (пришло сообщение WM_COPYDATA)
      ' а тут мы в обратном порядке извлекаем из полученной структуры строку
      Call CopyMemory(cds, ByVal lParam, Len(cds))
      ' Copy the string that was passed into a byte array.
      Call CopyMemory(buf(1), ByVal cds.lpData, cds.cbData)

      ' Convert the ASCII byte array back to a Unicode string.
      sString = StrConv(buf, vbUnicode)
      sString = Left$(sString, InStr(1, sString, Chr$(0)) - 1)

      ' Display the received string.
      Result.txtResult = sString
   End Select
End Function


