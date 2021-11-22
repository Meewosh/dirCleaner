import os, shutil

SOURCE_DIR = 'C:\\Users\\Meewosh\\Desktop\\temp'

DEST = 'I:\\'
DEST_PDF = 'PDF'
DEST_OFFICE = 'OFFICE'
DEST_ARCHIVE = 'ARCHIVE'
DEST_FOTOVIDEO = 'FOTOVIDEO'
DEST_PROGRAMMING = 'PROGRAMMING'
DEST_ISO = 'ISO'

EXT_PDF = ('.pdf','.epub')
EXT_OFFICE = ('.doc','.docx','.xlsx','.csv','.pptx', '.odp','.ppt')
EXT_ARCHIVE = ('.zip','.7z', '.rar')
EXT_FOTOVIDEO = ('.jpeg', '.jpg', '.png', '.mp4','.mkv','.mov')
EXT_PROGRAMMING = ('.cpp', '.c', '.py', '.json','.txt','.conf')
EXT_ISO = ('.ova', '.iso')
EXT_MSI = ('.msi')

def sort_function(source, destination, extension):
    for root, dirs, files in os.walk(source):
        for f in files:
            if f.lower().endswith(extension):
                path=os.path.join(root, f)
                shutil.move(path, destination)

def remove_function(source, extension):
    for root, dirs, files in os.walk(source):
        for f in files:
            if f.lower().endswith(extension):
                path=os.path.join(root, f)
                os.remove(path)

sort_function(SOURCE_DIR, f'{DEST}{DEST_PDF}', EXT_PDF)
sort_function(SOURCE_DIR, f'{DEST}{DEST_ARCHIVE}', EXT_OFFICE)
sort_function(SOURCE_DIR, f'{DEST}{DEST_ARCHIVE}', EXT_ARCHIVE)
sort_function(SOURCE_DIR, f'{DEST}{DEST_FOTOVIDEO}', EXT_FOTOVIDEO)
sort_function(SOURCE_DIR, f'{DEST}{DEST_PROGRAMMING}', EXT_PROGRAMMING)
sort_function(SOURCE_DIR, f'{DEST}{DEST_ISO}', EXT_ISO)

remove_function(SOURCE_DIR, EXT_MSI)

#TODO: Rename the file if it exists in the destination folder then move