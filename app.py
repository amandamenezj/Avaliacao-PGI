from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def ():

"""Página inicial!"""
    return render_template ('/')

@app.route('/index.html', methods = ['GET', 'POST'])
def card_header():
    erros = []
    resultado = None
    mb_3 = {
       'nome' : '',
       'peso' : '',
       'altura' : ''
    }

if request.method == 'POST':
    nome = request.form.get('nome', '').strip()
    peso = request.form.get('peso', '').strip()
    altura = request.form.get('altura', '').strip()

    mb_3['nome']= nome
    mb_3['peso']= peso
    mb_3['altura']= altura

nome = None
peso = None
altura = None

if not nome:
    erros.append('Informe o seu nome:')    
 else:
        erros.append('Nome inválido')

if not peso:
    erros.append('Informe o seu peso:')
 else:
        try:
            peso = float(peso)
            if peso > 1 or peso < 300:
                erros.append('Número inválido')
        except ValueError:
                    erros.append('Numero deve ser float!')


if not altura:
    erros.append('Informe a sua altura:')
 else:
        try:
            altura = float(altura)
            if altura > 0.5 or altura < 2.5:
               erros.append('O peso inserido é inválido')
        except ValueError:
                    erros.append('Numero deve ser float!')
if not erros:
    mb_1 = (peso / altura) * altura

    if mb_0 < 18.5:
        faixa = 'abaixo do peso'
        classe_alerta = 'alert-info'
        icone = '🔵'
    elif 18.5 >= mb_0 < 25:
        faixa = 'peso normal'
        classe_alerta = 'alert-success'
        icone = '🟢'
    elif 25 >= mb_0 < 30:
        faixa = 'Sobrepeso'
        classe_alerta = 'alert-warning'
        icone = '🟡'
 else:
            faixa = 'Obesidade'
            classe_alerta = 'alert-danger'
            icone = '🔴'


            mb_1 = {
                'nome': nome,
                'peso': peso,
                'altura': altura,
                'mb_1': mb_1,
                'mb_0': mb_0,
                'faixa': faixa,
                'classe_alerta': classe_alerta,
                'icone': icone
            }
            
    return render_template('index.html',erros = erros,mb_1 = mb_1, mb_3 = mb_3, nome = nome, peso = peso, altura = altura, faixa = faixa, classe_alerta = classe_alerta, icone = icone)
                
@app.route('/equipe.html')
def ():

"""Página sobre a equipe!"""
    return render_template ('equipe.html')


if __name__ == '__main__':
    app.run(debug=True)
