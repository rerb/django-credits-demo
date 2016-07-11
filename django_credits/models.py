from django.db import models


BOUNCE = "bounce"
FLASH = "flash"
PULSE = "pulse"
RUBBER_BAND = "rubberBand"
SHAKE = "shake"
HEAD_SHAKE = "headShake"
SWING = "swing"
TADA = "tada"
WOBBLE = "wobble"
JELLO = "jello"
BOUNCE_IN = "bounceIn"
BOUNCE_IN_DOWN = "bounceInDown"
BOUNCE_IN_LEFT = "bounceInLeft"
BOUNCE_IN_RIGHT = "bounceInRight"
BOUNCE_IN_UP = "bounceInUp"
BOUNCE_OUT = "bounceOut"
BOUNCE_OUT_DOWN = "bounceOutDown"
BOUNCE_OUT_LEFT = "bounceOutLeft"
BOUNCE_OUT_RIGHT = "bounceOutRight"
BOUNCE_OUT_UP = "bounceOutUp"
FADE_IN = "fadeIn"
FADE_IN_DOWN = "fadeInDown"
FADE_IN_DOWN_BIG = "fadeInDownBig"
FADE_IN_LEFT = "fadeInLeft"
FADE_IN_LEFT_BIG = "fadeInLeftBig"
FADE_IN_RIGHT = "fadeInRight"
FADE_IN_RIGHT_BIG = "fadeInRightBig"
FADE_IN_UP = "fadeInUp"
FADE_IN_UP_BIG = "fadeInUpBig"
FADE_OUT = "fadeOut"
FADE_OUT_DOWN = "fadeOutDown"
FADE_OUT_DOWN_BIG = "fadeOutDownBig"
FADE_OUT_LEFT = "fadeOutLeft"
FADE_OUT_LEFT_BIG = "fadeOutLeftBig"
FADE_OUT_RIGHT = "fadeOutRight"
FADE_OUT_RIGHT_BIG = "fadeOutRightBig"
FADE_OUT_UP = "fadeOutUp"
FADE_OUT_UP_BIG = "fadeOutUpBig"
FLIP_IN_X = "flipInX"
FLIP_IN_Y = "flipInY"
FLIP_OUT_X = "flipOutX"
FLIP_OUT_Y = "flipOutY"
LIGHTSPEED_IN = "lightspeedIn"
LIGHTSPEED_OUT = "lightspeedOut"
ROTATE_IN = "rotateIn"
ROTATE_IN_DOWN_LEFT = "rotateInDownLeft"
ROTATE_IN_DOWN_RIGHT = "rotateInDownRight"
ROTATE_IN_UP_LEFT = "rotateInUpLeft"
ROTATE_IN_UP_RIGHT = "rotateInUpRight"
ROTATE_OUT = "rotateOut"
ROTATE_OUT_DOWN_LEFT = "rotateOutDownLeft"
ROTATE_OUT_DOWN_RIGHT = "rotateOutDownRight"
ROTATE_OUT_UP_LEFT = "rotateOutUpLeft"
ROTATE_OUT_UP_RIGHT = "rotateOutUpRight"
HINGE = "hinge"
ROLL_In = "rollIn"
ROLL_OUT = "rollOut"
ZOOM_IN = "zoomIn"
ZOOM_IN_DOWN = "zoomInDown"
ZOOM_IN_LEFT = "zoomInLeft"
ZOOM_IN_RIGHT = "zoomInRight"
ZOOM_IN_UP = "zoomInUp"
ZOOM_OUT = "zoomOut"
ZOOM_OUT_DOWN = "zoomOutDown"
ZOOM_OUT_LEFT = "zoomOutLeft"
ZOOM_OUT_RIGHT = "zoomOutRight"
ZOOM_OUT_UP = "zoomOutUp"
SLIDE_IN_DOWN = "slideInDown"
SLIDE_IN_LEFT = "slideInLeft"
SLIDE_IN_RIGHT = "slideInRight"
SLIDE_IN_UP = "slideInUp"
SLIDE_OUT_DOWN = "slideOutDown"
SLIDE_OUT_LEFT = "slideOutLeft"
SLIDE_OUT_RIGHT = "slideOutRight"
SLIDE_OUT_UP = "slideOutUp"

ANIMATION_CHOICES = (
    (BOUNCE, "Bounce"),
    (FLASH, "Flash"),
    (PULSE, "Pulse"),
    (RUBBER_BAND, "Rubber Band"),
    (SHAKE, "Shake"),
    (HEAD_SHAKE, "Head Shake"),
    (SWING, "Swing"),
    (TADA, "Tada"),
    (WOBBLE, "Wobble"),
    (JELLO, "Jello"),
    (BOUNCE_IN, "Bounce In"),
    (BOUNCE_IN_DOWN, "Bounce In Down"),
    (BOUNCE_IN_LEFT, "Bounce In Left"),
    (BOUNCE_IN_RIGHT, "Bounce In Right"),
    (BOUNCE_IN_UP, "Bounce In Up"),
    (BOUNCE_OUT, "Bounce Out"),
    (BOUNCE_OUT_DOWN, "Bounce Out Down"),
    (BOUNCE_OUT_LEFT, "Bounce Out Left"),
    (BOUNCE_OUT_RIGHT, "Bounce Out Right"),
    (BOUNCE_OUT_UP, "Bounce Out Up"),
    (FADE_IN, "Fade In"),
    (FADE_IN_DOWN, "Fade In Down"),
    (FADE_IN_DOWN_BIG, "Fade In Down Big"),
    (FADE_IN_LEFT, "Fade In Left"),
    (FADE_IN_LEFT_BIG, "Fade In Left Big"),
    (FADE_IN_RIGHT, "Fade In Right"),
    (FADE_IN_RIGHT_BIG, "Fade In Right Big"),
    (FADE_IN_UP, "Fade In Up"),
    (FADE_IN_UP_BIG, "Fade In Up Big"),
    (FADE_OUT, "Fade Out"),
    (FADE_OUT_DOWN, "Fade Out Down"),
    (FADE_OUT_DOWN_BIG, "Fade Out Down Big"),
    (FADE_OUT_LEFT, "Fade Out Left"),
    (FADE_OUT_LEFT_BIG, "Fade Out Left Big"),
    (FADE_OUT_RIGHT, "Fade Out Right"),
    (FADE_OUT_RIGHT_BIG, "Fade Out Right Big"),
    (FADE_OUT_UP, "Fade Out Up"),
    (FADE_OUT_UP_BIG, "Fade Out Up Big"),
    (FLIP_IN_X, "Flip In X"),
    (FLIP_IN_Y, "Flip In Y"),
    (FLIP_OUT_X, "Flip Out X"),
    (FLIP_OUT_Y, "Flip Out Y"),
    (LIGHTSPEED_IN, "Lightspeed In"),
    (LIGHTSPEED_OUT, "Lightspeed Out"),
    (ROTATE_IN, "Rotate In"),
    (ROTATE_IN_DOWN_LEFT, "Rotate In Down Left"),
    (ROTATE_IN_DOWN_RIGHT, "Rotate In Down Right"),
    (ROTATE_IN_UP_LEFT, "Rotate In Up Left"),
    (ROTATE_IN_UP_RIGHT, "Rotate In Up Right"),
    (ROTATE_OUT, "Rotate Out"),
    (ROTATE_OUT_DOWN_LEFT, "Rotate Out Down Left"),
    (ROTATE_OUT_DOWN_RIGHT, "Rotate Out Down Right"),
    (ROTATE_OUT_UP_LEFT, "Rotate Out Up Left"),
    (ROTATE_OUT_UP_RIGHT, "Rotate Out Up Right"),
    (HINGE, "Hinge"),
    (ROLL_In, "Roll In"),
    (ROLL_OUT, "Roll Out"),
    (ZOOM_IN, "Zoom In"),
    (ZOOM_IN_DOWN, "Zoom In Down"),
    (ZOOM_IN_LEFT, "Zoom In Left"),
    (ZOOM_IN_RIGHT, "Zoom In Right"),
    (ZOOM_IN_UP, "Zoom In Up"),
    (ZOOM_OUT, "Zoom Out"),
    (ZOOM_OUT_DOWN, "Zoom Out Down"),
    (ZOOM_OUT_LEFT, "Zoom Out Left"),
    (ZOOM_OUT_RIGHT, "Zoom Out Right"),
    (ZOOM_OUT_UP, "Zoom Out Up"),
    (SLIDE_IN_DOWN, "Slide In Down"),
    (SLIDE_IN_LEFT, "Slide In Left"),
    (SLIDE_IN_RIGHT, "Slide In Right"),
    (SLIDE_IN_UP, "Slide In Up"),
    (SLIDE_OUT_DOWN, "Slide Out Down"),
    (SLIDE_OUT_LEFT, "Slide Out Left"),
    (SLIDE_OUT_RIGHT, "Slide Out Right"),
    (SLIDE_OUT_UP, "Slide Out Up"),
)


class AnimatedModel(models.Model):

    class Meta:
        abstract = True

    entrance_animation = models.CharField(max_length=32,
                                          choices=ANIMATION_CHOICES,
                                          blank=True,
                                          null=True)
    exit_animation = models.CharField(max_length=32,
                                      choices=ANIMATION_CHOICES,
                                      blank=True,
                                      null=True)


class Contributor(models.Model):

    given_name = models.CharField(max_length=255,
                                  blank=True,
                                  null=True)
    family_name = models.CharField(max_length=255,
                                   blank=True,
                                   null=True,
                                   db_index=True)

    class Meta:
        ordering = ("family_name", "given_name")

    def __str__(self):
        u = ""
        if self.given_name:
            u = self.given_name
            if self.family_name:
                u += " "
        if self.family_name:
            u += self.family_name
        return u


class Credit(AnimatedModel, models.Model):

    headline = models.CharField(max_length=255)
    contributors = models.ManyToManyField(Contributor,
                                          through="Contribution",
                                          blank=True)
    ordinal = models.PositiveIntegerField(blank=True,
                                          db_index=True)

    class Meta:
        ordering = ("ordinal",)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if not self.ordinal:
            last_credit = Credit.objects.last()
            self.ordinal = last_credit.ordinal + 1 if last_credit else 1
        return super().save(*args, *kwargs)


class Contribution(AnimatedModel, models.Model):
    contributor = models.ForeignKey(Contributor,
                                    on_delete=models.CASCADE)
    credit = models.ForeignKey(Credit,
                               on_delete=models.CASCADE)
