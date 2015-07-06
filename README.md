# short behavior dataset
Dataset for behavior recognition on NAO robot. Behavior are adapted from [1]

Dataset is divided into 6 different behavior classes:
 1. Ball Lift
 2. Ball Roll
 3. Bell Ring Left
 4. Bell Ring Right
 5. Ball Roll Plate
 6. Ropeway
 
Each in class of behaviors are in their own respective folders.
In my research, I have used the dataset for classifications of behaviors on NAO robot [2].

The behavior data is saved in a .txt file. In each .txt file, there are 10000 rows and 10 columns. The number of rows represents the number of samples. The columns represents the joint position. In our case we 10 columns that corresponds to ten joints in the following order:

1.  Right Shoulder Pitch (RSP)
2.  Right Shoulder Roll (RSR)
3.  Right Elbow Roll (RER)	
4.  Right Elbow Yaw (REY)
5.  Right Wrist Yaw (RWY)
6.  Left Shoulder Pitch (LSP)
7.  Left Shoulder Roll (LSR)
8.  Left Elbow Roll (LER)
9.  Left Elbow Yaw (LEY)
10. Left Wrist Yaw (LWY)


For each behavior class, there are 10,000 timesteps of continuous sampling on the joints of NAO robot while performing the behavior. You can partition the data into many samples in order to train your neural network architecture. I have personally tested partitioning them into 100 timesteps and 200 timesteps. Both works ok. 

I have tested using the dataset on MLP, RNN and LSTM architecture. Best results obtained by LSTM. I will post my publication soon. 

[1] K. Noda, H. Arie, Y. Suga, and T. Ogata, “Multimodal integration
    learning of robot behavior using deep neural networks,” Robotics and
    Autonomous Systems, vol. 62, no. 6, pp. 721–736, 2014.

[2] D. N. T. How, K. S. M. Sahari, Y. Hu, and L. C. Kiong, “Multiple
sequence behaviour recognition on humanoid robots using long short
term memory (lstm),” in IEEE 2014 International Symposium on
Robotics and Mnufacturing Automation (IEEE-ROMA2014). IEEE,
2014.
