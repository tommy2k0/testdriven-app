# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:07:18 2019

@author: tommy
"""

from flask.cli import FlaskGroup
from project import app

cli = FlaskGroup(app)   # allows to run and manage the app from the command line

if __name__ == '__main__':
    cli()

