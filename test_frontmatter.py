import frontmatter
from pathlib import Path

p = Path("/Users/ramikhouri/Desktop/Taliaz/person/Rami Khouri.md")
post = frontmatter.load(str(p))
print("Keys:", post.metadata.keys())
print("Type:", post.metadata.get("type"))
