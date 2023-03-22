# Aditya Halder // @AdityaHalder
from AdityaHalder.utilities import dbb

Rbun = dbb["RBAN"]


async def rkaal(user, reason="#MATHERCHOD"):
    await Rbun.insert_one({"user": user, "reason": reason})


async def runkaal(user):
    await Rbun.delete_one({"user": user})


async def rban_list():
    return [lo async for lo in Rbun.find({})]


async def kaalub_info(user):
    kk = await Rbun.find_one({"user": user})
    return kk["reason"] if kk else False


# Aditya Halder // @AdityaHalder

Lbun = dbb["LBAN"]


async def rlove(user, reason="#MYLOVER"):
    await Lbun.insert_one({"user": user, "reason": reason})


async def runlove(user):
    await Lbun.delete_one({"user": user})


async def lban_list():
    return [lo async for lo in Lbun.find({})]


async def loveub_info(user):
    um = await Lbun.find_one({"user": user})
    return um["reason"] if um else False
