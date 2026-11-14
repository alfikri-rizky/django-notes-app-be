from rest_framework.reverse import reverse
from rest_framework import serializers

from notes.models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()
    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'tags', 'created_at', 'updated_at', "_links")

    def get__links(self, obj):
        request = self.context.get("request")
        return [
            {
                "rel": "self",
                "href": reverse("note-list", request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse("note-detail", request=request, kwargs={"pk": obj.pk}),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse("note-detail", request=request, kwargs={"pk": obj.pk}),
                "action": "PUT",
                "types": ["application/json"]
            }
        ]