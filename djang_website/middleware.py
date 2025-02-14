from django.contrib import messages
from django.utils import timezone
from etkinlikler.models import etkinlik_bildirimi

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.track_page_visit(request)
        return response

    def track_page_visit(self, request):
        client_ip = self.get_client_ip(request)
        bildirim = etkinlik_bildirimi.objects.last()
        # Set a session variable with the notification message
        request.session['notification_message'] = bildirim.bildirim_mesaji
        request.session['notification_id'] = bildirim.id
        print(f"Bildirim gönderildi: {bildirim.bildirim_mesaji}")

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
