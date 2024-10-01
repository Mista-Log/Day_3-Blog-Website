from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('single-post/<str:pk>', views.single_post, name='single-post')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
