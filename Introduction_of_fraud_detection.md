

##### 1. Reference

https://en.wikipedia.org/wiki/Data_analysis_techniques_for_fraud_detection
https://www.zhihu.com/question/30508773

[https://p1htmlkernalweb.mybluemix.net/articles/fraud+detection%E8%AE%BA%E6%96%87%E7%BB%BC%E8%BF%B0%E6%95%B4%E7%90%86%E7%9A%84%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE_3705250_csdn.html](https://p1htmlkernalweb.mybluemix.net/articles/fraud+detection论文综述整理的思维导图_3705250_csdn.html)





#### 2. Dataset

###### 2.1 Fraud Detection

Synthetic Financial Datasets For Fraud Detection
https://www.kaggle.com/ntnu-testimon/paysim1/home

Credit Card Fraud Detection
https://www.kaggle.com/mlg-ulb/creditcardfraud/data

Graph Fraud Datasets from Pro.Srijan Kumar
https://www.cc.gatech.edu/~srijan/

###### 2.2 Graph dataset

Standford graph datasets
http://snap.stanford.edu/data/?utm_source=qq&utm_medium=social&utm_oi=43664650797056#socnets

Bitcoin OTC trust weighted signed network
https://snap.stanford.edu/data/soc-sign-bitcoin-otc.html

###### Outlier Detection Datasets(ODDS)

http://odds.cs.stonybrook.edu/#table4



#### 3. Scenery 

cell phones, insurance claims, tax return, credit card transactions, government procurement

#### 4. Area

KDD(knowledge discovery in databases), data mining, machine learning and statistics

#### 5. Statistical techniques

data preprocessing(validation, error correction
filling up or missing or incorrect data)
calculation of various statistical parameters(e.g. averages, quantiles, probability distribution..)
computing user profiles
time-series analysis of time-dependent data
clustering and classification to find patterns and associations among groups of data
data matching(remove duplicate records and identify links between two datasets)
regression analysis(examine the relationship between two or more variables)

#### 6. AI techniques

data mining to classify/cluster/segment the data and find associations and rules in the data
expert systems
Pattern recognition
ML
Neural nets
link analysis, decision theory, sequence matching



#### 7. Feature of  fraud detection

##### blur definition

no specific type of fraud
different type of fraud may mess together
most of data have no label(hard to use supervised learning)
hard to identify noise and anomaly

##### ability to predict fraud detection

can detect similar fraud detection, but there many variants
may need domain experts

#### 8. How to do fraud detection

##### 1. visualization

correlation matrix/ multidimensional scaling  => try to see some problems

##### 2. Algorithms

Two kinds of assumptions

###### Time dependent

consider time information, e.g. detection spike(an anomaly), time stability -> vector auto-regression, more applied in financial area

###### Time independent

unsupervised algorithms:
e.g. isolation forest, density based clustering(CBLOF), notice: K-means and other k Modes may not suitable to detect anomaly, since noise and outliers have big influence to the model, peer group analysis, break point analysis, 

supervised algorithms:
supervised  neural networks, Bayesian learning neural network,  hybrid knowledge systems, link analysis
Classification: XGBoost, RF, GBM

graph model:
relation network: 1.detect community (Walktrap, InforMap, FastGreedy) 2. using good/bad user to propagate(Label Propagation, SIR Model. 



##### 3. Testify predictions

can not avoid bias





