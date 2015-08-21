import sys
if len(sys.argv)!= 3:
    print 'exe,path,txt'
    exit()
import os 
Path = os.path.abspath(sys.argv[1])
Found = sys.argv[2]
l=[]
def func(Path,Found):
    for i in os.listdir(Path):
        subpath=os.path.join(Path,i)
        print subpath
        if os.path.isdir(subpath):
            func(subpath,Found)
        if Found in os.path.split(subpath)[1]:
            l.append(subpath)
    return l
func(Path,Found)
print l

