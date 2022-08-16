from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from flask_app.__innit__ import DATABASE

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results =  connectToMySQL(DATABASE).query_db(query)
        dojos = []
        if results:
            for dojo in results:
                dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def ninjas_in_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query, data )
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["ninjas.first_name"],
                "last_name" : row["ninjas.last_name"],
                "age" : row["ninjas.age"]
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )
        return dojo
