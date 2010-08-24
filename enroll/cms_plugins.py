from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Enrollment
from forms import EnrollmentForm
from django.core.mail import mail_managers


class ContactPlugin(CMSPluginBase):
    model = Enrollment
    name = "Enroll Online"
    render_template = "enroll.html"
    
    def render(self, context, instance, placeholder):
        request = context['request']

        if request.method == "POST":
            form = EnrollmentForm(request.POST)
            if form.is_valid():
                obj = form.save()
                mail_managers('New enrollment submission', """You've got a new enrollment application! Log in at http://kippendeavor.org/admin/ to read it.""")
                return context
        else:
            form = EnrollmentForm()

        
            context.update({
            'contact': instance,
            'form': form,
                })
            return context
    
plugin_pool.register_plugin(ContactPlugin)
