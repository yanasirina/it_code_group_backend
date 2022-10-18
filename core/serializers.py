from rest_framework import serializers

from .models import Tag, Item, User


class TagSerializer(serializers.ModelSerializer):
    display = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = "__all__"

    def get_display(self, obj: Tag):
        return f"{obj.id}: {obj.name}"


class TagSearch(serializers.Serializer):
    name = serializers.CharField(label="Название", required=True)

    def validate_name(self, value):
        if not Tag.objects.filter(name__icontains=value):
            raise serializers.ValidationError(f'Нет меток, содержащих "{value}"')
        return value

    def validate(self, attrs):
        return attrs


class ItemSerializer(serializers.ModelSerializer):
    # tag = TagSerializer(many=True)

    class Meta:
        model = Item
        exclude = ('user', )


class RegisterUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже есть')
        return value


class LoginUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if not user or not user.check_password(attrs['password']):
            raise serializers.ValidationError('Неверное имя пользователя или пароль')
        return attrs


