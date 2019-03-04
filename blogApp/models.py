from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# ```username```username, ```blog_title```, and ```blog_entry```

class BlogModel(models.Model):
    userName = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    blogTitle=models.CharField(max_length=200, default="")
    blogEntry = models.TextField(max_length=3000)

    def __str__(self):
        return self.blogTitle