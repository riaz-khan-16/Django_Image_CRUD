from django.urls import path
from crud_app import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crud_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('persons', views.crud_list),
    path('persons/<int:id>', views.crud_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)



