#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
from bs4.element import Tag
import black

def replace_components(html,local_scope):
    soup = BeautifulSoup(html, 'html.parser')

    components = soup.find_all(attrs={"component": True})
    comp: Tag
    for comp in components:
        comp.attrs['children'] = parse(comp.decode_contents(),local_scope)
        new_html = parse(open(comp.attrs['component'],"r").read(),local_scope,props=comp.attrs)
        comp.replace_with(BeautifulSoup(new_html, 'html.parser'))

    return soup.prettify()

def parse(template,local_scope, props: dict = {}):
    template = replace_components(template,local_scope)
    local_scope['props'] = props

    # Pattern to find exec blocks
    exec_pattern = r"\{\$(.*?)\$\}"
    exec_matches = re.findall(exec_pattern, template, re.S)

    for part in exec_matches:
        formatted_code = black.format_str(part, mode=black.FileMode())
        print("exec", formatted_code, sep="\n")

        # Execute the code in the local scope
        exec(formatted_code,local_scope)  # Execute the code in the local scope

        # Remove the executed block from the template
        template = template.replace("{$" + part + "$}", "")

    # Pattern to find eval blocks
    eval_pattern = r"\{%(.*?)%\}"
    eval_matches = re.findall(eval_pattern, template, re.S)


    for part in eval_matches:
        formatted_code = black.format_str(part, mode=black.FileMode())
        print("val", formatted_code, sep="\n")

        val = eval(formatted_code,local_scope)  # Use the same local scope
        template = template.replace("{%" + part + "%}", str(val) if val is not None else "")

    return template
