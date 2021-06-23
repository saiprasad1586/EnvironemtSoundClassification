import librosa
import librosa.display
from tensorflow.keras.models import load_model
import numpy as np

class Result:
    def __init__(self,filename):
        self.file_name = filename
        self.model = load_model('model.h5')

    def getResult(self):
        sig, sr = librosa.load(self.file_name)
        for i in range(3):
            n = np.random.randint(0, len(sig) - (sr * 2))
            sig_ = sig[n : int(n + (sr * 2))]
            mf = librosa.feature.mfcc(sig_,sr=sr,n_mfcc=13)
        mf = mf.reshape(1,mf.shape[0],mf.shape[1],1)
        prediction = self.model.predict_classes(mf)
        return prediction

def main():
    file_name = '1-100032-A-0.wav'
    res = Result(file_name)
    print(res.getResult())

if __name__ == '__main__':
    main()