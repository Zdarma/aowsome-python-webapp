# coding = utf-8
import orm
from models import User, Blog, Comment
import asyncio


async def test():
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com',
             passwd='1234567890', image='about:blank')
    await u.save()
    u = await User.findAll()
    for i in u:
        print(i.id, i.name)
    await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
