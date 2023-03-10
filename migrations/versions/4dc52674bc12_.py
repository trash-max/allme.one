"""empty message

Revision ID: 4dc52674bc12
Revises: 4f057e4ed101
Create Date: 2023-02-10 01:02:40.491397

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4dc52674bc12'
down_revision = '4f057e4ed101'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_key',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('key', sa.String(length=32), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('last_used', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key')
    )
    with op.batch_alter_table('apikey', schema=None) as batch_op:
        batch_op.drop_index('key')

    op.drop_table('apikey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apikey',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', mysql.VARCHAR(length=16), nullable=True),
    sa.Column('key', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('count', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('last_used', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='apikey_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('apikey', schema=None) as batch_op:
        batch_op.create_index('key', ['key'], unique=False)

    op.drop_table('api_key')
    # ### end Alembic commands ###
