# BEGIN (write your solution here)
def memoized(func):
    result = {}
    def inner(*args):
      if args in result:
          return result[args]
      result[args] = func(*args)
      return (result[args])
    return inner
# END
