from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def whatsapp_webhook(request):
    if request.method != "POST":
        return HttpResponse("Only POST allowed", status=405)

    incoming_message = request.POST.get("Body", "").strip()

    response = MessagingResponse()
    reply = response.message()
    reply.body(f"I sent this msg: {incoming_message}")

    return HttpResponse(str(response), content_type="text/xml")
