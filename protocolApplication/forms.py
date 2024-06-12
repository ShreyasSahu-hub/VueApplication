from django.forms import ModelForm #This is the ModelForm module from the forms django library
from django import forms #This is the forms module from the django library. This is used to develop forms.
from crispy_forms.helper import FormHelper #This is the FormHelper module from the crispy_forms django library
from crispy_forms.layout import Row, Layout, Submit #This is the Row, Layout, and Submit modules from the crispy_forms.layout django library. This is used structure the django form.
from crispy_forms.bootstrap import FormActions #This is the FormActions module from the crispy_froms.bootstrap django library.


#These are the python classes to create the form layout by implementing the essential fields and what type of data should each field accept
class SignUpForm(forms.Form):

     firstName = forms.CharField(
         max_length = 50
     )

     lastName = forms.CharField(
         max_length = 50
     )

     username = forms.CharField(
         label='Username: The username must be unique',
         max_length = 200,
         widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
            }
         )
     )

     user_email = forms.EmailField(
           label = "Email",
           max_length=254,
           widget=forms.TextInput(attrs={'autocomplete': 'user_email'})
     )

     password = forms.CharField(
          label='Password',
          max_length = 200,
          widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
     )

     password_confirm = forms.CharField(
           label='Confirm Password',
           max_length = 200,
           widget=forms.PasswordInput,
     )

     helper = FormHelper()
     helper.layout = Layout(
         Row('firstName', css_class='mb-2'),
         Row('lastName', css_class='mb-2'),
         Row('username', css_class='mb-2'),
         Row('user_email', css_class='mb-2'),
         Row('password', css_class='mb-2'),
         Row('password_confirm', css_class='mb-2'),
         FormActions(
             Submit('signup', 'Sign up', css_class="btn-primary"),
             css_class='mt-3'
         )
     )

     #def __str__(self):

         #return f"({self.username}), ({self.password})"

class LoginPage(forms.Form):

     username = forms.CharField(
         label = "Enter your username",
         max_length = 200,
         widget=forms.TextInput(attrs={'autocomplete': 'username'})
     )
     password = forms.CharField(
         label = "Enter your password",
         max_length = 200,
         widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
     )

     helper = FormHelper()
     helper.layout = Layout(
        Row('username', css_class="mb-2"),
        Row('password', css_class="mb-2")
     )