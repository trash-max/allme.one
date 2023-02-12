"""empty message

Revision ID: add21b9bad68
Revises: f901586797da
Create Date: 2023-02-10 00:36:09.572478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'add21b9bad68'
down_revision = 'f901586797da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('payment_UUID')
        batch_op.drop_column('payment_UUID')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('payment_UUID', mysql.VARCHAR(length=36), nullable=True))
        batch_op.create_index('payment_UUID', ['payment_UUID'], unique=False)

    # ### end Alembic commands ###