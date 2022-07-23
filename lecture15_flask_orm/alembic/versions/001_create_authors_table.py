"""001_create_authors_table

Revision ID: 001_create_authors_table
Revises: 
Create Date: 2022-07-23 13:44:53.384862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_authors_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("author_name", sa.String(300), nullable=False),
        sa.Column("author_email", sa.String(300), nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_table("authors")
