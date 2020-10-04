from django import forms
from decimal import Decimal

#sdfsfsfsdfsdfs
#4454564564645

class cal_wthkForm(forms.Form):
    from .calculation.cal_unit import UNIT_L1,UNIT_S,UNIT_P,UNIT_T
    #item0 - 1 to 6
    value_D = forms.DecimalField(label='Outside Diameter, D :')
    value_S = forms.DecimalField(label='SMYS, S :')
    value_P = forms.DecimalField(label='Internal Pressure , P :')
    value_T = forms.DecimalField(label='Temperator, Tp :',initial=Decimal("25"))
    value_F = forms.DecimalField(label='Design Factor, F :',initial=Decimal("0.6"))#,default=Decimal("0.6")
    value_E = forms.DecimalField(label='Weld Joint Factor, E :',initial=Decimal("1.0"))#
    #item1 to (7) to (12)
    unit_D = forms.ChoiceField(choices = UNIT_L1)
    unit_S = forms.ChoiceField(choices = UNIT_S)
    unit_P = forms.ChoiceField(choices = UNIT_P)
    unit_T = forms.ChoiceField(choices = UNIT_T)

    #Set initial value to avoid form.is_valid = False
    unit_F = forms.CharField(widget=forms.HiddenInput(),initial='-',disabled=True) 
    unit_E = forms.CharField(widget=forms.HiddenInput(),initial='-',disabled=True)

    
    


