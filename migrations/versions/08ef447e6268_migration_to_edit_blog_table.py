"""Migration to edit blog table

Revision ID: 08ef447e6268
Revises: 3e0eb00cb638
Create Date: 2021-06-20 10:12:14.788844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08ef447e6268'
down_revision = '3e0eb00cb638'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'blog_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
