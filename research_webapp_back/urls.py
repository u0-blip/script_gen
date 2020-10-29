"""research_webapp_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from music.views import music_file, show_image, longtask, download_mean, download_field
from research_webapp_back.create_plot import plot, struct_editor, patchPath
from music.celery_task import taskstatus


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('music/', csrf_exempt(music_file)),
    path('music/<str:id>', csrf_exempt(music_file)),
    path('sim_image_data/<type_img>', csrf_exempt(show_image)),
    path('longtask', csrf_exempt(longtask)),
    path('download_mean', csrf_exempt(download_mean)),
    path('download_field', csrf_exempt(download_field)),
    path('status/<task_id>', csrf_exempt(taskstatus)),
    path('plot/', csrf_exempt(plot)),
    path('patchPath/', csrf_exempt(patchPath)),
    path('editor/', csrf_exempt(struct_editor)),
]
