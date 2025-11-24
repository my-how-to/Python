# Types Overview

Quick reference for Python's built-in collection types. Click a type to jump to the local lesson file.

| Type | Ordered? | Changeable? | Allows Duplicates? | Example |
| --- | --- | --- | --- | --- |
| [List](lists_in_python.py) | ✅ Yes | ✅ Yes | ✅ Yes | `["a", "b", "c"]` |
| [Tuple](tuples_in_python.py) | ✅ Yes | ❌ No | ✅ Yes | `("a", "b", "c")` |
| [Set](sets_in_python.py) | ❌ No | ✅ Yes | ❌ No | `{"a", "b", "c"}` |
| [Dictionary](dicts_in_python.py) | ✅ Yes | ✅ Yes | ❌ (keys only) | `{"a": 1, "b": 2}` |

---

## Extra Tips

- **Choose the right tool:** Tuples for fixed records, lists for sequences you edit often, sets when you only need membership/uniqueness, dictionaries for labeled data.
- **Conversions are easy:** Use `list()`, `tuple()`, `set()`, and `dict()` to convert between types; this is handy when deduplicating or freezing data.
- **Immutability matters:** Tuples and frozensets are hashable, so they can act as dict keys or set members.
- **Memory & performance:** Sets/dicts provide O(1) average lookup; lists preserve order and allow indexing; tuples are slightly smaller/faster when data never changes.
- **Advanced modules to explore:** `collections` (namedtuple, deque, Counter) and `typing` (type hints like `list[str]`) extend what you can do with these basics.
- **Comprehensions:** See [comprehensions.py](comprehensions.py) for list/dict/set comprehensions that build these collections in one expressive line.
