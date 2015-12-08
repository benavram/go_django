# -*- coding: utf-8 -*-
"""Setup Django Project Template Setup (go_django)
    dependencies:
        django==1.8
https://github.com/benavram/go_django.git
"""

import os
import shutil

DIRECTORY = ['static', 'static/media_root', 'static/static_root']
for i in DIRECTORY:
    try:
        if not os.path.exists(i):
            os.makedirs(i)
            msg = i + " created"
            print(msg)
    except OSError as error:
        print('%s (%s)' % (error, type(error)))

PROJ_DIR = '{{ project_name }}'
try:
    shutil.move(PROJ_DIR, 'src')
    print('project directory renamed')
except OSError as error:
    print(error)



