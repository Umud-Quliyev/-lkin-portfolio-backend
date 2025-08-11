from rest_framework import generics
from .models import Lab,ContactMessage
from .serializers import LabSerializer,ContactMessageSerializer
from django.core.mail import send_mail

class LabListView(generics.ListAPIView):
	queryset = Lab.objects.all()
	serializer_class = LabSerializer

class LabDetailView(generics.RetrieveAPIView):
	queryset = Lab.objects.all()
	serializer_class = LabSerializer
	lookup_field = 'key'

def some_existing_function():
	pass
from django.shortcuts import render

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        send_mail(
            subject=f"Yeni Əlaqə Mesajı - {instance.name}",
            message=f"""
Ad: {instance.name}
Email: {instance.email}
Mesaj:
{instance.message}
""",
            from_email=None,  
            recipient_list=["umudquliyev.1806@gmail.com"],
            fail_silently=False,
        )