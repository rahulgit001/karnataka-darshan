from django.contrib import admin
from .models import TravelEnquiry
from .models import (
    User, SeoKeywords, UpcomingEvents, EventImage,
    TourCategories, TourCategoriesImage, ourlatestblogs, ourlatestblogsImage,
    TravelEnquiry, contactfrom
)
from django_summernote.admin import SummernoteModelAdmin
from django.urls import reverse
from django.utils.html import format_html

    
admin.site.register(User)
admin.site.register(SeoKeywords)
admin.site.register(UpcomingEvents)
admin.site.register(EventImage)
admin.site.register(TourCategories)
admin.site.register(TourCategoriesImage)
@admin.register(ourlatestblogs)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(ourlatestblogsImage)
admin.site.register(TravelEnquiry)
admin.site.register(contactfrom)