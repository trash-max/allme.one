"""empty message

Revision ID: 35b07c7414d7
Revises: 442ec0c18c58
Create Date: 2023-02-05 22:10:51.784733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35b07c7414d7'
down_revision = '442ec0c18c58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stackoverflow',
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
    op.drop_table('stackoverflow')
    # ### end Alembic commands ###
