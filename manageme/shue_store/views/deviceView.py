from bootstrap_modal_forms.generic import BSModalFormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

# form
from ..forms.deviceRegisterForm import DeviceRegister

# model
from ..models import DeviceMaster


def showList(request):
    object_list = DeviceMaster.objects.order_by('create_datetime').reverse().all()
    return render(
            request,
            'shue_store/device_list.html',
            {'object_list': object_list}
    )


def delete(request, id):
    DeviceMaster.objects.filter(device_id=id).delete()
    return redirect('device')


class Register(LoginRequiredMixin, BSModalFormView):
    template_name = 'shue_store/input_modal.html'
    form_class = DeviceRegister
    success_message = 'Success: Item was created.'
    success_url = reverse_lazy('device')

    def form_valid(self, form):
        # django-bootstrap-modal-forms bug
        meta = self.request.META.get('HTTP_X_REQUESTED_WITH')
        if not meta == 'XMLHttpRequest':

            deviceMaster = DeviceMaster(
                    device_id=self.request.POST.get('deviceId'),
                    instagram_id=self.request.POST.get('instagramId'),
                    preparation_flg=self.request.POST.get('preparationFlg'),
                    max_follow_count=self.request.POST.get('maxFollowCount'),
                    create_datetime=datetime.datetime.now(),
                    update_datetime=datetime.datetime.now())
            deviceMaster.save()

        response = super().form_valid(form)
        return response
