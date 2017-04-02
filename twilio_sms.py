from twilio.rest import TwilioRestClient

#Provide Account Sid  and Auth Token from twilio Account
account_sid = "AC536753ea1798ce32388fd6dede31a9f0"
auth_token =  "bccb912ab359ca46450e491f4bae728f"
twilio_client = TwilioRestClient (account_sid, auth_token)

message = twilio_client.sms.messages.create(
    body = "Hi Subh, Are you interested for IT job in united states" \
            "? Send your resume to abbyjohn1989@gmail.com",
    to = "+14808685168", #Receives phone number
    from_ = "+12025688424"  )

print (message.sid)
