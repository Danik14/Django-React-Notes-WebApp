from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        # fiels = ['body', 'time'...] => another method
        fields = "__all__"
