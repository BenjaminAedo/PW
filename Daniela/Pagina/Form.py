from django.forms import ModelForm

from CarritoApp.models import Producto

class ProdForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio']

