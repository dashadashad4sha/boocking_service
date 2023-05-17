from users.api.serializers import UserForChatSerializer
from chat.models import Conversation, Message
from halls.api.serializers import HallSerializer
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('conversation_id',)


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = UserForChatSerializer()
    receiver = UserForChatSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'last_message']

    def get_last_message(self, instance):
        message = instance.message_set.first()
        return MessageSerializer(instance=message)


class ConversationSerializer(serializers.ModelSerializer):
    initiator = UserForChatSerializer()
    receiver = UserForChatSerializer()
    hall = HallSerializer()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'hall', 'message_set']
