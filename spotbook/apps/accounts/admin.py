from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Account

class UserCreationForm(forms.ModelForm):
    #create new user form
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_password2(self):
        #check password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords dont match')
        return password2

    def save(self, commit=True):
        #save hashed password
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    #update user forms
    #replace password field with hash
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'password', 'username', 'is_admin', 'is_active', 'is_staff', 'is_superuser')

    def clean_password(self):
        #return initial value, regardless of what user provides
        return self.initial['password']

class UserAdmin(BaseUserAdmin):
    #forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    #fields to be used in displaying the User model
    #overrides definitions on base UserAdmin
    #that reference specific fields on auth.User
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_admin', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# register the new UserAdmin
admin.site.register(Account, UserAdmin)

# unregister Group model from admin since were not using djangos built in permissions
admin.site.unregister(Group)
