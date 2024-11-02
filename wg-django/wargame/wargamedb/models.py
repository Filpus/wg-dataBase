# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accessestonations(models.Model):
    fk_nations = models.ForeignKey('Nations', models.DO_NOTHING, db_column='fk_nations')
    fk_users = models.ForeignKey('Users', models.DO_NOTHING, db_column='fk_users')
    dateacquired = models.DateField(blank=True, null=True)
    isactive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'accessestonations'


class Accessestounits(models.Model):
    fk_nations = models.ForeignKey('Nations', models.DO_NOTHING, db_column='fk_nations')
    fk_unittypes = models.ForeignKey('Unittypes', models.DO_NOTHING, db_column='fk_unittypes')

    class Meta:
        managed = False
        db_table = 'accessestounits'
        unique_together = (('fk_nations', 'fk_unittypes'),)


class Actions(models.Model):
    fk_nations = models.ForeignKey('Nations', models.DO_NOTHING, db_column='fk_nations')
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=25000)
    result = models.CharField(max_length=25000, blank=True, null=True)
    issettled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'actions'


class Armies(models.Model):
    name = models.CharField(max_length=255)
    fk_nations = models.ForeignKey('Nations', models.DO_NOTHING, db_column='fk_nations')
    fk_locations = models.ForeignKey('Locations', models.DO_NOTHING, db_column='fk_locations')

    class Meta:
        managed = False
        db_table = 'armies'


class Cultures(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'cultures'


class Events(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Grantedpermissions(models.Model):
    fk_users = models.ForeignKey('Users', models.DO_NOTHING, db_column='fk_users')
    fk_permissions = models.ForeignKey('Permissions', models.DO_NOTHING, db_column='fk_permissions')

    class Meta:
        managed = False
        db_table = 'grantedpermissions'
        unique_together = (('fk_users', 'fk_permissions'),)


class Locationresources(models.Model):
    fk_locations = models.ForeignKey('Locations', models.DO_NOTHING, db_column='fk_locations')
    fk_resources = models.ForeignKey('Resources', models.DO_NOTHING, db_column='fk_resources')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'locationresources'
        unique_together = (('fk_locations', 'fk_resources'),)


class Locations(models.Model):
    name = models.CharField(unique=True, max_length=255)
    size = models.IntegerField()
    fortifications = models.IntegerField()
    fk_nations = models.ForeignKey('Nations', models.DO_NOTHING, db_column='fk_nations')

    class Meta:
        managed = False
        db_table = 'locations'


class Maintenancecosts(models.Model):
    fk_unittypes = models.ForeignKey('Unittypes', models.DO_NOTHING, db_column='fk_unittypes')
    fk_resources = models.ForeignKey('Resources', models.DO_NOTHING, db_column='fk_resources')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maintenancecosts'
        unique_together = (('fk_unittypes', 'fk_resources'),)


class Modifiers(models.Model):
    fk_events = models.ForeignKey(Events, models.DO_NOTHING, db_column='fk_events')
    target = models.TextField()  # This field type is a guess.
    fk_resources = models.ForeignKey('Resources', models.DO_NOTHING, db_column='fk_resources', blank=True, null=True)
    fk_socialgroups = models.ForeignKey('Socialgroups', models.DO_NOTHING, db_column='fk_socialgroups', blank=True, null=True)
    fk_cultures = models.ForeignKey(Cultures, models.DO_NOTHING, db_column='fk_cultures', blank=True, null=True)
    fk_religions = models.ForeignKey('Religions', models.DO_NOTHING, db_column='fk_religions', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modifiers'


class Nations(models.Model):
    name = models.CharField(unique=True, max_length=255)
    fk_cultures = models.ForeignKey(Cultures, models.DO_NOTHING, db_column='fk_cultures')
    fk_religions = models.ForeignKey('Religions', models.DO_NOTHING, db_column='fk_religions')

    class Meta:
        managed = False
        db_table = 'nations'


class Offeredresources(models.Model):
    fk_resources = models.ForeignKey('Resources', models.DO_NOTHING, db_column='fk_resources')
    fk_tradeagreements = models.ForeignKey('Tradeagreements', models.DO_NOTHING, db_column='fk_tradeagreements')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'offeredresources'


class Ownedresources(models.Model):
    fk_nations = models.ForeignKey(Nations, models.DO_NOTHING, db_column='fk_nations')
    fk_resources = models.ForeignKey('Resources', models.DO_NOTHING, db_column='fk_resources')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ownedresources'
        unique_together = (('fk_nations', 'fk_resources'),)


class Permissions(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'permissions'


class Populations(models.Model):
    fk_socialgroups = models.ForeignKey('Socialgroups', models.DO_NOTHING, db_column='fk_socialgroups')
    fk_cultures = models.ForeignKey(Cultures, models.DO_NOTHING, db_column='fk_cultures')
    fk_religions = models.ForeignKey('Religions', models.DO_NOTHING, db_column='fk_religions')
    fk_locations = models.ForeignKey(Locations, models.DO_NOTHING, db_column='fk_locations')
    happiness = models.FloatField()

    class Meta:
        managed = False
        db_table = 'populations'


class Productioncosts(models.Model):
    fk_unittypes = models.ForeignKey('Unittypes', models.DO_NOTHING, db_column='fk_unittypes')
    fk_resources = models.ForeignKey('Resources', models.DO_NOTHING, db_column='fk_resources')
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productioncosts'
        unique_together = (('fk_unittypes', 'fk_resources'),)


class Productionshares(models.Model):
    fk_socialgroups = models.ForeignKey('Socialgroups', models.DO_NOTHING, db_column='fk_socialgroups')
    fk_resources = models.ForeignKey('Resources', models.DO_NOTHING, db_column='fk_resources')
    coefficient = models.FloatField()

    class Meta:
        managed = False
        db_table = 'productionshares'
        unique_together = (('fk_socialgroups', 'fk_resources'),)


class Relatedevents(models.Model):
    fk_nations = models.ForeignKey(Nations, models.DO_NOTHING, db_column='fk_nations')
    fk_events = models.ForeignKey(Events, models.DO_NOTHING, db_column='fk_events')

    class Meta:
        managed = False
        db_table = 'relatedevents'
        unique_together = (('fk_nations', 'fk_events'),)


class Religions(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'religions'


class Resources(models.Model):
    name = models.CharField(unique=True, max_length=255)
    ismain = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'resources'


class Socialgroups(models.Model):
    name = models.CharField(unique=True, max_length=255)
    basehappiness = models.FloatField()
    volunteers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'socialgroups'


class Tradeagreements(models.Model):
    fk_nationoffering = models.ForeignKey(Nations, models.DO_NOTHING, db_column='fk_nationoffering')
    fk_nationreceiving = models.ForeignKey(Nations, models.DO_NOTHING, db_column='fk_nationreceiving', related_name='tradeagreements_fk_nationreceiving_set')
    isaccepted = models.BooleanField()
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tradeagreements'


class Troops(models.Model):
    quantity = models.IntegerField()
    fk_armies = models.ForeignKey(Armies, models.DO_NOTHING, db_column='fk_armies')
    fk_unittypes = models.ForeignKey('Unittypes', models.DO_NOTHING, db_column='fk_unittypes')

    class Meta:
        managed = False
        db_table = 'troops'


class Unitorders(models.Model):
    fk_nations = models.ForeignKey(Nations, models.DO_NOTHING, db_column='fk_nations')
    fk_unittypes = models.ForeignKey('Unittypes', models.DO_NOTHING, db_column='fk_unittypes')
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unitorders'
        unique_together = (('fk_nations', 'fk_unittypes'),)


class Unittypes(models.Model):
    name = models.CharField(unique=True, max_length=255)
    melee = models.IntegerField()
    range = models.IntegerField()
    speed = models.IntegerField()
    morale = models.IntegerField()
    defense = models.IntegerField()
    volunteersneeded = models.IntegerField()
    isnaval = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'unittypes'


class Usedresources(models.Model):
    fk_socialgroups = models.ForeignKey(Socialgroups, models.DO_NOTHING, db_column='fk_socialgroups')
    fk_resources = models.ForeignKey(Resources, models.DO_NOTHING, db_column='fk_resources')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usedresources'
        unique_together = (('fk_socialgroups', 'fk_resources'),)


class Users(models.Model):
    name = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    isarchived = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users'


class Wantedresources(models.Model):
    fk_resources = models.ForeignKey(Resources, models.DO_NOTHING, db_column='fk_resources')
    fk_tradeagreements = models.ForeignKey(Tradeagreements, models.DO_NOTHING, db_column='fk_tradeagreements')
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wantedresources'
