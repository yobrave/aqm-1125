import json
import os

ROOF_LINE = 200


def source_text():
    origin = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(origin, "rb") as reader:
        blob = reader.read()
    text = blob.decode("utf-8").strip()
    if not text:
        raise RuntimeError("no text found")
    if len(text) > ROOF_LINE:
        raise RuntimeError("text over the roof")
    return text


def sink_text(text):
    root = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(root, exist_ok=True)
    road = os.path.join(root, "entry.txt")
    with open(road, "wb") as writer:
        writer.write((text + "\n").encode("utf-8"))
    with open(road, "rb") as reader:
        if reader.read().decode("utf-8").strip() != text:
            raise RuntimeError("sink mismatch")
    return road


TEXT = source_text()
ROAD = sink_text(TEXT)
print(json.dumps({"checked": True, "chars": len(TEXT), "road": ROAD, "quest": "smallest-win"}))
