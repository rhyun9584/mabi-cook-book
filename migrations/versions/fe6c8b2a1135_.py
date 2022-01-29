"""empty message

Revision ID: fe6c8b2a1135
Revises: b677b2ec8f15
Create Date: 2022-01-28 16:54:37.848740

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fe6c8b2a1135'
down_revision = 'b677b2ec8f15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collect',
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('cook', sa.Integer(), nullable=False),
    sa.Column('state', mysql.TINYINT(), nullable=False),
    sa.ForeignKeyConstraint(['cook'], ['cook.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user', 'cook')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collect')
    # ### end Alembic commands ###
