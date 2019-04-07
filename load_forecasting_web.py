
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify
from joblib import load
import numpy as np
import math


# In[2]:


app = Flask(__name__) 
rf = load('load_forecasting_model_v010.joblib') 


# In[3]:


no_of_features = rf.n_features_
print("The number of features that we use is:",no_of_features)


# In[ ]:


@app.route('/forecast')
def forecast():
    lights = request.args.get('lights')
    RH_1 = request.args.get('RH_1')
    RH_2 = request.args.get('RH_2')
    T3 = request.args.get('T3')
    RH_3 = request.args.get('RH_3')
    T4 = request.args.get('T4')
    T5 = request.args.get('T5')
    RH_5 = request.args.get('RH_5')
    RH_7 = request.args.get('RH_7')
    T8 = request.args.get('T8')
    RH_8 = request.args.get('RH_8')
    RH_9 = request.args.get('RH_9')
    T_out = request.args.get('T_out')
    Press_mm_hg = request.args.get('Press_mm_hg')
    Windspeed = request.args.get('Windspeed')
    Visibility = request.args.get('Visibility')
    Tdewpoint = request.args.get('Tdewpoint')
    RH_out = request.args.get('RH_out')
    HI_1 = request.args.get('HI_1')
    
    
    input_params = [lights, RH_1, RH_2, T3, RH_3, T4, T5, RH_5, RH_7, T8, RH_8, RH_9, T_out,
                   Press_mm_hg, Windspeed, Visibility, Tdewpoint, RH_out, HI_1]
    parameters = np.asarray(input_params).reshape(1,-1)
    
    
        
    predicted_value = rf.predict(parameters)
    
    #if parameters.shape[1] != no_of_features:
    #    response = jsonify(rf ='You have enter wrong number of parameters')
    #else:
    response = jsonify(rf='Random Forest',predicted_value=math.exp(predicted_value[0]))
    
    return response

    
if __name__ == '__main__':
    app.run(debug=False, port=9181)

