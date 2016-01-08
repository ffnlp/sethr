import sys

map=dict([(a,c) for a,b,c,d in [e.strip().split('\t') for e in open('../mte4r-upos.mapping')]])

for path in ['../set.hr.conll','../web.hr.conll','../news.hr.conll','../set.hr.test.conll','../set.sr.test.conll','../wiki.hr.test.conll','../wiki.sr.test.conll','../web.hr.test.conll']:
  lines=open(path).readlines()
  out=open(path,'w')
  for line in lines:
    if line.strip()=='':
      out.write('\n')
    else:
      line=line.split('\t')
      line[5]=map[line[4]]
      out.write('\t'.join(line))
  out.close()
  print path,'done'
  