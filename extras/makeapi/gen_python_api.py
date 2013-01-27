'''gen_python_api.py generates a python.api file for SciTE

The generated api file includes
  *) all Python keywords
  *) all builtin functions
  *) all module attributes

Module functions are represented by their docstring if available,
otherwise by the function definition from the source file.

Classes are represented by their constructor if available.

Usage:
Edit the list of modules which should be excluded.  This list is located
some lines below.  Look for excludemodulelist = [...]
Specify the modules whose contents should be added as global names
(i.e. from parrot import *).  Look for addasgloballist = [...]

Start the script by typing 'python gen_python_api.py' in the shell.
Don't start it from within SciTE on Win32 systems, because some
modules need a TTY when they are imported.

Copy the generated python.api file into your SciTE directory and
add the following lines to your SciTEUser.properties file:

api.*.py=$(SciteDefaultHome)/python.api
api.*.pyw=$(SciteDefaultHome)/python.api
autocomplete.choose.single=1
autocomplete.python.ignorecase=1
autocomplete.python.start.characters=.
autocomplete.python.fillups=(
#autocompleteword.automatic
calltip.python.ignorecase=1
calltip.python.word.characters=._$(chars.alpha)$(chars.numeric)

Restart SciTE.  Enjoy.

by Markus Gritsch (gritsch@iue.tuwien.ac.at)
'''

# if one of these substrings is found in a specific sys.path directory,
# the modules in this particular directory are not processed
excludedirlist = ['lib-tk', 'idle', 'Lightflow', 'plat-linux-i386',
                  'win32', 'pythonwin', 'plat-win',
                  'test', 'distutils', 'encodings', 'OpenGL', 'gnome', 'pyglade',
                  'happydoc', 'pygame', 'mx',
                  'wxPython']

# list of modules which should be excluded
excludemodulelist = ['win32traceutil', 'win32pdh', 'perfmondata', 'tzparse',
                     'libqtcmodule-2.2', 'libqtc',
                     'win32com',
                     'GDK', 'GTK', 'GdkImlib', 'GtkExtra', 'Gtkinter', 'gtk', 'GTKconst',
                     'zip_it']

# switch for excluding modules whose names begin with _
exclude_modules = 1

# list of modules whose contents should be added as global names
addasgloballist = ['qt']

# list of modules which are otherwise not accessible
# sourcefile-parsing is NOT done for these modules
# also activate the add_manual_modules-switch below
manuallist = []# ['os.path']

# import modules of the following type (the dot must be present!!)
moduletypes = ['.py', '.pyd', '.dll', '.so']

# some switches
add_keywords = 1 # e.g. print
add_builtins = 1 # e.g. open()
add_builtin_modules = 1 # e.g. sys
add_manual_modules = 1 # modules from manuallist
add_package_modules = 1 # modules which are directories with __init__.py files
add_other_modules = 1 # all the other modules

#------------------------------------------------------------------------------

import string, re, sys, os, types

api = {}

def processName(entryprefix, moduleprefix, name, ns):
    exec 'hasdoc = hasattr(' + moduleprefix + name + ', "__doc__")' in ns
    exec 'nametype = type(' + moduleprefix + name + ')' in ns
    if ns['hasdoc']:
        exec 'doc = ' + moduleprefix + name + '.__doc__' in ns
        pattern = re.compile('^ *' + name + r' *\(.*?\)')
        if ns['doc'] and type(ns['doc']) == types.StringType: # 'and'-part added by Peter Schoen <schoen@ZTT.Fh-Worms.DE>
            if pattern.search(ns['doc']):
                if not api.has_key(entryprefix + name):
                    api[entryprefix + name] = entryprefix + string.strip(string.split(ns['doc'], '\n')[0]) + '\n'
                    return
            else:
                if ns['nametype'] in [types.ClassType, types.FunctionType]:
                    api[entryprefix + name] = entryprefix + name + '(??) [doc: ' + string.strip(string.split(ns['doc'], '\n')[0]) + ']' + '\n'
    if not api.has_key(entryprefix + name):
        if ns['nametype'] == types.ClassType:
            api[entryprefix + name] = entryprefix + name + '(??) [class]\n'
        elif ns['nametype'] == types.FunctionType:
            api[entryprefix + name] = entryprefix + name + '(??) [function]\n'
        elif ns['nametype'] == types.ModuleType:
            api[entryprefix + name] = entryprefix + name + ':: [module]\n'
        else:
            api[entryprefix + name] = entryprefix + name + '\n'

def processModule(module, file=''):
    print ' ', string.ljust(module, 22), ': importing ...',
    if module in excludemodulelist:
        print 'in exclude list'
        return

    if exclude_modules and module[0] == '_':
        print 'modulename begins with _'
        return

    #~ if module in addasgloballist:
        #~ entryprefix = ''
    #~ else:
        #~ entryprefix = module + '.'
    entryprefix = module + '.'
    for addasglobal in addasgloballist:
        if module[:len(addasglobal)] == addasglobal:
            entryprefix = module[len(addasglobal)+1:]
            break

    ns = {}
    try:
        exec 'import ' + module in ns
        print 'ok,',
    except:
        print sys.exc_info()[0]
        return

    print 'processing ...',
    try:
        exec 'names = dir(%s)' % module in ns
    except:
        print sys.exc_info()[0]
        return
    for name in ns['names']:
        processName(entryprefix, module + '.', name, ns)
    print 'ok,',

    # parse module source file if available

    if file[-3:] != '.py':
        print 'no source file'
        return
    print 'parsing ...',
    try:
        f = open(file, 'rt')
    except IOError:
        print sys.exc_info()[0]
        return
    contents = f.readlines()
    f.close()

    def_p = re.compile(r'^def (\w*)( *\(.*?\)):')
    class_p = re.compile(r'^class +(\w*)')
    init_p = re.compile(r'^[ \t]+def +__init__\(\w*, *(.*?)\):')
    inclass = 0
    classname = ''
    for line in contents:
        def_m = def_p.search(line)
        if def_m:
            name = def_m.group(1)
            if api.has_key(entryprefix + name):
                docindex = string.find(api[entryprefix + name], '[doc:')
                if docindex + 1:
                    doc = ' ' + api[entryprefix + name][docindex:] # trailing \n included
                    api[entryprefix + name] = entryprefix + name + def_m.group(2) + doc
                if api[entryprefix + name] == entryprefix + name + '(??) [function]\n':
                    api[entryprefix + name] = entryprefix + name + def_m.group(2) + '\n'

        if inclass:
            init_m = init_p.search(line)
            if init_m:
                if api.has_key(entryprefix + classname):
                    docindex = string.find(api[entryprefix + classname], '[doc:')
                    if docindex + 1:
                        doc = ' ' + api[entryprefix + classname][docindex:] # trailing \n included
                        api[entryprefix + classname] = entryprefix + classname + '(' + init_m.group(1) + ')' + doc
                    if api[entryprefix + classname] == entryprefix + classname + '(??) [class]\n':
                        api[entryprefix + classname] = entryprefix + classname + '(' + init_m.group(1) + ')' + '\n'
                inclass = 0
            if not line[0] in ' \t\n':
                inclass = 0

        class_m = class_p.search(line)
        if class_m:
            inclass = 1
            classname = class_m.group(1)
    print 'ok'

def processFolder(folder, prefix=''):
    print 'processing', folder,
    for excludedir in excludedirlist:
        if string.find(folder, excludedir) + 1:
            print '... in exclude list',
            folder = ''
            break
    print
    if folder == '' or not os.path.isdir(folder):
        return

    entries = os.listdir(folder)
    for entry in entries:
        if add_package_modules and \
           os.path.isdir(folder + os.sep + entry) and \
           os.path.isfile(folder + os.sep + entry + os.sep + '__init__.py'):
            # package
            processFolder(folder + os.sep + entry, prefix=prefix+entry+'.')
            print '-done with', folder + os.sep + entry
        elif prefix and entry == '__init__.py':
            # modules which are directories with __init__.py files
            # The probing of 'prefix' is unfortunately necessary, because of
            # the incorrect behavior of some packages (e.g. PIL) which add
            # their directory to the searchpath via a .pth file AND are
            # packages because of an __init__.py file.
            module = prefix[:-1]
            file = folder + os.sep + entry
            processModule(module, file)
        elif add_other_modules:
            # normal file-modules
            root, ext = os.path.splitext(entry)
            if not ext in moduletypes:
                continue
            if entry[-9:] == 'module.so':
                module = prefix + entry[:-9]
            else:
                module = prefix + root
            file = folder + os.sep + entry
            processModule(module, file)

#------------------------------------------------------------------------------

# keywords
if add_keywords:
    print '\nadding keywords ...',
    keywords = string.split('''and assert break class continue def del elif else
    except exec finally for from global if import in is lambda None not or pass
    print raise return try while''')
    for keyword in keywords:
        api[keyword] = keyword + '\n'
    print 'ok'

# __builtins__
if add_builtins:
    print '\nadding __builtins__ ...',
    for builtin in dir(__builtins__):
        processName(entryprefix = '', moduleprefix = '', name = builtin, ns = {})
    print 'ok'

# sys.builtin_module_names
if add_builtin_modules:
    print '\nprocessing builtin modules'
    for module in sys.builtin_module_names:
        processModule(module)

# modules specified in manuallist
if add_manual_modules:
    print '\nprocessing modules specified in manuallist'
    for module in manuallist:
        processModule(module)

# modules from sys.path
if add_package_modules or add_other_modules:
    print '\nprocessing searchpath'
    # avoid duplicated entries in sys.path
    folders = {}
    for folder in sys.path:
        folders[folder] = None

    for folder in folders.keys():
        if folder != os.getcwd():
            processFolder(folder)

#------------------------------------------------------------------------------

# sorting
print 'sorting api file ...',
apilist = api.values()
apilist.sort()
print 'done'

# saving
print 'saving api file ...',
f = open('python.api', 'wt')
f.writelines(apilist)
f.close()
print 'done\n'
