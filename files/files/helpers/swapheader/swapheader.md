[back](../../../helpers.md)

## Swap C / Header

(By gusnan)

First - something simple but very useful for C/C++ programmers - keyboard-based switching between source and header file. Open the .SciTEUser.properties - which is availible from the SciTE menu

Options -> Open User Options File
and insert something like this: 

```
command.name.1.*=Swap C / Header
command.1.*=dofile /home/gusnan/scripts/scite/swapheader.lua
command.subsystem.1.*=3
command.mode.1.*=savebefore:no
command.shortcut.1.*=F11
```

This means we will have a new menu entry with 'Swap C / Header', which when activated will run the LUA script

/home/gusnan/scripts/scite/swapheader.lua

And that we also have a keyboard shortcut, key F11.

Point the file at line 2 to a file that contains the following:
(I have called it swapheader.lua)

```
function exists(file)
	res=false;
 
	f=io.open(file);
	if (f~=nil) then
		io.close(f);
		res=true;
	end
 
	return res;
end
 
local cpp_ext = 'cpp'
local cpp_ext2 = 'cc'
local c_ext='c'
local h_ext = 'h'
local f = props['FileName']    -- e.g 'test'
local ext = props['FileExt']   -- e.g 'cpp'
local path = props['FileDir']  -- e.g. '/home/steve/progs'
 
local filename=path..'/'..f..'.'..ext;
 
if ext==cpp_ext or ext==c_ext or ext==cpp_ext2 then
	ext=h_ext
elseif ext==h_ext then
	ext=cpp_ext
	filename=path..'/'..f..'.'..ext
	if (exists(filename)~=true) then
		ext=c_ext
		filename=path..'/'..f..'.'..ext
		if (exists(filename)~=true) then
			ext=cpp_ext2
			filename=path..'/'..f..'.'..ext
			if (exists(filename)~=true) then
 
			end
		end
	end
end
 
filename=path..'/'..f..'.'..ext
 
-- if the file exists, open it!
if (exists(filename)==true) then
   scite.Open(filename)
end
```

[back](../../../helpers.md)

