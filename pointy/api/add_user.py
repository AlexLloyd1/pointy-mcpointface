import logging

from werkzeug.datastructures import ImmutableMultiDict

from pointy.database.common import connect
from pointy.database.user import insert_user

logger = logging.getLogger(__name__)


def add_user(form: ImmutableMultiDict):
    logger.debug(f"Add team request: {form}")
    user = form.get('user')
    with connect() as conn:
        insert_user(conn, user.get('team_id'), user.get('id'))
