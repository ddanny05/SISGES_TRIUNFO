from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator, MinValueValidator,MaxValueValidator
from .Choices import ESTADO_CIVIL,ESTADO_SOCIO,CARGO,GENERO,TIPO_REUNION,REUNION,INGRESOS,EGRESOS

# Create your models here.
class Socios (models.Model):
    cedula = models.CharField (max_length=10,primary_key=True, validators=[MinLengthValidator(10), MaxLengthValidator(10)] )
    nombres = models.CharField (max_length=100, blank=False, )
    apellidos = models.CharField (max_length=100 )
    direccion = models.TextField (max_length=200, verbose_name="referencia domiciliaria")
    celular = models.CharField (max_length=10,blank=False, validators=[MinLengthValidator(10), MaxLengthValidator(10)] )
    correo_electronico = models.EmailField (unique=True )
    fecha_nacimiento = models.DateField (blank=False )
    
    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"
        db_table = "Socios"
    def __str__(self):
        return f"{self.cedula } - {self.apellidos} - {self.nombres}"

class Detalle_Socios (models.Model):
   
    socio = models.ForeignKey (Socios, on_delete=models.CASCADE )   
    genero = models.CharField (max_length=60,blank=False, choices=GENERO )
    estado_civil = models.CharField (max_length=60,choices=ESTADO_CIVIL ) 
    cargo= models.CharField(max_length=60,choices=CARGO)
    estado = models.CharField (max_length=60,choices=ESTADO_SOCIO, verbose_name="cargo")
    fecha_ingreso = models.DateField (blank=False )
    fecha_salida = models.DateField (blank=True, null=True )

    class Meta:
        verbose_name = "Detalle de Socio"
        verbose_name_plural = "Detalles de Socios"
        db_table = "Detalle_Socios"
    def __str__(self):
        return f"{self.socio.apellidos} - {self.socio.nombres}  - {self.estado}"
    
class Reuniones(models.Model):
    codigo = models.CharField(max_length=20,primary_key=True, default="CPBET-001")
    fecha = models.DateField (blank=False )
    lugar = models.CharField (max_length=100, blank=False )
    Descripcion = models.TextField (blank=False )
    tipo = models.CharField (max_length=50,blank=False, choices=TIPO_REUNION)
    
    class Meta:
        verbose_name = "Reunion"
        verbose_name_plural = "Reuniones"
        db_table = "Reuniones"
    def __str__(self):
        return f"{self.Descripcion}- {self.fecha} - {self.lugar} - "

    
class Asistencias (models.Model):
    socio = models.ForeignKey (Socios, on_delete=models.CASCADE )
    reunion = models.ForeignKey (Reuniones, on_delete=models.CASCADE )
    estado = models.CharField (max_length=60,choices=REUNION,blank=False)
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        db_table = "Asistencias"
    def __str__(self):
        return f"{self.socio.cedula} -- {self.estado}"
    
class Ingresos (models.Model):
    socio = models.ForeignKey (Socios, on_delete=models.CASCADE )
    tipo = models.CharField (max_length=50,choices=INGRESOS, help_text="concepto del cobro efectuado")
    descripcion = models.TextField (blank=False)
    monto = models.DecimalField (max_digits=10, decimal_places=2, blank=False, validators=[MinValueValidator(0),MaxValueValidator(1000)] )
    fecha = models.DateField (blank=False )
    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"
        db_table = "Ingresos"
    def __str__(self):
        return f"{self.socio.cedula} - {self.tipo} - {self.monto} - {self.fecha}"

class Egresos (models.Model):
    socio = models.ForeignKey (Socios, on_delete=models.CASCADE )
    tipo = models.CharField (max_length=80,choices=EGRESOS, help_text="concepto del gasto efectuado")
    descripcion = models.TextField(blank=False)
    monto = models.DecimalField (max_digits=10, decimal_places=2, blank=False, validators=[MinValueValidator(0),MaxValueValidator(200)])
    fecha = models.DateField (blank=False )
    class Meta:
        verbose_name = "Egreso"
        verbose_name_plural = "Egresos"
        db_table = "Egresos"
    def __str__(self):
        return f"{self.socio.cedula} - {self.tipo} - {self.monto} - {self.fecha}"

class Usuarios (models.Model):
    cedula = models.CharField(max_length=10,primary_key=True, validators=[MaxLengthValidator(10),MaxLengthValidator(10)])
    usuarios = models.CharField(max_length=50,unique=True)
    clave = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "Usuarios"
