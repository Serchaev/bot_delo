"""add constraints

Revision ID: 0003
Revises: 0002
Create Date: 2024-05-26 16:23:07.046360

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0003"
down_revision: Union[str, None] = "0002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_referrals_added"), "referrals", ["added"], unique=False)
    op.create_index(op.f("ix_referrals_adding"), "referrals", ["adding"], unique=False)
    op.create_index(op.f("ix_users_tg_id"), "users", ["tg_id"], unique=True)
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=False)
    op.create_unique_constraint("uq_referrer", "referrals", ["added", "adding"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_index(op.f("ix_users_tg_id"), table_name="users")
    op.drop_index(op.f("ix_referrals_adding"), table_name="referrals")
    op.drop_index(op.f("ix_referrals_added"), table_name="referrals")
    op.drop_constraint("uq_referrer", "referrals")
    # ### end Alembic commands ###
