"""adiciona imagem_url em categoria

Revision ID: a1b2c3d4e5f6
Revises: fc99c64c9446
Create Date: 2026-08-31 21:40:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = 'fc99c64c9446'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('categoria', sa.Column('imagem_url', sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column('categoria', 'imagem_url')
