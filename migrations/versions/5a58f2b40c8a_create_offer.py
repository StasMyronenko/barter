"""Create offer

Revision ID: 5a58f2b40c8a
Revises: 89178159b244
Create Date: 2023-06-04 14:35:08.623150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a58f2b40c8a'
down_revision = '89178159b244'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('partner_id', sa.Integer(), nullable=False),
    sa.Column('give_product_id', sa.Integer(), nullable=False),
    sa.Column('take_product_id', sa.Integer(), nullable=False),
    sa.Column('is_accepted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['give_product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['partner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['take_product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('offer')
    # ### end Alembic commands ###
