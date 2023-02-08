"""empty message

Revision ID: 3d69f59f1e3e
Revises: 35b07c7414d7
Create Date: 2023-02-08 17:55:43.381848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d69f59f1e3e'
down_revision = '35b07c7414d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('payment_period', sa.String(length=12), nullable=True))
        batch_op.create_unique_constraint(None, ['payment_UUID'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('payment_period')

    # ### end Alembic commands ###
