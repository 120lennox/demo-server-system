from django.db import models
from cms_app.models import Page

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # cms integration 
    cms_page = models.ForeignKey('cms_app.Page', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_cms_content(self):
        if self.cms_page:
            return {
                'title': self.cms_page.title,
                'content': self.cms_page.content
            } 
        return None