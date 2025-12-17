from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models
from slugify import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField  


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class SeoKeywords(models.Model):
    Page = models.CharField(max_length=255, null=True, blank=True)
    Meta_Keywords = models.TextField(null=True, blank=True)
    Header_Tag = models.CharField(max_length=255, null=True, blank=True)
    Meta_Title = models.TextField(null=True, blank=True)
    Meta_Discription = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.Page}   -     {self.Meta_Title}    -     {self.Meta_Discription}"
    
    
class UpcomingEvents(models.Model):
    event_title = models.TextField()
    event_description = models.TextField()
    event_rate = models.FloatField()
    event_duration = models.IntegerField() 
    def __str__(self):
        return self.event_title   
   
    
class EventImage(models.Model):
    event = models.ForeignKey(UpcomingEvents, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="event_images/")
    def __str__(self):
        return f"Image for {self.event.event_title}"
    
    
class TourCategories(models.Model):
    tour_title = models.TextField()
    number_of_event = models.IntegerField() 
    def __str__(self):
        return self.tour_title   


class TourCategoriesImage(models.Model):
    event = models.ForeignKey(TourCategories, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="tour_images/")
    def __str__(self):
        return f"Image for {self.event.tour_title}"
    
    
class ourlatestblogs(models.Model):
    blogs_title = models.CharField(max_length=255)                        
    seo_url = models.CharField(max_length=255)                               
    short_description = models.TextField()                                
    content = RichTextUploadingField()
    meta_title = models.CharField(max_length=255, blank=True, null=True)  
    keywords = models.CharField(max_length=255, blank=True, null=True)    
    meta_description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=150, default="xyz")
    meta_keywords = models.CharField(max_length=250, default="xyz")
    category = models.CharField(max_length=250, default="xyz")  
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft") 
    featured = models.BooleanField(default=False)  
    excerpt = models.TextField(null=True, blank=True)
    order_number = models.PositiveIntegerField(default=0)  
    
    # --- Author Info ---
    author_name = models.CharField(max_length=255, default="xyz")
    author_bio = models.TextField(null=True, blank=True)  
    
    # --- Blog Statistics ---
    view_count = models.PositiveIntegerField(default=0)
    reading_time = models.PositiveIntegerField(default=0) 
    
    # --- Timestamps ---
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.blogs_title
    
    
class ourlatestblogsImage(models.Model):
    blog = models.ForeignKey(ourlatestblogs, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="blog_images/") 
    def __str__(self):
        return f"Image for {self.blog.blogs_title}"
    

class TravelEnquiry(models.Model):
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=100)
    travel_type = models.CharField(max_length=50)
    transport_required = models.CharField(max_length=50)
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    rooms = models.PositiveIntegerField(default=1)
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    requirements = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.destination} - {self.from_location} - {self.to_location}"
    
class contactfrom(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=150)
    
    
    def __str__(self):
        return f"{self.name}"