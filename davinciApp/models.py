from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=300)
    blogIdea = models.CharField(null=True, blank=True, max_length=200)
    keywords = models.CharField(null=True, blank=True, max_length=300)
    audience = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        app_label = 'davinciApp'  
        db_table = 'blog'  
