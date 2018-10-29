from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

class ReadTime(models.Model):
    read_time=models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class ReadTimeExpandMethond():
    def get_read_time(self):
        try:
            ct=ContentType.objects.get_for_model(self)
            readtime=ReadTime.objects.get(content_type=ct,object_id=self.pk)
            return readtime.read_time
        except exceptions.ObjectDoesNotExist:
            return 0

class ReadDetail(models.Model):
    date=models.DateField(default=timezone.now)
    read_time=models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')