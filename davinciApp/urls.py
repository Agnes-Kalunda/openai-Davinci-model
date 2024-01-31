from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blogTopic, name='home'),  
    path('generate-blog-topic/', views.blogTopic, name='blog-topic'),
    path('generate-blog-sections/', views.blogSections, name='blog-sections'),
    path('save-blog-topic/<str:blogTopic>/', views.saveBlogTopic, name='save-blog-topic'),
    path('use-blog-topic/<str:blogTopic>/', views.useBlogTopic, name='use-blog-topic'),
    # path('view-generated-blog/<slug:slug>/', views.viewGeneratedBlog, name='view-generated-blog'),
    path('generated-blog/', views.generatedBlog, name='generated-blog')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
