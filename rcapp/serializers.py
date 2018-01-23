from rest_framework import serializers, request
from rcapp.models import Recordings
from django.contrib.auth.models import User

class UserRecordingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recordings
        fields = (
            'url',
            'datafile'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    recordings = UserRecordingSerializer(many=True, read_only=True)

    def create(self, validated_data):
        recordings = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='recordings-detail',
        )
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance

    class Meta:
        model=User
        fields=(
            'username',
            'url',
            'pk',
            'email',
            'password',
            'recordings')

class RecordingSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
        )

    class Meta:
        model = Recordings
        depth = 4
        fields = (
            'url',
            'owner',
            'created',
            'datafile',
            'result')
