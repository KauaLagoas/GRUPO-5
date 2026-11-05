# Sprint 8 — Chat interno do Desenrola

Implementação Django de um chat simples entre dois usuários autenticados.

## O que foi entregue

- Tabela `chat_mensagem`: remetente, destinatário, texto e data/hora.
- Views de lista de usuários e conversa privada.
- Rotas `/chat/` e `/chat/<id-do-usuario>/`.
- Templates HTML e CSS separado, em múltiplas linhas e responsivo.
- Migração do banco e seis testes automatizados.
- Integração às configurações e rotas do projeto existente.
- Correção do conflito de merge que já existia em `manage.py`.

O remetente é sempre obtido da sessão autenticada. Cada usuário só visualiza mensagens trocadas entre ele e a pessoa selecionada. Textos vazios ou acima de 2.000 caracteres são recusados; os formulários usam CSRF e o HTML das mensagens é escapado.

## Como integrar

Copie o conteúdo deste pacote para a raiz do repositório GRUPO-5, preservando a pasta `Projeto Desenrola Django`. Os únicos arquivos existentes alterados são `manage.py`, `Desenrola/settings.py` (inclusão de `chat`) e `Desenrola/urls.py` (rotas do chat e autenticação). Se esses arquivos tiverem sido alterados pela equipe depois de 04/11/2026, aplique somente essas mudanças em vez de sobrescrevê-los.

O chat usa as contas `django.contrib.auth`, as mesmas usadas pelo login Django. A tabela personalizada `Desenrola.Usuario` é separada; seus IDs não devem ser usados como IDs das contas do chat.

## Executar no Windows

Dentro de `Projeto Desenrola Django`:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abra `http://127.0.0.1:8000/admin/`, entre com o superusuário e crie duas contas em Users/Usuários, definindo suas senhas. Use contas fictícias para testar.

1. Em uma janela normal, acesse `http://127.0.0.1:8000/accounts/login/?next=/chat/` e entre com a primeira conta.
2. Em uma janela anônima, abra a mesma URL e entre com a segunda conta.
3. Escolha o outro usuário e envie uma mensagem.
4. Na outra janela, clique em **Atualizar conversa** para recebê-la e responder.

O recebimento exige atualizar a página; esta versão não utiliza WebSocket nem atualização automática. Exibe as 100 mensagens mais recentes; as anteriores continuam no banco. Não contém anexos nem confirmação de leitura. O cadastro e os demais fluxos existentes do site não foram reimplementados.

Para ligar a outra tela Django ao chat:

```html
<a href="{% url 'chat:lista' %}">Mensagens</a>
```

## Verificar

```powershell
python manage.py test chat
python manage.py check
```

Validado com Django 5.2: seis testes passaram (login, envio e persistência, privacidade, validação, CSRF e escape de HTML). O projeto já apresenta um aviso sobre a chave primária de `Desenrola.Usuario`, sem impedir os testes. A aparência não foi verificada em navegador.

## Colocar no GitHub

Crie uma branch e copie os arquivos antes dos comandos:

```powershell
git switch -c feat/chat-interno
 git add "Projeto Desenrola Django/chat" "Projeto Desenrola Django/Desenrola/settings.py" "Projeto Desenrola Django/Desenrola/urls.py" "Projeto Desenrola Django/manage.py" "Projeto Desenrola Django/CHAT_README.md"
git commit -m "Implementa chat interno entre usuarios"
git push -u origin feat/chat-interno
```

Depois abra um Pull Request no GitHub para a branch principal. Não adicione `.venv`, `__pycache__` nem `db.sqlite3`. A migração `chat/migrations/0001_initial.py` deve ser versionada.

Título sugerido: **Sprint 8: implementar chat interno entre dois usuários**.

Descrição sugerida: Implementa mensagens persistidas, lista de usuários, conversa privada, rotas e telas com CSS separado. Integra o chat à autenticação Django e corrige o conflito em manage.py. Validação: seis testes automatizados passaram. Recebimento por atualização manual da página.
