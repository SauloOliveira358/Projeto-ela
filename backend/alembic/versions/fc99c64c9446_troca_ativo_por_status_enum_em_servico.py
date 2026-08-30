"""troca ativo por status enum em servico

Revision ID: fc99c64c9446
Revises: 207dfdf6b074
Create Date: 2026-08-29 11:48:53.157018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc99c64c9446'
down_revision: Union[str, Sequence[str], None] = '207dfdf6b074'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Cria o tipo ENUM no PostgreSQL antes de adicionar a coluna
    status_servico_enum = sa.Enum('ATIVO', 'INATIVO', 'EXCLUIDO', name='statusservico')
    status_servico_enum.create(op.get_bind(), checkfirst=True)

    # 2. Adiciona a coluna usando o tipo criado
    op.add_column('servico', sa.Column('status', status_servico_enum, nullable=True))
    op.drop_column('servico', 'ativo')


def downgrade() -> None:
    op.add_column('servico', sa.Column('ativo', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=True))
    op.drop_column('servico', 'status')

    # Remove o tipo ENUM se desfizer a migration
    status_servico_enum = sa.Enum('ATIVO', 'INATIVO', 'EXCLUIDO', name='statusservico')
    status_servico_enum.drop(op.get_bind(), checkfirst=True)

