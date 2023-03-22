from AdityaHalder.modules.databases import cli

collection = cli["Kaal"]["gmute"]


async def gmute_user(chat):
    doc = {"_id": "Gmute", "users": [chat]}
    r = await collection.find_one({"_id": "Gmute"})
    if r:
        await collection.update_one({"_id": "Gmute"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_gmuted_users():
    results = await collection.find_one({"_id": "Gmute"})
    return results["users"] if results else []


async def ungmute_user(chat):
    await collection.update_one({"_id": "Gmute"}, {"$pull": {"users": chat}})
