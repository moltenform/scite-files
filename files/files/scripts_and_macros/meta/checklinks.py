
from ben_python_common import *
import re

def go():
    presentLocally = dict()
    for full, short in files.recursefiles(localroot):
        assert full.startswith(localroot)
        trunc = full[len(localroot):]
        trunc = trunc.replace('\\', '/')
        presentLocally[trunc] = 0
    
    reg = re.compile(r'https://raw.githubusercontent.com/downpoured/scite-files/master(/[^ ()">]+)')
    for full, short in files.recursefiles(localroot):
        if short.endswith('.md'):
            alltxt = files.readall(full, 'rb', 'utf-8')
            assert 'googlecode' not in alltxt
            for match in re.finditer(reg, alltxt):
                path = match.group(1)
                if path not in presentLocally:
                    print 'broken link'
                    print 'in markdown file ' + full
                    print 'points to non-existant ' + match.group(0)
                    print '(%s)' % path
                    assert False
                else:
                    presentLocally[path] = 1
    
    for path in presentLocally:
        if presentLocally[path] == 0:
            if '.gitattributes' in path or '.gitignore' in path:
                continue
            if '/archived/' in path:
                continue
            if '/greek_site/' in path:
                continue
            if path.endswith('.md'):
                continue
            print 'warning: did not see any links to ' + path
    
localroot = r'C:\b\pydev\dev\scite-with-python\scite-files\scite-files'
go()
