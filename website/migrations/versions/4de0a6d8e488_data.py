"""data

Revision ID: 4de0a6d8e488
Revises: b4906d5ee789
Create Date: 2022-04-17 00:14:40.712748

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4de0a6d8e488"
down_revision = "b4906d5ee789"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("data", sa.Column("magnetic_storms", sa.Integer(), nullable=True))
    op.add_column(
        "user",
        sa.Column("image", flask_image_alchemy.fields.StdImageField(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "image")
    op.drop_column("data", "magnetic_storms")
    # ### end Alembic commands ###
