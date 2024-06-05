from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField, BaseInlineFormSet
from catalog.models import Product
from version.models import Version
from config.settings import CATALOG_PRODUCT_CLEAN


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at',)

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        if clean_data in CATALOG_PRODUCT_CLEAN:
            raise ValidationError('Вы ввели запрещенное слово для имени !')

        return clean_data

    def clean_description(self):
        clean_data = self.cleaned_data.get('description')
        list_words = clean_data.split()
        for word in list_words:
            if word in CATALOG_PRODUCT_CLEAN:
                raise ValidationError(f'Ваш текст содержит запрещенное слово <{word}> !')

        return clean_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


# class VersionFormSet(BaseInlineFormSet):
#     def clean(self):
#         active_count = 0
#         for form in self.forms:
#             if form.cleaned_data.get('is_activ'):
#                 active_count += 1
#         if active_count > 1:
#             raise ValidationError('Может существовать только одна активная версия!')
#         super().clean()

class VersionFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        active_count = sum(1 for form in self.forms if form.cleaned_data.get('is_active', False))
        if active_count > 1:
            raise ValidationError("Может существовать только одна активная версия")
