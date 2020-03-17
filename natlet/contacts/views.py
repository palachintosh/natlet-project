import requests

from django.shortcuts import render
from django.shortcuts import redirect, reverse
from .forms import ContactForm
from django.views import View
from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
# Create your views here.

class Contacts(View):
    form_model = ContactForm

    def get(self, request):
        contact_form = self.form_model
        return render(request, 'contacts/contacts.html', locals())
    
    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            #captcha validation
            recaptcha_response = request.POST['g-recaptcha-response']
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response,
            }

            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            print(result)
            #captcha validation
            if result['success']:
                print('success! ')
                data = bound_form.cleaned_data
                html_mess = loader.render_to_string(
                    'contacts/html_message.html',
                    context={
                        'message': data['message'],
                        'from_user': data['email'],
                    })
                print(html_mess)
                
                if data['subject'] and data['message']:
                    try:
                        send_mail(data['subject'], data['message'], 'blog@palachintosh.com', ['parser9000@gmail.com'], html_message=html_mess)
                    except BadHeaderError:
                        messages.error(request, 'Invalid operation!')
                messages.success(request, 'Done')
            else:
                print('error code here! ')
                messages.error(request, 'Invalid capthca. Try again')
        print('else here! ')
        return redirect(reverse("contact_p_url"))


    