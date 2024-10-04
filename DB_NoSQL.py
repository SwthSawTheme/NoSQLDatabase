import uuid

class NoSQLDatabase:

    def __init__(self):
        self.data = {}
    
    def insert(self,documento: dict) -> str:

        # verifica se o _id contém no documento
        if "_id" not in documento:
            documento["_id"] = str(uuid.uuid4())
        
        # verifica se o _id contém no DATA
        if documento["_id"] in self.data:
            return "Erro: ID já existente!"
        
        self.data[documento["_id"]] = documento
        return "Documento gerado com sucesso!"
    
    def find_by_id(self,id:str) -> dict:

        if id not in self.data:
            return "ID não encontrado!"
        return self.data[id]
    
    def update_by_id(self,id:str,dados:str) -> str:

        if id not in self.data:
            return "ID não encontrado!"
        self.data[id].update(dados)
        return "Novos dados gravados com sucesso!"

    def delete_by_id(self,id: str) -> str:

        if id not in self.data:
            return "ID não encontrado!"
        
        del self.data[id]
        return "Removido com sucesso!"

if __name__ == "__main__":
    db = NoSQLDatabase()

    print(db.insert({"_id": "12","Gabriel": "22 anos"}))
    print(db.insert({"Saw": "22 anos"}))
    print(db.insert({"_id": "15","Clary": "22 anos"}))

    print(db.update_by_id("15",{"lucas": "19 anos"}))

    print(db.delete_by_id("12"))
    print(db.find_by_id("15"))
    print(db.find_by_id("12"))
    