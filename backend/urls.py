from django.urls import path
from backend import views
from django.conf import settings
from django.conf.urls.static import static
from .views import GenerateBarcode, DisplayBarcode, BarcodeList, ExcelUploadView, ExcelSuccessView

urlpatterns = [
    path('', views.motech, name='home'),
    path('student/', views.StudentAPI.as_view(), name='student-api-list'),
    path('student/<int:pk>/', views.StudentAPI.as_view(), name='student-api-detail'),
    path('student/send-email/', views.send_mail_view, name='send-mail'),
    path('send-email/', views.send_mail_view, name='send-email'),
    path('student/websites/', views.WebsitesAPI.as_view(), name='websites-api-list'),
    path('barcode/generate/', GenerateBarcode.as_view(), name='generate-barcode'),
    path('barcode/display/<int:barcode_id>/', DisplayBarcode.as_view(), name='display-barcode'),
    path('barcode/list/', BarcodeList.as_view(), name='barcode-list'),
    path('upload/', ExcelUploadView.as_view(), name='upload_page'),
    path('success/<int:pk>/', ExcelSuccessView.as_view(), name='success_page'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
