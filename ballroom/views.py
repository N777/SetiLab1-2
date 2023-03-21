# Create your views here.
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets

from ballroom.serializers import TrainerSerializer, TypeBallroomDancingSerializer, TeamSerializer, MemberSerializer, \
    CompetitionSerializer, CompetitionProgramSerializer, PointSerializer
from ballroom.models import Trainer, TypeBallroomDancing, Team, Member, Competition, CompetitionProgram, Point


class TrainerViewSet(viewsets.ModelViewSet):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend, SearchFilter]
    filterset_fields = ['full_name']
    search_fields = ['full_name']
    ordering_fields = '__all__'


class TypeBallroomDancingViewSet(viewsets.ModelViewSet):
    serializer_class = TypeBallroomDancingSerializer
    queryset = TypeBallroomDancing.objects.all()


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class CompetitionViewSet(viewsets.ModelViewSet):
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()


class CompetitionProgramViewSet(viewsets.ModelViewSet):
    serializer_class = CompetitionProgramSerializer
    queryset = CompetitionProgram.objects.all()


class PointViewSet(viewsets.ModelViewSet):
    serializer_class = PointSerializer
    queryset = Point.objects.all()
