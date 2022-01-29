import datetime
from app.configs.database import db

class Space():
    def __init__(self: str, featured: str, title: str, url: str, imageUrl: str, newSite: str, summary: str, launches=[], events=[]):
        date_now = datetime.datetime.utcnow()

        self.id = len(list(db.articles.find())) + 1
        self.title = title.title()
        self.url = url.lower()   
        self.imageUrl = imageUrl.lower()   
        self.newSite = newSite   
        self.summary = summary   
        self.publishedAt = date_now.strftime(f'%d/%m/%Y %H:%M:%S')   
        self.featured = featured   
        self.launches = launches   
        self.events =  events


    @staticmethod
    def get_all_articles():
        all_articles = list(db.articles.find())
        return all_articles
        
        
    @staticmethod
    def filter_by_id(id):
        art = db.articles.find_one({"id": id})
        if art:
            del art["_id"]
        return art
    

    def create_article(self):
        articles_list = list(db.articles.find())

        for i in self.launches:
            i['id'] = len(self.launches)+1
        for i in self.events:
            i['id'] = len(self.events)+1

        articles_list.append(self.__dict__)
        _id = db.articles.insert_one(self.__dict__).inserted_id
        new_art = db.articles.find_one({"_id": _id})

        return new_art


    @staticmethod
    def update_article(id, data):
        art = db.articles.find_one({"id": id})
        for k in data.keys():
            key = k
        data['id'] = len(art[key])+1
        if art:
            del art['_id']
        db.articles.update_one({"id": id},  {"$push": {key: data }} )
        return art


    @staticmethod
    def delete_article(id):
        art = Space.filter_by_id(id)
        if art:
            db.articles.delete_one({"id": id})
            return {"message": "Artigo excluido"}
        return {"message": "Artigo não existe"}
  