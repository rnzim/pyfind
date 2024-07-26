import os
import shutil
###Caminho desejado 
path = '/home/rnzimcpp/Downloads/testdisk-7.2/ot'+'/'
###
to = os.getcwd()+'/'+'size'

mainDir = os.listdir(path)
countFile = 0
extension = []
size = []
mb = 2

for folder in range(0,len(mainDir)):
    fileName = mainDir[folder]
    newDir = path+fileName
    for dir in range(0,len(os.listdir(newDir))):
       file = os.listdir(newDir)[dir]
       fileSize = int(os.path.getsize(newDir+'/'+file))
       fileSizeKb = (fileSize/1024)
       fileFullPath = newDir+'/'+file
      
       extensionFile = os.path.splitext(os.listdir(newDir)[dir])[1]
       print(10*'-')
       print(f'Procurando...\nEncontrados: {countFile}')
       #print(extensionFile)

       if (fileSize/1024) > 1000*mb:
      
        size.append('Path: '+str(fileFullPath)+' size: '+str((fileSize/1024/1024))+': MB')
        shutil.copy(fileFullPath,to)
      

       
       countFile+=1
print(f'Existe {countFile} Arquivos \nExiste {len(size)} Maio Que {mb} Mb')
with open(os.getcwd()+'/filesize.txt','w') as fileWrite:
      fileWrite.write(str(size))
      fileWrite.close()
print('end')



