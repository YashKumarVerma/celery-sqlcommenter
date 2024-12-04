import sys

if sys.version_info.major <= 2:
    import urllib

    url_quote_fn = urllib.quote
else:
    import urllib.parse

    url_quote_fn = urllib.parse.quote

KEY_VALUE_DELIMITER = ","


def generate_sql_comment(**meta):
    """
    Return a SQL comment with comma delimited key=value pairs created from
    **meta kwargs.
    """
    if not meta:  # No entries added.
        return ""

    # Sort the keywords to ensure that caching works and that testing is
    # deterministic. It eases visual inspection as well.

    return (
        " /*"
        + KEY_VALUE_DELIMITER.join(
            "{}={!r}".format(url_quote(key), url_quote(value))
            for key, value in sorted(meta.items())
            if value is not None
        )
        + "*/"
    )


def add_sql_comment(sql, **meta):
    comment = generate_sql_comment(**meta)
    sql = sql.rstrip()
    if sql[-1] == ";":
        sql = sql[:-1] + comment + ";"
    else:
        sql = sql + comment
    return sql


def url_quote(s):
    if not isinstance(s, (str, bytes)):
        return s
    quoted = url_quote_fn(s)
    # Since SQL uses '%' as a keyword, '%' is a by-product of url quoting
    # e.g. foo,bar --> foo%2Cbar
    # thus in our quoting, we need to escape it too to finally give
    #      foo,bar --> foo%%2Cbar
    return quoted.replace("%", "%%")
