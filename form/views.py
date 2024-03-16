from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import Form
from django.core.mail import send_mail
from django.conf import settings
import translators as ts

class FormView(FormView):
    template_name = 'form/form_form.html'
    form_class = Form
    success_url = reverse_lazy('form')

    def form_valid(self, form):
        # Create a "success" message
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for filling in the form!'
        )

        #sending email
        school_email = form.cleaned_data.get("school_email")
        name = form.cleaned_data.get("name")
        category = form.cleaned_data.get("category")
        message = form.cleaned_data.get("message")
        language = form.cleaned_data.get("language")
        message = ts.translate_text(message)
        school_name = form.cleaned_data.get("school_name")
        email = form.cleaned_data.get("email")
        cat_dict = {'racial':'Racial Discrimination', 'sexism': 'Sexism', 'lgbtq':'LGBTQ', 'bullying':'Bullying'}
        full_message = f"\nDear {school_name}, \n\nThis is the PTERYX Foundation, a registered Canadian nonprofit organization established in 2020, dedicated to fostering the well-being of newcomer and minority youth. We have recently received a submission from {name} indicating that there is a category occurring within your school. As a third-party organization, we hope the school will thoroughly investigate the situation to help protect the rights of the students. Please see the attached details for more information.\n\nStudent Name: {name}\nStudent Email: {email}\nCategory: {cat_dict[category]}\nDescription of Situation: {message}\n\nSincerely,\n\nPTERYX Foundation"

        send_mail(
            subject = "Bullying Report",
            message = full_message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [school_email, email],
            auth_password = settings.EMAIL_HOST_PASSWORD,
        )

        # Continue with default behaviour
        return super().form_valid(form)


    