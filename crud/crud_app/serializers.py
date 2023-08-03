from rest_framework import serializers
from crud_app.models import Intro


class CrudSerializer(serializers.Serializer):
            id=serializers.IntegerField()
            name = serializers.CharField(max_length=100)
            hometown=serializers.CharField(max_length=100)
            present_address=serializers.CharField(max_length=100)
            occupation=serializers.CharField(max_length=100)
            height=serializers.CharField(max_length=100)
            color=serializers.CharField(max_length=100)

            def create(self, validated_data):
                return Intro.objects.create(**validated_data)

                

            def update(self, instance, validated_data):
                instance.id = validated_data.get('id', instance.id)
                instance.name = validated_data.get('name', instance.name)
                instance.hometown=validated_data.get('hometown', instance.hometown)
                instance.present_address=validated_data.get('present_address', instance.present_address)
                instance.occupation=validated_data.get('occupation', instance.occupation)
                instance.height=validated_data.get('height', instance.height)
                instance.color=validated_data.get('color', instance.color)
                instance.save()
                return instance
