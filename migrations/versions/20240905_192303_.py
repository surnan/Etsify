"""empty message

Revision ID: 594652e66ee4
Revises: 
Create Date: 2024-09-05 19:23:03.213198

"""
from alembic import op
import sqlalchemy as sa
import os

# Get environment variables
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '594652e66ee4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Define schema prefix for production environment
    schema_prefix = f"{SCHEMA}." if environment == "production" else ""

    # Create users table
    op.create_table(
        f'{schema_prefix}users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=40), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username'),
        schema=SCHEMA if environment == "production" else None
    )

    # Create shoppingcarts table
    op.create_table(
        f'{schema_prefix}shoppingcarts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('userId', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['userId'], [f'{schema_prefix}users.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('userId'),
        schema=SCHEMA if environment == "production" else None
    )

    # Create products table
    op.create_table(
        f'{schema_prefix}products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('sellerId', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('stock', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['sellerId'], [f'{schema_prefix}users.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA if environment == "production" else None
    )

    # Create cartproducts table
    op.create_table(
        f'{schema_prefix}cartproducts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('shoppingCartId', sa.Integer(), nullable=False),
        sa.Column('productId', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['shoppingCartId'], [f'{schema_prefix}shoppingcarts.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA if environment == "production" else None
    )

    # Create favorites table
    op.create_table(
        f'{schema_prefix}favorites',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('userId', sa.Integer(), nullable=False),
        sa.Column('productId', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['userId'], [f'{schema_prefix}users.id']),
        sa.ForeignKeyConstraint(['productId'], [f'{schema_prefix}products.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA if environment == "production" else None
    )

    # Create productimages table
    op.create_table(
        f'{schema_prefix}productimages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('productId', sa.Integer(), nullable=False),
        sa.Column('image_url', sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(['productId'], [f'{schema_prefix}products.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA if environment == "production" else None
    )

    # Create reviews table
    op.create_table(
        f'{schema_prefix}reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('stars', sa.Integer(), nullable=False),
        sa.Column('review', sa.String(length=255), nullable=False),
        sa.Column('userId', sa.Integer(), nullable=False),
        sa.Column('productId', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['userId'], [f'{schema_prefix}users.id']),
        sa.ForeignKeyConstraint(['productId'], [f'{schema_prefix}products.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=SCHEMA if environment == "production" else None
    )

def downgrade():
    # Drop tables in reverse order of creation
    schema_prefix = f"{SCHEMA}." if environment == "production" else ""

    op.drop_table(f'{schema_prefix}reviews')
    op.drop_table(f'{schema_prefix}productimages')
    op.drop_table(f'{schema_prefix}favorites')
    op.drop_table(f'{schema_prefix}cartproducts')
    op.drop_table(f'{schema_prefix}products')
    op.drop_table(f'{schema_prefix}shoppingcarts')
    op.drop_table(f'{schema_prefix}users')
