from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Date, PrimaryKeyConstraint, DATETIME
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime




database = create_engine('sqlite:///GestaoAulas.db')
Sessao = sessionmaker(bind=database)
sessao = Sessao()

base = declarative_base()

# Criar todas as tabelas no banco de dados
# Tabelas serão criadas com base nas classes definidas nos modelos
#Aluno = aluno()
# Tabela Aluno
class Aluno(base):
    __tablename__ = 'aluno'
    idAluno = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50))
    telefone = Column(String(9))
    palavraPasse = Column(String)

    def __init__(self, nome, email, telefone, palavraPasse):
        self.nome = nome
        self.email = email
        self.telefone =telefone
        self.palavraPasse = palavraPasse

# Tabela Professor
class Professor(base):
     __tablename__ = 'professor'
     idProfessor = Column(Integer, primary_key=True, autoincrement=True)
     nome = Column(String(50), nullable=False)
     email = Column(String)
     telefone = Column(String)
     palavraPasse = Column(String, nullable=False)

     def __init__(self, nome, email, telefone, palavraPasse):
         self.nome = nome
         self.email = email
         self.telefone = telefone
         self.palavraPasse = palavraPasse

# Tabela Aula
class Aula(base):
    __tablename__ = 'aula'
    idAula = Column(Integer, primary_key=True, autoincrement=True)
    idProfessor = Column(Integer, ForeignKey('professor.idProfessor'))
    titulo = Column(String(40))
    descricao = Column(String)
    dataHora = Column(DateTime)

    def __init__(self, idProfessor, titulo, descricao, dataHora):
        self.idProfessor = idProfessor
        self.titulo = titulo
        self.descricao = descricao
        self.dataHora = dataHora

# # Tabela Presenca
class Presenca(base):
    __tablename__ = 'presenca'
    idAluno = Column(Integer, ForeignKey('aluno.idAluno'))
    idAula = Column(Integer, ForeignKey('aula.idAula'))
    presenca = Column(Boolean)
    dataHora = Column(DateTime)
    __table_args__ = (
       PrimaryKeyConstraint('idAluno', 'idAula'),
    )
    
    def __init__(self, idAluno, idAula, presenca, dataHora):
        self.idAluno = idAluno
        self.idAula = idAula
        self.presenca = presenca
        self.dataHora = dataHora

# # Tabela gravação
class Gravacao(base):
    __tablename__ = 'gravacao'
    idGravacao = Column(Integer, primary_key=True, autoincrement=True)
    idAula = Column(Integer, ForeignKey('aula.idAula'))
    linkArquivo = Column(String)
    duracao = Column(Date)

    def __init__(self, idAula, duracao):
        self.idAula = idAula
        self.duracao = duracao

# # Tabela Conteudo
class Conteudo(base):
    __tablename__ = 'conteudo'
    idConteudo = Column(Integer, primary_key=True, autoincrement=True)
    idAula = Column(Integer, ForeignKey('aula.idAula'))
    tema = Column(String(40))
    conteudo = Column(String)

    def __init__(self, idAula, tema, conteudo):
        self.idAula = idAula
        self.tema = tema
        self.conteudo = conteudo

base.metadata.create_all(bind=database)

