# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Indianlegacysectionsangle(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    rz = models.FloatField(db_column='Rz', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsAngle'


class Indianlegacysectionschannel(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.
    r2 = models.FloatField(db_column='R2', blank=True, null=True)  # Field name made lowercase.
    rivet_dia = models.FloatField(db_column='Rivet Dia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g = models.FloatField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    g1 = models.IntegerField(db_column='G1', blank=True, null=True)  # Field name made lowercase.
    h1 = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'IndianLegacySectionsChannel'


class IndianlegacysectionsconversionErrors(models.Model):
    object_type = models.CharField(db_column='Object Type', max_length=510, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    object_name = models.CharField(db_column='Object Name', max_length=510, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    error_description = models.TextField(db_column='Error Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'IndianLegacySectionsConversion Errors'


class Indianlegacysectionsdbinfo(models.Model):
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countryadj = models.CharField(db_column='CountryAdj', max_length=100, blank=True, null=True)  # Field name made lowercase.
    materialtype = models.CharField(db_column='MaterialType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsDBInfo'


class IndianlegacysectionsfieldUnits(models.Model):
    tablename = models.CharField(db_column='TableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field0 = models.CharField(db_column='Field0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field6 = models.CharField(db_column='Field6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field7 = models.CharField(db_column='Field7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field8 = models.CharField(db_column='Field8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field9 = models.CharField(db_column='Field9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field10 = models.CharField(db_column='Field10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field11 = models.CharField(db_column='Field11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field12 = models.CharField(db_column='Field12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field13 = models.CharField(db_column='Field13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field15 = models.CharField(db_column='Field15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field16 = models.CharField(db_column='Field16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field17 = models.CharField(db_column='Field17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field18 = models.CharField(db_column='Field18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field19 = models.CharField(db_column='Field19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field20 = models.CharField(db_column='Field20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field21 = models.CharField(db_column='Field21', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsField Units'


class IndianlegacysectionsiShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsI Shape'


class IndianlegacysectionsmShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsM Shape'


class Indianlegacysectionspipe(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    od = models.FloatField(db_column='OD', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    i = models.FloatField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    z = models.FloatField(db_column='Z', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsPipe'


class IndianlegacysectionssShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.
    r2 = models.FloatField(db_column='R2', blank=True, null=True)  # Field name made lowercase.
    rivet_dia1 = models.FloatField(db_column='Rivet Dia1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rivet_dia2 = models.FloatField(db_column='Rivet Dia2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g1 = models.FloatField(db_column='G1', blank=True, null=True)  # Field name made lowercase.
    g2 = models.FloatField(db_column='G2', blank=True, null=True)  # Field name made lowercase.
    g3 = models.IntegerField(db_column='G3', blank=True, null=True)  # Field name made lowercase.
    h1 = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'IndianLegacySectionsS Shape'


class IndianlegacysectionstShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsT Shape'


class Indianlegacysectionstube(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsTube'


class IndianlegacysectionswShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianLegacySectionsW Shape'


class Indiansectionsangle(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    rz = models.FloatField(db_column='Rz', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsAngle'


class Indiansectionschannel(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.
    r2 = models.FloatField(db_column='R2', blank=True, null=True)  # Field name made lowercase.
    rivet_dia = models.FloatField(db_column='Rivet Dia', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g = models.FloatField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    g1 = models.IntegerField(db_column='G1', blank=True, null=True)  # Field name made lowercase.
    h1 = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'IndianSectionsChannel'


class Indiansectionsdbinfo(models.Model):
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countryadj = models.CharField(db_column='CountryAdj', max_length=100, blank=True, null=True)  # Field name made lowercase.
    materialtype = models.CharField(db_column='MaterialType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=510, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsDBInfo'


class IndiansectionsfieldUnits(models.Model):
    tablename = models.CharField(db_column='TableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field0 = models.CharField(db_column='Field0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field6 = models.CharField(db_column='Field6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field7 = models.CharField(db_column='Field7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field8 = models.CharField(db_column='Field8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field9 = models.CharField(db_column='Field9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field10 = models.CharField(db_column='Field10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field11 = models.CharField(db_column='Field11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field12 = models.CharField(db_column='Field12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field13 = models.CharField(db_column='Field13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field15 = models.CharField(db_column='Field15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field16 = models.CharField(db_column='Field16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field17 = models.CharField(db_column='Field17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field18 = models.CharField(db_column='Field18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field19 = models.CharField(db_column='Field19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field20 = models.CharField(db_column='Field20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field21 = models.CharField(db_column='Field21', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsField Units'


class IndiansectionsiShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsI Shape'


class IndiansectionsmShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsM Shape'


class Indiansectionspipe(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    od = models.FloatField(db_column='OD', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    i = models.FloatField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    z = models.FloatField(db_column='Z', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsPipe'


class IndiansectionssShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.
    r2 = models.FloatField(db_column='R2', blank=True, null=True)  # Field name made lowercase.
    rivet_dia1 = models.FloatField(db_column='Rivet Dia1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rivet_dia2 = models.FloatField(db_column='Rivet Dia2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g1 = models.FloatField(db_column='G1', blank=True, null=True)  # Field name made lowercase.
    g2 = models.FloatField(db_column='G2', blank=True, null=True)  # Field name made lowercase.
    g3 = models.IntegerField(db_column='G3', blank=True, null=True)  # Field name made lowercase.
    h1 = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'IndianSectionsS Shape'


class IndiansectionstShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsT Shape'


class Indiansectionstube(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsTube'


class IndiansectionswShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'IndianSectionsW Shape'


class Jindalsectionsdbinfo(models.Model):
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countryadj = models.CharField(db_column='CountryAdj', max_length=100, blank=True, null=True)  # Field name made lowercase.
    materialtype = models.CharField(db_column='MaterialType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsDBInfo'


class JindalsectionsfieldUnits(models.Model):
    tablename = models.CharField(db_column='TableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field0 = models.CharField(db_column='Field0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field6 = models.CharField(db_column='Field6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field7 = models.CharField(db_column='Field7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field8 = models.CharField(db_column='Field8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field9 = models.CharField(db_column='Field9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field10 = models.CharField(db_column='Field10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field11 = models.CharField(db_column='Field11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field12 = models.CharField(db_column='Field12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field13 = models.CharField(db_column='Field13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field15 = models.CharField(db_column='Field15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field16 = models.CharField(db_column='Field16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field17 = models.CharField(db_column='Field17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field18 = models.CharField(db_column='Field18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field19 = models.CharField(db_column='Field19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field20 = models.CharField(db_column='Field20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field21 = models.CharField(db_column='Field21', max_length=510, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsField Units'


class JindalsectionsheShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsHE Shape'


class JindalsectionsipeShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsIPE Shape'


class JindalsectionsismcShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.
    r2 = models.FloatField(db_column='R2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsISMC Shape'


class JindalsectionsnpbShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsNPB Shape'


class JindalsectionsubShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsUB Shape'


class JindalsectionsucShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsUC Shape'


class JindalsectionswpbShape(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    bf = models.FloatField(db_column='Bf', blank=True, null=True)  # Field name made lowercase.
    tf = models.FloatField(db_column='Tf', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='Iz', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    ct = models.FloatField(db_column='Ct', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    r1 = models.FloatField(db_column='R1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'JindalSectionsWPB Shape'


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    idd = models.CharField(max_length=24, blank=True, null=True)
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
        
        db_table = 'Job'


class JobMaterial(models.Model):
    job_id = models.IntegerField(primary_key=True)
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
        
        db_table = 'Job_material'


class Joint(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    job_id = models.IntegerField()
    idd = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField(blank=True, null=True)
    support = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'Joint'
        unique_together = (('job_id', 'idd'),)


class Member(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    job_id = models.IntegerField()
    member_id = models.IntegerField()
    member_property = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'Member'
        unique_together = (('job_id', 'member_id'),)


class MemberIncidence(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    job_id = models.IntegerField()
    member_id = models.IntegerField()
    joint_id = models.IntegerField()

    class Meta:
        
        db_table = 'Member_incidence'
        unique_together = (('job_id', 'member_id', 'joint_id'),)


class MemberProperty(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    job_id = models.IntegerField()
    idd = models.IntegerField()
    type = models.CharField(max_length=24)
    yd = models.FloatField(db_column='YD', blank=True, null=True)  # Field name made lowercase.
    zd = models.FloatField(db_column='ZD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Member_property'
        unique_together = (('job_id', 'idd'),)


class Tatastructuressectionschs(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    od = models.FloatField(db_column='OD', blank=True, null=True)  # Field name made lowercase.
    tw = models.FloatField(db_column='Tw', blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    i = models.FloatField(db_column='I', blank=True, null=True)  # Field name made lowercase.
    z = models.FloatField(db_column='Z', blank=True, null=True)  # Field name made lowercase.
    c = models.FloatField(db_column='C', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TataStructuresSectionsCHS'


class Tatastructuressectionsdbinfo(models.Model):
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countryadj = models.CharField(db_column='CountryAdj', max_length=100, blank=True, null=True)  # Field name made lowercase.
    materialtype = models.CharField(db_column='MaterialType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TataStructuresSectionsDBInfo'


class TatastructuressectionsfieldUnits(models.Model):
    tablename = models.CharField(db_column='TableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field0 = models.CharField(db_column='Field0', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field6 = models.CharField(db_column='Field6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field7 = models.CharField(db_column='Field7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field8 = models.CharField(db_column='Field8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field9 = models.CharField(db_column='Field9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field10 = models.CharField(db_column='Field10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field11 = models.CharField(db_column='Field11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field12 = models.CharField(db_column='Field12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field13 = models.CharField(db_column='Field13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field15 = models.CharField(db_column='Field15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field16 = models.CharField(db_column='Field16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field17 = models.CharField(db_column='Field17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field18 = models.CharField(db_column='Field18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field19 = models.CharField(db_column='Field19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    field20 = models.CharField(db_column='Field20', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TataStructuresSectionsField Units'


class Tatastructuressectionsrhs(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='IZ', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    c = models.FloatField(db_column='C', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TataStructuresSectionsRHS'


class Tatastructuressectionsshs(models.Model):
    recno = models.IntegerField(db_column='RECNO', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=510, blank=True, null=True)  # Field name made lowercase.
    staadname = models.CharField(db_column='StaadName', max_length=510, blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    d = models.FloatField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    b = models.FloatField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    iz = models.FloatField(db_column='IZ', blank=True, null=True)  # Field name made lowercase.
    iy = models.FloatField(db_column='Iy', blank=True, null=True)  # Field name made lowercase.
    ix = models.FloatField(db_column='Ix', blank=True, null=True)  # Field name made lowercase.
    zx = models.FloatField(db_column='Zx', blank=True, null=True)  # Field name made lowercase.
    zy = models.FloatField(db_column='Zy', blank=True, null=True)  # Field name made lowercase.
    c = models.FloatField(db_column='C', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'TataStructuresSectionsSHS'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        
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
        
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        
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
        
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        
        db_table = 'django_session'
