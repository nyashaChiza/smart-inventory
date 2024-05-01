from django.urls import path

from job_card.views import (
    create_job_card, create_job_card_item, JobCardList, JobCardDetailView, assess_card
    )

urlpatterns = [
    path('', create_job_card, name='create_job_card'),
    path('index', JobCardList.as_view() , name='job_card_list'),
    path('details/<int:pk>', JobCardDetailView.as_view() , name='job_card_details'),
    path('assess/<int:pk>', assess_card , name='assess_card'),
    path('item/create/<int:pk>', create_job_card_item, name='create_job_card_item'),
]
