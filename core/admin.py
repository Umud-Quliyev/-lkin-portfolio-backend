from django.contrib import admin
from django import forms
from .models import Lab, LabImage, LabExtra


class LabImageInline(admin.TabularInline):
    model = LabImage
    extra = 1


class LabExtraInline(admin.StackedInline):
    model = LabExtra
    extra = 0
    max_num = 1


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    inlines = [LabImageInline, LabExtraInline]
    list_display = ('key', 'title', 'color')
    search_fields = ('key', 'title')

    class form(forms.ModelForm):
        class Meta:
            model = Lab
            fields = '__all__'
            widgets = {
                'color': forms.TextInput(attrs={'type': 'color'}),
                'background': forms.TextInput(attrs={'type': 'color'}),
                'text_color': forms.TextInput(attrs={'type': 'color'}),
            }

    form = form


@admin.register(LabImage)
class LabImageAdmin(admin.ModelAdmin):
    list_display = ('lab', 'image')


class LabExtraForm(forms.ModelForm):
    class Meta:
        model = LabExtra
        fields = '__all__'
        widgets = {
            'goal': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'contents': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'system': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    def clean_goal(self):
        data = self.cleaned_data['goal']
        if isinstance(data, str):
            return [line.strip() for line in data.splitlines() if line.strip()]
        return data

    def clean_contents(self):
        data = self.cleaned_data['contents']
        if isinstance(data, str):
            return [line.strip() for line in data.splitlines() if line.strip()]
        return data

    def clean_system(self):
        data = self.cleaned_data['system']
        if isinstance(data, str):
            return [line.strip() for line in data.splitlines() if line.strip()]
        return data


@admin.register(LabExtra)
class LabExtraAdmin(admin.ModelAdmin):
    list_display = ('lab', 'title')
    form = LabExtraForm
