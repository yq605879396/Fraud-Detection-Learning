### This folder contains two part:  
#### 1. Train  
The dataset used is Bankloan.csv, contains customers data and whether they can get load permission  
including a jupyter notebook which is a neural network classifier model  
trained model saved at ./train/models: loan_model=> used to do the classification, scaler_model => used to scale input when predict  

these two models will be used in the web application 

#### 2. Web Application
It contains all the things about visualization.


### How to run it: 
#### requirement:    
python 3.6   
pip install django 
pip install django-crispy-forms   
pip install djangorestframwork   
pip install tensorflow==2.2.0   
pip install scikit-learn==0.23.1   
keras = 2.4.3   
pandas = 0.24.2   


#### Command  
base path: visualize_ML_model/web/  
run this command in the terminal:  
python manage.py runserver  # start the web application  

Then you can open 127.0.0.1:8000/form in your browser  
It should be a form, where you can fill in some data according to the indication,   
and click submit it will return an result indicating "Approval" or "Reject" of the loan application.  

#### Referring：
Thanks the tutorial from "Django Rest Framework API Development": https://www.youtube.com/watch?v=dJihgq_4gNg






