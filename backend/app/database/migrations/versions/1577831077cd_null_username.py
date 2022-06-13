"""null_username

Revision ID: 1577831077cd
Revises: 9946c74b8e69
Create Date: 2022-06-12 22:27:00.562353

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1577831077cd'
down_revision = '9946c74b8e69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_user_username', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_user_username', 'user', ['username'])
    # ### end Alembic commands ###
