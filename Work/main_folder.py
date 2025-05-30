import os 
import librosa
import sklearn
import sklearn.ensemble
import joblib
import sklearn.metrics
class Directory:
    def __init__(self):
        #Input your link fake
        self.link0 =r""
        #Input your link reale
        self.link1 =r""
        self.list_audiofile0 = os.listdir(self.link0 )
        self.list_audiofile1 = os.listdir(self.link1 )
        print(self.list_audiofile0)
    def analysis_global(self):
        self.list_audiofilex = self.list_audiofile0 + self.list_audiofile1
        list_range0, list_range1 = len(self.list_audiofile0), len(self.list_audiofile1)
        list_audiofiley = [0] * list_range0 + [1] * list_range1
        analization_answers = [None] * len(list_audiofiley)
        gb=GB()
        for i in range(len(self.list_audiofilex)):
            folder = "fake" if i < list_range0 else "real"
            #Input your link mainfolder
            audiofile_path = os.path.join(r"", folder, self.list_audiofilex[i])
            audiofile = Audiofile(audiofile_path,gb)
            analization_answers[i] = audiofile.processer_mfcc()
        analization_answers=gb.worker(analization_answers)
        return analization_answers, list_audiofiley

class Audiofile:
    def __init__(self, path,gb):
        self.srr = 16000
        self.local_path = path
        self.gb_object=gb
    def processer_mfcc(self):
        signal, sr = librosa.load(path=self.local_path, sr=self.srr)
        self.y_harmonic, self.y_percussive = librosa.effects.hpss(signal)
        af_mfcc = librosa.feature.mfcc(y=self.y_harmonic, sr=self.srr,n_mfcc=15).tolist()
        mfcc_f=[]
        for i in af_mfcc :
            mfcc_f+=i 
        return mfcc_f
class ML:
    def __init__(self): 
        #Input your link fake
        self.link0 = r''
        #Input your link reale
        self.link1 = r''

    def search_gb(self):
        af_gb = self.link0
        af_gb1 = self.link1
        list_audiofile0 = os.listdir(af_gb)
        list_audiofile1 = os.listdir(af_gb1)
        list_audiofile = list_audiofile0 + list_audiofile1
        learny = [0] * len(list_audiofile0) + [1] * len(list_audiofile1)
        len_list_audiofile = len(list_audiofile)
        learnx = [None] * len_list_audiofile
        for i in range(len_list_audiofile):
            if i >= len(list_audiofile0):
                path = os.path.join(self.link1, list_audiofile1[i - len(list_audiofile0)])
            else:
                path = os.path.join(self.link0, list_audiofile0[i])
            audiofile = Audiofile(path,None)
            learnx[i] = audiofile.processer_mfcc()

        return learnx, learny
    @staticmethod
    def save(object_ML, filename):
        joblib.dump(object_ML, filename)

    @staticmethod
    def load(filename):
        if os.path.exists(filename):
            try:
                return joblib.load(filename)
            except EOFError:
                print(f"Error: The file {filename} seems to be untrained or corrupted.")
                return None
        else:
            print(f"Error: The file {filename} does not exist or not found.")
            return None
class GB:
    def __init__(self):
        self.path_learn = 'MLGB.pkl'
        self.gb_object = sklearn.ensemble.GradientBoostingClassifier(max_depth=9,                                 
                                           max_features=20, 
                                           subsample=0.3,
                                           min_samples_split=0.01,   
                                           min_samples_leaf=0.01,
                                           min_weight_fraction_leaf=0,
                                           min_impurity_decrease=0,
                                           max_leaf_nodes=61,                                          
                                           learning_rate=0.25, 
                                           n_estimators=800,
                                           random_state=84)
        self.load_model()
    def load_model(self):
        saved_model = ML.load(self.path_learn)
        if saved_model is not None:
            self.gb_object = saved_model
        else:
            self.learning()

    def learning (self):
        ml_object=ML()
        learnGB_x, learnGB_y = ml_object.search_gb()
        self.gb_object.fit(learnGB_x, learnGB_y)
        ML.save(self.gb_object, self.path_learn)

    def worker(self, work):
        return self.gb_object.predict(work)

def main():
    directory = Directory()
    y_pred,y_true=directory.analysis_global()
    print(sklearn.metrics.accuracy_score(y_true=y_true,y_pred=y_pred))
if __name__ == "__main__":
    main()
