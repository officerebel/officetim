from rest_framework import serializers
from .models import Post, Contact, Tag


class PostSerializer(serializers.ModelSerializer):
    # Read: expose tags as a list of strings
    tags = serializers.SerializerMethodField()
    # Read: absolute URL to the image for frontend consumption
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
    # Keep 'image' for write (uploads) and add computed 'image_url' for reads
    fields = ('id', 'created_at', 'title', 'body', 'image', 'image_url', 'tags')

    def get_tags(self, instance):
        try:
            return [t.name for t in instance.tags.all()]
        except Exception:
            # If relation is temporarily unavailable (e.g., migrations race), fail soft
            return []

    def _get_or_create_tags(self, tag_names):
        tags = []
        for raw in tag_names or []:
            name = raw.strip()
            if not name:
                continue
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        return tags

    def get_image_url(self, instance):
        try:
            if not instance.image:
                return None
            request = self.context.get('request')
            url = instance.image.url
            # When request context is available, build absolute URL
            if request is not None:
                return request.build_absolute_uri(url)
            # Fallback: return relative URL
            return url
        except Exception:
            return None

    def create(self, validated_data):
        # Accept tags from incoming payload (list or comma-separated string)
        raw = self.initial_data.get('tags', [])
        if isinstance(raw, str):
            tag_names = [s.strip() for s in raw.split(',') if s.strip()]
        else:
            tag_names = list(raw or [])
        post = super().create(validated_data)
        post.tags.set(self._get_or_create_tags(tag_names))
        return post

    def update(self, instance, validated_data):
        # Accept tags as above; if not provided, leave unchanged
        tag_names = self.initial_data.get('tags', None)
        if isinstance(tag_names, str):
            tag_names = [s.strip() for s in tag_names.split(',') if s.strip()]
        instance = super().update(instance, validated_data)
        if tag_names is not None:
            instance.tags.set(self._get_or_create_tags(tag_names))
        return instance


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("id", "name", "email", "subject", "created_at")

