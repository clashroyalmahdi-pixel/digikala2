from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , SetPasswordForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile

class UpdateUserInfo(forms.ModelForm):

    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن'}),
        required=False
    )
    address1 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس اول'}),
        required=False
    )
    address2 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس دوم'}),
        required=False
    )
    city = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر'}),
        required=False
    )
    state = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'منطقه'}),
        required=False
    )
    zipcode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کد پستی'}),
        required=False
    )
    country = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کشور'}),
        required=False
    )
    
    class  Meta:
        model = Profile
        fields = ('phone','address1','address2','city','state','zipcode','country')




class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name' : 'password',
                'type' : 'password',
                'placeholder':'رمز بالای 8 کاراکتر را وارد کنید'

            }
        )
    )
    new_password2 = forms.CharField(
        label='',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name' : 'password',
                'type' : 'password',
                'placeholder':'دوباره رمز خود را وارد کنید'

            }
        )
    )
    
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if password1:
            if len(password1) < 8:
                raise ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")
            
            if password1.isdigit():
                raise ValidationError("رمز عبور نمی‌تواند فقط شامل اعداد باشد")
            
            if password1.isalpha():
                raise ValidationError("رمز عبور نمی‌تواند فقط شامل حروف باشد")
        return password1
    
    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("رمزهای وارد شده یکسان نیستند")
        return password2
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    class Meta:
        model =User
        fields =['new_password1','newpassword2']

class SignUpForm(UserCreationForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("این نام کاربری قبلاً ثبت شده است.")
        return username
    

    first_name =forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'}),
    )
    last_name =forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'}),
    )
    email =forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید'}),
    )
    username=forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری'}),
    )
    password1 = forms.CharField(
        label='',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name' : 'password',
                'type' : 'password',
                'placeholder':'رمز بالای 8 کاراکتر را وارد کنید'

            }
        )
    )
    password2 = forms.CharField(
        label='',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name' : 'password',
                'type' : 'password',
                'placeholder':'دوباره رمز خود را وارد کنید'

            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')


class UpdateUserForm(UserCreationForm):
    password1 = None
    password2 = None
    first_name =forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'}),
        required=False
    )
    last_name =forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'}),
        required=False
    )
    email =forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید'}),
        required=False
    )
    username=forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username',)
