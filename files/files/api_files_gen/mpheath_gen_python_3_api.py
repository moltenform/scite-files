#! /usr/bin/env python3
# Author : Michael Heath
# Github : https://github.com/mpheath/generate-python-3-api
# Home   : http://users.tpg.com.au/mpheath/gen_python_3_api
# Licence: GPLv3
# Python : 3.2 to 3.8 or later
# Version: 1.4

r'''Make files for SciTE and Notepad++ for autocomplete and styling.

Module names are collected with the pydoc module.

Keywords may be included to make the editors autocomplete
to be more helpful.

Some global settings are available which can change how the
script performs the task.

SciTE
-----

The property setting of e.g.

    api.$(file.patterns.py)=$(SciteDefaultHome)\python3.api

will inform SciTE to load the file python3.api from the
directory in which the Global Options file is found.

    calltip.python.use.escapes=1

will inform SciTE to interpret escapes like \n in call signatures
and doc strings that this script may insert based on the settings.

A SciTE user can add property settings to the User Options file
to overrule the other property files.

The python3_keywords.properties file content can be used to
update python.properties or can be added to the User Options
file. It contains styles of the builtins, keywords and modules.
Some adjustments needed i.e. key names are not the same
as the key names in the python.properties, so may have no
effect until renamed.

Notepad++
---------

Notepad++ will accept newline xml escapes of &#x0a; with the
default settings in the editor.

If userDefineLang_python3.xml does exist in current directory,
it will be used as the xml source to update, rather than the
internal xml source. This allows user changes to the xml file
to be retained when future updating of keywords may be needed.

Files:
  python3.xml
    Copy to "<installdir>\autoCompletion"
    or possibly copy to "%AppData%\Notepad++\autoCompletion".

  functionlist.xml
    Modify the existing file in "<installdir>".

        <association id="python_syntax" userDefinedLangName="Python3"/>

    inserted will use the existing regular expressions for
    python to get the function list to work with this user
    defined language name of Python3.

  userDefineLang_python3.xml
    Copy to "<installdir>\userDefineLangs"
    or possibly copy to "%AppData%\Notepad++\userDefineLangs".

Advanced:
  If Python 2 is obsolete for your use, rename python3.xml to
  python.xml and replace python.xml in "<installdir>\autoCompletion".
  functionlist.xml should be OK as is. The keywords, builtins
  and module names can be merged and inserted into the
  Style Configurator Gui -> Language: Python -> Style: KEYWORDS.
  Ensure you backup if you do this, so that recovery can be
  done if the result is not to your satisfaction.
'''


import csv
import importlib
import inspect
import keyword
import os
import re
import subprocess
import sys
import xml.dom.minidom
import xml.etree.ElementTree


# Start of settings to configure.
settings = {}

# The callable tag i.e. 0='', 1='[f]', 2='[function]'.
# Output of 2 e.g. func(arg) [function] A line from the doc.
settings['callable_tag'] = 2

# Calltip use escapes. 0 or 1.
# Only applies to python3.api used in SciTE.
# Set calltip.python.use.escapes=1 in SciTE to enable escapes in SciTE.
# The setting will change to 1 if doc_line_count is -1 or > 1.
# The setting will change to 1 if escape_long_signatures is 1.
settings['calltip_use_escapes'] = 0

# Set the width which will be approximately to size for the calltip.
# This can affect doc strings width and escape long signatures width.
settings['calltip_width'] = 80

# Change to directory which contains pydoc.py. 0 or 1.
# Can avoid importing from the current directory.
# A string dir path can be used and if is invalid, 1 is implied.
settings['change_to_pydoc_dir'] = 1

# If module has attribute __all__, use this instead. 0 or 1.
# Reduces members to the module authors recommendations.
settings['define_members_by_all_attribute'] = 1

# Doc line count. -1, 0, 1 or > 1.
# Escaped doc lines are inserted into the calltip if line count is > 1.
# Escaped doc lines up to \n\n, else all of doc, if line count is -1.
# Set doc_compact to 1 if empty lines not wanted. 0 or 1.
settings['doc_line_count'] = 1
settings['doc_compact'] = 0

# Doc string content as doc or dir.
# Members of dir starting with underscore are omitted.
# Output of dir is like "dir: open, read, close." and so it starts
# with "dir:" and ends with ".". No "." means incomplete due to settings.
# 0='', 1=doc only, 2=doc or dir, 3=dir or doc, 4=dir only.
settings['doc_type'] = 1

# Exclude members that start with 2 underscores. 0 or 1.
# This can exclude __name__, __doc__ etc.
settings['exclude_members_startswith_double_underscore'] = 1

# Exclude members that start with just 1 underscore. 0 or 1.
settings['exclude_members_startswith_single_underscore'] = 0

# Exclude members of modules that comply with _ as being private members.
# These modules may not have set __all__ or some other reason for wanting this.
# The setting will change to [] if define_members_by_all_attribute=0.
settings['exclude_members_startswith_single_underscore_by_module'] = [
    'abc', 'array', 'ast', 'asyncore', 'atexit', 'ctypes', 'encodings',
    'faulthandler', 'hmac', 'inspect', 'ipaddress', 'itertools',
    'msilib', 'nt', 'os', 'platform', 'selectors', 'signal',
    'site', 'ssl', 'stat', 'sunau', 'symbol', 'time', 'tkinter',
    'tracemalloc', 'uuid', 'zipimport']

# Exclude modules that are unwanted.
settings['exclude_modules_fullname'] = [
    'antigravity', 'pydoc_data', 'sqlite3.dbapi2',
    'this', 'xml.etree.ElementPath']

if sys.platform == 'win32':

    # Exclude modules known to cause import problems on win32.
    settings['exclude_modules_fullname'].extend([
        'crypt', 'curses', 'pty', 'tty'])

# Exclude modules starts with. Does not include submodules.
settings['exclude_modules_startswith'] = ['gen_python_3_api']

# Exclude modules starts with underscore. Includes submodules. 0 or 1.
settings['exclude_modules_startswith_underscore'] = 1

# Escape long signatures to calltip_width. 0 or 1.
settings['escape_long_signatures'] = 0

# Enable Python argument -S when pydoc is run.
# 0=Don't, 1=Do imply 'import site' on initialization.
settings['import_site'] = 0

# Include custom signatures for builtins etc. that may have none. 0 or 1.
# View the dictionary named custom_signatures to understand more.
settings['include_custom_signatures'] = 1

# Include keywords to display in autocomplete. 0 or 1.
settings['include_keywords'] = 1

# Include modules not listed by pydoc.
settings['include_modules_fullname'] = [
    'concurrent.futures',
    'ctypes.util', 'ctypes.wintypes',
    'distutils.core',
    'email.contentmanager', 'email.headerregistry',
    'email.mime', 'email.mime.application',
    'email.mime.audio', 'email.mime.base',
    'email.mime.image', 'email.mime.message',
    'email.mime.multipart', 'email.mime.nonmultipart',
    'email.mime.text', 'email.policy',
    'encodings.idna',
    'html.entities', 'html.parser',
    'http.client', 'http.cookiejar',
    'http.cookies', 'http.server',
    'importlib.abc', 'importlib.machinery',
    'importlib.resources', 'importlib.util',
    'multiprocessing.connection', 'multiprocessing.dummy',
    'multiprocessing.managers', 'multiprocessing.pool',
    'multiprocessing.shared_memory', 'multiprocessing.sharedctypes',
    'tkinter.colorchooser', 'tkinter.dialog',
    'tkinter.dnd', 'tkinter.filedialog',
    'tkinter.font', 'tkinter.scrolledtext',
    'tkinter.tix', 'tkinter.ttk',
    'unittest.mock',
    'urllib.error', 'urllib.request',
    'urllib.robotparser',
    'wsgiref.handlers', 'wsgiref.headers',
    'wsgiref.simple_server', 'wsgiref.util',
    'wsgiref.validate',
    'xml.dom.pulldom',
    'xml.sax', 'xml.sax.handler',
    'xml.sax.saxutils', 'xml.sax.xmlreader',
    'xmlrpc.client', 'xmlrpc.server']

if sys.platform != 'win32':

    # Include modules fullname for unix.
    settings['include_modules_fullname'].extend([
        'curses.ascii', 'curses.panel', 'curses.textpad'])

# Include module names that need to be imported before others.
# This might be useful for modules that require other modules to be imported first.
# These module names are prepended to the module list after sorting.
settings['include_modules_fullname_import_first'] = []

# Include module names i.e. module name only added to the api. 0 or 1.
settings['include_module_names'] = 1

# Inspect members more to get class methods etc. 0 or 1.
# A list of allowed modules can be used instead of an integer.
# May increase calltips output by more than 10 times.
settings['inspect_members_more'] = 0

# Modify object representation strings. 0 or 1.
# Signatures are evaluated when parsed which may return <...> strings.
# A parameter of a inspected signature could be e.g.
#     copy_function=<function copy2 at 0x0000000002BE4820>
# Setting:
#     0 = copy_function=<??>
#     1 = copy_function=<function copy2>
# 0 modifies all parameter values of the object representations
# with <??> including e.g <class 'dict'>.
# 1 only modifies removal of memory location, so the signature remains
# verbose with the object representation. Note: some can be long in length.
settings['modify_object_representations'] = 0

# Replace commas and parentheses in parameters. 0 or 1 and dict for replace_symbols.
# Only applies to python3.api used in SciTE.
# Issue can be tuples etc. in parameters e.g.
#     func(p1, p2=(), p3=None)
# which may display in the calltip with a newline as:
#     func(p1, p2=()
#     , p3=None)
# The 1st found ) is interpreted by SciTE as end of
# signature and the rest on the 2nd line as the doc string.
# If set to 1, \ufd3e replaces ( and \ufd3f replaces ) in parameters.
# As commas in parameters are also an issue, \ufe50 replaces ,.
# As setting 1 uses unicode, ensure python3.api keeps the utf-8 encoding if edited.
# As success may vary, use replace_symbols to set symbols to use.
settings['replace_commas_in_parameters'] = 0
settings['replace_parentheses_in_parameters'] = 0
settings['replace_symbols'] = {'(': '\ufd3e', ',': '\ufe50', ')': '\ufd3f'}

# Space before doc in python3.api for SciTE. >= 0.
# Usually a space is added between the signature and the doc.
# The wrapped signature is 1 space indent.
# Display with space before doc:
#     func(p1, p2=(), p3=None, p4=None,
#      p5=None)
#      Doc to describe func.
# The doc aligns with the wrapped signature, so without the space before doc:
#     func(p1, p2=(), p3=None, p4=None,
#      p5=None)
#     Doc to describe func.
# Makes the doc appear more separate from the signature.
# Can use space_before_parameter_api >= 0.
# With space_before_parameter_api=2 and space_before_doc_api=0:
#     func(p1, p2=(), p3=None, p4=None,
#       p5=None)
#     Doc to describe func.
settings['space_before_doc_api'] = 1
settings['space_before_parameter_api'] = 1

# Space before doc in python3.xml for Notepad++. >= 0.
# The signature displays a space initially as position 0 is the return value "".
# The wrapped signature is 1 and the doc is 0.
# With space_before_parameter_xml=2 and space_before_doc_xml=0:
#      func(p1, p2=(), p3=None, p4=None,
#       p5=None)
#     Doc to describe func.
settings['space_before_doc_xml'] = 0
settings['space_before_parameter_xml'] = 1

# Remove annotations from signatures. 0 or 1.
# Return annotation is always removed as usually end of signature in SciTE is ).
settings['unannotate_signatures'] = 0


# Custom signatures referenced from the helpfile.
# Each is used only if no signature is detected for that member.
custom_signatures = {
    'array': {
        'array': [
            ['typecode[', 'initializer]']
        ]
    },
    'atexit': {
        'register': [
            ['func', '*args', '**kwargs']
        ],
        'unregister': [
            ['func']
        ]
    },
    'binascii': {
        'b2a_hex': [
            ['data[', 'sep[', 'bytes_per_sep=1]]']
        ],
        'hexlify': [
            ['data[', 'sep[', 'bytes_per_sep=1]]']
        ]
    },
    'bisect': {
        'bisect': [
            ['a', 'x', 'lo=0', 'hi=len(a)']
        ],
        'bisect_left': [
            ['a', 'x', 'lo=0', 'hi=len(a)']
        ],
        'bisect_right': [
            ['a', 'x', 'lo=0', 'hi=len(a)']
        ],
        'insort': [
            ['a', 'x', 'lo=0', 'hi=len(a)']
        ],
        'insort_left': [
            ['a', 'x', 'lo=0', 'hi=len(a)']
        ],
        'insort_right': [
            ['a', 'x', 'lo=0', 'hi=len(a)']
        ]
    },
    'builtins': {
        'bool': [
            ['[x]']
        ],
        'breakpoint': [
            ['*args', '**kws']
        ],
        'bytearray': [
            ['[source[', 'encoding[', 'errors]]]']
        ],
        'bytes': [
            ['[source[', 'encoding[', 'errors]]]']
        ],
        'classmethod': [
            ['function']
        ],
        'dict': [
            ['**kwarg'],
            ['iterable', '**kwarg'],
            ['mapping', '**kwarg']
        ],
        'dir': [
            ['[object]']
        ],
        'filter': [
            ['function', 'iterable']
        ],
        'frozenset': [
            ['[iterable]']
        ],
        'getattr': [
            ['object', 'name[', 'default]']
        ],
        'int': [
            ['[x]'],
            ['x', 'base=10']
        ],
        'iter': [
            ['object[', 'sentinel]']
        ],
        'map': [
            ['function', 'iterable', '...']
        ],
        'max': [
            ['arg1', 'arg2', '*args[', 'key]'],
            ['iterable', '*[', 'key', 'default]']
        ],
        'min': [
            ['arg1', 'arg2', '*args[', 'key]'],
            ['iterable', '*[', 'key', 'default]']
        ],
        'next': [
            ['iterator[', 'default]']
        ],
        'print': [
            ['*objects', "sep=' '", "end='\\n'", 'file=sys.stdout', 'flush=False']
        ],
        'range': [
            ['start', 'stop[', 'step]'],
            ['stop']
        ],
        'set': [
            ['[iterable]']
        ],
        'slice': [
            ['start', 'stop[', 'step]'],
            ['stop']
        ],
        'staticmethod': [
            ['function']
        ],
        'str': [
            ["object=''"],
            ["object=b''", "encoding='utf-8'", "errors='strict'"]
        ],
        'super': [
            ['[type[', 'object-or-type]]']
        ],
        'type': [
            ['name', 'bases', 'dict'],
            ['object']
        ],
        'vars': [
            ['[object]']
        ],
        'zip': [
            ['*iterables']
        ]
    },
    'cProfile': {
        'Profile': [
            ['timer=None', 'timeunit=0.0', 'subcalls=True', 'builtins=True']
        ]
    },
    'cmath': {
        'log': [
            ['x[', 'base]']
        ]
    },
    'codecs': {
        'backslashreplace_errors': [
            ['exception']
        ],
        'ignore_errors': [
            ['exception']
        ],
        'namereplace_errors': [
            ['exception']
        ],
        'replace_errors': [
            ['exception']
        ],
        'strict_errors': [
            ['exception']
        ],
        'xmlcharrefreplace_errors': [
            ['exception']
        ]
    },
    'collections' : {
        'OrderedDict': [
            ['[items]']
        ],
        'defaultdict': [
            ['[default_factory[', '...]]']
        ],
        'deque': [
            ['[iterable[', 'maxlen]]']
        ]
    },
    'contextvars': {
        'ContextVar': [
            ['name[', '*', 'default]']
        ]
    },
    'csv': {
        'field_size_limit': [
            ['[new_limit]']
        ],
        'get_dialect': [
            ['name']
        ],
        'reader': [
            ['csvfile', "dialect='excel'", '**fmtparams']
        ],
        'register_dialect': [
            ['name[', 'dialect[', '**fmtparams]]']
        ],
        'unregister_dialect': [
            ['name']
        ],
        'writer': [
            ['csvfile', "dialect='excel'", '**fmtparams']
        ]
    },
    'ctypes': {
        'Array': [
            ['*args']
        ],
        'BigEndianStructure': [
            ['*args', '**kw']
        ],
        'FormatError': [
            ['[code]']
        ],
        'LittleEndianStructure': [
            ['*args', '**kw']
        ],
        'POINTER': [
            ['type']
        ],
        'Structure': [
            ['*args', '**kw']
        ],
        'Union': [
            ['*args', '**kw']
        ],
        'addressof': [
            ['obj']
        ],
        'alignment': [
            ['obj_or_type']
        ],
        'byref': [
            ['obj[', 'offset]']
        ],
        'memmove': [
            ['dst', 'src', 'count']
        ],
        'memset': [
            ['dst', 'c', 'count']
        ],
        'pointer': [
            ['obj']
        ],
        'resize': [
            ['obj', 'size']
        ],
        'sizeof': [
            ['obj_or_type']
        ]
    },
    'curses': {
        'color_content': [
            ['color_number']
        ],
        'color_pair': [
            ['color_number']
        ],
        'curs_set': [
            ['visibility']
        ],
        'delay_output': [
            ['ms']
        ],
        'getwin': [
            ['file']
        ],
        'halfdelay': [
            ['tenths']
        ],
        'has_key': [
            ['ch']
        ],
        'init_color': [
            ['color_number', 'r', 'g', 'b']
        ],
        'init_pair': [
            ['pair_number', 'fg', 'bg']
        ],
        'is_term_resized': [
            ['nlines', 'ncols']
        ],
        'keyname': [
            ['k']
        ],
        'meta': [
            ['flag']
        ],
        'mouseinterval': [
            ['interval']
        ],
        'mousemask': [
            ['mousemask']
        ],
        'napms': [
            ['ms']
        ],
        'newpad': [
            ['nlines', 'ncols']
        ],
        'newwin': [
            ['nlines', 'ncols'],
            ['nlines', 'ncols', 'begin_y', 'begin_x']
        ],
        'pair_content': [
            ['pair_number']
        ],
        'pair_number': [
            ['attr']
        ],
        'putp': [
            ['str']
        ],
        'qiflush': [
            ['[flag]']
        ],
        'resize_term': [
            ['nlines', 'ncols']
        ],
        'resizeterm': [
            ['nlines', 'ncols']
        ],
        'setsyx': [
            ['y', 'x']
        ],
        'setupterm': [
            ['term=None', 'fd=-1']
        ],
        'tigetflag': [
            ['capname']
        ],
        'tigetnum': [
            ['capname']
        ],
        'tigetstr': [
            ['capname']
        ],
        'tparm': [
            ['str[', '...]']
        ],
        'typeahead': [
            ['fd']
        ],
        'unctrl': [
            ['ch']
        ],
        'unget_wch': [
            ['ch']
        ],
        'ungetch': [
            ['ch']
        ],
        'ungetmouse': [
            ['id', 'x', 'y', 'z', 'bstate']
        ],
        'use_env': [
            ['flag']
        ]
    },
    'curses.panel': {
        'new_panel': [
            ['win']
        ]
    },
    'datetime': {
        'date': [
            ['year', 'month', 'day']
        ],
        'datetime': [
            ['year', 'month', 'day', 'hour=0', 'minute=0', 'second=0', 'microsecond=0', 'tzinfo=None', '*', 'fold=0']
        ],
        'time': [
            ['hour=0', 'minute=0', 'second=0', 'microsecond=0', 'tzinfo=None', '*', 'fold=0']
        ],
        'timedelta': [
            ['days=0', 'seconds=0', 'microseconds=0', 'milliseconds=0', 'minutes=0', 'hours=0', 'weeks=0']
        ],
        'timezone': [
            ['offset', 'name=None']
        ]
    },
    'faulthandler': {
        'dump_traceback': [
            ['file=sys.stderr', 'all_threads=True']
        ],
        'dump_traceback_later': [
            ['timeout', 'repeat=False', 'file=sys.stderr', 'exit=False']
        ],
        'enable': [
            ['file=sys.stderr', 'all_threads=True']
        ]
    },
    'functools': {
        'cmp_to_key': [
            ['func']
        ],
        'partial': [
            ['func', '/', '*args', '**keywords']
        ],
        'reduce': [
            ['function', 'iterable[', 'initializer]']
        ]
    },
    'gc': {
        'get_referents': [
            ['*objs']
        ],
        'get_referrers': [
            ['*objs']
        ],
        'set_threshold': [
            ['threshold0[', 'threshold1[', 'threshold2]]']
        ]
    },
    'hashlib': {
        'sha3_224': [
            ['[data]']
        ],
        'sha3_256': [
            ['[data]']
        ],
        'sha3_384': [
            ['[data]']
        ],
        'sha3_512': [
            ['[data]']
        ],
        'shake_128': [
            ['[data]']
        ],
        'shake_256': [
            ['[data]']
        ]
    },
    'itertools': {
        'chain': [
            ['*iterables']
        ],
        'islice': [
            ['iterable', 'start', 'stop[', 'step]'],
            ['iterable', 'stop']
        ],
        'product': [
            ['*iterables', 'repeat=1']
        ],
        'repeat': [
            ['object[', 'times]']
        ],
        'zip_longest': [
            ['*iterables', 'fillvalue=None']
        ]
    },
    'keyword': {
        'iskeyword': [
            ['s']
        ]
    },
    'locale': {
        'strcoll': [
            ['string1', 'string2']
        ],
        'strxfrm': [
            ['string']
        ]
    },
    'lzma': {
        'LZMACompressor': [
            ['format=FORMAT_XZ', 'check=-1', 'preset=None', 'filters=None']
        ]
    },
    'math': {
        'hypot': [
            ['*coordinates']
        ],
        'log': [
            ['x[', 'base]']
        ]
    },
    'mmap': {
        'mmap': [
            ['fileno', 'length', 'flags=MAP_SHARED', 'prot=PROT_WRITE|PROT_READ', 'access=ACCESS_DEFAULT[', 'offset]'],
            ['fileno', 'length', 'tagname=None', 'access=ACCESS_DEFAULT[', 'offset]']
        ]
    },
    'msilib': {
        'CreateRecord': [
            ['count']
        ],
        'FCICreate': [
            ['cabname', 'files']
        ],
        'OpenDatabase': [
            ['path', 'persist']
        ]
    },
    'operator': {
        'attrgetter': [
            ['*attr'],
            ['attr']
        ],
        'itemgetter': [
            ['*items'],
            ['item']
        ],
        'methodcaller': [
            ['name', '/', '*args', '**kwargs']
        ]
    },
    'os': {
        'get_terminal_size': [
            ['fd=STDOUT_FILENO']
        ],
        'startfile': [
            ['path[', 'operation]']
        ],
        'utime': [
            ['path', 'times=None', '*', '[ns', ']dir_fd=None', 'follow_symlinks=True']
        ]
    },
    'parser': {
        'compilest': [
            ['st', "filename='<syntax-tree>'"]
        ],
        'expr': [
            ['source']
        ],
        'isexpr': [
            ['st']
        ],
        'issuite': [
            ['st']
        ],
        'sequence2st': [
            ['sequence']
        ],
        'st2list': [
            ['st', 'line_info=False', 'col_info=False']
        ],
        'st2tuple': [
            ['st', 'line_info=False', 'col_info=False']
        ],
        'suite': [
            ['source']
        ],
        'tuple2st': [
            ['sequence']
        ]
    },
    'pickle': {
        'PickleBuffer': [
            ['buffer']
        ]
    },
    'pyexpat': {
        'ParserCreate': [
            ['encoding=None', 'namespace_separator=None']
        ]
    },
    'signal': {
        'set_wakeup_fd': [
            ['fd', '*', 'warn_on_full_buffer=True']
        ]
    },
    'socket': {
        'close': [
            ['fd']
        ],
        'gethostbyaddr': [
            ['ip_address']
        ],
        'gethostbyname': [
            ['hostname']
        ],
        'gethostbyname_ex': [
            ['hostname']
        ],
        'getnameinfo': [
            ['sockaddr, flags']
        ],
        'getprotobyname': [
            ['protocolname']
        ],
        'getservbyname': [
            ['servicename[', 'protocolname]']
        ],
        'getservbyport': [
            ['port[', 'protocolname]']
        ],
        'htonl': [
            ['x']
        ],
        'htons': [
            ['x']
        ],
        'if_indextoname': [
            ['if_index']
        ],
        'if_nametoindex': [
            ['if_name']
        ],
        'inet_aton': [
            ['ip_string']
        ],
        'inet_ntoa': [
            ['packed_ip']
        ],
        'inet_ntop': [
            ['address_family', 'packed_ip']
        ],
        'inet_pton': [
            ['address_family', 'ip_string']
        ],
        'ntohl': [
            ['x']
        ],
        'ntohs': [
            ['x']
        ],
        'setdefaulttimeout': [
            ['timeout']
        ]
    },
    'sqlite3': {
        'complete_statement': [
            ['sql']
        ],
        'connect': [
            ['database[', 'timeout', 'detect_types', 'isolation_level', 'check_same_thread', 'factory', 'cached_statements', 'uri]']
        ],
        'enable_callback_tracebacks': [
            ['flag']
        ],
        'register_adapter': [
            ['type', 'callable']
        ],
        'register_converter': [
            ['typename', 'callable']
        ]
    },
    'stat': {
        'S_IFMT': [
            ['mode']
        ],
        'S_IMODE': [
            ['mode']
        ],
        'S_ISBLK': [
            ['mode']
        ],
        'S_ISCHR': [
            ['mode']
        ],
        'S_ISDIR': [
            ['mode']
        ],
        'S_ISDOOR': [
            ['mode']
        ],
        'S_ISFIFO': [
            ['mode']
        ],
        'S_ISLNK': [
            ['mode']
        ],
        'S_ISPORT': [
            ['mode']
        ],
        'S_ISREG': [
            ['mode']
        ],
        'S_ISSOCK': [
            ['mode']
        ],
        'S_ISWHT': [
            ['mode']
        ],
        'filemode': [
            ['mode']
        ]
    },
    'struct': {
        'pack': [
            ['format', 'v1', 'v2', '...']
        ],
        'pack_into': [
            ['format', 'buffer', 'offset', 'v1', 'v2', '...']
        ]
    },
    'sys': {
        'audit': [
            ['event', '*args']
        ],
        'breakpointhook': [
            ['*args', '**kws']
        ],
        'getsizeof': [
            ['object[', 'default]']
        ],
        'set_asyncgen_hooks': [
            ['firstiter', 'finalizer']
        ],
        'setprofile': [
            ['profilefunc']
        ],
        'settrace': [
            ['tracefunc']
        ]
    },
    'threading': {
        'excepthook': [
            ['args', '/']
        ],
        'stack_size': [
            ['[size]']
        ]
    },
    'time': {
        'asctime': [
            ['[t]']
        ],
        'ctime': [
            ['[secs]']
        ],
        'get_clock_info': [
            ['name']
        ],
        'gmtime': [
            ['[secs]']
        ],
        'localtime': [
            ['[secs]']
        ],
        'mktime': [
            ['t']
        ],
        'sleep': [
            ['secs']
        ],
        'strftime': [
            ['format[', 't]']
        ],
        'strptime': [
            ['string[', 'format]']
        ]
    },
    'tkinter': {
        'getint': [
            ['[x]'],
            ['x', 'base=10']
        ]
    },
    'tkinter.commondialog': {
        'getint': [
            ['[x]'],
            ['x', 'base=10']
        ]
    },
    'tkinter.dialog': {
        'getint': [
            ['[x]'],
            ['x', 'base=10']
        ]
    },
    'tkinter.filedialog': {
        'getint': [
            ['[x]'],
            ['x', 'base=10']
        ]
    },
    'tkinter.simpledialog': {
        'getint': [
            ['[x]'],
            ['x', 'base=10']
        ]
    },
    'tkinter.tix': {
        'getint': [
            ['[x]'],
            ['x', 'base=10']
        ]
    },
    'types': {
        'MappingProxyType': [
            ['mapping']
        ],
        'TracebackType': [
            ['tb_next', 'tb_frame', 'tb_lasti', 'tb_lineno']
        ]
    },
    'unicodedata': {
        'decimal': [
            ['chr[', 'default]']
        ],
        'digit': [
            ['chr[', 'default]']
        ],
        'name': [
            ['chr[', 'default]']
        ],
        'numeric': [
            ['chr[', 'default]']
        ]
    },
    'unittest.mock': {
        'call': [
            ['*args', '**kwargs']
        ]
    },
    'warnings': {
        'warn_explicit': [
            ['message', 'category', 'filename', 'lineno', 'module=None', 'registry=None', 'module_globals=None', 'source=None']
        ]
    },
    'weakref': {
        'getweakrefs': [
            ['object']
        ],
        'proxy': [
            ['object[', 'callback]']
        ],
        'ref': [
            ['object[', 'callback]']
        ]
    },
    'xml.etree.ElementTree': {
        'Element': [
            ['tag', 'attrib={}', '**extra']
        ],
        'SubElement': [
            ['parent', 'tag', 'attrib={}', '**extra']
        ],
        'TreeBuilder': [
            ['element_factory=None', '*', 'comment_factory=None', 'pi_factory=None', 'insert_comments=False', 'insert_pis=False']
        ],
        'XMLParser': [
            ['html=0', 'target=None', 'encoding=None']
        ]
    },
    'xml.parsers.expat': {
        'ParserCreate': [
            ['encoding=None', 'namespace_separator=None']
        ]
    }}

# Adjust custom signatures based on Python version.
if sys.version_info < (3, 8):
    custom_signatures['binascii']['b2a_hex'] = [
        ['data']
    ]

    custom_signatures['binascii']['hexlify'] = [
        ['data']
    ]

    custom_signatures['xml.etree.ElementTree']['TreeBuilder'] = [
        ['element_factory=None']
    ]

if sys.version_info < (3, 3):
    custom_signatures['builtins']['print'] = [
        ['*objects', "sep=' '", "end='\\n'", 'file=sys.stdout']
    ]

    custom_signatures['os']['utime'] = [
        ['path', 'times=None']
    ]


class Calltips():
    '''Make files for SciTE and Notepad++ for autocomplete and styling.'''

    def __init__(self, settings=None):
        '''Initiate settings for the autocomplete and styling.

        self.api:
            List containing the calltips.
        self.keywordclasses:
            Tuple of 3 lists containing keywords, builtins and modules.
        self.modules:
            List containing module names.
        self.settings:
            Dictionary containing settings.
            If settings is not None, settings updates self.settings.
        '''

        # Default settings.
        self.settings = {
            'callable_tag': 2,
            'calltip_use_escapes': 0,
            'calltip_width': 80,
            'change_to_pydoc_dir': 1,
            'define_members_by_all_attribute': 1,
            'doc_compact': 0,
            'doc_line_count': 1,
            'doc_type': 1,
            'exclude_members_startswith_double_underscore': 1,
            'exclude_members_startswith_single_underscore': 0,
            'exclude_members_startswith_single_underscore_by_module': [],
            'exclude_modules_fullname': [],
            'exclude_modules_startswith': [],
            'exclude_modules_startswith_underscore': 1,
            'escape_long_signatures': 0,
            'import_site': 0,
            'include_custom_signatures': 1,
            'include_keywords': 1,
            'include_modules_fullname': [],
            'include_modules_fullname_import_first': [],
            'include_module_names': 1,
            'inspect_members_more': 0,
            'modify_object_representations': 0,
            'replace_commas_in_parameters': 0,
            'replace_parentheses_in_parameters': 0,
            'replace_symbols': {'(': '\ufd3e', ',': '\ufe50', ')': '\ufd3f'},
            'space_before_doc_api': 1,
            'space_before_doc_xml': 0,
            'space_before_parameter_api': 1,
            'space_before_parameter_xml': 1,
            'unannotate_signatures': 0}

        # Update settings.
        print('settings:')

        if isinstance(settings, dict):
            print('  updating')
            self.settings.update(settings)

            # Sanity checks.
            if not self.settings['doc_line_count']:
                if self.settings['doc_type']:
                    print('  changing doc_type=0')
                    self.settings['doc_type'] = 0

            if not self.settings['doc_type']:
                if self.settings['doc_line_count']:
                    print('  changing doc_line_count=0')
                    self.settings['doc_line_count'] = 0

            if not self.settings['calltip_use_escapes']:
                if self.settings['doc_line_count'] not in (0, 1):
                    print('  changing calltip_use_escapes=1')
                    self.settings['calltip_use_escapes'] = 1

            if not self.settings['calltip_use_escapes']:
                if self.settings['escape_long_signatures']:
                    print('  changing calltip_use_escapes=1')
                    self.settings['calltip_use_escapes'] = 1

            if not self.settings['define_members_by_all_attribute']:
                if self.settings['exclude_members_startswith_single_underscore_by_module']:
                    print('  changing exclude_members_startswith_single_underscore_by_module=[]')
                    self.settings['exclude_members_startswith_single_underscore_by_module'] = []
        else:
            print('  default')

        # Stores the module names.
        self.modules = []

        # Stores the calltips and keywords.
        self.api = []
        self.keywordclasses = ()

        # Flag for printing 'write:' line only once to stdout.
        self._write_started = 0

        # Used by write methods to resolve callable tag names.
        self._callable_tags = {'f': 'function', 'c': 'class', 'm': 'method'}


    def build_module_list(self):
        '''Build a list of module names by use of pydoc.

        Return:
            self.modules
        '''

        # include modules by full name.
        modules = set(self.settings['include_modules_fullname'])

        # Set a directory which can avoid importing from the current directory.
        libpath = self.settings['change_to_pydoc_dir']

        if not libpath:
            libpath = None
        elif not isinstance(libpath, str) or not os.path.isdir(libpath):
            for libpath in sys.path[1:]:
                if os.path.isfile(os.path.join(libpath, 'pydoc.py')):
                    break
            else:
                libpath = None

        print('run_in_cwd:\n  {}'.format(libpath if libpath else os.getcwd()))

        # Run pydoc module to get the module names.
        command = [sys.executable, '-m', 'pydoc', 'modules']

        if not self.settings['import_site']:
            command.insert(1, '-S')

        with subprocess.Popen(command,
                              cwd=libpath,
                              stdout=subprocess.PIPE,
                              universal_newlines=True) as p:
            stdout = p.communicate()[0]

            for line in stdout.splitlines():
                if line == '':
                    continue

                # Expect 4 columns to be split.
                words = line.split()

                if len(words) > 4:
                    continue

                # Add modules from pydoc output.
                for item in words:
                    modules.add(item)

            # Exclude modules by full name.
            for item in self.settings['exclude_modules_fullname']:
                if item in modules:
                    modules.remove(item)

            # Exclude modules by starts with.
            for prefix in self.settings['exclude_modules_startswith']:
                for item in modules.copy():
                    if item.startswith(prefix):
                        modules.remove(item)

            # Exclude modules by starts with underscore.
            if self.settings['exclude_modules_startswith_underscore']:
                for item in modules.copy():
                    if item.startswith('_'):
                        modules.remove(item)

        self.modules = sorted(modules)

        # Include modules that need to be imported first.
        for item in reversed(self.settings['include_modules_fullname_import_first']):
            if item in self.modules:
                self.modules.remove(item)

            self.modules.insert(0, item)

        return self.modules


    def generate_api_list(self, modules=None):
        '''Generate api list and keywordclass lists from a list of module names.

        Return:
            self.api, self.keywordclasses
        '''

        def _add_api(item):
            '''Append item to api only if not in the list.'''

            if item not in api:
                api.append(item)

        def _get_callable_tag(member_object):
            '''Get callable tag.'''

            # Set tag as a letter which changes to actual tag text later.
            if self.settings['callable_tag'] not in (1, 2):
                return ''
            elif inspect.isfunction(member_object):
                return 'f'
            elif inspect.isclass(member_object):
                return 'c'
            elif inspect.ismethod(member_object):
                return 'm'
            else:
                return ''

        def _get_doc(module, member, member_object):
            '''Get the doc string.'''

            def _filter_doc(doc):
                '''Return 1 line to width, else return escaped multiple lines.'''

                if not doc:
                    return ''

                doc = doc.strip()

                # Fix formfeed and tab being spaces in Python 3.8.
                if module == 'ast' and member == '_pad_whitespace':
                    doc = doc.replace("'\f     '", "'\\f\\t'")

                # Replace escape sequence with literal.
                if '\f' in doc:
                    doc = doc.replace('\f', '\\f')
                    print(r'    info: Escape sequence \f replaced with \\f'
                           ' in doc string of {}.{}'.format(module, member))

                # These repetitive doc strings seem to be inherited and unwanted.
                if module in ('ctypes', 'ctypes.wintypes'):
                    if doc == 'XXX to be provided':
                        return ''
                elif module in ('importlib.resources', 'typing', 'typing.re'):
                    if doc.startswith('The central part of internal API.'):
                        return ''

                # Start filtering the doc.
                if self.settings['doc_line_count'] == -1:

                    # Find the end of the 1st paragraph.
                    eol = doc.find('\n\n')

                    if eol > 0:
                        doc = doc[:eol + 2]
                        doc = doc.strip()

                    if self.settings['doc_compact']:
                        while '\n\n' in doc:
                            doc.replace('\n\n', '\n')

                    return doc.strip()

                if self.settings['doc_line_count'] == 1:

                    # Make the doc all one line.
                    doc = doc.replace('\n', ' ').strip()
                    doc = re_remove_excess_space.sub(' ', doc)

                    # Trim doc back to a space to allowed width.
                    if len(doc) > self.settings['calltip_width']:
                        eol = doc.find(' ', self.settings['calltip_width'])

                        if eol > 0:
                            doc = doc[:eol + 1]

                    doc = doc.strip()

                    # Trim to a period for an end of sentence.
                    if not doc.endswith('.'):
                        eol = doc.find('. ')

                        if eol > 0:
                            doc = doc[:eol + 1]

                    doc = doc.strip()
                elif '\n' not in doc:

                    # Proceed only if the text width is much larger.
                    if len(doc) <= (self.settings['calltip_width'] * 1.1):
                        return doc

                    line = ''
                    new_doc = ''
                    count = 0

                    # Split into words and concat to the allowed line width.
                    for item in doc.split(' '):
                        line += item + ' '

                        if len(line) >= self.settings['calltip_width']:
                            new_doc += line.rstrip() + '\n'
                            line = ''
                            count += 1

                            if count == self.settings['doc_line_count']:
                                break
                    if line:
                        new_doc += line

                    doc = new_doc.strip()
                else:
                    new_doc = ''
                    count = 0

                    # Get lines of doc.
                    for item in doc.split('\n'):
                        if self.settings['doc_compact'] and not item:
                            continue

                        new_doc += item + '\n'
                        count += 1

                        if count == self.settings['doc_line_count']:
                            break

                    doc = new_doc.strip()

                return doc

            if not self.settings['doc_type']:
                doc = ''
            else:
                doc = inspect.getdoc(member_object)

                if self.settings['doc_type'] > 1:
                    dox = 'dir: {}.'.format(', '.join([x for x in dir(member_object)
                                                         if not x.startswith('_')]))
                    if dox == 'dir: .':
                        dox = ''

                    if self.settings['doc_type'] == 2:
                        doc = doc or dox
                    elif self.settings['doc_type'] == 3:
                        doc = dox or doc
                    elif self.settings['doc_type'] == 4:
                        doc = dox

                doc = _filter_doc(doc)

            return doc

        def _get_members(module, module_object):
            '''Get the members from a module object.'''

            def _get_more_members(members):
                '''Get another level of members.'''

                more_members = []

                for member, member_object in members:
                    if callable(member_object):
                        for submember, submember_object in inspect.getmembers(member_object):

                            # Exclude members that starts with underscores.
                            if submember.startswith('__'):
                                if self.settings['exclude_members_startswith_double_underscore']:
                                    continue
                            elif submember.startswith('_'):
                                if self.settings['exclude_members_startswith_single_underscore']:
                                    continue

                            # A module as a member is not wanted.
                            if inspect.ismodule(submember_object):
                                continue

                            more_members.append([member + '.' + submember, submember_object])

                    more_members.append([member, member_object])

                return more_members

            # Get the members.
            members = inspect.getmembers(module_object)

            # Reduce to members listed by __all__ attribute.
            if self.settings['define_members_by_all_attribute'] and module != 'os':
                if hasattr(module_object, '__all__'):
                    members_backup = members
                    members = []

                    for items in members_backup:
                        if items[0] in module_object.__all__:
                            members.append((items[0], items[1]))

            # Get more members.
            if isinstance(self.settings['inspect_members_more'], (list, tuple, set)):
                if module in self.settings['inspect_members_more']:
                    members = _get_more_members(members)
            elif self.settings['inspect_members_more']:
                members = _get_more_members(members)

            return members

        def _get_signatures(module, member, member_object):
            '''Get the signatures of a callable object.'''

            # No parameters to match the helpfile.
            if module == 'logging' and member == 'shutdown':
                return [[]]

            # Avoid invalid signature_object type with Python 3.3.
            if module == 'unittest.mock' and member == 'call':
                if sys.version_info < (3, 4):
                    return [['*args', '**kwargs']]

            # Get the objects signature.
            try:
                signature_object = inspect.signature(member_object)
            except Exception:

                # Add to the api with an empty or custom signature.
                if not self.settings['include_custom_signatures']:
                    return [[]]

                if module in custom_signatures:
                    if member in custom_signatures[module]:
                        return custom_signatures[module][member]

                return [[]]

            signature = []
            last = ''

            for items in signature_object.parameters.items():
                if self.settings['unannotate_signatures']:
                    parameter_object = items[1].replace(annotation=inspect.Parameter.empty)
                else:
                    parameter_object = items[1]

                # Add / and * parameter markers as needed.
                if parameter_object.kind == parameter_object.POSITIONAL_ONLY:
                    current = 'PO'
                elif parameter_object.kind == parameter_object.POSITIONAL_OR_KEYWORD:
                    current = 'POK'
                elif parameter_object.kind == parameter_object.VAR_POSITIONAL:
                    current = 'VP'
                elif parameter_object.kind == parameter_object.KEYWORD_ONLY:
                    current = 'KO'
                elif parameter_object.kind == parameter_object.VAR_KEYWORD:
                    current = 'VK'

                if last == 'PO' and current != 'PO':
                    signature.append('/')

                if last != 'KO' and current == 'KO':
                    signature.append('*')

                # Tidy the parameter string.
                parameter = str(parameter_object)
                parameter = parameter.replace(os_environ, 'os.environ')
                parameter = parameter.replace(sys_executable, 'sys.executable')

                for re_pattern, re_replacement in re_modify_object_representations:
                    parameter = re_pattern.sub(re_replacement, parameter)

                # Add parameter.
                signature.append(parameter)

                last = current

            # Add / to end if the parameters are positional only.
            if last == 'PO':
                signature.append('/')

            return [signature]

        def _import_modules(modules):
            '''Import from a list of modules.'''

            print('import:')

            # Set the count of imports.
            import_stats = {'fail': 0, 'pass': 0}

            # Loop through the modules names.
            for module in modules:
                print(' ', module)

                # Import the module.
                if '.' in module:
                    pkg, subpkg = module.split('.', 1)

                try:
                    if '.' in module:
                        importlib.import_module('.' + subpkg, pkg)
                    else:
                        importlib.import_module(module)
                except Exception as except_msg:
                    print('    fail:', except_msg)
                    import_stats['fail'] += 1
                else:
                    import_stats['pass'] += 1

            # Get list of module names and module objects from copy of sys.modules.
            sys_modules = sys.modules.copy()
            modules = []

            for module in sys_modules:
                if module in self.settings['exclude_modules_fullname']:
                    continue

                if module.startswith(tuple(self.settings['exclude_modules_startswith'])):
                    continue

                if self.settings['exclude_modules_startswith_underscore']:
                    passed = True

                    for item in module.split('.'):
                        if item.startswith('_'):
                            passed = False
                            break

                    if not passed:
                        continue

                modules.append([module, sys_modules[module]])

            return sorted(modules), import_stats


        if modules is None:
            modules = self.modules

        api = []
        keywordclass0 = set()
        keywordclass1 = set()
        keywordclass2 = set()

        # Doc re pattern for _get_doc().
        re_remove_excess_space = re.compile(r'( {2,})')

        # Signature re pattern for _get_signatures().
        re_modify_object_representations = [
            [re.compile(r'(\w+)=<(function) <(lambda)> at 0x[0-9A-Fa-f]+>'), r'\1=<\2 \3>']]

        if self.settings['modify_object_representations'] == 1:
            re_modify_object_representations.append(
                [re.compile(r'(\w+)=<(.+?) at 0x[0-9A-Fa-f]+>'), r'\1=<\2>'])
        else:
            re_modify_object_representations.append(
                [re.compile(r'(\w+)=<.+?>'), r'\1=<??>'])

        # Signature replacements of evaluated values for _get_signatures().
        os_environ = str(os.environ)
        sys_executable = "'" + sys.executable.replace('\\', '\\\\') + "'"

        # Get the modules, module objects and statistics.
        modules, import_stats = _import_modules(modules)

        print('generate:')

        # Add keywords to api.
        if self.settings['include_keywords']:
            for item in keyword.kwlist:
                _add_api([item])

        # Add keywords to keywordclass.
        for item in keyword.kwlist:
            keywordclass0.add(item)

        # Add to api and keywordclasses by inspecting the modules and members.
        for module, module_object in modules:
            print(' ', module)

            # Add module to api.
            if self.settings['include_module_names']:
                _add_api([module])

            # Add module to keywordclass.
            keywordclass2.add(module.split('.')[0])

            # Process the members.
            members = _get_members(module, module_object)

            for member, member_object in members:

                # Exclude members that starts with underscores.
                if member.startswith('__'):
                    if self.settings['exclude_members_startswith_double_underscore']:
                        continue
                elif member.startswith('_'):
                    if self.settings['exclude_members_startswith_single_underscore']:
                        continue

                    # Modules known to comply to start with _ as a private member.
                    elif module in self.settings['exclude_members_startswith_'
                                                 'single_underscore_by_module']:
                        if module == 'os' and member == '_exit':
                            pass
                        else:
                            continue

                # A module as a member is not wanted.
                if inspect.ismodule(member_object):
                    continue

                # Add builtins to keywordclass.
                if module == 'builtins':
                    keywordclass1.add(member.split('.')[0])

                # Add to the api if not callable.
                if not callable(member_object):
                    if module == 'builtins':
                        _add_api([member])

                    _add_api([module + '.' + member])

                    continue

                # Get the doc string.
                doc = _get_doc(module, member, member_object)

                # Get the callable tag.
                tag = _get_callable_tag(member_object)

                # Get the objects signature.
                signatures = _get_signatures(module, member, member_object)

                # Add the callable calltip to the api.
                if module == 'builtins':
                    _add_api([member, signatures, tag, doc])

                _add_api([module + '.' + member, signatures, tag, doc])

        # Reduce common keywords False, None and True.
        keywordclass1 -= keywordclass0

        # Sort the sequences into lists.
        self.api = sorted(api)
        self.keywordclasses = (sorted(keywordclass0),
                               sorted(keywordclass1),
                               sorted(keywordclass2))

        # Display statistics.
        print('import_stats:\n'
              '  passed {pass}\n'
              '  failed {fail}'.format_map(import_stats))

        print('generate_stats:\n'
              '  {:<13} {}\n'
              '  {:<13} {}\n'
              '  {:<13} {}\n'
              '  {:<13} {}\n'
              '  {:<13} {}'.format('modules', len(modules),
                                   'api', len(api),
                                   'keywordclass0', len(keywordclass0),
                                   'keywordclass1', len(keywordclass1),
                                   'keywordclass2', len(keywordclass2)))

        return self.api, self.keywordclasses


    def make_npp_files(self):
        '''Make the xml files for Notepad++.

        This method is for the convenience of reducing the main code.
        '''

        if not self.modules:
            self.build_module_list()

        if not self.api:
            self.generate_api_list()

        self.write_autocomplete_xml()
        self.write_udl_xml()


    def make_scite_files(self):
        '''Make the api and property files for SciTE.

        This method is for the convenience of reducing the main code.
        '''

        if not self.modules:
            self.build_module_list()

        if not self.api:
            self.generate_api_list()

        self.write_api()
        self.write_properties()


    def write_api(self, file='python3.api', api=None):
        '''Write python3.api for SciTE.

        api:
            The api list. If None, use the list of self.api.
        '''

        if not self._write_started:
            print('write:')
            self._write_started += 1

        print(' ', file)

        if api is None:
            api = self.api

        # Prepare replacement symbols.
        opener = self.settings['replace_symbols']['(']
        closer = self.settings['replace_symbols'][')']
        separator = self.settings['replace_symbols'][',']

        # Prepare for signature indentation of wrapped lines.
        if self.settings['space_before_parameter_api'] > 0:
            indent = ' ' * self.settings['space_before_parameter_api']
        else:
            indent = ''

        # Write calltips to the api file.
        with open(file, 'w', encoding='utf-8') as w:
            for items in api:
                if len(items) == 1:
                    w.write(items[0] + '\n')
                else:
                    name, signatures, tag, doc = items

                    if tag:
                        if self.settings['callable_tag'] == 2:
                            tag = '[' + self._callable_tags[tag] + ']'
                        else:
                            tag = '[' + tag + ']'

                    if doc and self.settings['calltip_use_escapes']:
                        doc = doc.replace('\\', '\\\\')
                        doc = doc.replace('\n', '\\n')

                    for parameters in signatures:
                        length = len(name)
                        signature = '('

                        # Join the parameters.
                        for index, parameter in enumerate(parameters):
                            length += len(parameter) + 2

                            if self.settings['calltip_use_escapes']:
                                parameter = parameter.replace('\\', '\\\\')

                            if index and self.settings['escape_long_signatures']:
                                if length >= self.settings['calltip_width']:
                                    signature = signature.strip()
                                    parameter = '\\n' + indent + parameter
                                    length = len(indent)

                            if self.settings['replace_commas_in_parameters']:
                                parameter = parameter.replace(',', separator)

                            if self.settings['replace_parentheses_in_parameters']:
                                parameter = parameter.replace('(', opener)
                                parameter = parameter.replace(')', closer)

                            signature += parameter + ', '

                        if signature == '(':
                            signature += ')'
                        else:
                            signature = signature[:-2] + ')'

                        # Write the calltip.
                        pattern = '{0}{1}'

                        if self.settings['space_before_doc_api'] > 0:
                            if tag or doc:
                                pattern += ' ' * self.settings['space_before_doc_api']

                        if tag and doc:
                            pattern += '{2} {3}'
                        elif tag:
                            pattern += '{2}'
                        elif doc:
                            pattern += '{3}'

                        w.write(pattern.format(name, signature, tag, doc) + '\n')


    def write_properties(self, file='python3_keywords.properties',
                               keywordclasses=None):
        '''Write python3_keywords.properties for SciTE.

        keywordclasses:
            A list of keywordclasses lists.
            If None, use the tuple of self.keywordclasses.
        '''

        if not self._write_started:
            print('write:')
            self._write_started += 1

        print(' ', file)

        if keywordclasses is None:
            keywordclasses = self.keywordclasses

        # Build a comment header to describe the generator details.
        header = ('# Generator: gen_python_3_api.py\n'
                  '# Platform : {}\n'
                  '# Python   : {}.{}.{} {}').format(sys.platform,
                                                     sys.version_info[0],
                                                     sys.version_info[1],
                                                     sys.version_info[2],
                                                     sys.version_info[3])
        # Write keywords to a property file.
        with open(file, 'w', encoding='utf-8') as w:
            w.write(header + '\n\n')

            for index, keywordclass in enumerate(keywordclasses):
                w.write('keywordclass{}.python3=\\\n'.format(index))

                line_length = 0
                last_index = len(keywordclass) - 1

                for index, item in enumerate(keywordclass):
                    line_length += len(item) + 1

                    if index == last_index:
                        w.write(item + '\n')
                    else:
                        w.write(item + ' ')

                    if line_length > 50:
                        w.write('\\\n')
                        line_length = 0

                w.write('\n')


    def write_autocomplete_xml(self, file='python3.xml'):
        '''Write python3.xml for Notepad++.'''

        if not self._write_started:
            print('write:')
            self._write_started += 1

        print(' ', file)

        # Prepare for signature indentation of wrapped lines.
        if self.settings['space_before_parameter_xml'] > 0:
            indent = ' ' * self.settings['space_before_parameter_xml']
        else:
            indent = ''

        # Start building the xml tree.
        tree = xml.etree.ElementTree.TreeBuilder()
        root = tree.start('NotepadPlus', {})
        tree.start('AutoComplete', {})

        tree.start('Environment', {'ignoreCase': 'no',
                                   'startFunc': '(',
                                   'stopFunc': ')',
                                   'paramSeparator': ',',
                                   'additionalWordChar': '.'})
        tree.end('Environment')

        for items in self.api:
            if len(items) == 1:
                name, signatures, tag, doc = items[0], [], '', ''
            else:
                name, signatures, tag, doc = items
                doc = doc.replace('\n', '[INSERT_NEWLINE]')

                if tag:
                    if self.settings['callable_tag'] == 2:
                        tag = '[' + self._callable_tags[tag] + ']'
                    else:
                        tag = '[' + tag + ']'

                if tag and doc:
                    doc = tag + ' ' + doc
                elif tag:
                    doc = tag

                if doc and self.settings['space_before_doc_xml'] > 0:
                    doc = ' ' * self.settings['space_before_doc_xml'] + doc

            # Start xml section.
            tree.start('KeyWord', {'func': 'yes', 'name': name}
                       if signatures else {'name': name})

            # Add parameters into xml section.
            for signature in signatures:
                if not signature and not doc:
                    continue

                length = len(name)

                tree.start('Overload', {'descr': doc, 'retVal': ''})

                for index, parameter in enumerate(signature):
                    length += len(parameter) + 2

                    if index and self.settings['escape_long_signatures']:
                        if length >= self.settings['calltip_width']:
                            parameter = '[INSERT_NEWLINE]' + indent + parameter
                            length = 0

                    tree.start('Param', {'name': parameter})
                    tree.end('Param')

                tree.end('Overload')

            tree.end('KeyWord')

        # End the xml tree.
        tree.end('AutoComplete')
        tree.end('NotepadPlus')
        tree.close()

        # Convert the xml object to a pretty xml string.
        root_string = xml.etree.ElementTree.tostring(root).decode()

        xml_string = (xml.dom.minidom.parseString(root_string)
                      .toprettyxml(indent='\t', encoding='utf-8').decode())

        xml_string = xml_string.replace('[INSERT_NEWLINE]', '&#x0a;')

        # Write the xml file.
        with open(file, 'w', encoding='utf-8') as w:
            w.write(xml_string)


    def write_udl_xml(self, file='userDefineLang_python3.xml'):
        '''Write userDefineLang_python3.xml for Notepad++.'''

        if not self._write_started:
            print('write:')
            self._write_started = 1

        print(' ', file)

        if os.path.isfile(file):
            print('    read from xml file')
            tree = xml.etree.ElementTree.parse(file)
            root = tree.getroot()
        else:
            print('    read from template')
            xml_string = udl_xml_template()
            root = xml.etree.ElementTree.fromstring(xml_string)
            tree = xml.etree.ElementTree.ElementTree(root)

        for keywords in root.findall('./UserLang/KeywordLists/*'):
            for index, name in enumerate(('Keywords1', 'Keywords2', 'Keywords3')):
                if keywords.get('name') == name:
                    keywords.text = ' '.join(self.keywordclasses[index])

        tree.write(file, encoding='utf-8', xml_declaration='utf-8')


def udl_xml_template():
    '''Template for userDefineLang_python3.xml before keywords are inserted.

    These xml tags are expected to be updated with keywords:
        <Keywords name="Keywords1">
        <Keywords name="Keywords2">
        <Keywords name="Keywords3">

    If values in these tags exist, they will be replaced.
    If any of these tags do not exist, then the missing
    tags get no keywords inserted.

    Return:
        xml as string
    '''

    return r'''<?xml version="1.0" encoding="utf-8"?>
<NotepadPlus>
    <UserLang name="Python3" ext="py pyw" udlVersion="2.1">
        <Settings>
            <Global caseIgnored="no" allowFoldOfComments="yes" foldCompact="no" forcePureLC="0" decimalSeparator="0" />
            <Prefix Keywords1="no" Keywords2="no" Keywords3="no" Keywords4="no" Keywords5="no" Keywords6="no" Keywords7="no" Keywords8="no" />
        </Settings>
        <KeywordLists>
            <Keywords name="Comments">00# 01 02((EOL)) 03&quot;&quot;&quot; 03&apos;&apos;&apos; 04&quot;&quot;&quot; 04&apos;&apos;&apos;</Keywords>
            <Keywords name="Numbers, prefix1"></Keywords>
            <Keywords name="Numbers, prefix2"></Keywords>
            <Keywords name="Numbers, extras1"></Keywords>
            <Keywords name="Numbers, extras2"></Keywords>
            <Keywords name="Numbers, suffix1"></Keywords>
            <Keywords name="Numbers, suffix2"></Keywords>
            <Keywords name="Numbers, range"></Keywords>
            <Keywords name="Operators1">( ) [ ] { } , : . ; @ = - + * / % &amp; | ^ &gt; &lt;</Keywords>
            <Keywords name="Operators2"></Keywords>
            <Keywords name="Folders in code1, open"></Keywords>
            <Keywords name="Folders in code1, middle"></Keywords>
            <Keywords name="Folders in code1, close"></Keywords>
            <Keywords name="Folders in code2, open"></Keywords>
            <Keywords name="Folders in code2, middle"></Keywords>
            <Keywords name="Folders in code2, close"></Keywords>
            <Keywords name="Folders in comment, open"></Keywords>
            <Keywords name="Folders in comment, middle"></Keywords>
            <Keywords name="Folders in comment, close"></Keywords>
            <Keywords name="Keywords1"></Keywords>
            <Keywords name="Keywords2"></Keywords>
            <Keywords name="Keywords3"></Keywords>
            <Keywords name="Keywords4"></Keywords>
            <Keywords name="Keywords5"></Keywords>
            <Keywords name="Keywords6"></Keywords>
            <Keywords name="Keywords7"></Keywords>
            <Keywords name="Keywords8"></Keywords>
            <Keywords name="Delimiters">00&quot; 00&apos; 01\ 01\ 02&quot; 02&apos; 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23</Keywords>
        </KeywordLists>
        <Styles>
            <WordsStyle name="DEFAULT" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="COMMENTS" fgColor="7F0000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="LINE COMMENTS" fgColor="007F00" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="NUMBERS" fgColor="007F7F" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="KEYWORDS1" fgColor="00007F" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />
            <WordsStyle name="KEYWORDS2" fgColor="00007F" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />
            <WordsStyle name="KEYWORDS3" fgColor="DD9900" bgColor="FFFFFF" fontName="" fontStyle="1" nesting="0" />
            <WordsStyle name="KEYWORDS4" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="KEYWORDS5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="KEYWORDS6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="KEYWORDS7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="KEYWORDS8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="OPERATORS" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="FOLDER IN CODE1" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="FOLDER IN CODE2" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="FOLDER IN COMMENT" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS1" fgColor="7F007F" bgColor="FFF9FF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS2" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS3" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS4" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
            <WordsStyle name="DELIMITERS8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" nesting="0" />
        </Styles>
    </UserLang>
</NotepadPlus>
'''


if __name__ == '__main__':

    # Display help message if requested.
    if len(sys.argv) > 1:
        if sys.argv[1] in ('-h', '--help', '/?'):
            print(__doc__.strip())
            exit()
        else:
            exit('Arguments supported: -h, --help, /?')

    # Create an instance with updated settings.
    calltips = Calltips(settings)

    # Make SciTE files.
    calltips.make_scite_files()

    # Make Notepad++ files.
    if sys.platform == 'win32':
        calltips.make_npp_files()

    print('done')
