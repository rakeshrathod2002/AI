import streamlit as st
import joblib,os
import pickle


# Loading Models
def load_prediction_model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))


def main():
    st.title("Predicting CoVid19 Recovery Rate")
    
    active_cases = st.text_input("Active CoVid Cases")
    active_deaths = st.text_input("Active Deaths")
    death_rate = st.text_input("Death Rate")
    
    if st.button("Predict"):
            model = pickle.load(open('linearmodel.pkl', 'rb'))
            predictions = model.predict([[active_cases, active_deaths, death_rate]])
            st.success("Predicted Recovery Rate is {}%".format(round(predictions[0], 4)))
            
if __name__ == '__main__':
    main()