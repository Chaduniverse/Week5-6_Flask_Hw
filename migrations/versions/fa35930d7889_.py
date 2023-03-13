"""empty message

Revision ID: fa35930d7889
Revises: d5a391591542
Create Date: 2023-03-12 14:52:51.341649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa35930d7889'
down_revision = 'd5a391591542'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caught__pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ability', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('base_stat_hp', sa.Integer(), nullable=True),
    sa.Column('base_stat_defense', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ability', sa.String(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('base_stat_hp', sa.Integer(), nullable=True),
    sa.Column('base_stat_defense', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('catch_pokemon',
    sa.Column('Caught_Pokemon_id', sa.Integer(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Caught_Pokemon_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('catch_pokemon')
    op.drop_table('pokemon')
    op.drop_table('caught__pokemon')
    # ### end Alembic commands ###
