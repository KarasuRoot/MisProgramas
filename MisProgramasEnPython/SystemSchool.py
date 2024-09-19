from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
engine=create_engine('sqlite:///:memory:')
DBase=declarative_base


class Alumn(DBase):  
    __tablename__="alumno"   
    id=Column(Integer,Sequence('alumno_seq_id'),primary_key=True)
    nom=Column(String)
    ape=Column(String)
    curso_ida=Column(Integer,ForeignKey('cursos.id'))
    
    cursos=relationship("Curso",back_populates='estu')
    def __repr__(self):
        return'{}{}'.format(self.nom, self.ape)

class Curso(DBase):
    __tablename__='cursos'
    id=Column(Integer, Sequence('cursos_seq_id'),primary_key=True)
    nomc=Column(String)
        
    estu=relationship("Estudiante",back_populates='cursos')
    hora_curso=relationship("Cronos",back_populates='curso_hora')
    def __repr__(self):
        return'{}'.format(self.nomc)

class Cronos(DBase):
    __tablename__='horario'
    id=Column(Integer, Sequence('horario_seq_id'),primary_key=True)
    dia=Column(String)
    hora_ini=Column(String)
    hora_fin=Column(String)
    profesor_id=Column(Integer,ForeignKey('profesor.id'))
    curso_id=Column(Integer,ForeignKey('cursos.id'))
    
    curso_hora=relationship("Curso",back_populates='hora_curso')
    curso_profe=relationship("profe",back_populates='profe_curso')

    def __repr__(self):
        return'{}{}{}'.format(self.dia,self.hora_ini, self.hora_fin)

class profe(DBase):
    __tablename__='profesor'
    id=Column(Integer, Sequence('profesor_seq_id'),primary_key=True)
    nombrep=Column(String)
    apep=Column(String)
    
    profe_curso=relationship("Cronos",back_populates='curso_profe')
    def __repr__(self):
        return'{}{}'.format(self.nombrep, self.apep)

DBase.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

alumno1=Alumn(nombrea='Gonzalo', apellidoa='Pepito')
print(alumno1)
session.add(alumno1)
alumno1.cursos=Curso(nombrec='Historia')
print(alumno1.cursos)

horario1=Cronos(dia='Domingo',hora_inicio='9:00', hora_fin='10:00')
session.add(horario1)
horario1.curso_hora=Curso(nombrec='Quimica')
horario1.curso_profe=profe(nombrep='Sergio',apellidop='Lynch')


print(horario1.curso_profe)
print(session.query(Curso).filter(profe.profe_curso.any()).all())
print(session.query(Cronos).filter(profe.profe_curso.any()).all())

session.commit()
