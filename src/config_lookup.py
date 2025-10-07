def find_key(data, key):
    def _find(obj, key, seen):
        oid = id(obj)
        if oid in seen:
            return None
        seen.add(oid)

        if isinstance(obj, dict):
            if key in obj:
                return obj[key]
            for k in obj:
                val = obj[k]
                res = _find(val, key, seen)
                if res is not None:
                    return res
            return None

        if isinstance(obj, (list, tuple, set)):
            for item in obj:
                res = _find(item, key, seen)
                if res is not None:
                    return res
            return None

        return None

    return _find(data, key, set())
