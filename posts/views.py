from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)

from .models import Post, Contact
from .serializers import PostSerializer, ContactSerializer

class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()

    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)


class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    
    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            subject = f"New contact from {instance.name} <{instance.email}>"
            message = instance.subject
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[getattr(settings, 'CONTACT_FORWARD_TO', 'timtvogt@gmail.com')],
                fail_silently=False,
            )
            logger.info(
                "Contact mail attempted via %s from %s to %s",
                settings.EMAIL_BACKEND,
                settings.DEFAULT_FROM_EMAIL,
                getattr(settings, 'CONTACT_FORWARD_TO', 'timtvogt@gmail.com'),
            )
        except Exception:
            # We ignore email errors to not block API
            logger.exception("Contact mail send failed")

