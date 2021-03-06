from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):

    BIKES = 'BIKES'
    FRAMES = 'FRAMES'
    PRODUCT_TYPE = [
        (BIKES, 'BIKES'),
        (FRAMES, 'FRAMES'),
    ]

    URBAN = 'URBAN'
    ALL_ROAD = 'ALL ROAD'
    ROAD = 'ROAD'
    CARBON = 'CARBON'
    TITANIUM = 'TITANIUM'
    PRODUCT_GROUP = [
        (CARBON, 'CARBON'),
        (TITANIUM, 'TITANIUM'),
        (URBAN, 'URBAN'),
        (ALL_ROAD, 'ALL ROAD'),
        (ROAD, 'ROAD'),
    ]

    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPE,
        default=FRAMES,
    )
    product_group = models.CharField(
        max_length=20,
        choices=PRODUCT_GROUP,
        default=CARBON,
    )
    frame = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=120)
    fork = models.CharField(max_length=80)
    wheels = models.CharField(max_length=80, null=True, blank=True)
    tyres = models.CharField(max_length=80, null=True, blank=True)
    max_tyre_size = models.CharField(max_length=80, null=True, blank=True)
    crankset = models.CharField(max_length=80, null=True, blank=True)
    shift_levers = models.CharField(max_length=80, null=True, blank=True)
    derailleurs = models.CharField(max_length=80, null=True, blank=True)
    casette_or_sprocket = models.CharField(max_length=80,
                                           null=True, blank=True)
    chain_or_belt = models.CharField(max_length=80, null=True, blank=True)
    brakes = models.CharField(max_length=80, null=True, blank=False)
    handlebar = models.CharField(max_length=80, null=True, blank=True)
    stem = models.CharField(max_length=80, null=True, blank=True)
    saddle = models.CharField(max_length=80, null=True, blank=True)
    seatpost = models.CharField(max_length=80, null=True, blank=True)
    seat_clamp = models.CharField(max_length=80, null=True, blank=True)
    headset = models.CharField(max_length=80, null=True, blank=True)
    seatpost_diameter = models.CharField(max_length=20, null=True, blank=True)
    bottom_bracket = models.CharField(max_length=80, null=True, blank=True)
    dropouts = models.CharField(max_length=120, null=True, blank=True)
    is_bike = models.BooleanField(default=True, null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1,
                                 null=True, blank=True,
                                 validators=[MinValueValidator(0.01)])
    weight_alloy = models.DecimalField(max_digits=4, decimal_places=1,
                                       null=True, blank=True,
                                       validators=[MinValueValidator(0.01)])
    weight_carbon = models.DecimalField(max_digits=4, decimal_places=1,
                                        null=True, blank=True,
                                        validators=[MinValueValidator(0.01)])
    price = models.DecimalField(max_digits=4, decimal_places=0,
                                null=True, blank=True,
                                validators=[MinValueValidator(1)])
    price_alloy = models.DecimalField(max_digits=4, decimal_places=0,
                                      null=True, blank=True,
                                      validators=[MinValueValidator(1)])
    price_carbon = models.DecimalField(max_digits=4, decimal_places=0,
                                       null=True, blank=True,
                                       validators=[MinValueValidator(1)])
    price_comment = models.CharField(max_length=120, null=True, blank=True)
    image01 = models.ImageField(null=True, blank=False)
    img_url01 = models.URLField(max_length=1024, null=True, blank=True)
    image02 = models.ImageField(null=True, blank=False)
    img_url02 = models.URLField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.name
