

from sqlalchemy import Column, Integer, DateTime, ForeignKey,Date,Time,String
from database import Base
from sqlalchemy import Enum
import enum
from datetime import datetime

class StatusAgendamento(str, enum.Enum):
    PENDENTE = "pendente"
    CONFIRMADO = "confirmado"
    CANCELADO = "cancelado"
    FINALIZADO = "finalizado"

class Agendamento(Base):
    __tablename__ = "agendamento"

   

    id = Column(Integer, primary_key=True, index=True)
    data_agendamento = Column(Date, nullable=False)
    hora_agendamento = Column(Time, nullable=False)
    status = Column(Enum(StatusAgendamento), nullable=False)
    valor_total = Column(Integer, nullable=False)

    id_usuario = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    id_empresa = Column(Integer, ForeignKey("empresa.id"), nullable=False)
    id_servico = Column(Integer, ForeignKey("servico.id"), nullable=False)

    data_criacao = Column(DateTime, default=datetime.utcnow)
   
    def __init__(self, data_agendamento, hora_agendamento, status, valor_total, id_usuario, id_empresa, id_servico):
        self.data_agendamento = data_agendamento
        self.hora_agendamento = hora_agendamento
        self.status = status
        self.valor_total = valor_total
        self.id_usuario = id_usuario
        self.id_empresa = id_empresa
        self.id_servico = id_servico