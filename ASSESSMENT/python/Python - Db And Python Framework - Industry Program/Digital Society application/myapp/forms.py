from django import forms
from .models import society_member,SocietyWatchmen,notice_board,Event,visitor,charman

class member_profile(forms.ModelForm):
    class Meta:
        model  = society_member
        fields =  '__all__'

class watchman_form(forms.ModelForm):
    class Meta:
        model  = SocietyWatchmen
        fields =  '__all__'

class notice_form(forms.ModelForm):
    class Meta:
        model = notice_board
        fields ='__all__'

class event_form(forms.ModelForm):
    class Meta:
        model = Event
        fields ="__all__"
        
class visitor_form(forms.ModelForm):
    class Meta:
        model = visitor
        fields = "__all__"
        
class charman_form(forms.ModelForm):
    class Meta:
        model = charman
        fields= "__all__"
