
from django.template.loader import render_to_string
from django.utils import timezone
from django.db.models import Count

from orders.constants import ORDER_STATUS


methods, initial_method = {}, None


class BaseShipment():
    """Базовый класс доставки, реализующий основные алгоритмы расчета стоимости"""

    id, name, help_text, image = '', '', '', ''
    order_status = ORDER_STATUS['RESERVED']
    initial_gateway = 'Cash'
    checkout_form = None
    free_delivery_available = True

    def __init__(self, checkout_form=None):
        self.checkout_form = checkout_form

    def get_price(self):
        return 0

    @classmethod
    def update_form(cls, form):
        pass

    def render(self, renderer, i):
        # Renderer - cart.forms.CartRadioChoiceFieldRenderer
        # i - счетчик полей в списке
        w = renderer.choice_input_class(renderer.name, renderer.value,
                                        renderer.attrs.copy(), (self.id, self.name), i)

        return render_to_string('shipping/method.html', {
            'label': w,
            'method': self
        })