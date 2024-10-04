import uuid  # Biblioteca para gerar IDs únicos automaticamente

class NoSQLDatabase:

    def __init__(self):
        # Inicializa o "banco de dados" como um dicionário vazio
        self.data = {}
    
    def insert(self, documento: dict) -> str:
        """
        Insere um novo documento no banco de dados.
        Se o documento não contém o campo "_id", um ID único é gerado automaticamente.
        Retorna uma mensagem de sucesso ou erro caso o "_id" já exista.
        """

        # Verifica se o documento contém um "_id"; se não, gera um automaticamente
        if "_id" not in documento:
            documento["_id"] = str(uuid.uuid4())
        
        # Verifica se o "_id" já existe no banco de dados (self.data)
        if documento["_id"] in self.data:
            return "Erro: ID já existente!"
        
        # Insere o documento no "banco de dados" (dicionário)
        self.data[documento["_id"]] = documento
        return "Documento gerado com sucesso!"
    
    def find_by_id(self, id: str) -> dict:
        """
        Busca um documento pelo seu "_id".
        Retorna o documento se encontrado, ou uma mensagem de erro se o ID não for encontrado.
        """
        # Verifica se o "_id" existe no banco de dados
        if id not in self.data:
            return "ID não encontrado!"
        
        # Retorna o documento correspondente ao "_id"
        return self.data[id]
    
    def update_by_id(self, id: str, dados: dict) -> str:
        """
        Atualiza um documento existente no banco de dados com base no "_id".
        O documento é atualizado com os novos dados fornecidos.
        Retorna uma mensagem de sucesso ou erro caso o "_id" não seja encontrado.
        """
        # Verifica se o documento com o "_id" existe no banco de dados
        if id not in self.data:
            return "ID não encontrado!"
        
        # Atualiza o documento existente com os novos dados (substitui/insere novos campos)
        self.data[id].update(dados)
        return "Novos dados gravados com sucesso!"

    def delete_by_id(self, id: str) -> str:
        """
        Remove um documento do banco de dados com base no "_id".
        Retorna uma mensagem de sucesso ou erro caso o "_id" não seja encontrado.
        """
        # Verifica se o documento com o "_id" existe
        if id not in self.data:
            return "ID não encontrado!"
        
        # Remove o documento do banco de dados
        del self.data[id]
        return "Removido com sucesso!"
    
    def find_all(self) -> list:
        """
        Retorna uma lista de todos os documentos armazenados no banco de dados.
        """
        # Retorna todos os documentos como uma lista de dicionários
        return list(self.data.values())

# Bloco principal para testar a classe NoSQLDatabase
if __name__ == "__main__":
    # Cria uma instância da classe NoSQLDatabase
    db = NoSQLDatabase()

    # Insere alguns documentos no banco de dados
    print(db.insert({"_id": "12", "Gabriel": "22 anos"}))  # Inserção com ID manual
    print(db.insert({"Saw": "22 anos"}))  # Inserção sem ID (gerado automaticamente)
    print(db.insert({"_id": "15", "Clary": "22 anos"}))  # Inserção com ID manual

    # Atualiza um documento existente pelo ID
    print(db.update_by_id("15", {"Lucas": "19 anos"}))  # Adiciona novo campo "Lucas"

    # Remove um documento do banco de dados pelo ID
    print(db.delete_by_id("12"))  # Remove o documento com _id "12"

    # Busca um documento pelo ID
    print(db.find_by_id("15"))  # Exibe o documento com _id "15"
    print(db.find_by_id("12"))  # Tenta exibir o documento removido (erro esperado)

    # Exibe todos os documentos no banco de dados
    print(db.find_all())
