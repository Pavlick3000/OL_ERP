# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Reference175(models.Model):
    # field_idrref = models.TextField(db_column='_IDRRef', primary_key=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_version = models.TextField(db_column='_Version')  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    # field_marked = models.TextField(db_column='_Marked')  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    # field_ismetadata = models.TextField(db_column='_IsMetadata')  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    # field_parentidrref = models.TextField(db_column='_ParentIDRRef')  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    # field_folder = models.TextField(db_column='_Folder')  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    # field_code = models.CharField(db_column='_Code', max_length=11, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase. Field renamed because it started with '_'.
    # field_description = models.CharField(db_column='_Description', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld3194 = models.CharField(db_column='_Fld3194', max_length=25, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld3204rref = models.TextField(db_column='_Fld3204RRef')  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3196 = models.TextField(db_column='_Fld3196', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3197 = models.DecimalField(db_column='_Fld3197', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld3198 = models.TextField(db_column='_Fld3198', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3199 = models.TextField(db_column='_Fld3199', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3200 = models.TextField(db_column='_Fld3200', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3201 = models.TextField(db_column='_Fld3201', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3202 = models.TextField(db_column='_Fld3202', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    # field_fld3203rref = models.TextField(db_column='_Fld3203RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3207rref = models.TextField(db_column='_Fld3207RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3205rref = models.TextField(db_column='_Fld3205RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3206rref = models.TextField(db_column='_Fld3206RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3210rref = models.TextField(db_column='_Fld3210RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3208 = models.TextField(db_column='_Fld3208', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3209rref = models.TextField(db_column='_Fld3209RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3211 = models.TextField(db_column='_Fld3211', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld3213 = models.TextField(db_column='_Fld3213', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3212rref = models.TextField(db_column='_Fld3212RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3217rref = models.TextField(db_column='_Fld3217RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3214rref = models.TextField(db_column='_Fld3214RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3215rref = models.TextField(db_column='_Fld3215RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3216rref = models.TextField(db_column='_Fld3216RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3218rref = models.TextField(db_column='_Fld3218RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3219rref = models.TextField(db_column='_Fld3219RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3222rref = models.TextField(db_column='_Fld3222RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3220 = models.TextField(db_column='_Fld3220', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3221 = models.TextField(db_column='_Fld3221', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3232rref = models.TextField(db_column='_Fld3232RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3223 = models.TextField(db_column='_Fld3223', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3224 = models.TextField(db_column='_Fld3224', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3225rref = models.TextField(db_column='_Fld3225RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3226rref = models.TextField(db_column='_Fld3226RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3227rref = models.TextField(db_column='_Fld3227RRef')  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3228rref = models.TextField(db_column='_Fld3228RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3229rref = models.TextField(db_column='_Fld3229RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3230rref = models.TextField(db_column='_Fld3230RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3231 = models.TextField(db_column='_Fld3231', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld3233rref = models.TextField(db_column='_Fld3233RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3240rref = models.TextField(db_column='_Fld3240RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3234 = models.TextField(db_column='_Fld3234', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3235 = models.TextField(db_column='_Fld3235', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3236 = models.TextField(db_column='_Fld3236', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld31409 = models.TextField(db_column='_Fld31409', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3237 = models.DecimalField(db_column='_Fld3237', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld3238rref = models.TextField(db_column='_Fld3238RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld3239 = models.DecimalField(db_column='_Fld3239', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld3195 = models.TextField(db_column='_Fld3195', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld32059 = models.TextField(db_column='_Fld32059', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld32060rref = models.TextField(db_column='_Fld32060RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld32853 = models.TextField(db_column='_Fld32853', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld32966 = models.CharField(db_column='_Fld32966', max_length=13, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld33045rref = models.TextField(db_column='_Fld33045RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld34164 = models.DecimalField(db_column='_Fld34164', max_digits=23, decimal_places=11, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_fld34165rref = models.TextField(db_column='_Fld34165RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld36355 = models.TextField(db_column='_Fld36355', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld37835rref = models.TextField(db_column='_Fld37835RRef', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.
    field_fld37899 = models.TextField(db_column='_Fld37899', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'. This field type is a guess.

    class Meta:
        managed = False
        db_table = '_Reference175'
        unique_together = (('field_parentidrref', 'field_folder', 'field_code', 'field_idrref'), ('field_parentidrref', 'field_folder', 'field_description', 'field_idrref'), ('field_code', 'field_idrref'), ('field_description', 'field_idrref'), ('field_parentidrref', 'field_folder', 'field_fld3194', 'field_idrref'), ('field_fld3194', 'field_idrref'), ('field_parentidrref', 'field_folder', 'field_fld3212rref', 'field_idrref'), ('field_fld3212rref', 'field_idrref'), ('field_parentidrref', 'field_folder', 'field_fld3217rref', 'field_idrref'), ('field_fld3217rref', 'field_idrref'), ('field_parentidrref', 'field_folder', 'field_fld3216rref', 'field_idrref'), ('field_fld3216rref', 'field_idrref'), ('field_parentidrref', 'field_folder', 'field_fld3228rref', 'field_idrref'), ('field_fld3228rref', 'field_idrref'),)
