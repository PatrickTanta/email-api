from rest_framework import serializers

from emails.models import Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'fromm', 'subject', 'body', 'sentAt', 'archived', 'read')
