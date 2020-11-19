from . models import approvals
from . forms import ApprovalForm
from . serializers import approvalsSerializers
#from sklearn.externals 
import joblib
import pickle, json, os
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from keras import models
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib import messages
from django.shortcuts import render

base_path = os.getcwd()

class ApprovalsView(viewsets.ModelViewSet):
	queryset = approvals.objects.all()
	serializer_class = approvalsSerializers
'''
def myform(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
    else:
        form = MyForm()
'''
def ohevalue(df):
    
    #ohe_col = joblib.load(base_path+ '\loan_model.pkl')
    #print(ohe_col.summary())
    ohe_col = [ 'Dependents', 'ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Gender_Female','Gender_Male','Married_No','Married_Yes','Education_Graduate','Education_Not_Graduate','Self_Employed_No','Self_Employed_Yes','Property_Area_Rural','Property_Area_Semiurban','Property_Area_Urban']

    cat_columns = ['Gender','Married','Education','Self_Employed','Property_Area']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf


#@api_view(["POST"])
def approvereject(unit):
	print("caculating....")
	if(True):
		mdl=models.load_model(base_path+"\loan_model.h5")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		#mydata=request.data
		#unit=np.array(list(mydata.values()))
		#unit=unit.reshape(1,-1)
		scalers=joblib.load(base_path+"\scaler_model")
		#scalers = MinMaxScaler()
		X=scalers.transform(unit)
		y_pred=mdl.predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		#print(newdf)
		#return JsonResponse('Your Status is {}'.format(newdf), safe=False)
		return (newdf.values[0][0], X[0])
    #except ValueError as e:
	#	return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def cxcontact(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['firstname']
            Lastname = form.cleaned_data['lastname']
            Dependents = form.cleaned_data['Dependents']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            VoapplicatIncome = form.cleaned_data['CoapplicatIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Loan_Amount_Term =form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']
           
            #print(Firstname, Lastname, Dependents, Married)
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            #print(ohevalue(df))
            answer = approvereject(ohevalue(df))[0]
            Xscalers = approvereject(ohevalue(df))[1]
            if int(df['LoanAmount']) <25000:
                messages.success(request, 'Application Status:{}'.format(answer))
            else:
                messages.success(request, 'Invalid: Your Loan request Exceeds the $25,000 Limit')
            #print(answer.data)
            #messages.success(request,'Application Status: {}'.format(answer))

    form = ApprovalForm()
    return render(request,'myform/cxform.html',{'form':form})