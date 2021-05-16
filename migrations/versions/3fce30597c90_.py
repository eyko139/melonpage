"""empty message

Revision ID: 3fce30597c90
Revises: 2688e5f15b10
Create Date: 2021-05-05 22:11:44.480883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fce30597c90'
down_revision = '2688e5f15b10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('member_since', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'member_since')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###