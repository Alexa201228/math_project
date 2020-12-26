from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from trueSite.settings import ALLOWED_HOSTS

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                        self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique_for_date='publish')

    body = models.TextField()
    image = models.FileField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices = STATUS_CHOICES,
                                default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                                self.publish.month,
                                self.publish.day,
                                self.slug])

    def get_full_url(self):
        domain = ALLOWED_HOSTS[1]
        return 'https://{domain}{path}'.format(domain=domain,path=self.get_absolute_url())

    def little_part_of_post(self):
        return " ".join(self.body.split()[:20]) + "..."
        
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

class PostImages(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.post.title

class SocialShares(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    share_source = models.URLField()

    def name_cap(self):
        return str(self.name).title()
    
    def link_name(self):
        return str(self.name).lower()

