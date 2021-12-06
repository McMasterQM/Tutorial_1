import os

path = os.getcwd()
fname='Normalizing_eigenfunctions.py'

os.system('jupyter nbconvert --to script Normalizing_eigenfunctions.ipynb')

with open(fname, 'r') as f:
    lines = f.readlines()
with open(os.path.join(path, 'problem', fname), 'w') as f:
    for line in lines:
        if "get_ipython()" in line:
            continue
        elif 'nbconvert --to script' in line:
            break
        else:
            f.write(line)
os.remove(fname)
