# API | Flask | MongoDB

O Projeto consiste me um sistema de cadastro de artigos.

## Instalação/Utilização

Para ter acesso à estrutura da API, faça o fork e depois clone este projeto.

O projeto feito construido na linguagem `Python` versão `3.9.6` com o framework `Flask`,
e com o banco de dados em `MongoDB`.

Após clonar o projeto faça a criação de seu ambiente virtual de desenvolvimento:

```json
python -m venv venv --upgrade-deps
```

Em seguida faça a sinstação das dependêncas com o comando:

```json
pip install -r requirements.txt
```

Para rodar e servidor e utilizar as rotas, utilize o comando:

```json
flask run
```

## Rotas

<h3 align='center'> Cadastro de artigo</h3>

`POST /articles - para cadastro de artigos formato da requisição `

```json
{
  "title": "DoD weapons testers to assess cybersecurity of GPS satellites, ground system and user equipment",
  "url": "https://spacenews.com/dod-weapons-testers-to-assess-cybersecurity-of-gps-satellites-ground-system-and-user-equipment/",
  "imageUrl": "https://spacenews.com/wp-content/uploads/2018/01/GPS-airman-enters-coordinates.jpg",
  "newsSite": "SpaceNews",
  "summary": "DoD's office of operational test and evaluation will assess \"the survivability of the entire GPS enterprise in a contested space environment\"",
  "featured": false,
  "launches": [],
  "events": []
}
```

Caso dê tudo certo, a resposta será assim:

`POST /articles - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 13751,
  "title": "DoD weapons testers to assess cybersecurity of GPS satellites, ground system and user equipment",
  "url": "https://spacenews.com/dod-weapons-testers-to-assess-cybersecurity-of-gps-satellites-ground-system-and-user-equipment/",
  "imageUrl": "https://spacenews.com/wp-content/uploads/2018/01/GPS-airman-enters-coordinates.jpg",
  "newsSite": "SpaceNews",
  "summary": "DoD's office of operational test and evaluation will assess \"the survivability of the entire GPS enterprise in a contested space environment\"",
  "publishedAt": "2022-01-27T23:42:46.000Z",
  "featured": false,
  "launches": [],
  "events": []
}
```

<h3 align='center'> Buscar todos os artigos</h3>

`GET /articles - não há corpo de requisição `

```json

no body

```

Caso dê tudo certo, a resposta será assim:

`POST /articles - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 13751,
    "title": "DoD weapons testers to assess cybersecurity of GPS satellites, ground system and user equipment",
    "url": "https://spacenews.com/dod-weapons-testers-to-assess-cybersecurity-of-gps-satellites-ground-system-and-user-equipment/",
    "imageUrl": "https://spacenews.com/wp-content/uploads/2018/01/GPS-airman-enters-coordinates.jpg",
    "newsSite": "SpaceNews",
    "summary": "DoD's office of operational test and evaluation will assess \"the survivability of the entire GPS enterprise in a contested space environment\"",
    "publishedAt": "2022-01-27T23:42:46.000Z",
    "featured": false,
    "launches": [],
    "events": []
  },
  {
    "id": 2,
    "title": "Falcon 9 launch with Italian CSG-2 Earth observation satellite scrubbed again",
    "url": "https://www.nasaspaceflight.com/2022/01/falcon-9-csg-2/",
    "imageUrl": "https://www.nasaspaceflight.com/wp-content/uploads/2022/01/NSF-2022-01-27-22-55-57-560.jpg",
    "newsSite": "NASA Spaceflight",
    "summary": "The Italian Space Agency’s CSG-2 mission, the second satellite in its COSMO-SkyMed Second Generation constellation, scrubbed its second launch attempt, following a scrub on Thursday, both caused by unacceptable weather. The launch from Cape Canaveral Space Force Station will be the fourth Falcon 9 flight of the year, and is now scheduled for liftoff on Saturday at 6:11 PM EST (23:11 UTC) from Space Launch Complex 40 (SLC-40).",
    "publishedAt": "2022-01-28T17:29:56.000Z",
    "featured": false,
    "launches": [
      {
        "id": "23229c2b-abb7-4b94-b624-981a9adc88d2",
        "provider": "Launch Library 2"
      }
    ],
    "events": []
  }
]
```

<h3 align='center'> Buscar um único artigo</h3>

`GET /articles/id - Não a corpo na requisição `

```json

no body

```

Caso dê tudo certo, a resposta será assim:

`GET /articles/2 - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 2,
  "title": "Falcon 9 launch with Italian CSG-2 Earth observation satellite scrubbed again",
  "url": "https://www.nasaspaceflight.com/2022/01/falcon-9-csg-2/",
  "imageUrl": "https://www.nasaspaceflight.com/wp-content/uploads/2022/01/NSF-2022-01-27-22-55-57-560.jpg",
  "newsSite": "NASA Spaceflight",
  "summary": "The Italian Space Agency’s CSG-2 mission, the second satellite in its COSMO-SkyMed Second Generation constellation, scrubbed its second launch attempt, following a scrub on Thursday, both caused by unacceptable weather. The launch from Cape Canaveral Space Force Station will be the fourth Falcon 9 flight of the year, and is now scheduled for liftoff on Saturday at 6:11 PM EST (23:11 UTC) from Space Launch Complex 40 (SLC-40).",
  "publishedAt": "2022-01-28T17:29:56.000Z",
  "featured": false,
  "launches": [
    {
      "id": "23229c2b-abb7-4b94-b624-981a9adc88d2",
      "provider": "Launch Library 2"
    }
  ],
  "events": []
}
```

<h3 align='center'> Editar artigo</h3>

`PATCH /articles/id - FORMATO DA REQUISIÇÃO `

```json
{
  "launches": [
    {
      "provider": "Launch Library 2"
    }
  ]
}
```

Caso dê tudo certo a resposta será assim:

`PATCH /articles/2 - FORMATO DA RESPOSTA - 200`

```json
{
  "launches": [
    {
      "id": 1,
      "provider": "Launch Library 2"
    }
  ]
}
```

<h3 align='center'> Deletar artigo</h3>

`DEL /articles/id - Não a corpo na requisição `

```json

no body

```

Caso dê tudo certo, a resposta será assim:

`DEL /articles/1 - FORMATO DA RESPOSTA - STATUS 201`

```json

no body

```
