from collections import UserList
from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    localbank_register_request,
    login_page,
    add_client,
    edit_client,
    show_transanctions,
    confirm_status,
    make_transaction_request,
    get_transaction_status,
    get_all_users,
    show_status_comp,
    local_register,
    foreign_register,
    Foreign_bank_register,
    foreign_login_page,
    add_client_request,
    edit_client_request,
    show_clients,
    transaction,
    login_local,
    show_foreign_transaction,
    index_request,
    about_request,
    services_request,
    contact_request,
    header_request,
    footer_request,
    blog_request,
    single_request,
    foreign_login,
    date_request,
    logout_request,
)


urlpatterns = [
    # path('balance/',BankBalance,name='balance'),
    path("", index_request, name=""),
    path("localbank_Register/", localbank_register_request, name="localbank_Register"),
    path("localbank/", local_register, name="localbank"),
    path("Foreignbank/", foreign_register, name="Foreignbank"),
    path("Register_ForeignBank/", Foreign_bank_register, name="Register_ForeignBank"),
    path("login/", login_page, name="login"),
    path("local_login/", login_local, name="local_login"),
    path("foreign_login/", foreign_login_page, name="foreign_login"),
    path("foreign/", foreign_login, name="foreign"),
    path("add_Client/", add_client_request, name="add_Client"),
    path("add_client_request/", add_client, name="add_client_request"),
    path("clients/", show_clients, name="clients"),
    path("editclient/<str:pk>", edit_client, name="editclient"),
    path("edit_Client/<str:pk>", edit_client_request, name="edit_Client"),
    path("create_transanction/", transaction, name="create_transanction"),
    path("show_transaction/", show_transanctions, name="show_transaction"),
    path("confirm_status/<str:pk>", confirm_status, name="confirm_status"),
    path("make_transaction/", make_transaction_request, name="make_transaction"),
    path("transaction_status/", get_transaction_status, name="transaction_status"),
    path("UserList", get_all_users, name="UserList"),
    path("completed_transaction/", show_status_comp, name="completed_transaction"),
    path(
        "show_foreign_transaction/",
        show_foreign_transaction,
        name="show_foreign_transaction",
    ),
    path("about/", about_request, name="about"),
    path("services/", services_request, name="services"),
    path("contact_us/", contact_request, name="contact_us"),
    path("header/", header_request, name="header"),
    path("blog/", blog_request, name="blog"),
    path("single-post/", single_request, name="single-post"),
    path("footer/", footer_request, name="footer"),
    path("date/",date_request,name="date"),
    path('logout/',logout_request,name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
