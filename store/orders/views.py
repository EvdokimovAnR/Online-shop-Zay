import stripe
from http import HTTPStatus
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from orders.forms import OrderForm
from orders.models import Order
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from products.models import Basket
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessTemplateView(TemplateView):
    template_name = 'orders/success.html'


class CancelTemplateView(TemplateView):
    template_name = 'orders/cancel.html'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('order_create')



    def post(self, request, *args, **kwargs):
        super(OrderCreateView, self).post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        checkout_session = stripe.checkout.Session.create(
            line_items=baskets.stripe_products(),
            metadata={'order_id':self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('order_cancel'))
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)
    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['session'],
        )
        # line_items = session
        # Fulfill the purchase...
        # fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)


# def fulfill_order(session):
#     order_id = int(session.metadata.order_id)
#     order = Order.objects.get(id=order_id)
#     order.update_after_payment()

