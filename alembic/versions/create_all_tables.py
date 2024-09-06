"""create all tables

Revision ID: b774c151e768
Revises: ffdc0a98111c
Create Date: 2024-09-04 21:15:24.355693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b774c151e768'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    op.create_table('cartproducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shoppingCartId', sa.Integer(), nullable=False),
    sa.Column('productId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('productId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('orderproducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orderId', sa.Integer(), nullable=False),
    sa.Column('productId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sellerId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('productimages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productId', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('review', sa.String(length=255), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('productId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('shoppingcarts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )



    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###qqqqqqqqq


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
