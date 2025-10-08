from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Warga
from .serializers import WargaSerializer

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer

class WargaDetailAPIView(RetrieveAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer