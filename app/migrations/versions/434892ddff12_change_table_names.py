"""change table names

Revision ID: 434892ddff12
Revises: 6129dff0c322
Create Date: 2020-11-26 18:04:19.109122

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '434892ddff12'
down_revision = '6129dff0c322'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('task', 'tasks')
    op.rename_table('user', 'users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('tasks', 'task')
    op.rename_table('users', 'user')
    # ### end Alembic commands ###
