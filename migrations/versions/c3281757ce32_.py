"""empty message

Revision ID: c3281757ce32
Revises: 
Create Date: 2023-01-14 17:22:24.811554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3281757ce32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.drop_column('adress')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.add_column(sa.Column('adress', sa.VARCHAR(length=160), nullable=True))

    # ### end Alembic commands ###