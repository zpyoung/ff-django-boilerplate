from django.conf import settings
from django.conf.urls import include, url{%- if cookiecutter.include_cms == 'yes' %}
from django.conf.urls.i18n import i18n_patterns
{%- endif %}
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView


admin.autodiscover()

urlpatterns = {% if cookiecutter.include_cms == 'yes' %}i18n_patterns({% else %}[{% endif %}
    url(r'^api/', include('{{cookiecutter.repo_name}}.api_urls')),
    url(r'^{{cookiecutter.django_admin_path}}/', include(admin.site.urls)),
    {%- if cookiecutter.include_cms == 'yes' %}
    url(r'^filer/', include('filer.urls')),
    # CMS urls should be handled last to avoid possible conflicts
    url(r'^cms/', include('cms.urls')),
    {%- endif %}
{% if cookiecutter.include_cms == 'yes' %}){% else %}]{% endif %}

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    handler500 = '{{cookiecutter.repo_name}}.views.server_error'
    handler404 = '{{cookiecutter.repo_name}}.views.page_not_found'

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass


urlpatterns += [
    url(r'^$', RedirectView.as_view(url=settings.SITE_URL, permanent=False), name='index')
]
