from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from django.core.exceptions import ValidationError

from ..models import ParentAccount


# exists check
def checkExists(value):
    # database search
    count = ParentAccount.objects.filter(
                parent_id=value
            ).count()

    if count > 0:
        raise ValidationError('This id is already registered!')


class AccountRegister(BSModalForm):
    # account id
    accountId = forms.CharField(label='account id',
                                required=True,
                                max_length=50,
                                validators=[checkExists])

    class Meta:
        fields = ['accountId']
