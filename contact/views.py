import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from accounts.models import SeoKeywords



def save_contact_details(body):
    return


def fetch_seo_keyword():
    seo = SeoKeywords.objects.filter(Page = "contact_page").first()
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


@csrf_exempt
def contact_page(request):
    seo_title, page, meta_description, header_tag, meta_keyword = fetch_seo_keyword()
    if request.method == "GET": 
        return render(request, 'contact/contact.html',{
        "seo_title": seo_title,
        "page": page,
        "meta_description": meta_description,
        "header_tag":  header_tag,
        "meta_keyword": meta_keyword,
        })
    else:
        body = json.loads(request.body)
        # print(body)
        save_contact_details(body)
        return render(request, 'contact/contact.html', {"contact_send_status": "saved",
        "seo_title": seo_title,
        "page": page,
        "meta_description": meta_description,
        "header_tag":  header_tag,
        "meta_keyword": meta_keyword,
        })
