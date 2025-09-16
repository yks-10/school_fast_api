"""Create classrooms table

Revision ID: d3c8916726f8
Revises: 
Create Date: 2025-09-16 13:01:05.996520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd3c8916726f8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create classrooms table
    op.create_table('classrooms',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('class_name', sa.String(), nullable=False),
        sa.Column('class_teacher', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # Create indexes
    op.create_index(op.f('ix_classrooms_id'), 'classrooms', ['id'], unique=False)
    op.create_index(op.f('ix_classrooms_class_name'), 'classrooms', ['class_name'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    # Drop indexes
    op.drop_index(op.f('ix_classrooms_class_name'), table_name='classrooms')
    op.drop_index(op.f('ix_classrooms_id'), table_name='classrooms')
    # Drop table
    op.drop_table('classrooms')
