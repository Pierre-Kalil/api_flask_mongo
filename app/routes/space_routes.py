from flask import Flask, jsonify, request
from app.exceptions.exc import InvalidArticlesError
from app.model.space_model import Space
from http import HTTPStatus


def init_app(app: Flask):

    @app.get('/')
    def hello():
        return jsonify({"message":'Back-end Challenge 2021 🏅 - Space Flight News'})

    @app.post('/articles')
    def create():
        data = request.json
        try:
            art = Space(**data)
            new_art = art.create_article()
            if new_art:
                del new_art["_id"]
            return jsonify(new_art), HTTPStatus.CREATED
        except (TypeError) as t:
            return {"message": f"{t} Dados invalidos"}, HTTPStatus.BAD_REQUEST
        except (KeyError) as e:
            return {"message": f"Campo '{str(e)}' não existe para esse cadastro"}, HTTPStatus.BAD_REQUEST
        
      

    @app.get('/articles')
    def articles_all():
      art = Space.get_all_articles()
      for item in art:
          del item['_id']
      
      return jsonify(art), HTTPStatus.OK


   
    @app.get('/articles/<int:id>')
    def get_by_id(id):
        try:
            art_id = Space.filter_by_id(id)
            if art_id:
                return art_id, HTTPStatus.OK
            return {'message': "Artigo não encontrado"}, HTTPStatus.BAD_REQUEST
        except KeyError as e:
            {"message": f"O {str(e)} não existe para esta pesquisa"}, HTTPStatus.BAD_REQUEST

   
    
    @app.patch('/articles/<int:id>')
    def update(id):
        data = request.json
        try:
            Space.update_article(id, data)
            art_update = Space.filter_by_id(id)
            if art_update:
                return jsonify(art_update), HTTPStatus.OK
        except InvalidArticlesError:
            return {"msg": "Dados não existem"}, HTTPStatus.BAD_REQUEST
        except KeyError as e:
            return{"message": f"O {str(e)} selecionado não existe"}, HTTPStatus.BAD_REQUEST
    

    @app.delete('/articles/<int:id>')
    def delete(id):
        try:
            delete = Space.delete_article(id)
            return delete, HTTPStatus.NO_CONTENT
        except InvalidArticlesError:
            {"msg": "Dados não existem"}, HTTPStatus.BAD_REQUEST
        except KeyError as e:
            {"message": f"O {str(e)} selecionado não existe"}, HTTPStatus.BAD_REQUEST
  

  