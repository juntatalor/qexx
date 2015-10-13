__author__ = 'Сергей'

from django.template.loader import render_to_string

from orders.constants import PAYMENT_STATUS


gateways = {}


class BaseGateway():
    """
    Базовый класс оплаты
    """

    id, name, help_text, image = '', '', '', ''
    online_payment = False
    payment_status = PAYMENT_STATUS['NOT_PAYED']
    urls = []

    @classmethod
    def get_payment_url(cls, order):
        pass

    @classmethod
    def update_form(cls, form):
        pass

    def render(self, renderer, i):
        # Renderer - cart.forms.CartRadioChoiceFieldRenderer
        # i - счетчик полей в списке
        w = renderer.choice_input_class(renderer.name, renderer.value,
                                        renderer.attrs.copy(), (self.id, self.name), i)

        return render_to_string('payment/gateway.html', {
            'label': w,
            'gateway': self
        })