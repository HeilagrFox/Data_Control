from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name='home'),
    path('faculty', views.get_entrants_by_faculty,name='faculty'),
    path('marks', views.marks,name='marks'),
    path('classrooms',views.classrooms,name='classrooms'),
    path('faculty/<int:pk>', views.get_certificate.as_view(), name='get_certificate'),
    path('report', views.get_report, name='report')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)