# from rest_framework import serializers
# from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = Post
#         # fields = ['user', 'title', 'content', 'created_at', 'updated_at']
#         fields = '__all__'


from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user','created_at', 'updated_at']
        

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(user=user, **validated_data)
        return post
