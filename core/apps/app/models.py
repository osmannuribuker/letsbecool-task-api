from django.db import models
from django.utils import timezone
from django.conf import settings

class Base(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        verbose_name='Oluşturan Kullanıcı',
        related_name="%(app_label)s_%(class)s_related_created",
        related_query_name="%(app_label)s_%(class)ssc",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        verbose_name='Güncelleyen Kullanıcı',
        related_name="%(app_label)s_%(class)s_related_updated",
        related_query_name="%(app_label)s_%(class)ssp",
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Oluşturulma Tarihi')
    updated_date = models.DateTimeField(verbose_name='Güncellenme Tarihi', blank=True, null=True)

    class Meta:
        abstract = True

class Todo(Base):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "{} - {}".format(str(self.id), self.title)
    
    def what_is_task(self):
        return 'Task is "{}"'.format(self.title)