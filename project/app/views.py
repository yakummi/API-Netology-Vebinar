from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from .models import Note
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_anonymous:
            qs = qs.filter(is_private=False)
        else:
            qs = qs.filter(Q(is_private=False) | Q(user=self.request.user))
        return qs
