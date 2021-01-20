from django.shortcuts import render  
import mimetypes
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
from converter.functions import *
from converter.form import Uploadform  
import converter.txttohand
import converter.input
from . import txttohand
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Image
from .form import ImageForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



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
            print(path_to_pdf)
            return render(request,"download.html",{'path_to_pdf':path_to_pdf}) 
            #return render(request,"home.html") 
    else:  
        uploaded_form = Uploadform()  
        return render(request,"index.html",{'form':uploaded_form})

def download_file(request):
    print('..............ha agaya....')
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
        #return (request,"home.html")
    else:
        return render(request, 'upload_hdwriting.html')


def showimage(request):
    if request.method == 'POST':
        print("uploaded file name is")
        #print(request.FILES['name'])
        print(request.FILES)
        name_of_person="tmep"
        request.FILES['imagefile1'].name='0_9.jpg'
        request.FILES['imagefile2'].name='a_n.jpg'
        request.FILES['imagefile3'].name='m_z.jpg'
        request.FILES['imagefile4'].name='A_N.jpg'
        request.FILES['imagefile5'].name='M_Z.jpg'
        request.FILES['imagefile6'].name='text.jpg'
        current_form=ImageForm(request.POST,request.FILES)
        if current_form.is_valid():
            current_form.save()
        lastimage= Image.objects.last()
        imagefile= lastimage.imagefile1
        context={'imagefile':imagefile,'form':current_form}
        return render(request,'image.html',context)
    else:
        current_form=ImageForm()
        context={'form':current_form}
        return render(request,'image.html',context)

def access_data(request):
    image_data= Image.objects.get(name=70)
    print("Myoutput",image_data)
    return render(request,'show_image.html',{'data': image_data})



def homepage(request):
    return render(request = request,template_name='home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("converter:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = UserCreationForm()
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})



def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("converter:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})