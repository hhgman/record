from rest_framework import serializers, request
from rcapp.models import Recordings, UserInfo
from django.contrib.auth.models import User
from rcapp import views

class UserRecordingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recordings
        fields = (
            'url',
            'datafile'
        )

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = (
            'gender',
            'age'
        )

class InformationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
        )

    class Meta:
        model = UserInfo
        depth = 4
        fields = (
            'owner',
            'gender',
            'age'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    recordings = UserRecordingSerializer(many=True, read_only=True)
    userinfo = UserInfoSerializer(many=True, read_only=True)

    def create(self, validated_data):
        recordings = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='recordings-detail',
        )
        userinfo = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='user-info'
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
            'password',
            'userinfo',
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
            'device',
            'result')
