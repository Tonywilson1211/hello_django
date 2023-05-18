from django.db import models

# Create your models here.


class Item(models.Model):
    # null = prevents items from being created without a name progmmatically
    # blank = makes the field required on forms
    # default = false by default (todo items)
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
