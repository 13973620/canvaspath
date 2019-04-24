# coding:utf-8
# life is short, you need Python！
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'username', 'required': 'required',
                                          'autofocus': 'autofocus'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}))


class CourseForm(forms.Form):
    course = forms.CharField(label="course",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'course id', 'required': 'required',
                                        'autofocus': 'autofocus'}))
    name = forms.CharField(label="name",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'name', 'required': 'required'}))
    dec = forms.CharField(label="dec",
                          widget=forms.TextInput(
                              attrs={'class': 'form-control', 'placeholder': 'description'}))
    sec_no = forms.CharField(label="sec_no",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'description'}))
    sec_type = forms.CharField(label="sec_type")


class UserForm(forms.Form):
    username = forms.CharField(label="username",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'course id', 'required': 'required',
                                          'autofocus': 'autofocus'}))
    email = forms.CharField(label="email",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'name', 'required': 'required'}))
    password = forms.CharField(label="password",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'description',
                                          'required': 'required'}))
    role = forms.CharField(label="role",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'description', 'required': 'required'}))

    name = forms.CharField(label="name",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'description'}))
