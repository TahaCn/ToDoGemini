"""phone number added

Revision ID: 4660a0ef22f1
Revises: 
Create Date: 2025-03-16 12:20:08.546663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4660a0ef22f1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    #op.drop_column("users", "phone_number")
    pass
