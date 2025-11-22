from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    name = models.CharField(_('name'), max_length=100)
    named_url = models.CharField(
        _('named URL'), 
        max_length=100, 
        blank=True, 
        help_text=_('Named URL from urls.py')
    )
    explicit_url = models.CharField(
        _('explicit URL'), 
        max_length=200, 
        blank=True,
        help_text=_('Explicit URL (if not using named URL)')
    )
    menu_name = models.CharField(
        _('menu name'), 
        max_length=50,
        help_text=_('Unique name for the menu this item belongs to')
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('parent item')
    )
    order = models.IntegerField(_('order'), default=0)

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')
        ordering = ['menu_name', 'order', 'name']

    def __str__(self):
        return f"{self.menu_name} - {self.name}"

    def get_url(self):
        """Get URL for menu item, trying named_url first, then explicit_url"""
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.explicit_url or '#'
        return self.explicit_url or '#'

    @property
    def has_children(self):
        return self.children.exists()