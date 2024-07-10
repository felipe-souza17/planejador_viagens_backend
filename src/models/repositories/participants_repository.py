from typing import Dict, Tuple, List
from sqlite3 import Connection

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                insert into participants(
                    id, trip_id, emails_to_invite_id, name
                ) 
                values
                (?, ?, ?, ?)
            ''',
            (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"]
            )
        )
        self.__conn.commit()