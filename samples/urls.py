from django.urls import path

from samples import views


urlpatterns = [
    path('samples', views.SampleListCreate.as_view()),
    path('samples/<pk>', views.SampleDetailsUpdateDelete.as_view()),
    path('excel/samples', views.SampleExcel.as_view()),
    path('statistics/samples', views.SampleStatistics.as_view()),
]
