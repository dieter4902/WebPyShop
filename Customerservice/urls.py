from django.urls import path
from django.views.generic import TemplateView
from . import views
from Product import views as productviews

urlpatterns = [
    path('delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('edit/<int:pk>/', views.CommentEditView.as_view(), name='comment-edit'),
    path('editdelete/<int:pk>/', views.comment_edit_delete, name='comment-edit-delete'),
    path('unflag/<int:pk>/', productviews.comment_flag_remove, name='comment-flag-remove'),
    path('portal/', TemplateView.as_view(template_name='portal.html'), name='portal'),
]
