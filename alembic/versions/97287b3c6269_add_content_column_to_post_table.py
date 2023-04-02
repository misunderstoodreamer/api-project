"""add content column to post table

Revision ID: 97287b3c6269
Revises: 86484afc4ae5
Create Date: 2023-04-02 20:21:35.230278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97287b3c6269'
down_revision = '86484afc4ae5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

