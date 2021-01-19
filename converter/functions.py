
import os
def write_to_file(f,folder):
    path=os.path.join("converter/static/upload",folder,f.name)
    print('path== ',path)
    #path='converter/static/upload/'+f.name
    with open(path, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    return path

def handle_uploaded_file(f):  
    return write_to_file(f,'file_to_convert')
    
def handle_uploaded_file2(files):
    list_files=[]
    list_files.append(files['small_file1'])
    list_files.append(files['small_file2'])
    list_files.append(files['capital_file1'])
    list_files.append(files['capital_file2'])
    list_files.append(files['digit_file'])
    path_to_uploaded=[]
    for f in list_files:
        path_to_uploaded.append(write_to_file(f,'traine_model'))
    path_to_uploaded.append(write_to_file(files['text_file'],'file_to_convert'))
    print(path_to_uploaded)
    return path_to_uploaded




        
