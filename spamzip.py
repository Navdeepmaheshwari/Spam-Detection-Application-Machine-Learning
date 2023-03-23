import zipfile
my_zip = zipfile.ZipFile('txt.zip') # Specify your zip file's name here
storage_path = '.'
data=[]
for file in my_zip.namelist():
    if my_zip.getinfo(file).filename.endswith('.txt'):
       data.append( my_zip.read(file))
    #    data.append( my_zip.extract(file) )# extract the file to current folder if it is a text file
print(data)