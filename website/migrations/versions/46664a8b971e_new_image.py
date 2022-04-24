"""new_image

Revision ID: 46664a8b971e
Revises: a725f550593e
Create Date: 2022-04-21 16:32:21.077614

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '46664a8b971e'
down_revision = 'a725f550593e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image', sqlite.JSON(), nullable=True))
    # ### end Alembic commands ###
