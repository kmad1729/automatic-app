from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

#import hello.views
import scoresheet_app.views

# Examples:
# url(r'^$', 'automatic_app.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    #url(r'^$', hello.views.index, name='index'),
    #url(r'^db', hello.views.db, name='db'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', scoresheet_app.views.home, name='home'),
]
