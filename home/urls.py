from django.urls import path
from .views import index, about, booking, menu, service, team, testimonial,\
    contact, staff_page, delete, delete_contact, cart, checkout, thanks_view, update_item, \
    process_order, send_email, submit_review,recommend_view, search_items
urlpatterns = [
    path('', index, name='home'),
    path("staff-page/", staff_page, name="staff_page"),
    path("about/", about, name="about"),
    path("booking/", booking, name="booking"),
    path("menu/", menu, name="menu"),
    path('recommend_items/', recommend_view, name='recommend_items'),
    path("service/", service, name="service"),
    path("team/", team, name="team"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("send-email/", send_email, name="send_email"),
    path('update-item/', update_item, name='update_item'),
    path('process-order/', process_order, name='process_order'),
    path("contact/", contact, name="contact"),
    path('search/', search_items, name='search_items'),
    path("testimonial/", testimonial, name="testimonial"),
    path("delete/<int:id>/", delete, name="delete"),
    path("delete-contact/<int:id>/", delete_contact, name="delete_contact"),
    path("index/", index, name="index"),
    path('submit_review/<int:item_id>/', submit_review, name='submit_review'),
    path('thanks/', thanks_view, name='thanks_views'),

]
