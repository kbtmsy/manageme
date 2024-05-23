# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountFollowHistory(models.Model):
    instagram_id = models.CharField(primary_key=True, max_length=50)  # The composite primary key (instagram_id, follow_id) found, that is not supported. The first column is selected.
    follow_id = models.CharField(max_length=50)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    update_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_follow_history'
        unique_together = (('instagram_id', 'follow_id'),)


class AccountPool(models.Model):
    follow_id = models.CharField(primary_key=True, max_length=50)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    update_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_pool'


class DeviceMaster(models.Model):
    device_id = models.BigIntegerField(primary_key=True)
    instagram_id = models.CharField(max_length=50, blank=True, null=True)
    preparation_flg = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    max_follow_count = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    update_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_master'


class FileRequest(models.Model):
    request_id = models.CharField(primary_key=True, max_length=12)  # The composite primary key (request_id, device_id) found, that is not supported. The first column is selected.
    device_id = models.BigIntegerField()
    file_name = models.CharField(max_length=20, blank=True, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    update_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_request'
        unique_together = (('request_id', 'device_id'),)


class ParentAccount(models.Model):
    parent_id = models.CharField(primary_key=True, max_length=50)
    collection_date = models.DateField(blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    update_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent_account'
