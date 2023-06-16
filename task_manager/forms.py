from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

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


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="E-mail")
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label="Password(repeat)",
                                widget=forms.PasswordInput,)

    def clean_password1(self):
        password1 = self.cleaned_data["password1"]
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password1"]
        if password1 and password2 and password1 != password2:
            errors = {"password2": ValidationError(
                "The entered passwords do not match",
                code="password_mismatch")}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        return user

    class Meta:
        model = Worker
        fields = ("username",
                  "email",
                  "password1",
                  "password2",
                  "first_name",
                  "last_name"
                  )
