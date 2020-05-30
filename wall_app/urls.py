from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('success/<int:user_Val>', views.successDisplay),
    path('success/create', views.create_user),
    path('login/display', views.validate_login),
    path('logoutUser', views.logout),
    path('notlogin', views.index),
    path('success/update/message', views.give_me_messages),
    path('success/update/comment/<int:val>', views.give_me_comments),
    path('message/delete/<int:got_Val>/', views.deleteMessage),
    path('comment/delete/<int:this_val>/', views.deleteComment),

]