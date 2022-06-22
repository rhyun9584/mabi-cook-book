"""empty message

Revision ID: 615c7ae9ee9e
Revises: eec41a5bd802
Create Date: 2022-05-31 00:34:29.740132

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '615c7ae9ee9e'
down_revision = 'eec41a5bd802'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reset_pw',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('addr', sa.String(length=36), nullable=False),
    sa.Column('is_expired', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('addr')
    )
    op.drop_index('addr', table_name='change_pw')
    op.drop_table('change_pw')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('change_pw',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('addr', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('is_expired', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user'], ['user.id'], name='change_pw_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('addr', 'change_pw', ['addr'], unique=False)
    op.drop_table('reset_pw')
    # ### end Alembic commands ###