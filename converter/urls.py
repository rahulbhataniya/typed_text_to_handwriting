from django.urls import path
from . import views

app_name = 'converter'

urlpatterns=[path("homepage", views.homepage, name="homepage"),
                path('',views.index,name='index'),
                path('pdf',views.download_file,name='download_file'),
                path('train_upload',views.train_upload,name='train_upload'),
                path('showimage',views.showimage,name='showimage'),
                path('access_data',views.access_data,name='access_data'),
                path("register", views.register, name="register"),
                path("logout", views.logout_request, name="logout"),
                path("login", views.login_request, name="login"),
                path("already_exist", views.check_data_exist, name="check_data_exist"),
                path("user_handwriting", views.user_index, name="user_index"),
                ]

#name of view use for pdf to view in hyperlink ex  {{%url download_file %}}