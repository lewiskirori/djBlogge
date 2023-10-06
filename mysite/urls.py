from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import handler404, handler500
from django.contrib.auth import views as auth_views
from django.views.static import serve
from personal.views import (
    home_screen_view,
)
from mysite.views import custom_404, custom_500
from account.views import(
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
)

handler404 = custom_404
handler500 = custom_500
admin.site.site_title = 'djBlogge Mgr.'
admin.site.site_header = 'djBlogge (A) Console'
admin.site.index_title = 'Webcare administration'

urlpatterns = [
    path('', home_screen_view, name="home"),
    path('admin/', admin.site.urls),
    path('account/', account_view, name="account"),
    path('blog/', include('blog.urls', 'blog')),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('register/', registration_view, name="register"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.htm'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.htm'), 
        name='password_change'),

    path('password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.htm',
            email_template_name='registration/password_reset_email.htm',
            subject_template_name='registration/password_reset_subject.htm'
            ), 
            name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.htm'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.htm'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.htm'), name='password_reset_complete'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),    
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]