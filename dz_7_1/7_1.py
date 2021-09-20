import os

ROOT = os.path.dirname(__file__)
print(__file__)
dir_name = 'my_project/settings'
dir_path = os.path.join(ROOT, dir_name)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

dir_name = 'my_project/mainapp'
dir_path = os.path.join(ROOT, dir_name)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

dir_name = 'my_project/adminapp'
dir_path = os.path.join(ROOT, dir_name)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)


dir_name = 'my_project/authapp'
dir_path = os.path.join(ROOT, dir_name)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
