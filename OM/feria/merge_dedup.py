import csv, glob, re, unicodedata, difflib, json
csv.field_size_limit(10**9)
A=glob.glob('/mnt/user-data/attachments/*/')[0]
out='/tmp/claude-0/-home-claude/ce90152d-f7e1-55e4-a5e5-960a64c736b9/scratchpad/rsl_data/'
def norm(t):
    t=unicodedata.normalize('NFKD',t or '').encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+',' ',t).strip()
def ndoi(d): 
    d=(d or '').strip().lower()
    return re.sub(r'^https?://(dx\.)?doi\.org/','',d)

sc=[]
for r in csv.DictReader(open(glob.glob(A+'*scopus_86.csv')[0],encoding='utf-8-sig')):
    sc.append(dict(titulo=r['Title'].strip(),autores=r['Authors'].strip(),anio=r['Year'],revista=r['Source title'].strip(),
        doi=ndoi(r['DOI']),base='Scopus',resumen=(r['Abstract'] or '').replace('[No abstract available]','').strip(),
        tipo=r['Document Type'],enlace=r['Link']))
se=[]
raw=open(glob.glob(A+'*scielo.csv')[0],encoding='utf-8-sig').read().replace('" \n','"\n')
for r in csv.DictReader(raw.splitlines(),skipinitialspace=True):
    r={k.strip():(v or '').strip() for k,v in r.items() if k}
    se.append(dict(titulo=r['Title'],autores=r['Author(s)'],anio=r['Publication year'],revista=r['Journal'],doi='',
        base='SciELO',resumen='',tipo='',enlace=r['Fulltext URL']))
print('Scopus',len(sc),'SciELO',len(se))

merged=[];dups=[];fuzzy=[]
seen_doi={};seen_t={}
for rec in sc+se:
    nt=norm(rec['titulo']); d=rec['doi']
    hit=None;why=''
    if d and d in seen_doi: hit=seen_doi[d];why='DOI'
    elif nt in seen_t: hit=seen_t[nt];why='título normalizado'
    else:
        for k,m in seen_t.items():
            ratio=difflib.SequenceMatcher(None,nt,k).ratio()
            if ratio>=0.90: hit=m;why=f'título similar ({ratio:.2f})';break
    if hit is not None:
        dups.append(dict(eliminado=rec['titulo'],base_eliminado=rec['base'],conservado=hit['titulo'],base_conservada=hit['base'],criterio=why))
        for f in ('doi','resumen','tipo'):
            if not hit[f] and rec[f]: hit[f]=rec[f]
        hit['base']=' + '.join(sorted(set(hit['base'].split(' + '))|{rec['base']}))
        continue
    merged.append(rec)
    if d: seen_doi[d]=rec
    seen_t[nt]=rec
for i,r in enumerate(merged,1): r['id']=i
json.dump(dict(scopus=len(sc),scielo=len(se),unicos=len(merged),duplicados=dups),open(out+'stats.json','w'),ensure_ascii=False,indent=1)
cols=['id','titulo','autores','anio','revista','doi','base','resumen','tipo','enlace']
w=csv.DictWriter(open(out+'tabla_unica.csv','w',newline='',encoding='utf-8-sig'),fieldnames=cols+['decision','motivo_exclusion','rq'])
w.writeheader()
for r in merged: w.writerow({**{c:r[c] for c in cols},'decision':'','motivo_exclusion':'','rq':''})
print('unicos',len(merged),'duplicados',len(dups))
for d in dups: print(d)
print('sin DOI',sum(1 for r in merged if not r['doi']),'sin resumen',sum(1 for r in merged if not r['resumen']))
