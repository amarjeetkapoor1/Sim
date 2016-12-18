from django.contrib import admin
from .models import *

class IndianlegacysectionschannelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indianlegacysectionschannel._meta.get_fields()]

admin.site.register(Indianlegacysectionschannel, IndianlegacysectionschannelAdmin)

class IndianlegacysectionsconversionErrorsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndianlegacysectionsconversionErrors._meta.get_fields()]

admin.site.register(IndianlegacysectionsconversionErrors, IndianlegacysectionsconversionErrorsAdmin)

class IndianlegacysectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indianlegacysectionsdbinfo._meta.get_fields()]

admin.site.register(Indianlegacysectionsdbinfo, IndianlegacysectionsdbinfoAdmin)

class IndianlegacysectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndianlegacysectionsfieldUnits._meta.get_fields()]

admin.site.register(IndianlegacysectionsfieldUnits, IndianlegacysectionsfieldUnitsAdmin)

class IndianlegacysectionsiShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndianlegacysectionsiShape._meta.get_fields()]

admin.site.register(IndianlegacysectionsiShape, IndianlegacysectionsiShapeAdmin)

class IndianlegacysectionsmShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndianlegacysectionsmShape._meta.get_fields()]

admin.site.register(IndianlegacysectionsmShape, IndianlegacysectionsmShapeAdmin)

class IndianlegacysectionspipeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indianlegacysectionspipe._meta.get_fields()]

admin.site.register(Indianlegacysectionspipe, IndianlegacysectionspipeAdmin)

class IndianlegacysectionssShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndianlegacysectionssShape._meta.get_fields()]

admin.site.register(IndianlegacysectionssShape, IndianlegacysectionssShapeAdmin)

class IndianlegacysectionstShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndianlegacysectionstShape._meta.get_fields()]

admin.site.register(IndianlegacysectionstShape, IndianlegacysectionstShapeAdmin)

class IndianlegacysectionstubeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indianlegacysectionstube._meta.get_fields()]

admin.site.register(Indianlegacysectionstube, IndianlegacysectionstubeAdmin)

class IndianlegacysectionswShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndianlegacysectionswShape._meta.get_fields()]

admin.site.register(IndianlegacysectionswShape, IndianlegacysectionswShapeAdmin)

class IndiansectionsangleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indiansectionsangle._meta.get_fields()]

admin.site.register(Indiansectionsangle, IndiansectionsangleAdmin)

class IndiansectionschannelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indiansectionschannel._meta.get_fields()]

admin.site.register(Indiansectionschannel, IndiansectionschannelAdmin)

class IndiansectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indiansectionsdbinfo._meta.get_fields()]

admin.site.register(Indiansectionsdbinfo, IndiansectionsdbinfoAdmin)

class IndiansectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndiansectionsfieldUnits._meta.get_fields()]

admin.site.register(IndiansectionsfieldUnits, IndiansectionsfieldUnitsAdmin)

class IndiansectionsiShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndiansectionsiShape._meta.get_fields()]

admin.site.register(IndiansectionsiShape, IndiansectionsiShapeAdmin)

class IndiansectionsmShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndiansectionsmShape._meta.get_fields()]

admin.site.register(IndiansectionsmShape, IndiansectionsmShapeAdmin)

class IndiansectionspipeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indiansectionspipe._meta.get_fields()]

admin.site.register(Indiansectionspipe, IndiansectionspipeAdmin)

class IndiansectionssShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndiansectionssShape._meta.get_fields()]

admin.site.register(IndiansectionssShape, IndiansectionssShapeAdmin)

class IndiansectionstShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndiansectionstShape._meta.get_fields()]

admin.site.register(IndiansectionstShape, IndiansectionstShapeAdmin)

class IndiansectionstubeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Indiansectionstube._meta.get_fields()]

admin.site.register(Indiansectionstube, IndiansectionstubeAdmin)

class IndiansectionswShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in IndiansectionswShape._meta.get_fields()]

admin.site.register(IndiansectionswShape, IndiansectionswShapeAdmin)

class JindalsectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Jindalsectionsdbinfo._meta.get_fields()]

admin.site.register(Jindalsectionsdbinfo, JindalsectionsdbinfoAdmin)

class JindalsectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionsfieldUnits._meta.get_fields()]

admin.site.register(JindalsectionsfieldUnits, JindalsectionsfieldUnitsAdmin)

class JindalsectionsheShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionsheShape._meta.get_fields()]

admin.site.register(JindalsectionsheShape, JindalsectionsheShapeAdmin)

class JindalsectionsipeShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionsipeShape._meta.get_fields()]

admin.site.register(JindalsectionsipeShape, JindalsectionsipeShapeAdmin)

class JindalsectionsismcShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionsismcShape._meta.get_fields()]

admin.site.register(JindalsectionsismcShape, JindalsectionsismcShapeAdmin)

class JindalsectionsnpbShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionsnpbShape._meta.get_fields()]

admin.site.register(JindalsectionsnpbShape, JindalsectionsnpbShapeAdmin)

class JindalsectionsubShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionsubShape._meta.get_fields()]

admin.site.register(JindalsectionsubShape, JindalsectionsubShapeAdmin)

class JindalsectionsucShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionsucShape._meta.get_fields()]

admin.site.register(JindalsectionsucShape, JindalsectionsucShapeAdmin)

class JindalsectionswpbShapeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JindalsectionswpbShape._meta.get_fields()]

admin.site.register(JindalsectionswpbShape, JindalsectionswpbShapeAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Job._meta.get_fields()]

admin.site.register(Job, JobAdmin)

class JobMaterialAdmin(admin.ModelAdmin):
    list_display = [f.name for f in JobMaterial._meta.get_fields()]

admin.site.register(JobMaterial, JobMaterialAdmin)

class JointAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Joint._meta.get_fields()]

admin.site.register(Joint, JointAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Member._meta.get_fields()]

admin.site.register(Member, MemberAdmin)

class MemberIncidenceAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MemberIncidence._meta.get_fields()]

admin.site.register(MemberIncidence, MemberIncidenceAdmin)

class MemberPropertyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MemberProperty._meta.get_fields()]

admin.site.register(MemberProperty, MemberPropertyAdmin)

class TatastructuressectionschsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tatastructuressectionschs._meta.get_fields()]

admin.site.register(Tatastructuressectionschs, TatastructuressectionschsAdmin)

class TatastructuressectionsdbinfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tatastructuressectionsdbinfo._meta.get_fields()]

admin.site.register(Tatastructuressectionsdbinfo, TatastructuressectionsdbinfoAdmin)

class TatastructuressectionsfieldUnitsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TatastructuressectionsfieldUnits._meta.get_fields()]

admin.site.register(TatastructuressectionsfieldUnits, TatastructuressectionsfieldUnitsAdmin)

class TatastructuressectionsrhsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tatastructuressectionsrhs._meta.get_fields()]

admin.site.register(Tatastructuressectionsrhs, TatastructuressectionsrhsAdmin)

class TatastructuressectionsshsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tatastructuressectionsshs._meta.get_fields()]

admin.site.register(Tatastructuressectionsshs, TatastructuressectionsshsAdmin)
