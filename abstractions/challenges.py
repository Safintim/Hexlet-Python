from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


def make(url):
    return urlparse(url)


def get_scheme(data):
    return data.scheme


def set_scheme(data, scheme):
    return data._replace(scheme=scheme)


def get_host(data):
    return data.netloc


def set_host(data, host):
    return data._replace(netloc=host)


def get_path(data):
    return data.path


def set_path(data, path):
    return data._replace(path=path)


def get_query(data):
    return data.query


def set_query(data, query):
    return data._replace(query=query)


def get_query_param(data, param_name, default=None):
    return parse_qs(get_query(data)).get(param_name, [default])[0]


def set_query_param(data, key, value):
    qs = parse_qs(get_query(data))
    if value is None:
        qs.pop(key, None)
    else:
        qs.update({key: value})

    new_qs = urlencode(qs, doseq=True)
    return set_query(data, new_qs)


def to_string(data):
    return urlunparse(list(data))
