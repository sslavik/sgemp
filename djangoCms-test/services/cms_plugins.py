from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from services.models import ServicePluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class ServicePluginPublisher(CMSPluginBase):
    model = ServicePluginModel  # model where plugin data are saved
    module = _("Services")
    name = _("Services")  # name of the plugin in the interface
    render_template = "service_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context