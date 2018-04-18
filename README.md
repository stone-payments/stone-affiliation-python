![](https://travis-ci.org/stone-payments/stone-affiliation-python.svg?branch=develop)
# Stone Affiliation
Este pacote contém a implementação de um cliente para a API de Credenciamento da Stone Co. em Python

## Feito com
- Python 3.5 :heart:

## Dependências
É necessário instalar as dependências do projeto via _pip_ que estão descritas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

## How To
Para utilizar o client basta instanciar a classe stone_affiliation.StoneAffiliation e passar os seguintes parâmetros:
- api_url -> Url para a API de Credenciamento
- app_key -> Chave identificadora do cliente
- secret_key -> Chave secreta do cliente

Exemplo:
```python
from stone_affiliation import StoneAffiliation
client = StoneAffiliation(`api_url`, `app_key`, `secret_key`)
service = client.merchant_service(`user_email`, `source_ip`)
merchants = service.list()
```


## Testing
Para rodar todos os testes, execute os seguintes comandos na linha de comando:

*todos os testes*
```
pytest tests
```

*testes de unidade*
```
pytest tests/unit
```

*testes de integração*
```
pytest tests/integration
```

__Será necessário setar algumas váriaveis de ambiente ao rodar os testes de integração__

- API_URL -> Url para a API de Credenciamento
- APP_KEY -> Chave identificadora do cliente
- SECRET_KEY -> Chave secreta do cliente

## Versioning
Por favor, consulte nosso CHANGELOG.

## Distribution
Para gerar novas distribuições da biblioteca, edite o arquivo de setup com a versão correspondente e gere o pacote através do comando.

```
python setup.py bdist_wheel
```

O pacote gerado estará no diretório dist.


## Author

Build with :heart: by Dev RC Team!

## License

Copyright (C) 2017. Stone Pagamentos. All rights reserved.