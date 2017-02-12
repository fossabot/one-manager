from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from onemanager.account.models import OneManagerUser, OneManagerUserProfile, OneManagerUserContact


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = OneManagerUser
        fields = ('email', 'first_name', 'last_name', 'is_teacher', 'is_student', 'is_parent', 'is_admin')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')

        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = OneManagerUser
        fields = ('email', 'first_name', 'last_name', 'is_teacher', 'is_student', 'is_parent', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']


class OneManagerUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_teacher', 'is_student', 'is_parent', 'is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name')}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class OneManagerUserProfileAdmin(admin.ModelAdmin):
    pass


class OneManagerUserContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(OneManagerUser, OneManagerUserAdmin)
admin.site.register(OneManagerUserProfile, OneManagerUserProfileAdmin)
admin.site.register(OneManagerUserContact, OneManagerUserContactAdmin)
admin.site.unregister(Group)
