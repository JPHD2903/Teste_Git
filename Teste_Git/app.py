from flask import Flask, jsonify, request #importando a biblioteca, rqueste permite acessaros dados que estão indo e vindo, jsonfy é o formato experado de um flask 

app = Flask(__name__) # criando uma aplicação com o nome do arquivo atual

#precisamos de um BD, vamos usar um dicionário
livros = [
    {   #oq eu quero dos livros
        'id': 1,
        'título': 'O nome do Vento',
        'autor': 'Tolkie'
    },
    {   #oq eu quero dos livros
        'id': 2,
        'título': 'A sutil arte do fodasse',
        'autor': 'Lucas'
    },
    {   #oq eu quero dos livros
        'id': 3,
        'título': 'Harry Potter',
        'autor': 'Lira'
    }
]

#Consultar - todos -> precisamos de uma função para cada
@app.route('/livros',methods=['GET']) #isso vai deixar como api, preciso da rota para ativar essa função/O methods=['GET'] faz com que caso eu faça a requisição, ela aceite somente o método get
def obter_livros():
    return jsonify(livros)

#Consultar - id
@app.route('/livros/<int:id>',methods=['GET']) #estou esperando um valor em inteiro e garantindo um método e consulta
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id: #Estou entrando na lista (livro) e procurando (get) a propriedde com o nome de id e retorno ovalor dessa propriedade/Nesse if eu estou fazendo, se o id for igual o id informado, então retorne o livro informado   
            return jsonify(livro) 
#Editar 
@app.route('/livros/<int:id>',methods=['PUT']) #Somente métodos para editar
def editar_livro_id(id):
    livro_mudado = request.get__json()
    for indice,livro in enumerate(livros): #indicando qual livro devo editar através de um indice
        if livro.get('id') == id:
            livros[indice].update(livro_mudado)
            return jsonify(livros[indice])

#Criar
@app.route('/livros',methods=['POST'])
def criar_livro():
    novo_livro = request.get__json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True) #quado abrir o local host coloca a rota Ex.: localhost:5000/livros
