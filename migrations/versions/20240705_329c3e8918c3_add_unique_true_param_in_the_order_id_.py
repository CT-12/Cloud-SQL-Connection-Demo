"""Add unique=True param in the order_id in the Sale table.

Revision ID: 329c3e8918c3
Revises: 05ce8edda5d8
Create Date: 2024-07-05 11:32:57.548260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '329c3e8918c3'
down_revision: Union[str, None] = '05ce8edda5d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'sales', ['order_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sales', type_='unique')
    # ### end Alembic commands ###
