"""user table

Revision ID: c54b2b00fc42
Revises: fc84a1c437f1
Create Date: 2020-11-16 13:23:29.232962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c54b2b00fc42'
down_revision = 'fc84a1c437f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.add_column('task', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.add_column('task', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_task_timestamp'), 'task', ['timestamp'], unique=False)
    op.create_foreign_key(None, 'task', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_index(op.f('ix_task_timestamp'), table_name='task')
    op.drop_column('task', 'user_id')
    op.drop_column('task', 'timestamp')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
