from django.contrib import admin
from .models import *

class IndianlegacysectionschannelAdmin(admin.ModelAdmin):
    list_display = Indianlegacysectionschannel._meta.get_all_field_names()

admin.site.register(Indianlegacysectionschannel, IndianlegacysectionschannelAdmin)

class IndianlegacysectionsconversionErrorsAdmin(admin.ModelAdmin):
    list_display = IndianlegacysectionsconversionErrors._meta.get_all_field_names()

admin.site.register(IndianlegacysectionsconversionErrors, IndianlegacysectionsconversionErrorsAdmin)

class IndianlegacysectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = Indianlegacysectionsdbinfo._meta.get_all_field_names()

admin.site.register(Indianlegacysectionsdbinfo, IndianlegacysectionsdbinfoAdmin)

class IndianlegacysectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = IndianlegacysectionsfieldUnits._meta.get_all_field_names()

admin.site.register(IndianlegacysectionsfieldUnits, IndianlegacysectionsfieldUnitsAdmin)

class IndianlegacysectionsiShapeAdmin(admin.ModelAdmin):
    list_display = IndianlegacysectionsiShape._meta.get_all_field_names()

admin.site.register(IndianlegacysectionsiShape, IndianlegacysectionsiShapeAdmin)

class IndianlegacysectionsmShapeAdmin(admin.ModelAdmin):
    list_display = IndianlegacysectionsmShape._meta.get_all_field_names()

admin.site.register(IndianlegacysectionsmShape, IndianlegacysectionsmShapeAdmin)

class IndianlegacysectionspipeAdmin(admin.ModelAdmin):
    list_display = Indianlegacysectionspipe._meta.get_all_field_names()

admin.site.register(Indianlegacysectionspipe, IndianlegacysectionspipeAdmin)

class IndianlegacysectionssShapeAdmin(admin.ModelAdmin):
    list_display = IndianlegacysectionssShape._meta.get_all_field_names()

admin.site.register(IndianlegacysectionssShape, IndianlegacysectionssShapeAdmin)

class IndianlegacysectionstShapeAdmin(admin.ModelAdmin):
    list_display = IndianlegacysectionstShape._meta.get_all_field_names()

admin.site.register(IndianlegacysectionstShape, IndianlegacysectionstShapeAdmin)

class IndianlegacysectionstubeAdmin(admin.ModelAdmin):
    list_display = Indianlegacysectionstube._meta.get_all_field_names()

admin.site.register(Indianlegacysectionstube, IndianlegacysectionstubeAdmin)

class IndianlegacysectionswShapeAdmin(admin.ModelAdmin):
    list_display = IndianlegacysectionswShape._meta.get_all_field_names()

admin.site.register(IndianlegacysectionswShape, IndianlegacysectionswShapeAdmin)

class IndiansectionsangleAdmin(admin.ModelAdmin):
    list_display = Indiansectionsangle._meta.get_all_field_names()

admin.site.register(Indiansectionsangle, IndiansectionsangleAdmin)

class IndiansectionschannelAdmin(admin.ModelAdmin):
    list_display = Indiansectionschannel._meta.get_all_field_names()

admin.site.register(Indiansectionschannel, IndiansectionschannelAdmin)

class IndiansectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = Indiansectionsdbinfo._meta.get_all_field_names()

admin.site.register(Indiansectionsdbinfo, IndiansectionsdbinfoAdmin)

class IndiansectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = IndiansectionsfieldUnits._meta.get_all_field_names()

admin.site.register(IndiansectionsfieldUnits, IndiansectionsfieldUnitsAdmin)

class IndiansectionsiShapeAdmin(admin.ModelAdmin):
    list_display = IndiansectionsiShape._meta.get_all_field_names()

admin.site.register(IndiansectionsiShape, IndiansectionsiShapeAdmin)

class IndiansectionsmShapeAdmin(admin.ModelAdmin):
    list_display = IndiansectionsmShape._meta.get_all_field_names()

admin.site.register(IndiansectionsmShape, IndiansectionsmShapeAdmin)

class IndiansectionspipeAdmin(admin.ModelAdmin):
    list_display = Indiansectionspipe._meta.get_all_field_names()

admin.site.register(Indiansectionspipe, IndiansectionspipeAdmin)

class IndiansectionssShapeAdmin(admin.ModelAdmin):
    list_display = IndiansectionssShape._meta.get_all_field_names()

admin.site.register(IndiansectionssShape, IndiansectionssShapeAdmin)

class IndiansectionstShapeAdmin(admin.ModelAdmin):
    list_display = IndiansectionstShape._meta.get_all_field_names()

admin.site.register(IndiansectionstShape, IndiansectionstShapeAdmin)

class IndiansectionstubeAdmin(admin.ModelAdmin):
    list_display = Indiansectionstube._meta.get_all_field_names()

admin.site.register(Indiansectionstube, IndiansectionstubeAdmin)

class IndiansectionswShapeAdmin(admin.ModelAdmin):
    list_display = IndiansectionswShape._meta.get_all_field_names()

admin.site.register(IndiansectionswShape, IndiansectionswShapeAdmin)

class JindalsectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = Jindalsectionsdbinfo._meta.get_all_field_names()

admin.site.register(Jindalsectionsdbinfo, JindalsectionsdbinfoAdmin)

class JindalsectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = JindalsectionsfieldUnits._meta.get_all_field_names()

admin.site.register(JindalsectionsfieldUnits, JindalsectionsfieldUnitsAdmin)

class JindalsectionsheShapeAdmin(admin.ModelAdmin):
    list_display = JindalsectionsheShape._meta.get_all_field_names()

admin.site.register(JindalsectionsheShape, JindalsectionsheShapeAdmin)

class JindalsectionsipeShapeAdmin(admin.ModelAdmin):
    list_display = JindalsectionsipeShape._meta.get_all_field_names()

admin.site.register(JindalsectionsipeShape, JindalsectionsipeShapeAdmin)

class JindalsectionsismcShapeAdmin(admin.ModelAdmin):
    list_display = JindalsectionsismcShape._meta.get_all_field_names()

admin.site.register(JindalsectionsismcShape, JindalsectionsismcShapeAdmin)

class JindalsectionsnpbShapeAdmin(admin.ModelAdmin):
    list_display = JindalsectionsnpbShape._meta.get_all_field_names()

admin.site.register(JindalsectionsnpbShape, JindalsectionsnpbShapeAdmin)

class JindalsectionsubShapeAdmin(admin.ModelAdmin):
    list_display = JindalsectionsubShape._meta.get_all_field_names()

admin.site.register(JindalsectionsubShape, JindalsectionsubShapeAdmin)

class JindalsectionsucShapeAdmin(admin.ModelAdmin):
    list_display = JindalsectionsucShape._meta.get_all_field_names()

admin.site.register(JindalsectionsucShape, JindalsectionsucShapeAdmin)

class JindalsectionswpbShapeAdmin(admin.ModelAdmin):
    list_display = JindalsectionswpbShape._meta.get_all_field_names()

admin.site.register(JindalsectionswpbShape, JindalsectionswpbShapeAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = Job._meta.get_all_field_names()

admin.site.register(Job, JobAdmin)

class JobMaterialAdmin(admin.ModelAdmin):
    list_display = JobMaterial._meta.get_all_field_names()

admin.site.register(JobMaterial, JobMaterialAdmin)

class JointAdmin(admin.ModelAdmin):
    list_display = Joint._meta.get_all_field_names()

admin.site.register(Joint, JointAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = Member._meta.get_all_field_names()

admin.site.register(Member, MemberAdmin)

class MemberIncidenceAdmin(admin.ModelAdmin):
    list_display = MemberIncidence._meta.get_all_field_names()

admin.site.register(MemberIncidence, MemberIncidenceAdmin)

class MemberPropertyAdmin(admin.ModelAdmin):
    list_display = MemberProperty._meta.get_all_field_names()

admin.site.register(MemberProperty, MemberPropertyAdmin)

class TatastructuressectionschsAdmin(admin.ModelAdmin):
    list_display = Tatastructuressectionschs._meta.get_all_field_names()

admin.site.register(Tatastructuressectionschs, TatastructuressectionschsAdmin)

class TatastructuressectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = Tatastructuressectionsdbinfo._meta.get_all_field_names()

admin.site.register(Tatastructuressectionsdbinfo, TatastructuressectionsdbinfoAdmin)

class TatastructuressectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = TatastructuressectionsfieldUnits._meta.get_all_field_names()

admin.site.register(TatastructuressectionsfieldUnits, TatastructuressectionsfieldUnitsAdmin)

class TatastructuressectionsrhsAdmin(admin.ModelAdmin):
    list_display = Tatastructuressectionsrhs._meta.get_all_field_names()

admin.site.register(Tatastructuressectionsrhs, TatastructuressectionsrhsAdmin)

class TatastructuressectionsshsAdmin(admin.ModelAdmin):
    list_display = Tatastructuressectionsshs._meta.get_all_field_names()

admin.site.register(Tatastructuressectionsshs, TatastructuressectionsshsAdmin)
