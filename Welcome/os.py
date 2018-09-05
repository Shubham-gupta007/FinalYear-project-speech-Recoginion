#It shows all files in dir

import os
names = os.popen('dir D:\\').readlines()
#os.path.commonpath('dir D:\\').readlines()
for name in names:
    print(name)