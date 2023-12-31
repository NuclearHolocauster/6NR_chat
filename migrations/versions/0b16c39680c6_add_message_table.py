"""add message table

Revision ID: 0b16c39680c6
Revises: 21bafe7c0240
Create Date: 2023-10-12 16:46:20.711507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b16c39680c6'
down_revision: Union[str, None] = '21bafe7c0240'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('text', sa.String(length=512), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_id'), 'message', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_message_id'), table_name='message')
    op.drop_table('message')
    # ### end Alembic commands ###
