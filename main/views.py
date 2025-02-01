from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, ArticleSeries

# Create your views here.
def homepage(request):
    matching_series = ArticleSeries.objects.all()
    
    return render(
        request=request,
        template_name='sayfalar/index.html',
        context={"objects": matching_series}
        )
