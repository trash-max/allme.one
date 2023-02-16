"""empty message

Revision ID: 14a396afff73
Revises: 691cb377d9ae
Create Date: 2023-02-16 20:49:59.332738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14a396afff73'
down_revision = '691cb377d9ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patreon',
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
    op.drop_table('patreon')
    # ### end Alembic commands ###