from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PDFDocument
from django.core.files.uploadedfile import SimpleUploadedFile

class PDFDocumentTests(APITestCase):
    def test_upload_pdf(self):
        url = reverse('pdfdocument-list')
        with open('test.pdf', 'rb') as pdf_file:
            response = self.client.post(url, {'file': pdf_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_query_pdf(self):
        url = reverse('pdfdocument-list')
        with open('test.pdf', 'rb') as pdf_file:
            response = self.client.post(url, {'file': pdf_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        pdf_id = response.data['id']


        query_url = reverse('pdfdocument-query', args=[pdf_id])
        response = self.client.post(query_url, {'query': 'What is the content?'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('answer', response.data)
