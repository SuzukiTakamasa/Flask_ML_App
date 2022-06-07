"""empty message

Revision ID: d71a5102129f
Revises: 88daab75e6ff
Create Date: 2022-06-08 00:00:48.487260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd71a5102129f'
down_revision = '88daab75e6ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_image_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_image_id', sa.String(), nullable=True),
    sa.Column('tag_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_image_id'], ['user_images.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_image_tags')
    # ### end Alembic commands ###