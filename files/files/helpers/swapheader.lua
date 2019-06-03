
-- Swap C / Header
-- By gusnan
function exists(file)
	res=false

	f=io.open(file)
	if (f~=nil) then
		io.close(f)
		res=true
	end

	return res
end

local cpp_ext = 'cpp'
local cpp_ext2 = 'cc'
local c_ext='c'
local h_ext = 'h'
local f = props['FileName']    -- e.g 'test'
local ext = props['FileExt']   -- e.g 'cpp'
local path = props['FileDir']  -- e.g. '/home/steve/progs'

local filename=path..'/'..f..'.'..ext
local curfilename=filename

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
		end
	end
end

filename=path..'/'..f..'.'..ext

-- if the file exists, open it!
if (exists(filename)==true) and (filename ~= curfilename) then
	scite.Open(filename)
else
	print('no c/header was found.')
end
