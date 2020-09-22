import psutil

from ruxit.api.base_plugin import BasePlugin
from ruxit.api.data import PluginMeasurement
from ruxit.api.selectors import FromPluginSelector

class NetworkExtension(BasePlugin):
    def query(self, **kwargs):
        try:
            value = None
            value = len(psutil.net_connections())
            if value is not None:
                self.results_builder.add_absolute_result(
                    PluginMeasurement(key="network_connection", value=value, entity_selector=FromPluginSelector())
                )                
        except Exception as e:
            error = f"Generic command - error running command: {e}"
            self.results_builder.report_error_event(error, "Network Extension Error")


if __name__ == "__main__":
    value = None
    value = len(psutil.net_connections())
    if value is not None:
        print(value)