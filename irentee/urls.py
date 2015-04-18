from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'irentee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'irent.home_views.home', name='home'),
    url(r'^login_full', 'irent.login_views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register', 'irent.views.register', name='register'),
    url(r'^show', 'irent.views.show', name='show'),
    url(r'^product_add', 'irent.product_views.product_add', name='product_add'),
    url(r'^product_data_add', 'irent.product_views.product_data_add', name='product_data_add'),
    url(r'^search_result', 'irent.product_views.search_result', name='search_result'),
    url(r'^login_fb', 'irent.views.login_fb', name='login_fb'),
    url(r'', include('social_auth.urls'))
)