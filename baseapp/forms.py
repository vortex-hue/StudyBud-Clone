from django.forms import ModelForm
from .models import Room

#Room form
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']