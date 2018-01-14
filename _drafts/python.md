#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

#!/bin/sh
find . -path "*/migrations/*" -not -name "__init__.py" -delete &&
find . -name "db.sqlite3" -delete &&
rm -rf media static &&
python manage.py makemigrations &&
python manage.py migrate &&
echo "\
from backend import init;\
init.init();\
" | python manage.py shell &&
python manage.py runserver





pip install virtualenv
virtualenv venv
source venv/bin/activate


ALLOWED_HOSTS = ['*']
LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'
