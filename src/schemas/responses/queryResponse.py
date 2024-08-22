class QueryResponse:
    QueryEventResponseSchema = {
        "type" : "object",
        "properties" : {
            "event_id" : {"type" : "number"},
            "event_name": {"type": "string"},
            "event_description": {"type": "string"},
            "start_date": {"type": "date"},
            "end_date": {"type": "date"},
            "tasks": {
                "type" : "object",
                "properties" : {
                    "task_id" : {"type" : "number"},
                    "task_name": {"type": "string"},
                    "task_description": {"type": "string"},
                    "event_id": {"type": "number"},
                    "task_type": {"type": "number"},
                    "npc_id": {"type": "number"},
                    "mandatory_items" : {
                        "type" : "object",
                        "properties" : {
                            "item_id" : {"type" : "number"},
                            "item_name" : {"type", "number"}
                        }
                    },
                    "restricted_items" : {
                        "type" : "object",
                        "properties" : {
                            "item_id" : {"type" : "number"},
                            "item_name" : {"type", "number"}
                        }
                    },
                }
            }
        }
    }
