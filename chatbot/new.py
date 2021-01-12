import pickle


infile=open('classes.pkl','rb')
print(pickle.load(infile))