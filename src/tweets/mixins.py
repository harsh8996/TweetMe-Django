

class FormUserNeededMixin(object):

    def form_valid(self,form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin,self).form_valid(form)
        else:
            return self.form_invalid(form)