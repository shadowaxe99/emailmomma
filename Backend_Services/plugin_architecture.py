```python
import abc

class PluginBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return

class PluginManager:
    def __init__(self):
        self._plugins = {}

    def register_plugin(self, identifier, plugin):
        self._plugins[identifier] = plugin

    def get_plugin(self, identifier):
        plugin = self._plugins.get(identifier)
        if not plugin:
            raise ValueError(identifier)
        return plugin

# Usage
class EmailPlugin(PluginBase):
    def load(self, input):
        return f"Loading data from {input}"

    def save(self, output, data):
        return f"Saving {data} to {output}"

plugin_manager = PluginManager()
email_plugin = EmailPlugin()

plugin_manager.register_plugin('email', email_plugin)

# Later in the code
plugin = plugin_manager.get_plugin('email')
print(plugin.load('inbox'))
print(plugin.save('outbox', 'Hello, World!'))
```