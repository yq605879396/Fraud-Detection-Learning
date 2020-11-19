from django import forms

class ApprovalForm(forms.Form):
	firstname=forms.CharField(max_length=15, widget = forms.TextInput(attrs={'placeholder':'Enter Firstname'}))
	lastname=forms.CharField(max_length=15, widget = forms.TextInput(attrs={'placeholder':'Enter Lasttname'}))
	Dependents=forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Enter Number of Depenndents'}))
	ApplicantIncome=forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Enter Monthly Gross Income'}))
	CoapplicatIncome=forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Enter Co-Applicant Monthly Gross'}))
	LoanAmount=forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Requested Loan Amount'}))
	Loan_Amount_Term=forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder':'Loan Term in Months'}))
	Credit_History=forms.ChoiceField(choices=[('0',0),('1',1),('2',2),('3',3)])
	Gender=forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
	Married=forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
	Education=forms.ChoiceField(choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate')])
	Self_Employed=forms.ChoiceField(choices=[('Yes','Yes'), ('No', 'No')])
	Property_Area=forms.ChoiceField(choices= [('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])
