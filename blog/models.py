from django.db import models
from accounts.models import CustomUser

CATEGORIES = [
    ('Mental Health', 'Mental Health'),
    ('Heart Disease', 'Heart Disease'),
    ('Covid19', 'Covid19'),
    ('Immunization', 'Immunization'),
]

class BlogPost(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
