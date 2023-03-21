from rest_framework import serializers

from ballroom.models import Trainer, TypeBallroomDancing, Team, Member, Competition, CompetitionProgram, Point


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('__all__')


class TypeBallroomDancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeBallroomDancing
        fields = ('__all__')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('__all__')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('__all__')


class CompetitionProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionProgram
        fields = ('__all__')


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('__all__')
