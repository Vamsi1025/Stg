from django.conf import settings

def business_info(request):
    return {
        'BUSINESS_NAME': settings.BUSINESS_NAME,
        'BUSINESS_TAGLINE': settings.BUSINESS_TAGLINE,
        'BUSINESS_PHONE': settings.BUSINESS_PHONE,
        'WHATSAPP_NUMBER': settings.WHATSAPP_NUMBER,
        'BUSINESS_ADDRESS': settings.BUSINESS_ADDRESS,
        'GOOGLE_MAPS_EMBED': settings.GOOGLE_MAPS_EMBED,
    }
