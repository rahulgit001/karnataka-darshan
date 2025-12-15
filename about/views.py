from django.shortcuts import render
from accounts.models import SeoKeywords

def fetch_seo_keyword():
    seo = SeoKeywords.objects.filter(Page = "about_page").first()
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

def about(request):
    seo_title, page, meta_description, header_tag, meta_keyword = fetch_seo_keyword()
    return render(request, 'about/about.html', {
        "page_title" : "karnataka darshan",
        "site_name": "karnataka darshan",
        "seo_title": seo_title,
        "page": page,
        "meta_description": meta_description,
        "header_tag":  header_tag,
        "meta_keyword": meta_keyword
    })
