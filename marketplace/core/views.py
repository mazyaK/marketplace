from django.shortcuts import render, get_object_or_404

from .models import App


def app_list_view(request):
    template_name = 'core/app_list.html'
    app_list = App.objects.all()

    return render(request, template_name, context={'app_list': app_list})


def app_detail_view(request, slug):
    template_name = 'core/app_detail.html'
    app = get_object_or_404(App, slug=slug)

    return render(request, template_name, context={'app': app})
