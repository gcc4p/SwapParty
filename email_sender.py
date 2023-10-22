from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'swappartyofficial@gmail.com'
email_password = 'qcwu xasw nbjz yomv'
email_receiver = 'gulceapaydinn@gmail.com'

subject = 'You have a match!'
body = """
Congratulations! 

We're thrilled to inform you that your fashion journey just took an exciting turn! Your unique style has found its perfect match on SwapParty, and we're here to guide you through the next steps to ensure a seamless swap experience.

Here's what you need to do:

1. Accept the Swap:
To kick off the swap process, please click on the link below within the next 72 hours to accept the swap:

<a href="https://www.google.com/">click here</a>

2. Wait for Confirmation:
Once you've accepted the swap, your style soulmate will also need to confirm the swap. As soon as they accept, you'll receive an email with all the vital details to coordinate your exchange.

3. Package and Ship Your Box:
To keep things moving smoothly, kindly prepare and ship your carefully curated box within 48 hours of receiving the confirmation email. Be sure to pack your items securely and include any personalised touches you'd like to share with your new style companion.

4. Receive Your Surprise Box:
Anticipation is part of the fun! Once your swap partner ships their box to you, you can eagerly await your own surprise box. When it arrives, unbox and discover the unique pieces waiting to enhance your wardrobe.

We're excited to see how this style swap unfolds, and if you have any questions or need assistance along the way, please don't hesitate to reach out to us at [swappartyofficial@gmail.com]. Our team is here to ensure your swap adventure goes off without a hitch.

Thank you for being a part of the SwapParty community, and we hope this swap enriches your fashion journey in a meaningful way.

Best wishes,

SwapParty Official
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
