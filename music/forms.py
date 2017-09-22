from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']

        labels = {
            'album_title' : 'Product Title',
            'artist' : 'Product Name',
            'genre' : 'Category',
            'album_logo' : 'Product Image'
        }


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_number','song_title', 'song_desc','song_price','audio_file']

        labels = {
            'song_number': 'Item ID',
            'song_title' : 'Item Name',
            'song_desc' : 'Description',
            'song_price': 'Price',
            'audio_file' : 'Item Image'
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    #contact_phone = forms.RegexField(regex=r'^\+?1?\d{9,10}$',error_messages="")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Invalid Phone Number")
    contact_phone = forms.CharField(validators=[phone_regex], max_length=10, required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Email Address:"
        self.fields['contact_phone'].label = "Phone Number:"
        self.fields['content'].label = "What do you want to say?"