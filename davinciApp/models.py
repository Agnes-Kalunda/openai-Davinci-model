from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=300)
    blogIdea = models.CharField(null=True, blank=True, max_length=200)
    keywords = models.CharField(null=True, blank=True, max_length=300)
    audience = models.CharField(null=True, blank=True, max_length=100)
    # wordCount = models.CharField(null=True, blank=True, max_length=300)

    # # utility variables
    # uniqueId = models.CharField(null=True, blank=True, max_length=100)
    # slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return '{} {}'.format(self.title, self.uniqueId)

    # def save(self, *args, **kwargs):
    #     if self.date_created is None:
    #         self.date_created = timezone.localtime(timezone.now())
    #     if self.uniqueId is None:
    #         self.uniqueId = str(uuid4()).split('-')[4]

    #     self.slug = slugify('{}{}'.format(self.title, self.uniqueId))
    #     self.last_updated = timezone.localtime(timezone.now())
    #     super(Blog, self).save(*args, **kwargs)




class BlogSection(models.Model):
    title = models.CharField( max_length=300)
    body = models.TextField(null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

        #utility variable

    # uniqueId = models.CharField(null=True, blank=True, max_length=100)
    # slug= models.SlugField(max_length=500, unique=True, blank=True, null=True)
    # date_created=models.DateTimeField(blank=True, null=True)
    # last_updated= models.DateTimeField(blank=True, null=True)


    # def __str__(self):
    #     return '{} {}'.format(self.title, self.uniqueId)
    
    
    # def save(self, *args, **kwargs):
    #     if self.date_created is None:
    #         self.date_created = timezone.localtime(timezone.now())
    #     if self.uniqueId is None:
    #         self.uniqueId = str(uuid4()).split('-')[4]



    #     self.slug = slugify('{}{}'.format(self.title, self.uniqueId))
    #     self.last_updated = timezone.localtime(timezone.now())
    #     super(BlogSection, self).save(*args, **kwargs)