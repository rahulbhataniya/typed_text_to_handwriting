from django.shortcuts import render  
import mimetypes
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
from converter.functions import *
from converter.form import Uploadform  
import converter.txttohand
import converter.input
from . import txttohand
def index(request):  
    print(len(request.FILES))
    if request.method == 'POST':  
        uploaded_form = Uploadform(request.POST, request.FILES)  
        if uploaded_form.is_valid(): 
            path=handle_uploaded_file(request.FILES['file']) #its for upload file in data base
            #path=os.path.join("converter/static/upload",folder,f.name)
            #path_to_pdf=converter.txttohand.convert_to_pdf(path,request.FILES['file'].name,"E:\\txttohandwritting-master\\file\\") #for convertion of file in to handwriting
            nameof_file=request.FILES['file'].name
            filename=nameof_file.split('.')[0]
            path_to_pdf=converter.txttohand.convert_to_pdf(path,filename)

            
            return render(request,"download.html",{'path_to_pdf':path_to_pdf})  
    else:  
        uploaded_form = Uploadform()  
        return render(request,"index.html",{'form':uploaded_form})

def download_file(request):
    fl_path = request.GET['pdf_to_download']
    print('path to downlaodeble pdf in sidedownload function  : ',fl_path)
    filename = 'converted.pdf'
    fl = open(fl_path,'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def train_upload(request):
    print("insede more upload",len(request.FILES))
    if request.method == 'POST':
        print(type(request.FILES))
        list_of_6_path=handle_uploaded_file2(request.FILES)
        path_to_read=converter.input.genrate_char(list_of_6_path[:5])
        print( path_to_read)
        path_to_pdf=converter.txttohand.convert_to_pdf(list_of_6_path[5],request.FILES['text_file'].name) #for convertion of file in to handwriting
        return render(request,"download.html",{'path_to_pdf':path_to_pdf})
    else:
        return render(request, 'upload_hdwriting.html')
