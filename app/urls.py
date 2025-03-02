from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.home,name='home'),
  path('about/',views.about,name='about'),
  path('do/',views.do,name='do'),
  path('portfolio/',views.portfolio,name='portfolio'),
  path('contact/',views.contact,name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

