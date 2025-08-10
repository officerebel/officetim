"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.conf.urls.static import static


def home(_request):
    return JsonResponse(
        {
            "app": "blog_project",
            "status": "ok",
            "endpoints": {
                "posts": "/api/posts/",
                "post_detail": "/api/posts/<id>/",
                "admin": "/admin/",
                "health": "/healthz",
            },
        }
    )

urlpatterns = [
    path('', home, name='home'),
    path('healthz', lambda r: HttpResponse('ok'), name='healthz'),
    path('admin/', admin.site.urls),
    # Mount app under /api/ so endpoints are /api/posts/...
    path('api/', include('posts.urls')),
]

# Serve media in development
if settings.DEBUG or getattr(settings, 'SERVE_MEDIA', False):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
