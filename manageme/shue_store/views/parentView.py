from bootstrap_modal_forms.generic import BSModalFormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import datetime

# form
from ..forms.accountRegisterForm import AccountRegister

# model
from ..models import ParentAccount


def showList(request):
    object_list = ParentAccount.objects.order_by('create_datetime').reverse().all()
    return render(
            request,
            'shue_store/parent_account_list.html',
            {'object_list': object_list}
    )


def delete(request, id):
    ParentAccount.objects.filter(parent_id=id).delete()
    return redirect('parent')


class Register(BSModalFormView):
    template_name = 'shue_store/input_modal.html'
    form_class = AccountRegister
    success_message = 'Success: Item was created.'
    success_url = reverse_lazy('parent')

    def form_valid(self, form):
        # django-bootstrap-modal-forms bug
        meta = self.request.META.get('HTTP_X_REQUESTED_WITH')
        if not meta == 'XMLHttpRequest':
            account_id = self.request.POST.get('accountId')
            parentAccount = ParentAccount(
                    parent_id=account_id,
                    collection_date=None,
                    create_datetime=datetime.datetime.now(),
                    update_datetime=datetime.datetime.now())
            parentAccount.save()

        response = super().form_valid(form)
        return response
