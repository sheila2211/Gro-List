from django.db import models

list_type=[
    ('food', 'FOOD'),
    ('drink', 'DRINK'),
    ('snacks', 'SNACKS'),
    ('cleaning supplies', 'CLEANING SUPPLIES'),
    ('others', 'OTHERS')
    ] 

class Post(models.Model):

    text = models.CharField(max_length=100, blank=False, null=False)
    post_type = models.CharField(max_length=50, choices=list_type, default='others')
    neccessity = models.BooleanField(default=False)

    def __str__(self):
        return self.text