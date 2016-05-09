import copy

class Action:
    from_bucket = None
    to_bucket = None
    water = None

    def __init__(self, from_bucket, to_bucket, water):
        self.from_bucket = from_bucket
        self.to_bucket = to_bucket
        self.water = water


class BucketState:
    bucket_capacity = {0: 8, 1: 5, 2: 3}
    bucket_s = []       # list of bucket water
    curAction = None    # Action

    def __init__(self, bucket_s, curAction):
        self.bucket_s = bucket_s
        self.curAction = curAction

    def CanTakeDumpAction(self, from_bucket, to_bucket):
        """
        :type from_bucket: int
        :type to_bucket: int
        """
        assert (from_bucket >= 0) and (from_bucket < len(self.bucket_s))
        assert (to_bucket >= 0) and (to_bucket < len(self.bucket_s))

        # not same bucket, and there is water in from_bucket, and to_bucket is not full
        if (from_bucket != to_bucket) and (not self.IsBucketEmpty(from_bucket)) and (not self.IsBucketFull(to_bucket)):
            return True
        return False

    def DumpWater(self, from_bucket, to_bucket, next):
        """
        :type from_bucket: int
        :type to_bucket: int
        :type next: BucketState
        """
        next.SetBucket(copy.copy(self.bucket_s))
        dump_water = self.bucket_capacity[to_bucket] - next.bucket_s[to_bucket]
        if next.bucket_s[from_bucket] >= dump_water:
            next.bucket_s[to_bucket] += dump_water
            next.bucket_s[from_bucket] -= dump_water
        else:
            next.bucket_s[to_bucket] += next.bucket_s[from_bucket]
            dump_water = next.bucket_s[from_bucket]
            next.bucket_s[from_bucket] = 0
        if dump_water > 0: # it's a successful action
            next.SetAction(from_bucket, to_bucket, dump_water)
            return True
        return False

    def SetBucket(self, bucket_s):
        """
        :type bucket_s: List[int]
        """
        self.bucket_s = bucket_s

    def SetAction(self, from_bucket, to_bucket, dump_water):
        """
        :type action: Action
        """
        self.curAction = Action(from_bucket, to_bucket, dump_water)

    def IsBucketEmpty(self, from_bucket):
        """
        :type from_bucket: int
        """
        if self.bucket_s[from_bucket] == 0:
            return True
        return False

    def IsBucketFull(self, to_bucket):
        """
        :type to_bucket: int
        """
        if self.bucket_s[to_bucket] >= self.bucket_capacity[to_bucket]:
            return True
        return False

    def IsFinalState(self):
        if self.bucket_s == [4, 4, 0]:
            return True
        return False


def IsProcessedState(states, newState):
    """
    :type states: List[BucketState]
    :type newState: BucketState
    """
    return any(state.bucket_s == newState.bucket_s for state in states)


def PrintResult(states):
    """
    :type states: List[BucketState]
    """
    buckets = []
    actions = []
    for state in states:
        buckets.append(','.join(str(n) for n in state.bucket_s))
        actions.append(','.join(str(n) for n in [state.curAction.from_bucket, state.curAction.to_bucket, state.curAction.water]))
    print 'Bucket: ' + ' => '.join(buckets)
    print 'Action: ' + ' => '.join(actions)
    print "\n"


def SearchStateOnAction(states, current, from_bucket, to_bucket):
    """
    :type states: List[BucketState]
    :type current: BucketState
    :type from_bucket: int
    :type to_bucket: int
    """
    if current.CanTakeDumpAction(from_bucket, to_bucket):
        next = BucketState(None, None)
        # pour water from from_bucket to to_bucket, if success, return the bucket state after the action
        bucket_dump = current.DumpWater(from_bucket, to_bucket, next)
        if bucket_dump and (not IsProcessedState(states, next)):
            states.append(next)
            SearchState(states)
            states.pop()


def SearchState(states):
    """
    :type states: List[BucketState]
    """
    current = states[-1]
    if current.IsFinalState():
        PrintResult(states)
        return
    # use double loop to create all kinds of actions
    for j in range(0, len(current.bucket_s)):
        for i in range(0, len(current.bucket_s)):
            SearchStateOnAction(states, current, i, j)


def main():
    init_bucket_state = BucketState([8, 0, 0], Action(-1, 1, 8))
    states = [init_bucket_state]
    SearchState(states)


'''
bucket 1 => 8 L
bucket 2 => 5 L
bucket 3 => 3 L
From [8, 0, 0] to [4, 4, 0]
'''

if __name__ == '__main__':
    main()
