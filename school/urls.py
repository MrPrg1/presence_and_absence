from django.urls import path, include
from .views import AllPresenceAndAbsenceView, PresenceAndAbsenceView, AllScoreView, StudentView, AllStudentView, AllClassView, ClassView
# from .views import StudentView

urlpatterns = [
    path('student/<str:nationalCode>', StudentView.as_view()), #ایجاد ، تغییر ، حذف و مشاهده یک هنرجوی مد نظر
    path('allstudent/', AllStudentView.as_view()),  # فقط مشاهده تمامی هنرجو ها
    path('allclass/', AllClassView.as_view()), #ایجاد ، تغییر ، حذف و مشاهده یک کلاس مد نظر
    path('class/<str:name>', ClassView.as_view()),   # فقط مشاهده تمامی کلاس ها 
    path('allpresenceandabsence/', AllPresenceAndAbsenceView.as_view()),
    path('presenceandabsence/<str:date>', PresenceAndAbsenceView.as_view()),
    path('score/', AllScoreView.as_view()),

    # path('student/', StudentView.as_view()),
]
