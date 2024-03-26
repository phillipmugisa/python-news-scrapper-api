from asyncore import read
import queue
from rest_framework import serializers
from . import models


class NewsSourceSerializer(serializers.ModelSerializer, serializers.PrimaryKeyRelatedField):
    class Meta:
        model = models.NewsSource
        fields = ('name',)

    def to_internal_value(self, data):
        print("="*60)
        print("to_internal_value: ", data)
        print("="*60)
        return self.queryset.get(name=data).pk

    def to_representation(self, value):
        print("="*60)
        print("to_representation: ", value)
        print("="*60)
        return str(value)

class NewsSerializer(serializers.ModelSerializer):
    source = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = models.NewsArticle
        fields = '__all__'

    def create(self, validated_data):
        source_id = self.initial_data[0].get('source_id')
        validated_data['source_id'] = source_id

        super().create(validated_data)