"""empty message

Revision ID: 59cff083df44
Revises: c3281757ce32
Create Date: 2023-01-17 18:56:37.847621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59cff083df44'
down_revision = 'c3281757ce32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('about', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('boosty', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('buymeacoffe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('cloudtips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('facebook', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('instagram', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('twitter', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('payment_UUID', sa.String(length=36), nullable=True))

    with op.batch_alter_table('vkontakte', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    with op.batch_alter_table('youtube', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about', sa.String(length=32), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('youtube', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('vkontakte', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('payment_UUID')

    with op.batch_alter_table('twitter', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('instagram', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('facebook', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('email', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('cloudtips', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('buymeacoffe', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('boosty', schema=None) as batch_op:
        batch_op.drop_column('about')

    with op.batch_alter_table('about', schema=None) as batch_op:
        batch_op.drop_column('about')

    # ### end Alembic commands ###