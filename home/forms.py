from django import forms 
from  .models import Follower


class Follow(forms.ModelForm): 
    class Meta:
        model = Follower 
        fields = '__all__'

