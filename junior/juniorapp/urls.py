from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
    path('blog/', BlogHome.as_view(), name='blog'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),

]