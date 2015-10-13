__author__ = 'Сергей'

from django import forms

from ratings.models import Rating
from products.models import Product

class RatingForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     widget=forms.HiddenInput)

    def clean_comment(self):
        comment = self.cleaned_data['comment']
        if len(comment) < 9:
            raise forms.ValidationError(
                'Комментарий слишком короткий. Пожалуйста, изложите свои мысли более развернуто.')
        return comment

    class Meta:
        model = Rating
        fields = ['rating', 'comment', 'product']
