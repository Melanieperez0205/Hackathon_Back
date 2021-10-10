from authAppExample.models.post import Article
from rest_framework             import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Article
        fields = ['idpost', 'title','content','created_date','article_image','slug']