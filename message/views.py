from rest_framework.views import APIView
from rest_framework.response import Response
from message.email import EmailHandler, Msg
from config import logging


class MessageController(APIView):

    @classmethod
    def post(cls, request):
        msg = Msg(
            request.data['subject'],
            int(request.data['template']['id']),
            request.data['template']['variables'],
            request.data['recipients']
        )
        try:
            EmailHandler.send_msg(msg)
        except Exception as e:
            logging.critical(f'error: {str(e)}, input_data: {request.data}')
            return Response({'success': False})
        return Response({'success': True})

    @classmethod
    def get(cls, requests):
        pass