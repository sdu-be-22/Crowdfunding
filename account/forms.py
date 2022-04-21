import startup
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.models import UserStartupper, UserInvestor
from startup.models import Startup


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'class': 'mt-1 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget = forms.TextInput(attrs={'class': ' mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )

    first_name = forms.CharField(
        max_length=255,
        widget = forms.TextInput(attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )
    last_name = forms.CharField(
        max_length=255,
        widget = forms.TextInput(attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )

    password1 = forms.CharField(
        label="Password",
        widget = forms.PasswordInput(attrs={
            'class': 'mt-1 mb-5  form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 mb-5  form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )
    username = forms.CharField(
        max_length=255,
        widget = forms.TextInput(attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserStartupperForm(ModelForm):
    class Meta:
        model = UserStartupper
        fields = ('birth_date', 'phone', 'gender')
        widgets = {
            'birth_date': forms.SelectDateWidget(years=range(1960, 2022), attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'}),
            'phone':  forms.TextInput(attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'}),
            'gender': forms.TextInput(attrs={'class': 'mt-1 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
        }

class UserInvestorForm(ModelForm):
    class Meta:
        model = UserInvestor
        fields = ('birth_date', 'phone', 'gender')
        widgets = {
            'birth_date': forms.SelectDateWidget(years=range(1960, 2022), attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'}),
            'phone':  forms.TextInput(attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'}),
            'gender': forms.TextInput(attrs={'class': 'mt-1 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
        }

class AddStartup(ModelForm):
    class Meta:
        model = startup.models.Startup
        fields = ('title', 'description', 'category', 'initial_capital', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'}),
            'description': forms.TextInput(attrs={'class': 'mt-1 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'}),
            'category': forms.SelectDateWidget(years=range(1960, 2022), attrs={'class': 'mt-1 mb-5 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'}),
            'initial_capital': forms.TextInput(attrs={'class': 'mt-1 form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0  focus:text-gray-700 focus:bg-white focus:border-indigo-600 focus:outline-none'})
        }