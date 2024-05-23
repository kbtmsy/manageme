from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from django.core.exceptions import ValidationError

from ..models import DeviceMaster


# exists check
def checkExists(value):
    # database search
    count = DeviceMaster.objects.filter(
                device_id=value
            ).count()

    if count > 0:
        raise ValidationError('This id is already registered!')


class DeviceRegister(BSModalForm):

    # device id
    deviceId = forms.CharField(label='device id',
                                  required=True,
                                  max_length=18,
                                  validators=[checkExists])

    instagramId = forms.CharField(label='instagram id',
                                  required=True,
                                  max_length=50)

    preparationFlg = forms.ChoiceField(label='preparation',
                                       choices=(
                                           ('0', ''),
                                           ('1', 'preparation')
                                       ))

    maxFollowCount = forms.DecimalField(label='max follow count',
                                        max_digits=2,
                                        decimal_places=0
                                        )

    class Meta:
        fields = ['deviceId',
                  'instagramId',
                  'preparationFlg',
                  'maxFollowCount']
