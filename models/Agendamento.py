

from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Date, Time, String, Numeric, Enum
from database import Base
import enum
from datetime import datetime

class StatusAgendamento(str, enum.Enum):
    PENDENTE = "Pendente"
    CONFIRMADO = "Confirmado"
    CANCELADO = "Cancelado"
    FINALIZADO = "Finalizado"

class Agendamento(Base):
    __tablename__ = "agendamento"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    data_agendamento = Column(Date, nullable=False)
    hora_agendamento = Column(Time, nullable=False)
    status = Column(String(20), default="Pendente", nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)

    id_usuario = Column(BigInteger, ForeignKey("usuario.id"), nullable=False)
    id_empresa = Column(BigInteger, ForeignKey("empresa.id"), nullable=False)
    id_servico = Column(BigInteger, ForeignKey("servico.id"), nullable=False)

    data_criacao = Column(DateTime, default=datetime.utcnow)
   
    def __init__(self, data_agendamento, hora_agendamento, status, valor_total, id_usuario, id_empresa, id_servico):
        self.data_agendamento = data_agendamento
        self.hora_agendamento = hora_agendamento
        self.status = status
        self.valor_total = valor_total
        self.id_usuario = id_usuario
        self.id_empresa = id_empresa
        self.id_servico = id_servico