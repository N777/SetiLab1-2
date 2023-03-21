from django.db import models


# Create your models here.
class Trainer(models.Model):
    full_name = models.CharField(max_length=255)


class TypeBallroomDancing(models.Model):
    title = models.CharField(max_length=255)
    program = models.CharField(max_length=255)


class Team(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(TypeBallroomDancing, on_delete=models.SET_NULL, null=True)
    founding_date = models.DateField()


class Member(models.Model):
    # TODO можно расширить до User
    lastname = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    city = models.CharField(max_length=255)
    level = models.CharField(max_length=255)


class Competition(models.Model):
    title = models.CharField(max_length=255)


class CompetitionProgram(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, null=True)


class Point(models.Model):
    user = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey(CompetitionProgram, on_delete=models.SET_NULL, null=True)
    user_point = models.IntegerField()
