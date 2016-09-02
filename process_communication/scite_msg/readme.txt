By Ben Fisher, 2009
GPL v2 license
uses some code from Steve Donovan's 'scite_other'

This is a command-line tool that can send messages to a scite window.
In a vs2005 project but the cpps should be portable.

"Scite_msg.exe find {command}"
or
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