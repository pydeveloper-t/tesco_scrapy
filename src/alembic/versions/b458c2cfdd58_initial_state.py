"""Initial  state

Revision ID: b458c2cfdd58
Revises: 
Create Date: 2020-09-25 23:20:20.227421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b458c2cfdd58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tesco_bought_next',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('product_url', sa.String(length=2048), nullable=True),
    sa.Column('product_title', sa.String(length=4096), nullable=True),
    sa.Column('product_image_url', sa.String(length=2048), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tesco_products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_url', sa.String(length=2048), nullable=True),
    sa.Column('image_url', sa.String(length=2048), nullable=True),
    sa.Column('product_title', sa.String(length=4096), nullable=True),
    sa.Column('category', sa.String(length=1024), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('product_description', sa.Text(), nullable=True),
    sa.Column('name_and_address', sa.Text(), nullable=True),
    sa.Column('return_address', sa.Text(), nullable=True),
    sa.Column('net_contents', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('tesco_reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('review_title', sa.String(length=2048), nullable=True),
    sa.Column('stars_count', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(length=64), nullable=True),
    sa.Column('review_text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tesco_reviews')
    op.drop_table('tesco_products')
    op.drop_table('tesco_bought_next')
    # ### end Alembic commands ###
