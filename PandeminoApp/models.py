from django.db import models



class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    slug = models.SlugField(blank = True, unique = True)

    def __str__(self):
        return self.title