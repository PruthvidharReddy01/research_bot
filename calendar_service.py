from datetime import timedelta
from uuid import uuid4

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import os
import pickle


SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]


def get_calendar_service():

    creds = None

    if os.path.exists("token.pickle"):

        with open(
            "token.pickle",
            "rb"
        ) as token:

            creds = pickle.load(token)

    if not creds or not creds.valid:

        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(
            port=0
        )

        with open(
            "token.pickle",
            "wb"
        ) as token:

            pickle.dump(
                creds,
                token
            )

    service = build(
        "calendar",
        "v3",
        credentials=creds
    )

    return service


def create_meeting_event(
    attendee_email,
    meeting_time,
    meeting_topic
):

    service = get_calendar_service()

    end_time = (
        meeting_time +
        timedelta(hours=1)
    )

    event = {
        "summary":
        meeting_topic,

        "start": {
            "dateTime":
            meeting_time.isoformat(),

            "timeZone":
            "Asia/Kolkata"
        },

        "end": {
            "dateTime":
            end_time.isoformat(),

            "timeZone":
            "Asia/Kolkata"
        },

        "attendees": [
            {
                "email":
                attendee_email,

                "optional":
                False
            }
        ],

        "conferenceData": {
            "createRequest": {
                "requestId":
                str(uuid4())
            }
        }
    }

    event = service.events().insert(
        calendarId="primary",
        body=event,
        conferenceDataVersion=1,
        sendUpdates="all"
    ).execute()

    print("\n========== EVENT CREATED ==========")
    print("EVENT ID:", event.get("id"))
    print("MEET LINK:", event.get("hangoutLink"))
    print("ATTENDEES:", event.get("attendees"))
    print("===================================\n")

    return {
        "meet_link":
        event.get("hangoutLink"),

        "event_id":
        event.get("id"),

        "attendees":
        event.get("attendees")
    }