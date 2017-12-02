def get_handlers_names(commands):
    for cmd in commands:
        name = f'on_{cmd}'
        yield name


def get_input_values(commands):
    for cmd in commands:
        yield cmd.lower()


def map_input_values_to_handlers_names(values, names):
    return {
        v: n for v, n in zip(values, names)
    }


class Console:
    def input(self, *, prompt):
        return input(prompt)
