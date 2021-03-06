from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from PIL import Image

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = self.cleaned_data.get('password1')
        password1 = self.cleaned_data.get('password2')
        if password != password1:
            raise ValidationError({'password1': ['The passwords did not match']})

        else:
            if password:
                if len(password) < 8:
                    raise ValidationError({'password1': ['Passwords must be of more than 8 characters']})

                pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")
                if not bool(pattern.search(password)):
                    raise ValidationError(
                        {'password1': ['Password must contain alphabet characters, special characters and numbers']})

    def clean_email(self):
        email = self.cleaned_data['email']
        if validate_email(email) == False:
            raise ValidationError('Enter a valid Email address')

        if User.objects.filter(email=email):
            raise ValidationError('User with this email already exists')
        else:
            return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError('User with this username already exists')
        else:
            return username


class UserProfileForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    contact = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['address', 'contact', 'image', 'x', 'y', 'width', 'height']

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        pattern = re.compile(r'^\d{10}$')
        match = pattern.search(contact)
        if not pattern.search(contact):
            raise ValidationError('Enter a valid mobile number.')
        else:
            return contact

    def save(self):
        photo = super(UserProfileForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        if x is not None and y is not None:
            image = Image.open(photo.image)
            cropped_image = image.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((283, 283), Image.ANTIALIAS)
            resized_image.save(photo.image.path)
        return photo
