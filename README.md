<h1> Desenrola — Grupo 5</h1>

Projeto acadêmico desenvolvido pelo Grupo 5 da PUC-Rio. O Desenrola é uma aplicação web voltada à conexão entre pessoas interessadas em compartilhar e aprender habilidades.


<h2>Integrantes:</h2>

Riccardo	Bonuccelli;

Kauã Lagoas;

Pedro Werner;

Pedro Araujo;

Pedro Lilienthal.


<h2>Tecnologias utilizadas</h2>
- Python: lógica e processamento no back-end.
- Django: framework para desenvolvimento da aplicação web.
- HTML e CSS: estrutura e estilização das páginas.
- Git e GitHub: versionamento, revisão e colaboração.
- Lovable: apoio à prototipação de interfaces.
- Banco de dados relacional: persistência das informações gerenciadas pela aplicação Django (verificar o mecanismo configurado em settings.py).

  
<h2>Funcionalidades</h2>

O projeto contempla, em diferentes etapas de implementação:

- Cadastro e autenticação de usuários.
- Visualização de perfis e habilidades.
- Registro de habilidades oferecidas e procuradas.
- Solicitação e acompanhamento de trocas entre usuários.
- Chat interno vinculado às trocas.
- Avaliação das experiências realizadas.
  
As funcionalidades listadas representam o escopo da aplicação e podem estar em diferentes estágios de integração ou conclusão.


Estrutura de pastas
A tabela abaixo apresenta os principais diretórios identificados na raiz do repositório, sem incluir toda a estrutura interna do Django.
Pasta ou arquivo	Finalidade
Calculadora/	Materiais e implementação da calculadora
Entrevista/	Registros de entrevistas
Estratégia para atrair usuários/	Planejamento de atração de usuários
HTML/	Páginas HTML
Identidade do Desenrola/	Identidade visual do projeto
Login HTML/	Protótipos de login
Lovable/	Protótipos e referências de telas
Modelagem do site/	Diagramas de modelagem
Pesquisa/	Materiais de pesquisa
Projeto Desenrola Django/	Aplicação Django
Protótipo visual em HTML+CSS/	Protótipos de interface
Teste/	Materiais de teste
docs/	Imagens do README (a adicionar)
.gitignore	Arquivos ignorados pelo Git
README.md	Documentação principal


Também há no repositório a pasta Projeto Desenrola Django.errado, mantida no histórico atual. Antes de uma limpeza, é necessário verificar se ela contém arquivos que ainda serão aproveitados.

No Django, os principais arquivos a localizar são:
- manage.py: execução de comandos administrativos e inicialização do servidor.
- settings.py: configurações do projeto, aplicativos e banco de dados.
- urls.py: definição das rotas.
- models.py: modelagem das entidades da aplicação.
- views.py: tratamento das requisições e lógica das páginas.
- templates/ e static/: páginas HTML, estilos e outros recursos, quando presentes.

  
<h2>Modelagem do banco de dados</h2>

<img width="1086" height="712" alt="image" src="https://github.com/user-attachments/assets/6bfa76ae-1dd8-4d9a-a839-b23c39a7f8dc" />

O diagrama apresenta as entidades USUARIO, HABILIDADE, USUARIO_HABILIDADE, TROCA, MENSAGEM e AVALIACAO, incluindo suas chaves primárias e estrangeiras. A tabela intermediária USUARIO_HABILIDADE relaciona usuários às habilidades, enquanto as mensagens e avaliações se vinculam às trocas.


<h2>Como executar o projeto</h2>

Pré-requisitos: Python, pip e Git instalados.

1. Clone o repositório:
   git clone https://github.com/PedroFL1211/GRUPO-5.git
   cd GRUPO-5
2. Entre na pasta do projeto Django que contém o arquivo manage.py:
   cd "Projeto Desenrola Django"
   Caso o arquivo manage.py esteja em uma subpasta, navegue até ela antes de prosseguir.
3. Crie e ative um ambiente virtual:
   python -m venv .venv
   No Windows (PowerShell):
   .\.venv\Scripts\Activate.ps1
   No Linux/macOS:
   source .venv/bin/activate
4. Instale as dependências:
   pip install -r requirements.txt
   Esse comando pressupõe a existência de requirements.txt na pasta de execução. Se ainda não houver esse arquivo, as dependências do projeto deverão ser identificadas e documentadas antes da instalação.
5. Aplique as migrações e execute o servidor:
   python manage.py migrate
   python manage.py runserver
6. Acesse, normalmente, http://127.0.0.1:8000/ no navegador.

   
<h2>Como criar e popular o banco de dados</h2>

Com o ambiente virtual ativo e estando no diretório do manage.py:

1. Para gerar migrações após alterações nos modelos (quando necessário):
   python manage.py makemigrations
2. Para criar ou atualizar a estrutura do banco:
   python manage.py migrate
3. Para criar um usuário administrador:
   python manage.py createsuperuser
4. Para popular com dados de exemplo: se o projeto disponibilizar um arquivo de fixture JSON (por exemplo, dados_iniciais.json), será possível importá-lo com:
   python manage.py loaddata dados_iniciais.json
   Atenção: dados_iniciais.json é um nome ilustrativo. O comando de importação só funcionará se o arquivo existir e for compatível com os modelos. Criar o banco com migrate não significa preenchê-lo automaticamente com dados de exemplo. Se houver um comando de seed próprio do grupo, documentar aqui seu nome verdadeiro.

   
<h2>Organização e fluxo de trabalho</h2>

O desenvolvimento é realizado de forma colaborativa, com tarefas distribuídas entre os integrantes e acompanhamento por sprints. As atividades abrangem planejamento, pesquisa, prototipação, desenvolvimento, integração, testes e documentação.

O GitHub é utilizado para centralizar os arquivos e registrar a evolução das entregas. O fluxo de trabalho adotado inclui:
1. Definição das tarefas e dos responsáveis por sprint.
2. Desenvolvimento das funcionalidades em branches de trabalho.
3. Registro das alterações por commits com mensagens descritivas.
4. Abertura de pull requests para integração das contribuições.
5. Revisão, testes e atualização da documentação antes da incorporação à branch principal.
Estado do projeto
Em desenvolvimento acadêmico. A documentação de instalação e de população do banco deve ser conferida com os arquivos efetivamente presentes na versão final da aplicação.

**Desenrola, Ninguém Sabe Tudo**
