# execute.py celery application
import time

from tasks import pr1,pr2

# def doit():
#     print(resp+10)


# global resp
# result = add.apply_async((4, 4))
# result.ready()
# resp = result.get()
#
# for i in range(5):
#     time.sleep(2)
#     print(resp)
#
# print(addit. apply_async((3,3)).get())

result1 = pr1.delay()
result2 = pr2.delay()

print(result2.get())
print(result1.get())
