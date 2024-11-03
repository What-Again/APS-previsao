
from flask import Flask, request, render_template
import pickle
import numpy as np #numpy 1.19.5

app = Flask(__name__)

# Carregar o modelo.
model = pickle.load(open('projects/apsPrevisao/model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('aps.html')
#salva informações do formulario no programa.
@app.route('/predict', methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    
    if output>str(0.5):
        return render_template('aps.html',pred='Alta chances de incendios florestais: {}'.format(output),bhai="")
    else:
        return render_template('aps.html',pred='Baixas chances de incendios florestais{}'.format(output),bhai="")




if __name__ == '__main__':
    app.run(debug=True)