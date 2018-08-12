"""Add subworksheets to worksheet item

Revision ID: 136275e06649
Revises: 558ac277c2b9
Create Date: 2014-09-02 07:44:47.959083

"""

# revision identifiers, used by Alembic.
revision = '136275e06649'
down_revision = '558ac277c2b9'

from alembic import op
import sqlalchemy as sa

def upgrade():
    print('Adding subworksheets...')
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('worksheet_item', sa.Column('subworksheet_uuid', sa.String(length=63), nullable=True))
    op.create_index('worksheet_item_subworksheet_uuid_index', 'worksheet_item', ['subworksheet_uuid'], unique=False)
    ### end Alembic commands ###

def downgrade():
    print('Removing subworksheets...')
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('worksheet_item_subworksheet_uuid_index', table_name='worksheet_item')
    op.drop_column('worksheet_item', 'subworksheet_uuid')
    ### end Alembic commands ###
