from django import forms

class predict(forms.Form):
   age=forms.IntegerField()
   bmi=forms.IntegerField()
   sex=forms.CharField()
   children=forms.IntegerField()
   smoker = forms.CharField()
   region =forms.CharField()
   
   
