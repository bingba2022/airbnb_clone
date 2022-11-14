from django.db import models

# Create your models here.


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    #  We don't want to put this in a db we just want to reuse the code in here
    class Meta:
        # abstract : django will see this model and not put it to the db
        abstract = True
