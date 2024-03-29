#!/usr/bin/env python3
"""Session Auth"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Session Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create Session
        """
        if user_id is None or type(user_id) is not str:
            return None
        from uuid import uuid4
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User ID for Session ID
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
