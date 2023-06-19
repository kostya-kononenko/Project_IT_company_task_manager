from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

from task_manager.models import Task, Worker


class TaskForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"


class WorkerUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("position",)


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(attrs={
                               "placeholder": "Search task"}))


class WorkerSearchForm(forms.Form):
    username = forms.CharField(max_length=255,
                               required=False,
                               label="",
                               widget=forms.TextInput(attrs={
                                   "placeholder": "Search worker username"}))


class PositionSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(attrs={
                               "placeholder": "Search position"}))


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(attrs={
                               "placeholder": "Search task type"}))


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    def clean_password1(self):
        password1 = self.cleaned_data["password1"]
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            errors = {"password2": ValidationError(
                "The entered passwords do not match",
                code="password_mismatch")}
            raise ValidationError(errors)
        else:
            return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model = Worker
        fields = ("username",
                  "email",
                  "password1",
                  "password2",
                  )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
