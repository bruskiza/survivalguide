from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class TalkListDetailView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('A talk list')
