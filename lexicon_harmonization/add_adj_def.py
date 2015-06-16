#!/usr/bin/python
import sys
lexicon={}
for line in sys.stdin: # lexicon
  token,lemma,msd=line.decode('utf8').strip().split('\t')
  token=token.lower()
  if token not in lexicon:
    lexicon[token]=set()
  lexicon[token].add((lemma,msd))
#print 'lexicon loaded'
for line in open(sys.argv[1]):
  if line.strip()=='':
    sys.stdout.write(line)
  else:
    els=line.decode('utf8').split('\t')
    token=els[1].lower()
    lemma,msd=els[2],els[4]
    if msd.startswith('A'):
      if token not in lexicon:
        if msd.endswith('msn') and not token.endswith('i'):
          sys.stdout.write('\t'.join(els[:4]+[msd[:6]+'n'+msd[6:]]+els[5:]).encode('utf8'))
        else:
          sys.stdout.write('\t'.join(els[:4]+[msd[:6]+'y'+msd[6:]]+els[5:]).encode('utf8'))
      else:
        if ((lemma,msd[:6]+'n'+msd[6:]) in lexicon[token]) or (msd.endswith('msn') and not token.endswith('i')):
          sys.stdout.write('\t'.join(els[:4]+[msd[:6]+'n'+msd[6:]]+els[5:]).encode('utf8'))
        else:
          sys.stdout.write('\t'.join(els[:4]+[msd[:6]+'y'+msd[6:]]+els[5:]).encode('utf8'))
    else:
      sys.stdout.write(line)
