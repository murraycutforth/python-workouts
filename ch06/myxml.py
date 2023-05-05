def myxml(tag, content="", **kwargs):
    attr_string = "".join([f" {k}=\"{v}\"" for k, v in kwargs.items()])
    return f"<{tag}{attr_string}>{content}</{tag}>"

print(myxml("foo"))
print(myxml("foo", "bar"))
print(myxml("foo", "bar", a=1, b=2, c=3))
