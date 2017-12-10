import zipfile
from os import listdir
from os.path import isfile, join
directory = "E:\\Web Nano\\"
onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
for o in onlyfiles:
    if o.endswith(".zip"):
        print(directory+o)
        with zipfile.ZipFile(directory+o,"r") as zip_ref:
            zip_ref.extractall("E:\\Web Nano\\Files")