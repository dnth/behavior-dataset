# behavior-dataset
Dataset for behavior recognition on NAO robot. 

Dataset is divided into 6 different behavior classes:
 1. Ball Lift
 2. Ball Roll
 3. Bell Ring Left
 4. Bell Ring Right
 5. Ball Roll Plate
 6. Ropeway
 
Each in their own respective folders.
For each behavior class, there are 10,000 timesteps of continuous sampling on the joints of NAO robot while performing the behavior. You can partition the data into many samples in order to train your neural network architecture. I have personally tested partitioning them into 100 timesteps and 200 timesteps. Both works ok. 

I have tested using the dataset on MLP, RNN and LSTM architecture. Best results obtained by LSTM. I will post my publication soon. 
