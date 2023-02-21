import smtplib, ssl
from email.message import EmailMessage
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "home"

@app.route('/send-email', methods=['POST'])
def send_email():
    # get data from request body
    data = request.get_json()
    #email_sender = data['email_sender']
    #email_password = data['email_password']
    email_password="cpzrnpckgsihcgur"
    email_sender ="tamarcom.tech@gmail.com"
    email_receiver = data['email_receiver']
    subject = data['subject']
    link = 'https:www.google.com'
    
    # create email message
    body = (f'''You request for a new password, click on the link to reset your password: {link}. If you did not make this request simply ignore.''')
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    
    # send email using SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
    
    # return success message
    return jsonify({'message': 'Email sent successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
