from django.urls import path
from django.urls.resolvers import URLPattern
from .views import localbank_register_request, api_transaction, login_page, add_client, edit_client, show_transanctions, confirm_pending_status, make_transaction_request


urlpatterns = [
    path('transaction/', api_transaction, name='test'),
    # path('balance/',BankBalance,name='balance'),
    path('localbank_Register/', localbank_register_request,
         name='localbank_Register'),
    path('login/', login_page, name='login'),
    path('addclient/', add_client, name='add_client'),
    path('editclient/<str:pk>', edit_client, name='edit_client'),
    path('show_transaction/', show_transanctions, name='show_transaction'),
    path('confirm_status/<str:pk>', confirm_pending_status, name='confirm_status'),
    path('make_transaction/',make_transaction_request,name='make_transaction')

]
