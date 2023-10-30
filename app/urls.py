from django.urls import path
from app.views import (
    Index,
    AdminIndex,
    UserProfile,
    UserProfileUpdate,
    AccountList,
    AccountTransfer,
    BankList,
    BankCreate,
    BankDetail,
    BankUpdate,
    BankDelete,
    CardList,
    CardCreate,
    CardDetail,
    CardUpdate,
    CardDelete,
    SendSearchUser,
    SendMoney,
    SendSuccess,
    RequestSearchUser,
    RequestMoney,
    RequestSuccess,
    ActivityList,
    IncompleteTranList,
    IncompletePayment,
    IncompletePaymentConfirm,
    PaymentComplete,
    IncompleteRequest,
    IncompleteRequestDelete,
    StaffTransactionList,
    StaffTranDetail,
    StaffTranDelete,
    StaffUserList,
    StaffUserInfo,
    StaffUserTran,
    StaffUserTranDetail,
    StaffUserTranDelete,
    StaffUserPayment,
    StaffUserBankDetail,
    StaffUserCardDetail,
)

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
    path('admin-index/', AdminIndex.as_view(), name='admin_index'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdate.as_view(), name='profile_update'),
    path('wallet/', AccountList.as_view(), name='account'),
    path('transfer/<int:pk>/', AccountTransfer.as_view(), name='account_transfer'),
    path('bank/', BankList.as_view(), name='bank'),
    path('bank/add/', BankCreate.as_view(), name='bank_create'),
    path('bank/<int:pk>/detail/', BankDetail.as_view(), name='bank_detail'),
    path('bank/<int:pk>/update/', BankUpdate.as_view(), name='bank_update'),
    path('bank/<int:pk>/delete/', BankDelete.as_view(), name='bank_delete'),
    path('card/', CardList.as_view(), name='card'),
    path('card/add/', CardCreate.as_view(), name='card_create'),
    path('card/<int:pk>/detail/', CardDetail.as_view(), name='card_detail'),
    path('card/<int:pk>/update/', CardUpdate.as_view(), name='card_update'),
    path('card/<int:pk>/delete/', CardDelete.as_view(), name='card_delete'),
    path('activity/', ActivityList.as_view(), name='activity'),
    path('send/', SendSearchUser.as_view(), name='send'),
    path('send/<int:pk>/', SendMoney.as_view(), name='send_money'),
    path('send/success/', SendSuccess.as_view(), name='send_success'),
    path('request/', RequestSearchUser.as_view(), name='request'),
    path('request/<int:pk>/', RequestMoney.as_view(), name='request_money'),
    path('request/success/', RequestSuccess.as_view(), name='request_success'),
    path('incomplete/', IncompleteTranList.as_view(), name='incomplete'),
    path('incomplete/payment/<int:pk>/detail/', IncompletePayment.as_view(), name='incomplete_payment'),
    path('incomplete/payment/<int:pk>/confirm/', IncompletePaymentConfirm.as_view(), name='incomplete_payment_confirm'),
    path('incomplete/payment/complete/', PaymentComplete.as_view(), name='payment_complete'),
    path('incomplete/request/<int:pk>/detail/', IncompleteRequest.as_view(), name='incomplete_request'),
    path('incomplete/request/<int:pk>/delete/', IncompleteRequestDelete.as_view(), name='incomplete_request_delete'),

    path('staff/transaction/', StaffTransactionList.as_view(), name='staff_transaction'),
    path('staff/transaction/<int:pk>/detail/', StaffTranDetail.as_view(), name='staff_tran_detail'),
    path('staff/transaction/<int:pk>/delete/', StaffTranDelete.as_view(), name='staff_tran_delete'),
    path('staff/user/', StaffUserList.as_view(), name='staff_user'),
    path('staff/user/<int:pk>/info/', StaffUserInfo.as_view(), name='staff_user_info'),
    path('staff/user/<int:pk>/payment/', StaffUserPayment.as_view(), name='staff_user_pay'),
    path('staff/user/<int:pk>/bank/<int:bpk>', StaffUserBankDetail.as_view(), name='staff_user_bank'),
    path('staff/user/<int:pk>/card/<int:cpk>/', StaffUserCardDetail.as_view(), name='staff_user_card'),
    path('staff/user/<int:pk>/transactions/', StaffUserTran.as_view(), name='staff_user_tran'),
    path('staff/user/<int:pk>/transactions/<int:tpk>/detail', StaffUserTranDetail.as_view(), name='staff_user_tran_detail'),
    path('staff/user/<int:pk>/transactions/<int:tpk>/delete', StaffUserTranDelete.as_view(), name='staff_user_tran_delete'),

]
