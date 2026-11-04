"""Make a page's CSS smaller: drop rules for classes the page never uses, then minify.

Used for the home page. A selector is kept when every class it names appears in the
page HTML or in the page's JavaScript (classes added at runtime, like is-active).
"""
import re

_CLASS = re.compile(r"\.(-?[_a-zA-Z][\w-]*)")


def used_classes(html, js):
    found = set()
    for m in re.finditer(r'class="([^"]*)"', html):
        found.update(m.group(1).split())
    # class names mentioned anywhere in the JS (quoted words), e.g. 'is-active', 'du-visible'
    found.update(re.findall(r"""['"]([a-z][\w-]*)['"]""", js))
    found.update(re.findall(r"class=\\?['\"]([^'\"\\]*)", js))
    for chunk in list(found):
        found.update(chunk.split())
    return found


def _blocks(css):
    """Split CSS into top-level (prelude, body) pairs; body is None for @import etc."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j == -1:
            break
        prelude = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        out.append((prelude, css[j + 1:k - 1]))
        i = k
    return out


def _keep_selector(sel, used):
    return all(c in used for c in _CLASS.findall(sel))


def purge(css, used):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    res = []
    for prelude, body in _blocks(css):
        if prelude.startswith("@media") or prelude.startswith("@supports"):
            inner = purge(body, used)
            if inner.strip():
                res.append(f"{prelude}{{{inner}}}")
        elif prelude.startswith("@"):
            res.append(f"{prelude}{{{body}}}")          # keyframes, font-face: keep as is
        else:
            sels = [s for s in prelude.split(",") if _keep_selector(s, used)]
            if sels:
                res.append(f"{','.join(s.strip() for s in sels)}{{{body.strip()}}}")
    return "\n".join(res)


def minify(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    css = css.replace(";}", "}")
    return css.strip()


def slim(css, html, js):
    return minify(purge(css, used_classes(html, js)))
