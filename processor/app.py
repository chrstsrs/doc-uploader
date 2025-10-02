import asyncio
from consumer import consume_events
from db import init_db, insert_processed
from producer import publish_event

async def main():
    init_db()

    async for event in consume_events("image.uploaded"):
        # Simulate processing
        processed_data = {
            "id": event["id"],
            "userId": event["userId"],
            "status": "processed",
            "result": f"Processed file at {event['path']}"
        }
        insert_processed(processed_data["id"], processed_data["userId"], processed_data["status"], processed_data["result"])
        publish_event("image.processed", processed_data)

if __name__ == "__main__":
    asyncio.run(main())
