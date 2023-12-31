from django import forms

from desafios.models import Submissao

class SubmissaoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SubmissaoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'block w-full bg-slate-200 text-sm text-slate-700 p-4 mt-2 rounded-lg text-base'
            visible.field.widget.attrs['required'] = False


    class Meta:
        model = Submissao
        exclude = ('resultado', )