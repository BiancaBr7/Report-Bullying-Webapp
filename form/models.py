from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    school_name = models.CharField(max_length=100)
    school_email = models.EmailField()
    category = models.CharField(max_length=100,choices=[('racial', 'Racial Discrimination'), ('sexism', 'Sexism'), ('lgbtq', 'Lgbtq Discrimination'), ('bullying', 'Bullying')])
    language = models.CharField(max_length = 100, choices = [('en', 'English'), ('sp', 'Español'), ('ch_s', '中文简体'), ('ch_t','中文繁體'),('it', 'Italiano'), ('ar', 'عربي'), ('pu', 'ਪੰਜਾਬੀ'), ('fr', 'Français'), ('jp', '日本語'), ('kr', '한국인'), ('ger', 'Deutsch'),('ru', 'Русский'), ('po','Português')], default = 'English')
    message = models.TextField()
    

    def clean(self):
        super().clean()
        email_validator = EmailValidator(message="Please enter a valid email address.")
        email_validator(self.email)
        email_validator(self.school_email)
