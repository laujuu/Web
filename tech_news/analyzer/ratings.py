from tech_news.database import get_collection


# Requisito 10
def top_5_categories():
    db = get_collection()
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5}
    ]
    result = list(db.aggregate(pipeline))
    if not result:
        return []
    return [r["_id"] for r in result]
