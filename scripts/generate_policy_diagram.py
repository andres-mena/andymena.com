"""Generate the website's policy-learning illustrations (no third-party dependencies)."""
from pathlib import Path
import random
from html import escape

ASSETS = Path(__file__).resolve().parents[1] / 'site' / 'assets'
BLUE = '#80b7ff'
LIGHT = '#d7e5fa'
MUTED = '#9caecb'

def person(x, y, shape, color, opacity=1):
    body = '<path d="M-10 6H10L15 33H-15Z"/>' if shape else '<rect x="-11" y="6" width="22" height="27" rx="3"/>'
    return f'<g transform="translate({x} {y})" fill="{color}" opacity="{opacity}"><circle cy="-7" r="9"/>{body}</g>'

def text(x, y, value, color=LIGHT, size=12):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-family="Arial,Helvetica,sans-serif" text-anchor="middle">{escape(value)}</text>'

def population():
    s=''
    for row in range(3):
        for col in range(3):
            x,y=65+65*col,40+61*row
            s += person(x,y,(row+col)%2,MUTED,.8)
            s += text(x+17,y-15,'?',LIGHT,16)
    return s

def experiment():
    s=text(65,18,'TREATED',BLUE,11)+text(195,18,'CONTROL',LIGHT,11)
    s+='<path d="M130 33V196" stroke="#d7e5fa" stroke-opacity=".2"/>'
    for side in range(2):
        for row in range(3):
            for col in range(2):
                s+=person(40+50*col+130*side,51+55*row,(row+col)%2,BLUE if side==0 else LIGHT,.95 if side==0 else .65)
    return s

def learn():
    rng=random.Random(42)
    s='<path d="M25 178H242M32 185V28" stroke="#d7e5fa" stroke-opacity=".3"/>'
    s+='<path d="M56 178L204 35L238 35V178Z" fill="#80b7ff" fill-opacity=".075"/>'
    for i in range(98):
        x=max(44,min(228,rng.gauss(132,37)))
        y=max(38,min(168,rng.gauss(104,31)))
        score=x+y-231
        color=BLUE if score>0 else LIGHT
        shape=i%2
        if shape:
            s+=f'<path d="M{x:.1f} {y-3:.1f}l3.5 6h-7Z" fill="{color}" opacity=".8"/>'
        else:
            s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.7" fill="{color}" opacity=".7"/>'
    s+='<path d="M56 178L204 35" stroke="#aaccff" stroke-width="2" stroke-dasharray="5 5"/>'
    s+=text(80,202,'Different responses',LIGHT,11)+text(192,202,'Learn a rule',BLUE,11)
    return s

def decide():
    s=''
    selected={0,2,4,7}
    for row in range(3):
        for col in range(3):
            i=row*3+col;x,y=65+65*col,40+61*row
            is_selected=i in selected
            s+=person(x,y,(row+col)%2,BLUE if is_selected else MUTED,1 if is_selected else .4)
            if is_selected:
                s+=f'<circle cx="{x+17}" cy="{y-11}" r="9" fill="#d7e5fa"/><path d="M{x+13} {y-11}l3 3 5-6" fill="none" stroke="#233393" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    return s

stages=[('population','Start with people','Different people. Unknown effects.',population()),('experiment','Run an experiment','Compare treatment and control.',experiment()),('learn','Learn who benefits','Find patterns in treatment effects.',learn()),('decide','Make a decision','Choose whom to treat.',decide())]
for name,title,description,art in stages:
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 210" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{description}</desc>{art}</svg>\n'
    (ASSETS/f'policy-{name}.svg').write_text(svg)

full='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 430" role="img" aria-labelledby="title desc"><title id="title">Who should be treated?</title><desc id="desc">Policy learning: start with people, run an experiment, learn who benefits, and choose whom to treat. Conceptual illustration.</desc><rect width="1280" height="430" rx="12" fill="#122654"/>'
full+=text(640,42,'FROM CAUSAL INFERENCE TO POLICY LEARNING',LIGHT,13)
full+=text(640,80,'Who should be treated?','#ffffff',28)
for i,(_,title,description,art) in enumerate(stages):
    x=24+i*312
    full+=f'<g transform="translate({x} 105)"><rect width="296" height="278" rx="6" fill="#ffffff" fill-opacity=".035" stroke="#d7e5fa" stroke-opacity=".2"/><g transform="translate(18 6)">{art}</g>{text(148,238,title,"#ffffff",17)}{text(148,260,description,LIGHT,12)}</g>'
    if i<3: full+=text(x+304,243,'→',LIGHT,20)
full+=text(640,412,'A policy balances estimated benefits, costs, and constraints.',LIGHT,12)+'</svg>\n'
(ASSETS/'policy-learning.svg').write_text(full)
print('Generated four responsive panels and standalone diagram.')
