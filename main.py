import os
import functions_framework

import twilio

from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')  # get Twilio account sid from environment variable
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')  # get Twilio auth token from environment variable
TWILIO_NUMBER = '+15005550006'  # This is your test number which will not send SMS
TO_NUMBERS = ['+14125551234']  # any valid cell phone


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def send_sms(cloud_event):
    data = cloud_event.data
    bucket = data['bucket']
    name = data['name']

    event_id = cloud_event['id']
    event_type = cloud_event['type']

    the_body = "Item added to Cloud Storage bucket '" + bucket + "'.\n" + "Item added: " + name + "'.\n" + "Item event id: " + event_id + "Item event type: " + event_type

    client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    print('Sending SMS to: ' + str(TO_NUMBERS))
    print('with body: ' + the_body)
    for TO_NUMBER in TO_NUMBERS:
        rv = client.messages.create(
            to= TO_NUMBER,
            from_= TWILIO_NUMBER,
            body= the_body
        )
