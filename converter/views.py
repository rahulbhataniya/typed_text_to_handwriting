from django.forms.widgets import Media
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

def index(request):
    if request.method == 'POST': 
        print(str(request.user))
        print(User.username,type(User.username))
        print(len(request.FILES))
        uploaded_form = Uploadform(request.POST, request.FILES)  
        if uploaded_form.is_valid(): 
            path=handle_uploaded_file(request.FILES['file']) #its for upload file in data base
            nameof_file=request.FILES['file'].name
            filename=nameof_file.split('.')[0]
            path_to_pdf=converter.txttohand.convert_to_pdf(path,filename)
            print(path_to_pdf)
            return render(request,"download.html",{'path_to_pdf':path_to_pdf}) 
            #return render(request,"home.html") 
    else:  
        uploaded_form = Uploadform()  
        return render(request,"index.html",{'form':uploaded_form})


def user_index(request):
    if request.method == 'POST':  
        uploaded_form = Uploadform(request.POST, request.FILES) 
        u_name=str(request.user)
        request.FILES['file'].name=u_name
        if uploaded_form.is_valid(): 
            path_to_uploaded_file=handle_uploaded_file(request.FILES['file']) #its for upload file in data base
            filename=u_name
            ob=Image.objects.get(user_name=request.user)
            path_handwriting=[]
            front_path='/text_to_hand/media/'
            path_handwriting.append(front_path+str(ob.imagefile1))
            path_handwriting.append(front_path+str(ob.imagefile2))
            path_handwriting.append(front_path+str(ob.imagefile3))
            path_handwriting.append(front_path+str(ob.imagefile4))
            path_handwriting.append(front_path+str(ob.imagefile5))
            path_to_read=converter.input.genrate_char(path_handwriting,u_name)
            path_to_pdf=converter.txttohand.convert_to_pdf(path_to_uploaded_file,filename,path_to_read)
            print(path_to_pdf)
            return render(request,"download.html",{'path_to_pdf':path_to_pdf}) 
    else:  
        uploaded_form = Uploadform()  
        return render(request,"data_exist_check.html",{'form':uploaded_form})



def download_file(request):
    fl_path = request.GET['pdf_to_download']
    filename = 'converted.pdf'
    fl = open(fl_path,'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    #default_storage.delete(fl_path)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

@login_required(login_url=("converter:login"))
def check_data_exist(request):
    obj, created = Image.objects.get_or_create(user_name=request.user)
    if len(str(obj.imagefile1))!=0 and len(str(obj.imagefile2))!=0 and len(str(obj.imagefile3))!=0:
        return redirect("converter:user_index")
    else:
        return redirect("converter:train_upload")

@login_required(login_url=("converter:login"))
def train_upload(request):
    if request.method == 'POST':
        print("uploaded file name is")
        obj, created = Image.objects.get_or_create(user_name=request.user)
        if created==False:
            obj.delete()
        name_of_person="temp"
        request.FILES['imagefile1'].name='0_9.jpg'
        request.FILES['imagefile2'].name='a_n.jpg'
        request.FILES['imagefile3'].name='o_z.jpg'
        request.FILES['imagefile4'].name='A_M.jpg'
        request.FILES['imagefile5'].name='N_Z.jpg'
        current_form=ImageForm(request.POST,request.FILES)
        if current_form.is_valid():
            image_data=current_form.save(commit=False)
            image_data.user_name=str(request.user)
            image_data.save()
        img_list=Image.objects.get(user_name=request.user)
        #print(img_list.imagefile1) this return path of images
        return redirect("converter:user_index")
    else:
        current_form=ImageForm()
        context={'form':current_form}
        return render(request,'image.html',context)


        
@login_required(login_url=("converter:login"))
def access_data(request):
    image_data= Image.objects.get(user_name=request.user)
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

