import math 

# Measurement Update Function
def update(m1, s1, m2, s2):
    m = (1./(s1+s2))*((s2*m1) + (s1*m2))
    s = 1./((1./s1) + (1./s2))
    return m,s 

# Motion Prediction Function 
def predict(m1, s1, m2, s2):
    m = m1+m2 
    s = s1+s2 
    return m,s 

measurements = [5. ,6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4 
motion_sig = 2 

# Prior assumptions 
mu = 0
sig = 10000

for i in range(len(measurements)):
    mu, sig = update(mu, sig, measurements[i], measurement_sig)
    print(f"Update: mu: [{mu}] sig: [{sig}]")
    mu, sig = predict(mu, sig, motion[i], motion_sig)
    print(f"Predict: mu: [{mu}] sig: [{sig}]")