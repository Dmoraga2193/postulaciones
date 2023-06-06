from django.forms import ValidationError

class MaxSizeFileValidators:

    def __init__(self,max_file_size=5):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size * 1048576

        if size > max_size:
            raise ValidationError(f"El archivo debe de pesar como maximo {self.max_file_size}MB, intente nuevamente.")
        
        return value
    
def validaExtensionCV(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')