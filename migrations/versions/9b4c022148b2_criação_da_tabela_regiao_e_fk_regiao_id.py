"""criação da tabela regiao e FK regiao_id

Revision ID: 9b4c022148b2
Revises: 7e82de766098
Create Date: 2022-04-14 13:42:52.192458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b4c022148b2'
down_revision = '7e82de766098'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('regioes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('numero_estados', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.add_column('estados', sa.Column('regiao_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'estados', 'regioes', ['regiao_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'estados', type_='foreignkey')
    op.drop_column('estados', 'regiao_id')
    op.drop_table('regioes')
    # ### end Alembic commands ###
