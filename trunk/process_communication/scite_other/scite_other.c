// scite_other.dll does three things:
// (1) can send a command to another instance of SciTE
// (2) can access the 'perform' interface of the existing instance
// (3) supplies a 'quiet exec' operation for people tired of flashing black boxes
// For Visual C++, the command line is:
//    cl /LD scite_other.c user32.lib
// For Mingw, it's
//    gcc -shared scite_other.c -o scite_other.dll
//
// Steve Donovan, 2004
// here's some (optional) trickery by SpaceCommander@ByTeGeiZ.de
// to get a really lean & mean DLL. Switch it off if it causes trouble.
#pragma comment(linker,"/MERGE:.rdata=.data")
#pragma comment(linker,"/MERGE:.text=.data")
#pragma comment(lib,"msvcrt.lib")
#if (_MSC_VER < 1300)
 #pragma comment(linker,"/IGNORE:4078")
 #pragma comment(linker,"/OPT:NOWIN98")
#endif

#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static void SendToHandle(HWND hwnd, const char *Message)
{
  COPYDATASTRUCT cds;
  int size = strlen(Message);
  cds.dwData = 0;	
  cds.lpData = (void *)Message;
  cds.cbData = size;
  SendMessage(hwnd, WM_COPYDATA,(WPARAM)NULL,(LPARAM)&cds);
}

static int size_of_array(HWND* results)
{
  int idx = 0;	
  // find our place in the output array	
  for (idx = 0; results[idx] != NULL; idx++) ;	
  return idx;
}

BOOL CALLBACK EnumWindowsProc(HWND  hwnd, LPARAM  lParam)
{
  HWND* results = (HWND*)lParam;
  int idx = size_of_array(results);	
  char buff[256];
  GetClassName(hwnd,buff,sizeof(buff));	
  if (strcmp(buff,"DirectorExtension") == 0) {
	printf("found %x\n",hwnd);
	results[idx] = hwnd;
	results[idx+1] = NULL;
  }
  return TRUE;
}
void DebugMessage(const char *strMessage)
{
	MessageBox(NULL, strMessage, "Debug", MB_OK);
}

void strreplace(char *s, char chr, char repl_chr) {

    for (; *s; s++)             /* each character in s */
        if (*s == chr) {        /* that matches chr */
            *s = repl_chr;      /* will change repl_chr */
        }
}


static BOOL shell_exec( char *strCommand,  char *strArguments)
{
	//DebugMessage(strCommand);
	//DebugMessage(strArguments);
	strreplace(strCommand, '\r', '\0');
	strreplace(strCommand, '\n', '\0');
	
	strreplace(strArguments, '\r', '\0');
	strreplace(strArguments, '\n', '\0');
	
	ShellExecute(  NULL /*No owner*/,
	"open" /*default operation*/,
	strCommand,
	strArguments,
	NULL /*default directory*/,
	SW_SHOWNORMAL
	);
	
	
}
	
// based on code by Steven Szelei
static BOOL quiet_exec(const char *strCommand)
{
	STARTUPINFO StartupInfo;
	PROCESS_INFORMATION ProcessInfo;
	char Args[4096];
	char *pEnvCMD = NULL;
	ULONG rc;
	
	memset(&StartupInfo, 0, sizeof(StartupInfo));
	StartupInfo.cb = sizeof(STARTUPINFO);
	StartupInfo.dwFlags = STARTF_USESHOWWINDOW;
	StartupInfo.wShowWindow = SW_HIDE;

	Args[0] = 0;

	pEnvCMD = getenv("COMSPEC");
	strcpy(Args, pEnvCMD ? pEnvCMD : "CMD.EXE");        
	
	// "/c" option - Do the command then terminate the command window
	strcat(Args, " /c "); 
	/*the application you would like to run from the command window */
	strcat(Args, strCommand);  

	if (!CreateProcess( NULL, Args, NULL, NULL, FALSE,
		CREATE_NEW_CONSOLE, 
		NULL, 
		NULL,
		&StartupInfo,
		&ProcessInfo))
  	    return GetLastError();		

	WaitForSingleObject(ProcessInfo.hProcess, INFINITE);
	if(!GetExitCodeProcess(ProcessInfo.hProcess, &rc))
		rc = 0;

	CloseHandle(ProcessInfo.hThread);
	CloseHandle(ProcessInfo.hProcess);

	return rc;
}




static BOOL launch_scite(const char *command)
{ 
   char buff[512],path[256];	
   char* scite_location = getenv("SciTE_HOME");
   if (! scite_location) *path = '\0';
   else {
     strcpy(path,scite_location);
     strcat(path,"/");
   }
   sprintf(buff,"%sSciTE.exe -%s",path,command);
   return  (WinExec(buff,SW_SHOW) > 31);
}

#define TEMP_FILE_IN "/scite_other_temp1"
#define TEMP_FILE_OUT "/scite_other_temp2"
   
__declspec(dllexport)
void scite_other(void)
{
  HWND results[100],our_window;
  char command[4096];
  int action,i,nmsg = 0;
  // OK, read the request from the temp file!
  FILE *file = fopen(TEMP_FILE_IN,"r");
  fgets(command,sizeof(command),file);
	
  if (strncmp("quietexec:",command,10)==0) {
     quiet_exec(command+10);
fclose(file);	  
     return;		
  }
    if (strncmp("shellexec:",command,10)==0) 
    {
		char args[4096];
		fgets(args, sizeof(args), file);
		shell_exec(command+10, args);
		fclose(file);
		return;
  }  
  fscanf(file,"%d %x",&action,&our_window);
  fclose(file);
  results[0] = 0;
  EnumWindows(EnumWindowsProc,(long)results);
  nmsg = size_of_array(results);
  file = fopen(TEMP_FILE_OUT,"w");
  fprintf(file,"%d\n",nmsg);
  for (i = 0; i < nmsg; i++)
     fprintf(file,"%x\n",results[i]);
  if (action == 1) {
    HWND handle = our_window ? our_window : results[0]; 	
    fprintf(file,"%x\n",handle);	
    SendToHandle(handle,command);	
  } else
  if (nmsg == 1)  { // then there's only one instance! Launch SciTE!
     fprintf(file,"%d\n",launch_scite(command));
  } else if (nmsg > 1)  { // pick the first _other_ instance
     int idx = 0;
     if (results[idx] == our_window)
        idx++;
     fprintf(file,"%x\n",results[idx]);
     SendToHandle(results[idx],command);	
  } else {
     fprintf(file,"0\n");
  }
  fclose(file);
}
