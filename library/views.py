from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from library.filters import TaleFilter
from library.permissions import IsOwnerOrReadOnly
from library.serializers import TaleSerializer
from library.models import Tale


class TaleViewSet(ModelViewSet):
    queryset = Tale.objects.order_by('-pk')
    serializer_class = TaleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaleFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
