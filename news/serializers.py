from rest_framework.serializers import ModelSerializer
from .models import Newsletter
from tags.serializers import TagSerializer

class NewsletterSerializer(ModelSerializer):
    tags = TagSerializer(many=True,)
    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'target', 'tags', 'author')


class CreateNewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'target', 'tags', 'author')

class NewsletterNoAdminSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('name', 'description', 'target', 'author')