import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle

#previne que avisos parem o programa de ser executado
warnings.filterwarnings("ignore")

#le os dados salvos banco de dados salvo no arquivo .csv e os salva em um array.
data = pd.read_csv("apsPrevisao\Forest_fire.csv")
data = np.array(data)

#treina o modelo de machine learning usando sklearn

X = data[1:, 1:-1]
y = data[1:, -1]
y = y.astype('int')
X = X.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()

log_reg.fit(X_train, y_train)

inputt=[int(x) for x in "45 32 60".split(' ')]
final=[np.array(inputt)]

b = log_reg.predict_proba(final)

#pickel serializa os dados analisados e os salva no model.pkl
pickle.dump(log_reg,open('apsPrevisao\model.pkl','wb'))
model=pickle.load(open('apsPrevisao\model.pkl','rb'))