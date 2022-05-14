from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
# Create your views here.

from emails.models import Email
from emails.serializers import EmailSerializer


class EmailModelViewSet(ModelViewSet):
    filter_backends = (SearchFilter,)
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
