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
AWS_ENDPOINT_URL="http://localhost:9000"
```

3. Execute o servidor:
```bash
uv run server.py
```