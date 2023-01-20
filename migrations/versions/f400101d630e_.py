"""empty message

Revision ID: f400101d630e
Revises: 3c5d44f28bf2
Create Date: 2023-01-20 17:56:52.459164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f400101d630e'
down_revision = '3c5d44f28bf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('telegram',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=160), nullable=True),
    sa.Column('about', sa.String(length=32), nullable=True),
    sa.Column('network_name', sa.String(length=16), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('links_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['links_id'], ['links.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('telegram')
    # ### end Alembic commands ###
