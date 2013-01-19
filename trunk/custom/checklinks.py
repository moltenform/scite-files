
import os, shutil
urlbase = 'http://scite-files.googlecode.com/svn-history/'
trunkbase=r'C:\serve\scite-files-wiki\svn'
wikibase = trunkbase +'\\wiki'

#Ben Fisher: check for broken links on this site itself.

def gopair(wikilist, directory):
	txt=''
	for wiki in wikilist: txt+=getalltxt(os.path.join(wikibase, wiki))
	for fname in os.listdir(os.path.join(trunkbase,directory.replace('/','\\'))):
		if '(notonline)' in fname: continue
		if os.path.isdir(trunkbase+'\\'+directory+'\\'+fname): continue
		onlinename = urlbase+directory+'/'+fname
		parts = txt.split(onlinename+'"')
		if len(parts)==1: print fname, 'not found in', wikilist; assert False
		elif len(parts)>2: print 'waring:', fname, 'listed twice in', wikilist; assert False
			
	# now check for broken links
	allparts = txt.split(urlbase)[1:]
	for link in allparts:
		fulllink = urlbase+link.split('"')[0]
		assert not ' ' in fulllink, 'invalid link + '+fulllink
		filepath = trunkbase+'\\'+link.split('"')[0].replace('/','\\')
		if not os.path.exists(filepath):
			print 'broken link to ',filepath; assert False

def go():
	gopair(['Customization.wiki'], 'trunk/extras')
	gopair(['Translations.wiki'], 'trunk/translations')
	
	
def getalltxt(filename):
	assert os.path.exists(filename)
	f = open(filename, 'r')
	txt = f.read()
	f.close()
	return txt

if __name__=='__main__':
	go()