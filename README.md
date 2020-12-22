# Desafio SBTur

Projeto de avaliação técnica para função de desenvolvedor back-end da empresa SBTur. Trata-se de um pequeno serviço de API focado em recuperar, de forma seletiva ou não, uma representação serializável de uma vitrine (essencialmente, uma coleção da hotéis). Para fins de facilitar testes com o projeto também é possível inserir e remover objetos via interface Django admin.

## 🚀 Começando

Para obter o projeto utilizar:

```
$ git clone https://github.com/LePiN/desafio_sbtur.git
$ cd desafio_sbtur
```

### 📋 Pré-requisitos

- Python 3
- Git
- VirtualEnv
- Django
- Django REST


### 🔧 Instalação

Para criação do ambiente virtual:

- Criando e utilizando ambiente virtual Linux:
```
$ python -m venv .venv
$ source .venv/bin/activate
```

- Criando e utilizando ambiente virtual Windows:
```
$ python -m venv .venv
$ source .venv/Scripts/activate
```

Instalando dependências:
```
(.venv)$ pip install -r requirements.txt
```

Preparando banco de dados da aplicação:
```
(.venv)$ python manage.py makemigratios
(.venv)$ python manage.py migrate
(.venv)$ python manage.py loaddata populate_db.json
```

Verificando servidor da aplicação:
```
(.venv)$ python manage.py runserver
```
Com isso já será possivel navegar pelo projeto atraves da url http://127.0.0.1:8000/<end-points>.

## ⚙️ Executando os testes

Nessa versão, o esboço dos testes para os filtros de seleção de vitrines:
```
(.venv)$ python manage.py test -v2
```

Para testes de estilo do código:
```
(.venv)$ pycodestyle . --max-line-length=120
```

## 📦 Operações

As requisições de "vitrines" devem ser feitas no end-point "showcase" (exemplo, http://127.0.0.1:8000/showcase) através de conteúdo json, conforme a seguir:

- Requisitar todas as vitrines:
```
{"page_routes": []} ou {}
```

- Requisitar vitrines específicas pelo end-point associado as mesmas:
```
{"page_routes": ["/", "/destinos"]} 
```

- Requisitar vitrines específicas pelo status da vitrine:
```
{"status_showcase": ["ACTIVE"]} 
```

- Requisitar vitrines com hotéis específicos de acordo com o País dos mesmos:
```
{"target_countrys": ["Brasil", "Peru", "Chile"]}
```

- Requisitar vitrines com hotéis específicos de acordo com o Estado dos mesmos:
```
{"target_states": ["SC", "PR"]}
```
* Esse filtro sobrepõe o anterior.

- Requisitar vitrines com hotéis específicos de acordo com as Cidade dos mesmos:
```
{"target_citys": ["Florianópolis", "Gramado"]}
```
* Esse filtro sobrepõe o anterior.

- Requisitar vitrines com hotéis específicos de acordo a categoria dos mesmos:
```
{"target_category": ["Hospedagem"}
```

- Requisitar vitrines com um número definido de hotéis:
```
{"itens_limit": 2}
```

- Requisitar vitrines com os hotéis organizados por preço cadastrado:
```
{"itens_price_order": "crescent"}
```
* Para ordem decrescente utilizar "decrescent" caso contrário o padrão será a ordem crescente.

Os filtros são cumulativos, ou seja, podem ser utilizado para refinar as solicitações.
* Devido ao escopo proposta as demais operações (inserir, retirar, alterar vitrines e similares) foram resolvidas através de recursos padronizados do django e podem ser manipulados pela interface padrão que acompanha o framework.

## 📦 Modelos do projeto:

- Category:
```
    {"pk": <int>, "name": <string>, "slug": <string>}
```

- City:
```
    {"pk": <int>, "name": <string>, "slug": <string>, "state": <string-choice>}
```

- Country:
```
    {"pk": <int>, "name": <string>, "slug": <string>}
```

- Hotel:
```
    {"pk": <int>, "hotel_name": <string>, "slug": <string>, "image":<url>, "price": <int>, "city": <City-object>,
    "Country": <Country-object>, "Category": <Category-object>}
```

- Page Route:
```
    {"pk": <int>, "page_identifier": <string>}
```

- Showcase:
```
    {"pk": <int>, "title": <string>, "subtitle": <string>, "routes":<List-page-route-objects>, 
    "itens": <List-hotel-objects>, "status": <string-choices>}
```

## 🛠️ Construído com

* [Django](https://docs.djangoproject.com/en/3.1/) - O framework web usado
* [Django-REST](https://pycodestyle.pycqa.org/en/latest/intro.html) - O módulo REST utilizado

## ✒️ Autores

* **Leandro Pieper Nunes** - *Trabalho Inicial* - [Leandro Pieper Nunes](https://github.com/LePiN)

## 🎁 Agradecimentos

* Grato a toda equipe SBTur pela oportunidade de participar da seleção.


---
