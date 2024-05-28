from django import forms
from catalog.models import Product
from config.settings import CATALOG_PRODUCT_CLEAN


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        clean_data = self.cleaned_data.get('name')
        if clean_data in CATALOG_PRODUCT_CLEAN:
            raise forms.ValidationError('Вы ввели запрещенное слово для имени !')

        return clean_data

    def clean_description(self):
        clean_data = self.cleaned_data.get('description')
        list_words = clean_data.split()
        for word in list_words:
            if word in CATALOG_PRODUCT_CLEAN:
                raise forms.ValidationError(f'Ваш текст содержит запрещенное слово <{word}> !')

        return clean_data
