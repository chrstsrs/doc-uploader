import asyncio
from consumer import consume_events
from db import init_db, insert_notification
from producer import publish_event

async def main():
    init_db()

    async for event in consume_events("image.processed"):
        notif = {
            "id": event["id"],
            "userId": event["userId"],
            "message": f"Notification sent for {event['id']}",
        }
        insert_notification(notif["id"], notif["userId"], notif["message"])
        print(f"[Notifier] {notif['message']}")
        publish_event("notification.sent", notif)

if __name__ == "__main__":
    asyncio.run(main())
