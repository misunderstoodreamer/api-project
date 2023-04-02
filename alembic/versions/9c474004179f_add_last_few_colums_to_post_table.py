"""add last few colums to post table

Revision ID: 9c474004179f
Revises: 6dd2984ca58f
Create Date: 2023-04-02 20:59:14.751224

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9c474004179f'
down_revision = '6dd2984ca58f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'), )
    op.add_column('posts',
                  sa.Column('created_date', sa.TIMESTAMP(timezone=True), nullable=False,
                            server_default=sa.text('now()')), )


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_date')
