from django.db import models

# Create your models here.
class approvals(models.Model):
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	MARRIED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	GRADUATED_CHOICES = (
		('Graduate', 'Graduated'),
		('Not_Graduate', 'Not_Graduate')
	)
	SELFEMPLOYED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	PROPERTY_CHOICES = (
		('Rural', 'Rural'),
		('Semiurban', 'Semiurban'),
		('Urban', 'Urban')
	)
	firstname=models.CharField(max_length=15, default = "")
	lastname=models.CharField(max_length=15, default = "")
	Dependents=models.IntegerField(default=0)
	ApplicantIncome=models.IntegerField(default=0)
	CoapplicatIncome=models.IntegerField(default=0)
	LoanAmount=models.IntegerField(default=0)
	Loan_Amount_Term=models.IntegerField(default=0)
	Credit_History=models.IntegerField(default=0)
	Gender=models.CharField(max_length=15, choices=GENDER_CHOICES, default = "")
	Married=models.CharField(max_length=15, choices=MARRIED_CHOICES, default = "")
	Education=models.CharField(max_length=15, choices=GRADUATED_CHOICES, default = "")
	Self_Employed=models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES, default = "")
	Property_Area=models.CharField(max_length=15, choices=PROPERTY_CHOICES, default=SELFEMPLOYED_CHOICES)

	def __str__(self):
		return '{}, {}'.format(self.lastname, self.firstname)