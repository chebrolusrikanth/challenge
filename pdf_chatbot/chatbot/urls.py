from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDFDocumentViewSet

router = DefaultRouter()
router.register(r'pdfs', PDFDocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
