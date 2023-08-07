# Create HashMap Class
class HashMap:
    def __init__(self, capacity=40):
        self.list = []
        for i in range(capacity):
            self.list.append([])

    # The following is the insert package function, which will insert and update data.
    def insert(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # The following will update a key that is already in the bucket.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # The following will append false keys to the end of the list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # The following will search and find an item with a corresponding key in the hash table.
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

    # The following will remove a value from the hash table.
    def delete(self, key):
        del_bucket = hash(key) % len(self.list)
        bucket_inventory = self.list[del_bucket]

        if key in bucket_inventory:
            bucket_inventory.remove(key)
