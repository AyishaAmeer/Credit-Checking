from django import forms

class CreditForm(forms.Form):
    age = forms.IntegerField(min_value=18, max_value=100)
    annual_income = forms.FloatField(min_value=0, help_text="In your currency")
    existing_debt = forms.FloatField(min_value=0)
    credit_utilization = forms.FloatField(min_value=0, max_value=100,
                                          help_text="% of your total credit used")
    on_time_payments = forms.IntegerField(min_value=0)
    missed_payments = forms.IntegerField(min_value=0)
    history_years = forms.FloatField(min_value=0, help_text="Years of credit history")
    inquiries_last_6_months = forms.IntegerField(min_value=0)