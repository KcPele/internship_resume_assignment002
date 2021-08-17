from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import mail
from django.conf import settings

# Create your views here.


def index(request):

		return render(request, 'index.html')

def email_contact(request):
	if request.method == 'POST':
		name_email = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message_email = request.POST['message_email']
		message_email2 = 'We recieved a mail from you saying: \n ' + message_email + ' \n We will get back to you shortly' 
		connection = mail.get_connection()
		email1 = mail.EmailMessage(
    			subject,
    		message_email,
    		email,
    		[settings.EMAIL_HOST_USER],
    		connection=connection,
				)
		email1.send()
		email3 = mail.EmailMessage(
    		subject,
    		message_email2,
    		settings.EMAIL_HOST_USER,
    		[email],
				)
		connection.send_messages([email3])
		connection.close()
		messages.info(request, 'Thanks, A response has been sent to your mail')
		return redirect('index')

	else:
		return redirect('index')



def email_subscribe(request):
	
	if request.method == 'POST':
		message_email = 'thank u for subscribing, its an assignment form the internship, and you can join the forum using this link  https://internship.zuri.team'
		subject = 'Assingment'
		subscribe_email = request.POST['email_subscribe']

		send_mail(subject, message_email, settings.EMAIL_HOST_PASSWORD, 
			[subscribe_email], fail_silently=False,)
		messages.info(request, 'Thank you for subscribing, Check your mail or spam box')
		return redirect('/')

	else:
		return redirect('index')