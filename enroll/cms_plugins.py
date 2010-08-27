from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Enrollment, EnrollmentForAdmin
from forms import EnrollmentForm
from django.core.mail import mail_managers


class EnrollmentPlugin(CMSPluginBase):
    model = EnrollmentForAdmin
    name = "Enroll Online"
    render_template = "enroll.html"
    
    def render(self, context, instance, placeholder):
        request = context['request']

        form = EnrollmentForm(request.POST or None)
        if form.is_valid():
            form.save()
           # mail_managers('New enrollment submission', """You've got a new enrollment application! Log in at http://kippendeavor.org/admin/ to read it.""")
            context.update({
                'enroll':instance,
                'form':None,
                })
            return context
        context.update({
            'enroll': instance,
            'form': form,
            })
        return context
    
plugin_pool.register_plugin(EnrollmentPlugin)
