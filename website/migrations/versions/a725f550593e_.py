"""empty message

Revision ID: a725f550593e
Revises: 4de0a6d8e488
Create Date: 2022-04-19 19:31:46.530384

"""
from alembic import op
import sqlalchemy as sa
import flask_image_alchemy

# revision identifiers, used by Alembic.
revision = 'a725f550593e'
down_revision = '4de0a6d8e488'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image', flask_image_alchemy.fields.StdImageField(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image')
    # ### end Alembic commands ###
