import streamlit as st
from PIL import Image

st.header('TDS 3301 GROUP PROJECT')

option = st.sidebar.radio('Please choose a question',['General EDA & DP','1','2','3','4','5','6','7','8','9'])

if option == 'General EDA & DP':
	st.title('General Exploratory Data Analysis & Data Pre-processing')
	
	# data types
	st.title('Checking data types')
	st.write('First, we checked the data types after we select desired features from the dataset. Except the date and the state, the other features are all numeric which is correct. Thus no further data preprocessing needed.')
	st.image([Image.open("images/q2/EDA/data_types/1.png"),Image.open("images/q2/EDA/data_types/2.png"),Image.open("images/q2/EDA/data_types/3.png")],caption=['Checking data types(1)','Checking data types(2)','Checking data types(3)'])
	
	# missing values
	st.title('Checking missing values')
	st.write('Next, we checked whether there is any missing values in the dataset. As shown below, there is no missing values in the dataset.')
	st.image([Image.open("images/q2/EDA/missing_values/1.png"),Image.open("images/q2/EDA/missing_values/2.png"),Image.open("images/q2/EDA/missing_values/3.png")],caption=['Checking missing values(1)','Checking missing values(2)','Checking missing values(3)'])
	
	# outliers
	st.title('Detection and removal of outliers')
	st.write('Other than that, we also checked the skewness and distribution of each feature in the dataset to determine whether the removal of outliers is needed. All the data points of the features are distributed evenly except for the death cases and the number of individuals discharged from Covid-19 in PKRC. As shown below, there are three data points that are far apart from the remaining data point in death cases and one data point far apart in pkrc_discharged_covid. The skewness of these two features are 10.43 and 4.08. By setting a threshold of 200 and 2000, we are able to remove these far apart data points. We noticed that only the death cases improve the skewness a lot to 7.76, thus we would only remove the outliers for the death cases. ')
	st.image([Image.open("images/q2/EDA/distribution/before/Daily death cases_before.png"),Image.open("images/q2/EDA/distribution/after/deaths_new_after.png"),Image.open("images/q2/EDA/distribution/before/PKRC information_before.png")],caption=['Distribution of death cases (Before remove outliers)','Distribution of death cases (After remove outliers)','Distribution of the number of individuals discharged from Covid-19 in PKRC'])
	
	# EDA1
	st.title('Which gender are most susceptible to COVID-19?')
	st.write('In the positive cases of Covid-19, there are around 1,000,000 of females and 1,200,000 of male. Thus, it is confirmed that males are more likely to admit Covid-19 than females in Malaysia. The countplot is shown below for illustration.')
	st.image(Image.open("images/q2/EDA/questions/gender_counts.png"),caption='Gender countplot in positive cases of Covid-19')
	
	# EDA2
	st.title('Distribution of death by gender & state.')
	st.write('The bar chart below displays the distribution of the gender and state information in the death cases. It is observed that the distribution is not normal. The distribution of data points in gender in Selangor is a lot more than the remaining states which is approaching 100,000. ')
	st.image(Image.open("images/q2/EDA/questions/gender_state_distribution.png"),caption='Distribution of gender and state of death cases')
	
	# EDA3
	st.title('Any correlations between admitted and discharged of Covid-19 in hospital and PKRC?')
	st.write('There is only a weak correlation between the hospital and PKRC information. However, the admitted cases and discharged cases in both hospital and PKRC are highly and positively correlated. This indicates that if the admitted cases increase for 1% in hospital or PKRC, the discharged cases will also increase for more than 0.88% and vice versa.')
	st.image(Image.open("images/q2/EDA/questions/hospital_pkrc_correlation.png"),caption='Correlation heatmap of admitted and discharged cases in hospital and PKRC')
	
if option == '1':
	st.title('1. Has vaccination helped reduce the daily cases? What states have shown the effect of vaccination?')
	st.write('To answer this question, the correlation between the feature "daily_vaccination" and feature "cases_new" are compared for all the states. We have concluded that the effect of vaccination differs from each state and more time and data is needed to further produce an accurate conclusion. For example, the correlation of new cases and vaccination in Sarawak is a weak negative correlation which means the higher the vaccination rate, the lower the daily cases recorded. On the other hand, for Labuan the correlation between vaccination rate and daily cases is relatively weak. Although the correlation is very weak, it tells us that vaccination can help to slightly reduce or prevent the daily cases to rise. The conclusion is that vaccination does help in reducing the daily cases in some states such as Sarawak and Labuan.')
	st.image([Image.open("images/q2/1/Sarawak_heatmap.png"),Image.open("images/q2/1/W.P. Labuan_heatmap.png")],caption=['Correlation heatmap of Sarawak','Correlation heatmap of W.P. Labuan'])

if option == '2':
	st.title('2. Clustering states into several zones according to the attention level needed from the aspects of active cases rate and vaccination rate.')
	st.write('The current active cases rate at each state was calculated by subtracting the death and recovered cases from the total cases and then dividing by the population of the state. The same division was also carried out to obtain the vaccination rate at each state. Then, clustering technique was performed based on the dataframe and the result is displayed below. ')
	st.write('There are two zones clustered. It is observed that most of the states are clustered in Zone 0 where the vaccination rate is below 80% regardless of the active cases rate. This is because the difference between the lowest and the highest active cases rate is only around 1%. These states required more attention as the vaccination rate is lower compared to the other states. Next, Kuala Lumpur and Putrajaya are in Zone 1 where the vaccination rate is above 120% while the active cases rate is low (below 0.4%). This can be stated as the green zone due to high vaccination rate and low active cases rate.')
	st.image(Image.open("images/q2/2/zone.png"),caption='Clustering of states')
	
if option == '3':
	st.title('3. What are the strong features to death cases for Selangor, Sarawak, Sabah and Johor?')
	
	# selangor
	st.write('In this question, the strong features of the states are selected based on the correlation and mutual information score. From the heatmap and the mutual information displayed below, we can see that cases_new, hospital_admitted_covid, hospital_discharged_covid, daily_vaccination all have strong correlation and high mutual information score.Thus, they are selected as the strong features for Selangor.')
	st.image(Image.open("images/q2/3/Selangor_features.png"),caption='Correlation heatmap and mutual information importance of features in Selangor')
	
	# sarawak
	st.write('Moving on to Sarawak, from the heatmap and mutual information importance displayed below, we can conclude that cases_new, pkrc_discharged_covid, pkrc_covid are the strong features for Sarawak due to their strong correlations and high mutual information score. On the other hand, deaths_new is not taken because it has relatively weak score in correlation and mutual information.')
	st.image(Image.open("images/q2/3/Sarawak_features.png"),caption='Correlation heatmap and mutual information importance of features in Sarawak')
	
	# sabah
	st.write('As for Sabah, the heatmap and mutual information displayed below, we can conclude that hospital_admitted_covid, hospital_discharged_covid, icu_covid and daily_vaccination are the strong features because these features contain strong correlations which are higher than 0.7 and mutual information score more than 0.5.')
	st.image(Image.open("images/q2/3/Sabah_features.png"),caption='Correlation heatmap and mutual information importance of features in Sabah')	
	
	# johor
	st.write('As for Johor, the heatmap and mutual information displayed above, we can conclude that cases_new, hospital_admitted_covid, hospital_discharged_covid, daily_vaccination are the strong features because these features contain strong correlations.')
	st.image(Image.open("images/q2/3/Johor_features.png"),caption='Correlation heatmap and mutual information importance of features in Johor')
		
if option == '4':
	st.title('4. Is it possible to predict the recovered cases for Selangor, Sarawak, Sabah and Johor after the vaccination took place for two weeks? (2 regression models)')
	st.write('Due to different strong features being selected according to the correlation and mutual information score with the feature ‘cases_recovered’, the datasets were separated into different states too and further splitted into training and testing sets. Data normalization was also carried out on the features to scale the data between 0 and 1. Regression models were used to predict the recovered cases because it is a continuous value. The argument of n_estimators of Random Forest Regressor was set to 1000 while the depth of the Decision Tree Regressor was selected between 1 to 10 which the minimum depth produced the least Root-Mean-Squared Error (RMSE) and highest accuracy. ')
	st.write('The accuracy and the RMSE of different models for the four states is shown below. It is observed that Random Forest Regressor performed better for Selangor, Sarawak and Johor because the accuracy is above 75% which is higher than the Decision Tree Regressor. However, the RMSE of Selangor was much higher than the remaining states which is around 1000 for both models. As RMSE calculates the difference between the values predicted and observed, we can say that the predicted recovered cases of Selangor contained more false predictions compared to the other states. The accuracy of both models in Sabah is only around 60% while the RMSE is approximately 500.')
	st.write('By using accuracy and RMSE as the model evaluation, we can conclude that it is possible to predict the recovered cases by Random Forest Regressor in Sarawak and Johor with a higher accuracy. For Selangor and Sabah, it might not be accurate to predict the recovered cases due to low accuracy or high RMSE despite another evaluation being good. ')
	st.image(Image.open("images/q2/4/regression_result.png"),caption='Result graphs for regression models')

if option == '5':
	st.title('5. What are the features that are more relevant to being symptomatic to Covid-19?')
	st.write('In order to accurately classify positive cases into symptomatic cases or asymptomatic cases. We must first conduct feature extraction so that the model that we will be building will have the best possible features to train our model with. In this feature selection, we used Boruta and also Recursive Feature Elimination (RFE) to select the best features to train our model with. ')
	st.write('As shown in the Figure below, results obtained from Boruta shows that all of the features are relevant. So in order to increase the accuracy of the feature selection, we also took into consideration the results obtained from using RFE feature selection. Using RFE, we can see that the features ‘cluster’, ‘district’, ‘age’ and ‘malaysian’ are most relevant when classifying if the case is symptomatic or not. Thus, we took the features which are both relevant when conducting feature selection with Boruta and RFE which are ‘cluster’, ‘district’, ‘age’ and ‘malaysian’ to train our classification model.')
	st.image(Image.open("images/q2/5/features_selected.png"),caption='Features selected for classification models')
	
if option == '6':
	st.title('6. Is it possible to predict whether a person is showing the symptoms after he tested positive for Covid-19? (2 classification models)')
	st.write('First, we check whether the data are imbalance to decide the necessary of data imbalance treatment. The countplot is shown below and it indicates that the data are quite balanced, thus no data imbalance treatment needed. ')
	st.image(Image.open("images/q2/6/countplot.png"),caption='Countplot of the symptomatic feature')

	st.write('Then, we will use the features that we have selected above using Boruta and RFE which are ‘cluster’, ‘district’, ‘age’ and ‘malaysian’ to train our classification model. We will be using 2 classification models namely, Random Forest Classifier (RF) and Decision Tree Classifier (DTC). In order to select the optimum number of depth for the DTC, we tested the number of depth with values from 1 to 10 and used the number of depth with the higher accuracy. Then, both models were trained with the training set and their Receiver Operating Characteristic (ROC) Curve and Area Under the Curve (AUC) were recorded as shown in the figure below. ')
	st.write('We can conclude that it is possible to predict whether a person is showing the symptoms after he tested positive for Covid-19 because both classification models produce the AUC of more than 70%. DTC performs slightly better than RF as it produces more AUC which is 0.7477.')
	st.image(Image.open("images/q2/6/roc_auc.png"),caption='ROC and AUC graphs')

if option == '7':
	st.title('7. What is the probability of someone being brought-in-dead if they have comorbidities?')
	st.write('According to our question, we need to look at the association rule in which the antecedent is the person having comorbidities and the consequent is the person being brought-in-dead. So, the second rule is the rule we need. The support score is only 0.115504 which means that someone having comorbidities is very unlikely to be brought-in-dead. The confidence score of 0.154308 shows that this rule is not strong. For all cases that are having comorbidities, only around 15% of the people are brought-in-dead. In the other word, most people that have comorbidities are not likely to be brought-in-dead.')
	st.image(Image.open("images/q2/7/rules.png"),caption='Association Rule Mining(1)')

if option == '8':
	st.title('8. What is the probability of someone involved in a cluster if they are from Selangor?')
	st.write('According to our question, we need to look at the association rule which the antecedent is whether the person is from Selangor and the consequent is whether the person is involved in a cluster. So, the first rule is the rule we need. The support score is only 0.038 which means that the number of cases that a person from Selangor is involved in a cluster is very unlikely to happen among all the positive cases. The confidence score of 0.13 shows that this rule is not strong. For all the positive cases in Selangor, only around 13% of the people are involved in a cluster. In the other word, most of the positive cases in Selangor are individual cases and not involved in a cluster.')	
	st.image(Image.open("images/q2/8/rules.png"),caption='Association Rule Mining(2)')

if option == '9':
	st.title('9. When will the 80% vaccination rate be achieved?')
	st.write('Since we have the vaccination information from February 2021 to the end of September 2021, we decided to predict whether the 80% vaccination rate(at least one dose) can be achieved in October or November. From the time-series data of vaccination rate, we prepared the dataset by looking at the vaccination rate 30 days before the day. From the dataset, we used the last 30 days as our testing data.')
	st.write('As shown in the left figure below, the Long-Short Term Memory (LSTM) model successfully predicted the vaccination rate close enough to the real vaccination rate. Thus, we used the model to predict the vaccination rate for the next 60 days from the end of September, which is until the end of November. The prediction is shown as the figure at the right. It is observed that the 80% vaccination rate can be achieved roughly 30 days after the end of September, which is the end of October. ')
	st.image([Image.open("images/q2/9/test_vaccination.png"),Image.open("images/q2/9/forecast_vaccination.png")],caption=['Prediction and groundtruth of vaccination rate in test set','Prediction of vaccination rate for the next 60 days'])
