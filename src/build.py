"""Genera el sitio estático en la raíz del repositorio. Uso: cd src && python3 build.py"""
import re,importlib,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from common import css,JS
import anatomy
from anatomy_text import AN
EXTRA="""
.road.r4{grid-template-columns:repeat(4,1fr)}
.road.r4 div:nth-child(4)::before{border-color:SOFT}
.scope .rules li b{font:600 16px HEADF;color:INK}
.pick{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:40px 0 20px}
.pick a{text-decoration:none;color:INK;transition:transform .3s,border-color .3s}
.pick a:hover{transform:translateY(-4px);border-color:CORAL}
.pick h3{margin-top:12px}
@media (max-width:980px){.road.r4,.pick{grid-template-columns:1fr 1fr}}
@media (max-width:720px){.road.r4,.pick{grid-template-columns:1fr}}
"""
def fill(T,d):
    miss=set(re.findall(r'\{\{(\w+)\}\}',T))-set(d)
    if miss: raise SystemExit(f'faltan claves: {miss}')
    return re.sub(r'\{\{(\w+)\}\}',lambda m:d[m.group(1)],T)
T=open('template.html',encoding='utf-8').read()
for L in ['es','en','ar']:
    D=importlib.import_module(L).D
    d=dict(D); d.update(AN[L]); d['css']=css(L); d['js']=JS
    d['anat']=anatomy.spine(AN[L]); d['big3']=anatomy.big3(AN[L])
    for x in ['es','en','ar']: d['cur_'+x]='aria-current="page"' if x==L else ''
    open(f'../lumbar-saudi-{L}.html','w',encoding='utf-8',newline='\n').write(fill(T,d))
    print(L,'extra',set(D)-set(re.findall(r'\{\{(\w+)\}\}',T)))
es=importlib.import_module('es').D
open('../plan.html','w',encoding='utf-8',newline='\n').write(fill(open('plan_template.html',encoding='utf-8').read(),dict(css=css('es',EXTRA),js=JS,st_zen=es['st_zen'],bodymap=anatomy.bodymap())))
open('../index.html','w',encoding='utf-8',newline='\n').write(fill(open('index_template.html',encoding='utf-8').read(),dict(css=css('es',EXTRA),js=JS)))
print('ok: index.html, plan.html, lumbar-saudi-{es,en,ar}.html')
