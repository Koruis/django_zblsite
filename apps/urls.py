
"""定义apps的URL模式"""

from django.conf.urls import url

from . import views
from django.urls import path



urlpatterns = [
    #主页
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]