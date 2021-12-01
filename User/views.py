from django.http import HttpResponse

# Create your views here.


def user_detail(request):
    return HttpResponse('working')