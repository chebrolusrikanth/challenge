from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PDFDocument
from .serializers import PDFDocumentSerializer
from PyPDF2 import PdfReader

class PDFDocumentViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

    @action(detail=True, methods=['post'])
    def query(self, request, pk=None):
        document = self.get_object()
        query = request.data.get('query')

        if not query:
            return Response({'error': 'Query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        
        pdf_reader = PdfReader(document.file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or "" 

        
        if query.lower() in text.lower():
            response_text = f"The query '{query}' was found in the PDF."
        else:
            response_text = f"The query '{query}' was not found in the PDF."

        return Response({'response': response_text})
