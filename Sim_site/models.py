# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=24, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    date = models.CharField(max_length=10, blank=True, null=True)
    client = models.CharField(max_length=24, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    checker_name = models.CharField(max_length=24, blank=True, null=True)
    engineer_name = models.CharField(max_length=24, blank=True, null=True)
    approved_name = models.CharField(max_length=24, blank=True, null=True)
    checker_date = models.CharField(max_length=10, blank=True, null=True)
    ref = models.CharField(max_length=24, blank=True, null=True)
    part = models.CharField(max_length=24, blank=True, null=True)
    rev = models.CharField(max_length=24, blank=True, null=True)
    approved_date = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Job'


class JobMaterial(models.Model):
    job = models.ForeignKey(Job, models.DO_NOTHING)
    name = models.CharField(max_length=24)
    e = models.FloatField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    poisson = models.FloatField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    damp = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    g = models.FloatField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    strength = models.CharField(max_length=24, blank=True, null=True)
    type = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Job_material'
        unique_together = (('name', 'job'),)


class Joint(models.Model):
    job = models.ForeignKey(Job, models.DO_NOTHING)
    id = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField(blank=True, null=True)
    support = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Joint'
        unique_together = (('id', 'job'),)


class Member(models.Model):
    job = models.ForeignKey(Job, models.DO_NOTHING)
    member_id = models.IntegerField()
    member_property = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Member'
        unique_together = (('member_id', 'job'),)


class MemberIncidence(models.Model):
    job = models.ForeignKey(Joint, models.DO_NOTHING)
    member = models.ForeignKey(Member, models.DO_NOTHING)
    joint = models.ForeignKey(Joint, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Member_incidence'
        unique_together = (('job', 'member', 'joint'),)


class MemberProperty(models.Model):
    job = models.ForeignKey(Job, models.DO_NOTHING)
    id = models.IntegerField()
    type = models.CharField(max_length=24)
    yd = models.FloatField(db_column='YD', blank=True, null=True)  # Field name made lowercase.
    zd = models.FloatField(db_column='ZD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Member_property'
        unique_together = (('id', 'job'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
