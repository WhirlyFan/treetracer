"""create members and trees table

Revision ID: 2db6eb35d074
Revises: 3df8a9846da3
Create Date: 2024-05-05 00:28:44.318556

"""
from alembic import op
import sqlalchemy as sa
import os
is_production = os.environ.get('FLASK_DEBUG') == '0'
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '2db6eb35d074'
down_revision = '3df8a9846da3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_member_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('alternate_name', sa.String(length=255), nullable=True),
    sa.Column('picture', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['parent_member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if is_production:
        op.execute(sa.text(f"ALTER TABLE members SET SCHEMA {SCHEMA};"))
    op.create_table('trees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('parent_tree_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['parent_tree_id'], ['trees.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if is_production:
        op.execute(sa.text(f"ALTER TABLE trees SET SCHEMA {SCHEMA};"))
    op.create_table('tree_member',
    sa.Column('tree_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['tree_id'], ['trees.id'], ),
    sa.PrimaryKeyConstraint('tree_id', 'member_id')
    )
    if is_production:
        op.execute(sa.text(f"ALTER TABLE tree_member SET SCHEMA {SCHEMA};"))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tree_member')
    op.drop_table('trees')
    op.drop_table('members')
    # ### end Alembic commands ###
