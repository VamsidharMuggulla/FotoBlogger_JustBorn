from django.conf.urls import url, include, patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.forms import AuthenticationForm
# from views import myPosts, postit, profile, show, update, register, publish, allPosts,home
from views import profile, register, home, login_user, publish, allposts, likeit, myPosts, edit
from forms import LoginForm

app_name = "CodeSample"
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}, name='logout'),
    # url(r'^postit/$', postit, name='posting'),
    # url(r'^update/(?P<id>[0-9]+)/$', update, name='update'),
    # url(r'^show/(?P<id>[0-9]+)/$', show, name='show'),
    url(r'^accounts/profile/$', profile, name='profile'),
    # url(r'^login/$', 'django.contrib.auth.views.login'),  # If user is not login it will redirect to login page
    url(r'^login/$', login_user,
        name='login'),
    url(r'^register/$', register, name='registeration'),
    url(r'^publish/$', publish, name='publish'),
    url(r'^allposts/$', allposts, name='allposts'),
    url(r'^likeit/$', likeit, name='likeit'),
    url(r'^myposts/$', myPosts, name='myposts'),
    url(r'^edit/$', edit, name='edit'),
]

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))
