"""empty message

Revision ID: 186d6856094d
Revises: fb12da79d47b
Create Date: 2022-12-14 17:55:51.798850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '186d6856094d'
down_revision = 'fb12da79d47b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_detail_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_detail_product_id', 'products', ['product_id'], ['id'], ondelete='SET NULL')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_details', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_detail_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_order_detail_product_id', 'products', ['product_id'], ['id'])

    # ### end Alembic commands ###
