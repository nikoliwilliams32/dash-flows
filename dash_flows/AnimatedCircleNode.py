# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AnimatedCircleNode(Component):
    """An AnimatedCircleNode component.


Keyword arguments:

- data (dict; required)

    `data` is a dict with keys:

    - label (boolean | number | string | dict | list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flows'
    _type = 'AnimatedCircleNode'
    @_explicitize_args
    def __init__(self, data=Component.REQUIRED, **kwargs):
        self._prop_names = ['data']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['data']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AnimatedCircleNode, self).__init__(**args)
