"""003_relation_authors_with_books

Revision ID: 003_relation_authors_with_books
Revises: 002_create_books_table
Create Date: 2022-07-23 16:57:31.085783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_relation_authors_with_books'
down_revision = '002_create_books_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("authors", sa.Column("book_id", sa.Integer, sa.ForeignKey("books.id")))


def downgrade() -> None:
    op.drop_column("authors", "book_id")
