from collections import UserList
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import localbank_register_request,  login_page, add_client, edit_client, show_transanctions, confirm_pending_status, make_transaction_request,get_transaction_status,confirm_pending_status,get_all_users,show_status_comp,local_register,foreign_register,ForeignBank,foreign_login_page



urlpatterns  = [
    # path('balance/',BankBalance,name='balance'),
    path('localbank_Register/', localbank_register_request,
         name='localbank_Register'),
    path('localbank/',local_register,name="localbank"),
    path('Foreignbank/',foreign_register,name="Foreignbank"),
    path('Register_ForeignBank/',ForeignBank,name="Register_ForeignBank"),
    path('login/', login_page, name='login'),
    path('foreign_login/',foreign_login_page,name="foreign_login"),
    path('addclient/', add_client, name='add_client'),
    path('editclient/<str:pk>', edit_client, name='edit_client'),
    path('show_transaction/', show_transanctions, name='show_transaction'),
    path('confirm_status/<str:pk>', confirm_pending_status, name='confirm_status'),
    path('make_transaction/', make_transaction_request, name='make_transaction'),
    path('transaction_status/',get_transaction_status,name="transaction_status"),
    path('confirm_status/<str:pk>',confirm_pending_status,name='confirm_status'),
    path('UserList',get_all_users,name='UserList'),
    path('completed_transaction/',show_status_comp,name='completed_transaction'),

]
