import os
from subprocess import Popen, PIPE



home = os.path.expanduser('~')
print(home)
os = subprocess.call('diskpart')
print(os)
# osDrive = type(subprocess.run('%homedrive%'))
# # os.system('ipconfig')
# print(osDrive)
