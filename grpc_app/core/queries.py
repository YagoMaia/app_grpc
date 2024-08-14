class Queries():
    def inserir_usuario(self):
        return 'INSERT INTO usuarios (name, email) VALUES (%s, %s)'
    def atualizar_usuario(self):
        return 'UPDATE usuarios SET name = %s, email = %s WHERE id = %s'
    def excluir_usuario(self):
        return 'DELETE FROM usuarios WHERE id = %s'
    def listar_usuarios(self):
        return 'SELECT * FROM usuarios'
    def buscar_usuario_por_id(self):
        return 'SELECT * FROM usuarios WHERE id=%s'