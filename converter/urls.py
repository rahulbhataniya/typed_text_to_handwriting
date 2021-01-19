from django.urls import path
from . import views
urlpatterns=[path('',views.index,name='index'),
                path('pdf',views.download_file,name='download_file'),
                path('train_upload',views.train_upload,name='train_upload')]


#name of view use for pah to view in hyperlink ex  {{%url download_file %}}