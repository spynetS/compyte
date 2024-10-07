#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
from bs4.element import Tag


def replace_components(html):
    soup = BeautifulSoup(html, 'html.parser')

    components = soup.find_all(attrs={"component": True})
    comp: Tag
    for comp in components:
        comp.attrs['children'] = parse(comp.decode_contents())
        print(comp.attrs['children'])
        print(comp.attrs)
        new_html = parse(open(comp.attrs['component'],"r").read(),comp.attrs)
        print(new_html)
        comp.replace_with(BeautifulSoup(new_html, 'html.parser'))

    return soup.prettify()

def parse(template,props:dict = None):
    template = replace_components(template)

    exec_pattern = r"\{\$(.*?)\$\}"
    exec_matches = re.findall(exec_pattern, template)

    for part in exec_matches:
        exec(part.strip())
        template = template.replace("{$"+part+"$}", "")

    eval_pattern = r"\{%(.*?)%\}"
    eval_matches = re.findall(eval_pattern, template, re.S)

    for part in eval_matches:
        print("excecute",part.strip())
        val = ""
        val = str(eval(part.strip()))
        template = template.replace("{%"+part+"%}", val if val != None else "")
    return template
