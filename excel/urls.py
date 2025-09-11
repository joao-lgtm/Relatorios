from django.urls import path
from .views import ExcelUploadSaveView

urlpatterns = [
    path('upload-excel/', ExcelUploadSaveView.as_view(), name='upload-excel'),
]
