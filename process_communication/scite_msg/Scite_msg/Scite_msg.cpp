// Scite_msg.cpp
// LnzEditor for Launchorz, by Ben Fisher 2008
// Contains code from "scite_other" by Steve Donovan, 2004

// Not using precompiled headers.
// Not compiling as Unicode.

#include <iostream>
#include <tchar.h>

#include "Windows.h"
#include "SciteInteract.h"

const char* documentation = 
"Scite_msg.exe {hwnd} {command}\n"
"Sends command to Scite.\n"
"Hwnd should be the hwnd of the Director interface (not Scite itself) in decimal.\n"
"Hwnd can alternatively be 'find', to send to an open SciTE instance.\n"
"Backslashes and special chars in command must be escaped.\n"
"\n"
"Scite_msg.exe find \"insert:hello world\"\n"
"or, from Scite, command.x=scite_msg.exe $(WindowID) \"insert:hello world\"\n"
"Commands include:\n"
//"askfilename:\n" We don't have a way to receive the response.
//"askproperty:\n"
"close:\n"
"currentmacro:\n"
"cwd:\n"
"enumproperties:\n"
"exportashtml:\n"
"exportasrtf:\n"
"exportaspdf:\n"
"exportaslatex:\n"
"exportasxml:\n"
"find:\n"
"goto:\n"
"loadsession:\n"
"macrocommand:\n"
"macroenable:\n"
"macrolist:\n"
"menucommand:\n"
"open:\n"
"output:\n"
"property:\n"
"reloadproperties:\n"
"quit:\n"
"replaceall:\n"
"saveas:\n"
"savesession:\n"
"extender:\n"
"focus:";
// See SciTEBase::PerformOne in SciTEBase.cxx



int _tmain(int argc, _TCHAR* argv[])
{
	if (argc < 3)
	{
		puts(documentation);
		return 1;
	}
	const char* strHwnd = argv[1];
	const char* strAction = argv[2];

	char *containsColon = strchr(strAction, ':');
	if (! containsColon)
	{
		fputs("Invalid command. Should be in form close: or insert:hello", stderr);
		return 1;
	}

	if (strcmp(strHwnd, "find")==0)
	{
		HWND results[30];
		results[0] = 0;
		EnumWindows(EnumWindowsProc,(LPARAM) results);
		int nResults = size_of_array(results);

		if (nResults == 0)
		{
			fputs("Could not find an open instance of SciTE", stderr);
			return 1;
		}
		else 
		{
			//Pick the first instance of Scite found.
			//Assumes backslashes have been added by the input
			
			SendToHandle(results[0], strAction);
		}
	}
	else
	{
		// NOTE: not 64-bit safe. Is there a 64bit atoi?
		long nHwnd = atol(strHwnd);
		if (nHwnd==0 || nHwnd==LONG_MAX || nHwnd==LONG_MIN)
		{
			fputs("Invalid hwnd. Should be in decimal", stderr);
			return 1;
		}
		HWND hwnd = (HWND) nHwnd;

		SendToHandle(hwnd, strAction);
	}

	return 0;
}



