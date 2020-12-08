        # This two step validation process for the submitted form is very hacky in my opinion and I don't like it.
        # This needs to change in the next iteration of this web app.
        # Look into declaring a validator function and using that as the validator argument into the "parent" field in the User model class
        # This validator then needs to be connected to the ModelForm.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import userform
from django.core.validators import BaseValidator
from django.utils.translation import gettext_lazy as _, ngettext_lazy

# class ValidateUserSelectionType(BaseValidator):
#     message = _('Since you are trying to create a Student User, you must select a Parent as well during the Student registration process')
#     code = 'user_type_issue'

def validateusers(request, user_form):
    if user_form.cleaned_data["parent"] is None and user_form.cleaned_data["type"] == 'STUDENT':
        return render(request, "learn/index.html", {
            "userform": user_form,
            "message":"Since you are trying to create a Student User, you must select a Parent as well during the Student registration process"
            })

    elif not user_form.cleaned_data["parent"] is None and not user_form.cleaned_data["type"] == 'STUDENT':
        return render(request, "learn/index.html", {
            "userform": user_form,
            "message":"You can not select a Parent if you are not registering a Student. Please unselect the Parent and submit the form again."
            })

    elif user_form.cleaned_data["type"] == 'STUDENT' and user_form.cleaned_data["parent"].type in ['ADMIN', 'TEACHER', 'STUDENT']:
        return render(request, "learn/index.html", {
        "userform": user_form,
        "message":"Since you are trying to create a Student User, you must select a Parent as well during the Student registration process"
            })           

    else:
        user_form.save()
        # user_form = userform(None)
        return HttpResponseRedirect(reverse('index'))



