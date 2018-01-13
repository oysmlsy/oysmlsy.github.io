#!/bin/sh

$0就是该bash文件名
current_path=$(cd $(dirname $0); pwd)
parrent_path=$(cd $(dirname $0)/../; pwd)

python manage.py makemigrations 1>/dev/null

