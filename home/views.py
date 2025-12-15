from django.shortcuts import render
from accounts.models import EventImage, UpcomingEvents, TourCategories, ourlatestblogs, SeoKeywords


def fetch_upcoming_events():
    events = UpcomingEvents.objects.prefetch_related('images').all()
    return events


def fetch_tour_categories():
    tour = TourCategories.objects.prefetch_related('images').all()
    return tour

def fetch_our_latest_blogs():
    blogs = ourlatestblogs.objects.prefetch_related('images').all()
    return blogs

def fetch_seo_keyword():
    seo = SeoKeywords.objects.filter(Page = "home_page").first()
    if seo:
        seo_title = seo.Meta_Title
        page = seo.Page
        meta_description = seo.Meta_Discription
        header_tag = seo.Header_Tag
        meta_keyword = seo.Meta_Keywords
    else:
        seo_title = ""
        page = ""
        meta_description = ""
        header_tag = ""
        meta_keyword = ""
        
    return seo_title, page, meta_description, header_tag, meta_keyword

def home_page(request):
    events = fetch_upcoming_events()
    tours = fetch_tour_categories()
    blogs = fetch_our_latest_blogs()
    seo_title, page, meta_description, header_tag, meta_keyword = fetch_seo_keyword()
    return render(request, 'home/home.html', {
        "page_title" : "karnataka darshan",
        "site_name": "karnataka darshan",
        "events": events,
        "tours": tours,
        "blogs": blogs,
        "seo_title": seo_title,
        "page": page,
        "meta_description": meta_description,
        "header_tag":  header_tag,
        "meta_keyword": meta_keyword,
        
    })
