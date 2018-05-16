from celery import task
from django.core.mail import send_mail
from .models import Order, OrderItem


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = '[E-Shopper] Order nr. {}'.format(order.id)
    message = 'Hello {},\n\nYou have successfully placed an order at E-Shopper.Your order id is {}. \nWe will send a confirmation email when your item ships.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@eshopper.com', [order.email],)
    return mail_sent

