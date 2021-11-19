from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags,format_html
from django.template.loader import render_to_string
from django.shortcuts import render
from django.conf import settings
from django.views import View
from .forms import EmailForm
class SendEmailView(View):
    def get(self,request,*args, **kwargs):
        return render(request,"index.html",{"form":EmailForm()})
    def post(self,request,*args, **kwargs):
        form = EmailForm(request.POST)    
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            html_content = form.cleaned_data['html_content']
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                # subject
                subject,
                # body of email
                text_content,
                # from email
                settings.EMAIL_HOST_USER,
                # to email list
                [to_email]
            )
            email.attach_alternative(html_content,'text/html')
            email.send()
            return render(request,"index.html",{"form":EmailForm()})
        return render(request,"index.html",{"form":form})
