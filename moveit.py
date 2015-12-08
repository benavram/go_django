# -*- coding: utf-8 -*-
"""Setup Django Project Template Setup (go_django)
    moveit
https://github.com/benavram/go_django.git
"""
import shutil

shutil.move('.gitignore', '../.gitignore')
shutil.move('requirements.txt', '../requirements.txt')
shutil.move('main.py', '../main.py')

