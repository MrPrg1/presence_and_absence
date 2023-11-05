from django.urls import path
from .views import TeacherView, AllTeacherView


urlpatterns = [
    path('teacher/<str:nationalCode>', TeacherView.as_view()), # دیدن فقط یک کارکن مد نظر
    path('allteacher/', AllTeacherView.as_view()), # دیدن لیست تمامی کارکنان
]