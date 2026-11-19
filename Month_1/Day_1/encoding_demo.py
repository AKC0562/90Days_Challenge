samples = ["A", "é", "नमस्ते"]

for text in samples:
    print(f"{text!r}:")
    print("  UTF-8:", list(text.encode("utf-8")))

    try:
        print("  ASCII:", list(text.encode("ascii")))
    except UnicodeEncodeError:
        print("  ASCII: cannot encode")