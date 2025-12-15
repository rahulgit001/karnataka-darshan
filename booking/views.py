import json
from accounts.models import TravelEnquiry
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from accounts.models import SeoKeywords


def save_booking_details(body):
    booking = TravelEnquiry(
        from_location = body.get('from_location'),
        to_location = body.get('to_location'),
        destination = body.get('destination'),
        travel_type = body.get('travel_type'),
        transport_required = body.get('transport'),
        adults = body['travelers']['adults'],
        children = body['travelers']['children'],
        rooms = body['travelers']['rooms'],
        fullname = body.get('fullname'),
        email = body.get('email'),
        mobile = body.get('mobile'),
        requirements = body.get('requirements'),
    )
    # Save to DB
    booking.save()
    return True

def fetch_seo_keyword():
    seo = SeoKeywords.objects.filter(Page = "booking_page").first()
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
def booking_page(request):
    seo_title, page, meta_description, header_tag, meta_keyword = fetch_seo_keyword()
    if request.method == "GET": 
        return render(request, 'booking/booking.html', {
        "seo_title": seo_title,
        "page": page,
        "meta_description": meta_description,
        "header_tag":  header_tag,
        "meta_keyword": meta_keyword,
        })
    else:
        body = json.loads(request.body)
        save_booking_details(body)
        return render(request, 'booking/booking.html', {"booking_save_status": "saved",
        "seo_title": seo_title,
        "page": page,
        "meta_description": meta_description,
        "header_tag":  header_tag,
        "meta_keyword": meta_keyword,
        })
