from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.views.generic import View


class FeedBackView(View):
    def post(self, request):
        print('heeeere')
        form = FeedBackForm(request.POST)
        print('usfhisdcmsdc')
        print(form.is_bound)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/wrong_field')

# Create your views here.
def post(request):
    print('heeeere')
    form = FeedBackForm(request.POST)
    if form.is_valid():
        print(form)
        form.save()
        return redirect('/')
    else:
        return redirect('/wrong_field')