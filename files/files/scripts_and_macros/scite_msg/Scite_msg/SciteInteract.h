#include "Windows.h"

void SendToHandle(HWND hwnd, const char *Message);
int size_of_array(HWND* results);
BOOL CALLBACK EnumWindowsProc(HWND  hwnd, LPARAM  lParam);