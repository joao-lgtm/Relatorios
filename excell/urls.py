from django.urls import path
from .views import ExcelUploadView

urlpatterns = [
    path('upload-excel/', ExcelUploadView.as_view(), name='upload-excel'),
]
