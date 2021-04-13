# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Players(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    teams = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teams_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'players'


class PlayersHasReplay(models.Model):
    players = models.OneToOneField(Players, models.DO_NOTHING, db_column='players_ID', primary_key=True)  # Field name made lowercase.
    replay = models.ForeignKey('Replay', models.DO_NOTHING, db_column='replay_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'players_has_replay'
        unique_together = (('players', 'replay'),)


class Replay(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(db_column='SCORE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'replay'


class ReplayHasTeams(models.Model):
    replay = models.OneToOneField(Replay, models.DO_NOTHING, db_column='replay_ID', primary_key=True)  # Field name made lowercase.
    teams = models.ForeignKey('Teams', models.DO_NOTHING, db_column='teams_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'replay_has_teams'
        unique_together = (('replay', 'teams'),)


class Teams(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teams'
