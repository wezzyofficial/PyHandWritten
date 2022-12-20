
"""migrate all models

Revision ID: 20b1baf24ba2
Revises: 
Create Date: 2022-12-20 01:23:17.116716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20b1baf24ba2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('turns',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('hash', sa.Text(), nullable=False),
    sa.Column('st', sa.Text(), nullable=False),
    sa.Column('create_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('proccesed_text',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('turn_id', sa.Integer(), nullable=True),
    sa.Column('file_name', sa.Text(), nullable=True),
    sa.Column('file_path', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['turn_id'], ['turns.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('proccesed_text')
    op.drop_table('turns')
    # ### end Alembic commands ###
