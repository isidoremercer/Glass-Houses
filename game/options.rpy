## options.rpy — Game configuration

define config.name = _("Glass Houses")

define gui.show_name = False

define config.version = "1.0"

define gui.about = _p("""A visual novel about five girls in a share house, the versions of themselves they present, and what it means to truly see someone.

Created by Isidore & Mercer""")

define build.name = "GlassHouses"

define config.window_icon = "gui/window_icon.png"

## Sounds and music
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

## Transitions
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## Window behavior — "auto" shows/hides based on dialogue vs narration
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Text speed defaults
default preferences.text_cps = 40
default preferences.afm_time = 15
