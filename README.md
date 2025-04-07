# MCP Log Server

Este servidor MCP fornece acesso a arquivos de log armazenados no Amazon S3, implementado usando o framework MCP e FastMCP.

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
Crie um arquivo `.env` com as seguintes variáveis:
```
AWS_ACCESS_KEY_ID=seu_access_key
AWS_SECRET_ACCESS_KEY=seu_secret_key
AWS_REGION=sua_regiao
S3_BUCKET_NAME=nome_do_bucket
```

3. Execute o servidor:
```bash
python log.py
```

## Recursos MCP

O servidor expõe um recurso MCP chamado "logs" com as seguintes operações:

- `list_logs`: Lista todos os arquivos de log disponíveis
- `get_log_content`: Obtém o conteúdo de um arquivo de log específico
- `search_logs`: Pesquisa nos arquivos de log com filtros de data

## Endpoints FastMCP

- `GET /logs`: Lista todos os arquivos de log disponíveis
- `GET /logs/{filename}`: Obtém o conteúdo de um arquivo de log específico
- `GET /logs/search`: Pesquisa nos arquivos de log (query params: query, start_date, end_date)

## Uso via MCP Client

```python
from mcp.client import MCPClient

client = MCPClient()
logs = client.get_resource("logs")

# Listar logs
all_logs = await logs.list_logs()

# Obter conteúdo de um log
content = await logs.get_log_content("example.log")

# Pesquisar nos logs
results = await logs.search_logs(
    query="error",
    start_date="2024-01-01",
    end_date="2024-01-31"
)