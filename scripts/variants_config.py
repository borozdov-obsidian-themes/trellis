"""Which sibling themes become Style Settings variants of this one."""

ID = "borozdov-trellis"  # Style Settings section id and the body-class prefix
NAME = "Borozdov Trellis"
DEFAULT_LABEL = "Trellis"

# (repository folder next to this one, label in the Variant menu)
MEMBERS = [
    ("terrarium", "Terrarium"),
    ("herbarium", "Herbarium"),
    ("understory", "Understory"),
    ("voltage", "Voltage"),
    ("spruce", "Spruce"),
    ("canopy", "Canopy"),
    ("tonic", "Tonic"),
    ("apothecary", "Apothecary"),
    ("cultivar", "Cultivar"),
    ("kite", "Kite"),
    ("atelier", "Atelier"),
    ("riverstone", "Riverstone"),
    ("glacier", "Glacier"),
]

# Palette names of this theme that no Obsidian variable reads in section 3:
# which of the sibling's resolved variables to take for them instead.
ALIASES = {
    "--caption": "--text-muted",
    "--meadow": "--tag-background",
    "--on-meadow": "--tag-color",
    "--on-mark": "--text-normal",
}

# The palette name the highlight rule colours its text with: the generator
# picks whichever of the sibling's text and canvas reads on its highlight.
MARK_TEXT = "--on-mark"
