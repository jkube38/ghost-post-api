# from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer


from ghost2app.models import Posts


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'id',
            'boast_or_roast',
            'text',
            'likes',
            'dislikes',
            'created_time',
            )
