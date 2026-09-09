# workshop_API

API em FastAPI que gera números aleatórios sob demanda. O projeto foi feito como exercício de workshop para mostrar a diferença entre **compartilhar dados por arquivo** e **compartilhar dados por API**.

---

## O que ela faz

O servidor expõe um endpoint. Cada vez que alguém acessa esse endpoint, a aplicação sorteia um número inteiro entre 1 e 95 e devolve como resposta.

A ideia do exercício: em vez de um programa escrever num arquivo `.txt` e outro ficar lendo esse arquivo (com todos os problemas de concorrência e acoplamento que isso traz), um programa **serve** o dado e qualquer cliente **consome** via HTTP.

---

## Estrutura do projeto

```
workshop_API/
├── main.py            # o servidor FastAPI
├── cliente.py         # script que consome a API
├── programa_A.py      # versão antiga: escreve números num arquivo
├── programa_B.py      # versão antiga: lê o arquivo
├── recursos/          # onde ficava o arquivo compartilhado
├── requirements.txt   # dependências do projeto
└── .gitignore
```

---

## Pré-requisitos

- Python 3.10 ou superior
- `pip` (já vem com o Python)

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/eudesfh/workshop_API.git
cd workshop_API
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente

**Windows (Git Bash):**
```bash
source .venv/Scripts/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

Quando der certo, aparece `(.venv)` no início do prompt.

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

Esse comando lê o `requirements.txt` e instala tudo de uma vez. As dependências principais são `fastapi`, `uvicorn` e `requests`.

---

## Rodando a API

Com o ambiente ativado:

```bash
uvicorn main:servidor --reload
```

Entendendo o comando:

| Parte | Significado |
|---|---|
| `main` | nome do arquivo, **sem** o `.py` |
| `servidor` | nome da variável `FastAPI()` dentro do arquivo |
| `--reload` | reinicia o servidor sozinho quando você salva o código |

> Atenção: não pode haver espaço em `main:servidor`. Se escrever `main: servidor`, o uvicorn reclama de argumento extra.

Se subir corretamente, aparece no terminal:

```
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Para parar o servidor: `CTRL+C`.

---

## Usando a API

Com o servidor rodando, abra no navegador:

| URL | O que é |
|---|---|
| http://127.0.0.1:8000/recursos | o endpoint, devolve um número novo a cada acesso |
| http://127.0.0.1:8000/docs | documentação interativa (Swagger), gerada automaticamente |

O `/docs` é o jeito mais prático de testar: dá para disparar a requisição direto pelo navegador, sem escrever código.

### Endpoint

**`GET /recursos`**

Resposta (`200 OK`):

```json
42
```

O número também é impresso no terminal onde o uvicorn está rodando, por causa do `print(num)` dentro da função.

---

## Consumindo pelo cliente

O `cliente.py` faz a requisição via Python:

```python
import requests

URL = "http://127.0.0.1:8000/recursos"

response = requests.get(URL)
print(response.text)
```

Com o servidor rodando, abra **um segundo terminal**, ative o ambiente e execute:

```bash
python cliente.py
```

O servidor precisa continuar rodando no primeiro terminal. Se fechar, o cliente devolve erro de conexão.

---

## Deploy no Render

Para publicar a API e acessá-la de fora da sua máquina:

1. Suba o projeto para o GitHub (o `requirements.txt` precisa estar commitado)
2. No Render, crie um **New Web Service** e conecte o repositório
3. Configure:

| Campo | Valor |
|---|---|
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:servidor --host 0.0.0.0 --port $PORT` |

Duas diferenças em relação ao ambiente local:

- **`--host 0.0.0.0`** — sem isso o servidor só aceita conexões da própria máquina, e o Render não consegue expor a aplicação
- **`--port $PORT`** — o Render define a porta por variável de ambiente; não dá para fixar a 8000
- **sem `--reload`** — é uma opção de desenvolvimento e não deve ir para produção

Depois do deploy, é só trocar a URL no `cliente.py` pelo endereço que o Render gerar:

```python
URL = "https://seu-app.onrender.com/recursos"
```

> No plano gratuito o serviço hiberna após um período sem uso. A primeira requisição depois disso demora alguns segundos para responder.

---

## Atualizando o requirements.txt

Sempre que instalar um pacote novo, regenere o arquivo:

```bash
pip install <pacote>
pip freeze > requirements.txt
```

O `pip freeze` lista tudo que está instalado **no ambiente ativo** — por isso o `.venv` precisa estar ativado, senão ele pega os pacotes globais ou gera um arquivo vazio.

---

## Observações

A pasta `.venv` está no `.gitignore` e não vai para o repositório. Cada pessoa cria o próprio ambiente a partir do `requirements.txt`.

Os arquivos `programa_A.py` e `programa_B.py` são a versão anterior do exercício, que trocava dados gravando e lendo um arquivo em `recursos/`. Ficaram no repositório para comparação com a abordagem via API.