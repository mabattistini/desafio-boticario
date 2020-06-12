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



