from django.urls import path
from .views import ExcelUploadSaveView, ExcelDownloadView, ExcelJsonView

urlpatterns = [
    path('upload-excel/', ExcelUploadSaveView.as_view(), name='upload-excel'),
    path('get-excel/', ExcelDownloadView.as_view(), name='get-excel'),
    path('get-excel-json/', ExcelJsonView.as_view(), name='get-excel-json'),
]
