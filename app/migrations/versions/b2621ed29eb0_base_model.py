"""base model

Revision ID: b2621ed29eb0
Revises: c54b2b00fc42
Create Date: 2020-11-20 15:09:21.206290

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b2621ed29eb0'
down_revision = 'c54b2b00fc42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_task_created_at'), 'task', ['created_at'], unique=False)
    op.create_index(op.f('ix_task_updated_at'), 'task', ['updated_at'], unique=False)
    op.drop_index('ix_task_timestamp', table_name='task')
    op.drop_column('task', 'timestamp')
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_created_at'), 'user', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_updated_at'), 'user', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_updated_at'), table_name='user')
    op.drop_index(op.f('ix_user_created_at'), table_name='user')
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    op.add_column('task', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_index('ix_task_timestamp', 'task', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_task_updated_at'), table_name='task')
    op.drop_index(op.f('ix_task_created_at'), table_name='task')
    op.drop_column('task', 'updated_at')
    op.drop_column('task', 'created_at')
    # ### end Alembic commands ###