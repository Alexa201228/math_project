"""trueSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.sitemaps.views import sitemap
from mathpage.sitemaps import MathSitemap
from metodics.sitemaps import MetodSitemap
from School.sitemaps import SchoolSitemap
from blog.sitemaps import PostSitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import homepage.views

sitemaps1 = {
    'mathpage': MathSitemap,
}

sitemaps2 = {
    'metodics': MetodSitemap,
}

sitemaps3 = {
    'School': SchoolSitemap,
}

sitemaps4 = {
    'blog': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage.views.Home, name='Home'),
    path('math/', include('mathpage.urls'), name='math'),
    path('homework/', include('homework.urls')),
    path('School/', include('School.urls'), name='school'),
    path('metodics/', include('metodics.urls')),
    path('students/', include('students_works.urls')),
    path('blog/', include('blog.urls')),
    path('math/sitemap.xml', sitemap, {'sitemaps': sitemaps1},
    name='django.contrib.sitemaps.views.sitemap'),
    path('metodics/sitemap.xml', sitemap, {'sitemaps': sitemaps2},
    name='django.contrib.sitemaps.views.sitemap'),
    path('School/sitemap.xml', sitemap, {'sitemaps': sitemaps3},
    name='django.contrib.sitemaps.views.sitemap'),
    path('blog/sitemap.xml', sitemap, {'sitemaps': sitemaps4},
    name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
