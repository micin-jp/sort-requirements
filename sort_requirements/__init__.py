import re

VERSION = (1, 3, 0)
DEPS_RE = r"((?:#[^\n]+?\n)*)([^\n]+?)([=!~>]=)([^\\\n]+)((?:\\\n[^\\\n]+)*)"
WITHOUT_VERSION_RE = r"(?m)^((?:#[^\n]+?\n)*)([a-z][\w\-]*)(?=(?:\n|\Z))"

__version__ = ".".join(str(v) for v in VERSION)


def sort_requirements(requirements):
    matches = re.findall(DEPS_RE, requirements)
    data = re.sub(DEPS_RE, "{}", requirements)

    without_version_matches = re.findall(WITHOUT_VERSION_RE, data)
    data = re.sub(WITHOUT_VERSION_RE, "{}", data)

    matches.extend(without_version_matches)
    matches = sorted(matches, key=lambda d: d[1].lower())

    print(matches)
    deps = []
    for m in matches:
        if len(m) >= 3:
            deps.append("{}{}{}{}{}".format(*m))
        else:
            deps.append("{}{}".format(*m))

    data = data.format(*deps)
    return data
