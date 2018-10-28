"""empty message

Revision ID: b450b77ae1fa
Revises: 
Create Date: 2018-10-25 17:02:29.402007

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_json


# revision identifiers, used by Alembic.
revision = 'b450b77ae1fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('remotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('config', sqlalchemy_json.NestedMutableJson(), nullable=True),
    sa.Column('is_in_use', sa.Boolean(), nullable=True),
    sa.Column('fetched_before', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('torrents',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('DOWNLOADING', 'DOWNLOADED', 'ENQUEUED', 'PROCESSING', 'NEEDS_INPUT', 'FAILED', 'PROCESSED', 'IGNORED', name='status'), nullable=True),
    sa.Column('progress', sa.Float(), nullable=True),
    sa.Column('remote_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['remote_id'], ['remotes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('torrent_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['torrent_id'], ['torrents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lines')
    op.drop_table('torrents')
    op.drop_table('remotes')
    # ### end Alembic commands ###