from core.assets import Route


routes = ([])


def route(**kwargs):
    """Функция "command" - используется как декоратор - хендлер."""
    def with_args(handler):
        if kwargs.keys() & {'name'}:
            routes.append(Route(name=kwargs['name'], handler=handler,
                                auth=(kwargs['auth'] if 'auth' in kwargs else False),
                                post=(kwargs['post'] if 'post' in kwargs else False),
                                get=(kwargs['get'] if 'get' in kwargs else False),
                                put=(kwargs['put'] if 'put' in kwargs else False),
                                with_args=(kwargs['with_args'] if 'with_args' in kwargs else False),
            ))
        else:
            return False

    return with_args