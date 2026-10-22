# fastapi-ci-lab

![CI](https://github.com/SEU_USUARIO/fastapi-ci-lab/actions/workflows/ci.yml/badge.svg)

API FastAPI usada para praticar Integração Contínua com GitHub Actions: o pipeline testa cada push e cada Pull Request, e a branch `main` só aceita merge com os testes verdes.

## Problemas

Código com bug chegando na branch principal. O CI funciona como uma barreira automática antes do merge.

## Arquitetura

```
git push / Pull Request
        |
        v
GitHub Actions (job: verificar-api)
  1. checkout
  2. setup-python (matriz 3.10 / 3.11 / 3.12)
  3. pip install -r requirements.txt
  4. pytest
  5. sobe a API + curl (teste de integração)
        |
        v
Merge liberado somente se tudo passar
```

## Como rodar

```bash
docker compose up
```

A API sobe em http://localhost:8000 (documentação em `/docs`).

Sem Docker:

```bash
pip install -r requirements.txt
fastapi run main.py --port 8000
pytest -v
```

## Rotas

| Método | Rota | Resposta |
|--------|------|----------|
| GET | `/` | `{"status": "ok"}` |
| GET | `/somar/{a}/{b}` | `{"resultado": a + b}` |

## Screenshots

Adicione aqui os prints da aba Actions (execução verde, execução com falha e PR bloqueado) em `docs/`.

## Roadmap

- [x] Pipeline de testes com pytest
- [x] Proteção da branch `main`
- [x] Matriz de versões do Python
- [x] Teste de integração com curl
- [ ] Cobertura de testes no CI
- [ ] Deploy automático após o merge

## Licença

MIT
