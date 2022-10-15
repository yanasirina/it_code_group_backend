from rest_framework import serializers

from .models import Tag, Item


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
    class Meta:
        model = Item
        exclude = ('user', )

