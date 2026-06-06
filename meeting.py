from datetime import datetime
import re
import dateparser
from calendar_service import create_meeting_event


def schedule_meeting_handler(query, slack_client):

    users = get_workspace_users(slack_client)

    person_name = extract_person_name(query)
    print(
    "PERSON FOUND:",
    person_name
)
    meeting_topic = extract_meeting_topic(
    query
)

    print(
    "TOPIC FOUND:",
    meeting_topic
    )

    if not person_name:

        return {
            "output":
            "Could not find attendee name."
        }

    email = find_user_email(
        person_name,
        users
    )

    if not email:

        return {
            "output":
            f"No Slack user found for {person_name}"
        }

    meeting_time = extract_datetime(query)
    if not meeting_time:

        return {
        "output":
        "Could not understand meeting date/time."
    }

    meeting_info = create_meeting_event(
    email,
    meeting_time,
    meeting_topic
)

    return {
        "output":
        f"""
Attendee Found
Topic: {meeting_topic}
Name: {person_name}
Email: {email}

Time: {meeting_time}
Meet Link:
{meeting_info['meet_link']}
"""
    }


def extract_person_name(query):

    query_lower = query.lower()

    if "with" not in query_lower:
        return None

    name_part = query_lower.split(
        "with",
        1
    )[1]

    stop_words = [
        "today",
        "tomorrow",
        "next",
        "at",
        "on",
        "this",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
        "about",
        "regarding",
        "concerning"
    ]

    words = name_part.split()

    name_words = []

    for word in words:

        if word.lower() in stop_words:
            break

        name_words.append(word)

    if not name_words:
        return None

    return " ".join(name_words)

def extract_meeting_topic(query):

    match = re.search(
        r"about\s+(.*?)(?:\s+on|\s+at|\s+tomorrow|\s+today|$)",
        query,
        re.IGNORECASE
    )

    if match:

        topic = match.group(1).strip()

        if topic:
            return topic

    return "General Discussion"

def extract_datetime(query):

    query_lower = query.lower()

    datetime_text = extract_datetime_phrase(
        query_lower
    )

    print(
        "DATETIME TEXT:",
        datetime_text
    )

    if not datetime_text:
        return None

    current_time = datetime.now()

    print(
        "CURRENT TIME:",
        current_time
    )

    meeting_time = dateparser.parse(
        datetime_text,
        settings={
            "PREFER_DATES_FROM": "future",
            "RELATIVE_BASE": current_time
        }
    )

    print(
        "PARSED TIME:",
        meeting_time
    )

    return meeting_time


def extract_datetime_phrase(query):

    keywords = [
    "today",
    "tomorrow",
    "next",

    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",

    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

    words = query.split()

    for i, word in enumerate(words):

        if word in keywords:

            return " ".join(
                words[i:]
            )

    return None


def find_user_email(name, users):

    for user in users:

        user_name = (
            user.get(
                "name",
                ""
            )
            .lower()
            .strip()
        )

        if (
            name.lower().strip()
            in user_name
        ):

            return user.get("email")

    return None


def get_workspace_users(slack_client):

    users = slack_client.users_list()

    output = []

    for user in users["members"]:

        output.append(
            {
                "name":
                user.get(
                    "real_name"
                ),

                "email":
                user.get(
                    "profile",
                    {}
                ).get(
                    "email"
                )
            }
        )

    return output