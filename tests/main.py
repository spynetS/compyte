#!/usr/bin/env python3

from compyte.compyte import parse
from compyte.jinja import Jinja2TemplatesCompyte
# from fastapi.templating import Jinja2Templates
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2TemplatesCompyte(directory=str(BASE_DIR))
print(BASE_DIR)
# templates = Jinja2Templates(directory=str(BASE_DIR / "tests"))

print(templates.jinja_render('index.html',{'request':""}))
