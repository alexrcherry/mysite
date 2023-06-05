from django.urls import path

from . import views

app_name = 'solids'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:sensor_id>/", views.detail, name="detail"),
    path("<int:sensor_id>/measure/", views.measure, name="measure"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]