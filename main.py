import os
import shutil

path = '/home/rnzimcpp/Downloads/testdisk-7.2/perv'
to = os.getcwd() + '/'
countFiles = 0
png = 0
pdf = 0
jpg = 0
mp4 = 0

# Criar diretórios de destino se não existirem
if not os.path.exists(to + 'png'):
    os.makedirs(to + 'png')
if not os.path.exists(to + 'jpg'):
    os.makedirs(to + 'jpg')
if not os.path.exists(to + 'pdf'):
    os.makedirs(to + 'pdf')
if not os.path.exists(to + 'mp4'):
    os.makedirs(to + 'mp4')





for folder in os.listdir(path):
    newPath = os.path.join(path, folder)
    print(20*"-")
    print(f"Folder Now {folder}")
    print(f"Copy in {newPath}")
    print(f'Files {len(newPath)}')
  
    if os.path.isdir(newPath):  # Verifique se é um diretório
        for file in os.listdir(newPath):
            filePath = os.path.join(newPath, file)
            countFiles += 1
            if file.endswith('.png'):
                png += 1
               
                shutil.copy(filePath, os.path.join(to, 'png'))
              
            elif file.endswith('.jpg'):
                jpg += 1
               
                shutil.copy(filePath, os.path.join(to, 'jpg'))
               
            elif file.endswith('.pdf'):
                pdf += 1
               
                shutil.copy(filePath, os.path.join(to, 'pdf'))
            elif file.endswith('.mp4'):
                mp4 += 1
               
                shutil.copy(filePath, os.path.join(to, 'mp4'))    

print(f"Achei: {countFiles} Arquivos \nPng: {png} \nPDF: {pdf} \nMP4: {mp4} \nJPG: {jpg}")
