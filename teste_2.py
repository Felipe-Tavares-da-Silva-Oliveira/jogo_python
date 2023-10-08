import re
import json

s = '{"employee":{"name":"John", "age":30, "city":"New York"}}'
def json_from_s(s):
    match = re.findall(r"{.+[:,].+}|\[.+[,:].+\]", s)
    return json.loads(match[0]) if match else None
    print(json_from_s(s))
    print(json_from_s('{1:}'))

