from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify


class App(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(max_length=200, unique=True, blank=True, populate_from='name')
    description = models.CharField(max_length=10000)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(App, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name





