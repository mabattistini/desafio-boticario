# desafio-boticario
Desafio Desenvolvedor Boticario

Desafiante: Marcelo Angelo C. Battistini

##### Instalação
Após fazer o clone do projeto entra na pasta do mesmo e criar o virtualenv, ativa-lo e instalar as dependencias
````
virtualenv --python=python3 venv 
source venv/bin/activate
pip install -r requirements.txt
````

##### Criação do banco de dados
Para a criação do banco rodar seguir as seguintes etapas.
- rodar shell  banco.sh
- rodar script initDatabase.py (cria o usuário de autenticação do JWT)

##### Rotas
- http://host:5000/revendedor/create - Cadastra um revendedor - POST
- http://host:5000/revendedor/login - Realiza o login do revendedor - POST
- http://host:5000/venda/create - Cadastra uma nova venda  - POST
- http://host:5000/venda/edit - Altera uma venda cadastrada  - POST
- http://host:5000/venda/delete - Exclui uma venda cadastrada - POST
- http://host:5000/venda/list - Lista compras cadastradas  - GET
- http://host:5000/venda/cashback - Lista o acumulado de cashback - GET

##### Scripts de testes
Na pasta scripts contém scripts Python para a realização de testes. São eles:
- auth.py - classe de autenticação do JWT, será criado um token de acesso com tempo de vida de 10 segundos. Caso queira alterar este tempo  basta editar o arquivo config.py alterando o valor da variável TIME_TOKEN_EXPIRATION.
- revendedor_cadastrar.py - cadastra um revendedor no banco
- revendedor_login.py - realiza o login do revendedor
- venda_cadastrar.py - cadastra uma nova venda
- venda_alterar.py - realiza a edição de uma venda cadastrada
- venda_excluir.py - exclui uma venda cadastrada
- venda_lista.py - lista as vendas cadastradas
- cashback_acumulado.py - lista o acumulado de cashback


