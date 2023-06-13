from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from task_manager.models import Task, Worker


# class DriverLicenseUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Driver
#         fields = ("license_number",)
#
#     def clean_license_number(self):
#         license_number = self.cleaned_data["license_number"]
#
#         if len(license_number) != 8:
#             raise ValidationError(
#                 "Licence must be of 8 characters."
#             )
#         if not license_number[:3].isupper():
#             raise ValidationError(
#                 "First 3 symbol must be uppercase."
#             )
#         if not license_number[:3].isalpha():
#             raise ValidationError(
#                 "First 3 symbol must be letters"
#             )
#         if not license_number[3:].isnumeric():
#             raise ValidationError(
#                 "Last 5 symbol must be numbers."
#             )
#         return license_number


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
