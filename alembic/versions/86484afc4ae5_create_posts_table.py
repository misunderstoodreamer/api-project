"""create posts table

Revision ID: 86484afc4ae5
Revises: 
Create Date: 2023-04-02 19:22:03.626597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86484afc4ae5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))

    pass


def downgrade():
    op.drop_table('posts')

    pass
