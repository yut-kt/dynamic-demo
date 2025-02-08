import os

from lib.proto.protean import Protean


def select_dependencies() -> Protean:
    if os.getenv("DEP", None) == "A":
        from lib.a.impl import ProteanImpl
        return ProteanImpl()
    else:
        from lib.b.impl import ProteanImpl
        return ProteanImpl()
