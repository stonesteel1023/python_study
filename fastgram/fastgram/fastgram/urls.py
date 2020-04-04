from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from contents.views import HomeView, RelationView
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect


class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwagrgs):
        if not request.user.is_anonymous:
            return redirect('contents_home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwagrgs)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apis.urls')),
    path('', HomeView.as_view(), name='contents_home'),
    path('login/', NonUserTemplateView.as_view(template_name='login.htm'), name='login'),
    path('register/', NonUserTemplateView.as_view(template_name='register.htm'), name='register'),
    path('relation/', RelationView.as_view(template_name='relation.htm'), name='contents_relation'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)