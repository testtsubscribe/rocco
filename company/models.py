from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    display_order = models.IntegerField(default=0)  # Correct field name
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order', 'name']
    
    def __str__(self):
        return self.name

class StoneType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    display_order = models.IntegerField(default=0)  # Correct field name
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order', 'name']
    
    def __str__(self):
        return self.name

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name_plural = 'Contact inquiries'
    
    def __str__(self):
        return f"Inquiry from {self.name}"