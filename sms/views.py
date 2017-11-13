# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import QueryDict
from django.http import JsonResponse
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from models import PreRegisterPhone

class PreRegisterPhones(APIView):

    def get(self, request):
        return JsonResponse({ 'data': []})

    def post(self, request):
        pass

    def put(self, request):
        phone_text = request.data.get('phone')
        phone = PreRegisterPhone(phone_text=phone_text)
        phone.save()
        return JsonResponse({ 'data': []})
