from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationForm(forms.ModelForm):
    username =forms.CharField(label='اسم المستخدم', max_length=30, help_text='اسم المستخدم يجب الا يحتوي على مسافات.')
    email =forms.EmailField(label='البريد الالكتروني')
    first_name =forms.CharField(label='الاسم الاول')
    last_name =forms.CharField(label='الاسم الاخير')
    password =forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
    confirm_password =forms.CharField(label='تاكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def clean_confirm_password(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['confirm_password']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return clean_data['confirm_password']

    def clean_username(self):
        clean_data = self.cleaned_data
        if User.objects.filter(username=clean_data['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل في هذا الاسم')
        return clean_data['username']


class LoginForm(forms.ModelForm):
    username =forms.CharField(label='اسم المستخدم')
    password =forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())

    class Meta:
        model =User
        fields = ('username', 'password')


class UserUpadeForm(forms.ModelForm):
    first_name =forms.CharField(label='الاسم الاول')
    last_name =forms.CharField(label='الاسم الاخير')
    email =forms.EmailField(label='البريد الالكتروني')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileUpadeForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ('image',)