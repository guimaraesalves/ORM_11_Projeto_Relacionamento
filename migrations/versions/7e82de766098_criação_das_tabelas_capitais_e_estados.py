"""criação das tabelas capitais e estados

Revision ID: 7e82de766098
Revises: 
Create Date: 2022-04-12 12:28:00.659942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e82de766098'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('sigla', sa.String(length=2), nullable=False),
    sa.Column('populacao', sa.Integer(), nullable=True),
    sa.Column('area', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('sigla')
    )
    op.create_table('capitais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('bairros', sa.Integer(), nullable=True),
    sa.Column('populacao', sa.Integer(), nullable=True),
    sa.Column('estado_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['estado_id'], ['estados.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('estado_id'),
    sa.UniqueConstraint('nome')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('capitais')
    op.drop_table('estados')
    # ### end Alembic commands ###
