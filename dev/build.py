"""Generate the Sublime Text 4 .sublime-color-scheme files for both themes.

Run:  python build.py
Writes  ../<Theme Name>.sublime-color-scheme  (the repository root)

The base (non-JSON) rules and globals are ports of the original ST2/ST3 .tmTheme
files; the JSON depth rules are generated from depth_selectors.py.

Copyright (C) 2026 Lance Duvall
SPDX-License-Identifier: AGPL-3.0-or-later
Project: <https://github.com/lanz/sublime-json-color-schemes>
Licensed under the GNU Affero General Public License, version 3 or later.
See LICENSE, or <https://www.gnu.org/licenses/>.
"""

import io
import json
import os

import depth_selectors as S

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.dirname(HERE)

AUTHOR = "Lance Duvall"

def load_base(filename):
    """Globals and base rules extracted from another theme; see palettes/."""
    path = os.path.join(HERE, "palettes", filename)
    with io.open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    globals_ = sorted(doc["globals"].items())
    rules = [
        (
            r.get("name", ""),
            r["scope"],
            dict(
                (k, r[k])
                for k in ("foreground", "background", "font_style")
                if k in r
            ),
        )
        for r in doc["rules"]
    ]
    return globals_, rules

# --------------------------------------------------------------------------
# Palettes
#
# Both ramps come from the original ST2/ST3 .tmTheme files. Those files had no
# palette to read off, so each rule's nesting depth was recomputed from its scope
# selector and the colors tallied per depth to recover the ramp.
#
# Level 1 is the outermost key, and depth counts objects and arrays alike.
# --------------------------------------------------------------------------

MONOKAI_LEVELS = [
    "#FFFFFF",  # 1
    "#FFFFAA",  # 2
    "#FFAAFF",  # 3
    "#AAFFFF",  # 4
    "#AAAAFF",  # 5
    "#AAFFAA",  # 6
    "#FFAAAA",  # 7
    "#AAAAFA",  # 8   (near-duplicate of level 5 in the original)
    "#AAFAAA",  # 9   (near-duplicate of level 6 in the original)
    "#E6DB74",  # 10
]

# Levels 1-7 are Monokai's own palette: the default foreground, then the colors it
# uses for keywords, parameters, strings, functions, types and constants. Monokai
# only has seven, so levels 8-10 are extensions, picked for maximum separation from
# everything above them at the same saturation and lightness. Every pair of levels
# is at least dE 20 apart, so no two are easy to confuse at a glance.
# Recovered from the later of the two ST3 attempts, where the near-duplicate deep
# levels of MONOKAI_LEVELS were replaced with a distinct purple, pink and teal.
# There the ten colors were held in variables named rainbow1..rainbow10.
# Every pair of levels is at least dE 22 apart, against dE 2.7 for the original.
MONOKAI_CHALK_LEVELS = [
    "#D6D5E3",  # 1
    "#AAFFAA",  # 2
    "#FFAAFF",  # 3
    "#AAFFFF",  # 4
    "#AAAAFF",  # 5
    "#FFAAAA",  # 6
    "#FFFFAA",  # 7
    "#967BB6",  # 8   purple, where the original repeated level 5
    "#FF80AA",  # 9   pink, where the original repeated level 6
    "#21ABCD",  # 10  teal
]

MONOKAI_NEON_LEVELS = [
    "#F8F8F2",  # 1   foreground
    "#F92672",  # 2   keyword pink
    "#FD971F",  # 3   parameter orange
    "#E6DB74",  # 4   string yellow
    "#A6E22E",  # 5   function green
    "#66D9EF",  # 6   type cyan
    "#AE81FF",  # 7   constant purple
    "#4CF0A9",  # 8   extension: mint
    "#3692E2",  # 9   extension: blue
    "#F04CC5",  # 10  extension: magenta
]

JAZZ_LEVELS = [
    "#FFFFFF",  # 1
    "#00B1B3",  # 2
    "#BC9CF0",  # 3
    "#94A2FF",  # 4
    "#0BE9BF",  # 5   tie-break: original mixed #0B9CBF/#0BE9BF here; #0BE9BF
    #                  keeps level 5 distinct from level 8
    "#B8C9EE",  # 6
    "#FFAAFF",  # 7
    "#0B9CBF",  # 8
    "#A094A0",  # 9
    "#C76FB2",  # 10  tie-break: the most common value here was #BC9CF0, which
    #                  collides with level 3; #C76FB2 also occurs at this depth
]

# --------------------------------------------------------------------------
# Theme definitions: globals + base rules, ported from the .tmTheme files.
# tmTheme key -> .sublime-color-scheme global:
#   lineHighlight -> line_highlight, findHighlight -> find_highlight,
#   findHighlightForeground -> find_highlight_foreground,
#   selectionBorder -> selection_border, activeGuide -> active_guide,
#   bracketsForeground -> brackets_foreground, bracketsOptions -> brackets_options,
#   bracketContentsForeground -> bracket_contents_foreground,
#   bracketContentsOptions -> bracket_contents_options, tagsOptions -> tags_options
# --------------------------------------------------------------------------

MONOKAI = {
    "name": "Monokai JSON",
    "filename": "Monokai JSON",
    "blurb": [
        "Ported from my original ST2/ST3 .tmTheme. Built on the Monokai palette by",
        "Wimer Hazenberg. Not affiliated with or endorsed by Monokai or Monokai Pro.",
    ],
    "levels": MONOKAI_LEVELS,
    "variables": [
        ("background", "#272822"),
        ("foreground", "#F8F8F2"),
        ("caret", "#F8F8F0"),
        ("invisibles", "#3B3A32"),
        ("line_highlight", "#3E3D32"),
        ("selection", "#49483E"),
        ("selection_border", "#222218"),
        ("find_highlight", "#FFE792"),
        ("comment", "#75715E"),
        ("string", "#E6DB74"),
        ("purple", "#AE81FF"),
        ("pink", "#F92672"),
        ("cyan", "#66D9EF"),
        ("green", "#A6E22E"),
        ("orange", "#FD971F"),
        ("white", "#F8F8F0"),
    ],
    "globals": [
        ("background", "var(background)"),
        ("foreground", "var(foreground)"),
        ("caret", "var(caret)"),
        ("invisibles", "var(invisibles)"),
        ("line_highlight", "var(line_highlight)"),
        ("selection", "var(selection)"),
        ("selection_border", "var(selection_border)"),
        ("find_highlight", "var(find_highlight)"),
        ("find_highlight_foreground", "#000000"),
        ("active_guide", "#9D550FB0"),
        ("brackets_foreground", "#F8F8F2A5"),
        ("brackets_options", "underline"),
        ("bracket_contents_foreground", "#F8F8F2A5"),
        ("bracket_contents_options", "underline"),
        ("tags_options", "stippled_underline"),
    ],
    "rules": [
        ("Comment", "comment", {"foreground": "var(comment)"}),
        ("String", "string", {"foreground": "var(string)"}),
        ("Number", "constant.numeric", {"foreground": "var(purple)"}),
        ("Built-in constant", "constant.language", {"foreground": "var(purple)"}),
        (
            "User-defined constant",
            "constant.character, constant.other",
            {"foreground": "var(purple)"},
        ),
        ("Variable", "variable", {"font_style": ""}),
        ("Keyword", "keyword", {"foreground": "var(pink)"}),
        ("Storage", "storage", {"foreground": "var(pink)", "font_style": ""}),
        (
            "Storage type",
            "storage.type",
            {"foreground": "var(cyan)", "font_style": "italic"},
        ),
        (
            "Class name",
            "entity.name.class",
            {"foreground": "var(green)", "font_style": "underline"},
        ),
        (
            "Inherited class",
            "entity.other.inherited-class",
            {"foreground": "var(green)", "font_style": "italic underline"},
        ),
        (
            "Function name",
            "entity.name.function",
            {"foreground": "var(green)", "font_style": ""},
        ),
        (
            "Function argument",
            "variable.parameter",
            {"foreground": "var(orange)", "font_style": "italic"},
        ),
        (
            "Tag name",
            "entity.name.tag",
            {"foreground": "var(pink)", "font_style": ""},
        ),
        (
            "Tag attribute",
            "entity.other.attribute-name",
            {"foreground": "var(green)", "font_style": ""},
        ),
        (
            "Library function",
            "support.function",
            {"foreground": "var(cyan)", "font_style": ""},
        ),
        (
            "Library constant",
            "support.constant",
            {"foreground": "var(cyan)", "font_style": ""},
        ),
        (
            "Library class/type",
            "support.type, support.class",
            {"foreground": "var(cyan)", "font_style": "italic"},
        ),
        ("Library variable", "support.other.variable", {"font_style": ""}),
        (
            "Invalid",
            "invalid",
            {
                "foreground": "var(white)",
                "background": "var(pink)",
                "font_style": "",
            },
        ),
        (
            "Invalid deprecated",
            "invalid.deprecated",
            {"foreground": "var(white)", "background": "var(purple)"},
        ),
        ("diff.header", "meta.diff, meta.diff.header", {"foreground": "var(comment)"}),
        ("diff.deleted", "markup.deleted", {"foreground": "var(pink)"}),
        ("diff.inserted", "markup.inserted", {"foreground": "var(green)"}),
        ("diff.changed", "markup.changed", {"foreground": "var(string)"}),
        (
            "Find in files: line number",
            "constant.numeric.line-number.find-in-files - match",
            {"foreground": "#AE81FFA0"},
        ),
        (
            "Find in files: filename",
            "entity.name.filename.find-in-files",
            {"foreground": "var(string)"},
        ),
    ],
}

JAZZ = {
    "name": "Jazz Solo Cup JSON",
    "filename": "Jazz Solo Cup JSON",
    "blurb": [
        "Named after 'Jazz', the teal-and-purple design that Sweetheart Cup",
        "Company printed on disposable cups from 1992: a wide jagged teal stroke",
        "with a thin purple zig-zag above it, and one of the most recognizable",
        "images of 1990s American pop culture. This palette follows that pairing",
        "-- teal as the base, purple as the accent. Only the colors are borrowed;",
        "no part of the design is reproduced. Not affiliated with or endorsed by",
        "Solo Cup Company or Sweetheart Cup Company.",
    ],
    "levels": JAZZ_LEVELS,
    "variables": [
        ("background", "#121719"),
        ("foreground", "#A094A0"),
        ("caret", "#9473FF"),
        ("invisibles", "#0BE9BF"),
        ("line_highlight", "#1C3438"),
        ("selection", "#1C3438"),
        ("selection_border", "#1C3438"),
        ("find_highlight", "#FFE792"),
        ("teal", "#00B1B3"),
        ("mint", "#0BE9BF"),
        ("violet", "#9473FF"),
        ("lavender", "#BC9CF0"),
        ("pink", "#FF9BEC"),
        ("white", "#FFFFFF"),
    ],
    "globals": [
        ("background", "var(background)"),
        ("foreground", "var(foreground)"),
        ("caret", "var(caret)"),
        ("invisibles", "var(invisibles)"),
        ("line_highlight", "var(line_highlight)"),
        ("selection", "var(selection)"),
        ("selection_border", "var(selection_border)"),
        ("find_highlight", "var(find_highlight)"),
        ("find_highlight_foreground", "#000000"),
        ("active_guide", "#9D550FB0"),
        ("brackets_foreground", "var(teal)"),
        ("brackets_options", "underline"),
        ("bracket_contents_foreground", "var(teal)"),
        ("bracket_contents_options", "underline"),
        ("tags_options", "stippled_underline"),
    ],
    "rules": [
        ("Comment", "comment", {"foreground": "var(foreground)"}),
        ("String", "string", {"foreground": "var(mint)"}),
        ("Plaintext", "text.html", {"foreground": "var(violet)"}),
        ("Number", "constant.numeric", {"foreground": "var(pink)"}),
        ("Built-in constant", "constant.language", {"foreground": "var(pink)"}),
        (
            "User-defined constant",
            "constant.character, constant.other",
            {"foreground": "var(teal)"},
        ),
        ("Variable", "variable", {"font_style": ""}),
        ("Keyword", "keyword", {"foreground": "var(pink)"}),
        ("Storage", "storage", {"foreground": "var(pink)", "font_style": ""}),
        (
            "Storage type",
            "storage.type",
            {"foreground": "var(teal)", "font_style": "italic"},
        ),
        (
            "Class name",
            "entity.name.class",
            {"foreground": "var(teal)", "font_style": "underline"},
        ),
        (
            "Inherited class",
            "entity.other.inherited-class",
            {"foreground": "var(teal)", "font_style": "italic underline"},
        ),
        (
            "Function name",
            "entity.name.function",
            {"foreground": "var(white)", "font_style": ""},
        ),
        (
            "Function argument",
            "variable.parameter",
            {"foreground": "var(mint)", "font_style": "italic"},
        ),
        ("Tag name", "entity.name.tag", {"foreground": "var(teal)", "font_style": ""}),
        (
            "Tag attribute",
            "entity.other.attribute-name",
            {"foreground": "var(lavender)", "font_style": ""},
        ),
        (
            "Library function",
            "support.function",
            {"foreground": "var(white)", "font_style": ""},
        ),
        (
            "Library constant",
            "support.constant",
            {"foreground": "var(lavender)", "font_style": ""},
        ),
        (
            "Library class/type",
            "support.type, support.class",
            {"foreground": "var(lavender)", "font_style": "italic"},
        ),
        ("Library variable", "support.other.variable", {"font_style": ""}),
        (
            "Invalid",
            "invalid",
            {
                "foreground": "#F8F8F0",
                "background": "var(teal)",
                "font_style": "",
            },
        ),
        (
            "Invalid deprecated",
            "invalid.deprecated",
            {"foreground": "#F8F8F0", "background": "var(pink)"},
        ),
        ("diff.header", "meta.diff, meta.diff.header", {"foreground": "#75715E"}),
        ("diff.deleted", "markup.deleted", {"foreground": "var(teal)"}),
        ("diff.inserted", "markup.inserted", {"foreground": "var(lavender)"}),
        ("diff.changed", "markup.changed", {"foreground": "var(lavender)"}),
        (
            "Find in files: line number",
            "constant.numeric.line-number.find-in-files - match",
            {"foreground": "#FF9BECA0"},
        ),
        (
            "Find in files: filename",
            "entity.name.filename.find-in-files",
            {"foreground": "var(lavender)"},
        ),
    ],
}

# Same base palette, globals and syntax rules as Monokai JSON; only the depth ramp
# and the identifying fields differ.
MONOKAI_CHALK = dict(
    MONOKAI,
    name="Monokai Chalk JSON",
    filename="Monokai Chalk JSON",
    levels=MONOKAI_CHALK_LEVELS,
    blurb=[
        "Monokai JSON's soft pastels, but with all ten levels actually distinct:",
        "the second pass at that ramp swapped its near-duplicate deep levels for a",
        "purple, a pink and a teal of their own. Built on the Monokai palette by",
        "Wimer Hazenberg. Not affiliated with or endorsed by Monokai or Monokai Pro.",
    ],
)

MONOKAI_NEON = dict(
    MONOKAI,
    name="Monokai Neon JSON",
    filename="Monokai Neon JSON",
    levels=MONOKAI_NEON_LEVELS,
    blurb=[
        "Monokai JSON with the color turned up: the depth ramp uses Monokai's own",
        "accent colors at full strength rather than pastel tints of them. Built on",
        "the Monokai palette by Wimer Hazenberg. Not affiliated with or endorsed by",
        "Monokai or Monokai Pro.",
    ],
)

# Monokai Neue's own ramp is six Monokai accents on a six-level cycle, kept
# as authored. Its JSON support covered object keys in objects only, so the
# generated rules add arrays, values, numbers and booleans.
MONOKAI_NEUE_LEVELS = [
    "#66D9EF",  # 1  cyan
    "#AE81FF",  # 2  purple
    "#F92672",  # 3  pink
    "#A6E22E",  # 4  green
    "#FD971F",  # 5  orange
    "#E6DB74",  # 6  yellow
]

_NEUE_GLOBALS, _NEUE_RULES = load_base("monokai-neue-base.json")

MONOKAI_NEUE = {
    "name": "Monokai Neue JSON",
    "filename": "Monokai Neue JSON",
    "blurb": [
        "Monokai Neue by Josh Kaplan, with a fuller set of depth rules. Neue",
        "colored object keys in objects; this adds arrays, string values,",
        "numbers and booleans, and carries the ramp past level 10. Its six-color",
        "cycle is unchanged.",
        "",
        "Derived from Monokai Neue, Copyright (c) 2015 Josh Kaplan",
    ],
    "levels": MONOKAI_NEUE_LEVELS,
    "variables": [],
    "globals": _NEUE_GLOBALS,
    "rules": _NEUE_RULES,
}

KIND_LABEL = {
    "key": "object key",
    "string": "string value / array element",
    "number": "number",
    "constant": "true / false / null",
}

HEADER = """\
// {name} -- Sublime Text 4 color scheme
//
{blurb}// Every level of JSON nesting gets its own color, so you can see at a glance
// which level a piece of content belongs to. Levels 1-{palette} use the palette
// below, then it cycles: level {next} reuses json_level1, and so on to level
// {maxlevel}. Anything nested deeper than {maxlevel} keeps the level {maxlevel} color.
//
// Sublime Text 4's JSON syntax nests
// `meta.mapping.value.json` / `meta.sequence.json` (not `meta.mapping.json`), and
// a run of N `meta` atoms matches anything nested N deep or deeper. That leaves
// every shallower rule matching a deep token as well, so each depth rule below is
// made mutually exclusive with `- <deeper chain>`: level N means "at least N deep"
// AND NOT "at least N+1 deep". Exactly one rule can match a given token, which
// keeps the result independent of how Sublime ranks competing rules.
// Verified against ST4 build 4200.
//
// To recolor a level, edit json_level1..json_level{palette} -- nothing else needs to change.
// Generated by dev/build.py; edit that rather than this file.
//
// Copyright (C) 2026 Lance Duvall
// SPDX-License-Identifier: AGPL-3.0-or-later
// Project: https://github.com/lanz/sublime-json-color-schemes
// Licensed under the GNU Affero General Public License, version 3 or later.
// See LICENSE, or <https://www.gnu.org/licenses/>.
"""


def q(s):
    return '"%s"' % s


def _blurb(theme):
    """The theme's note as a comment block, or nothing if it has none."""
    lines = theme.get("blurb")
    if not lines:
        return ""
    out = ""
    for line in lines:
        out += ("// %s\n" % line) if line else "//\n"
    return out + "//\n"


def render(theme):
    max_level = S.MAX_LEVEL
    palette_size = len(theme["levels"])
    out = io.StringIO()
    out.write(
        HEADER.format(
            name=theme["name"],
            blurb=_blurb(theme),
            palette=palette_size,
            next=palette_size + 1,
            maxlevel=max_level,
        )
    )
    out.write("{\n")
    out.write('\t"name": %s,\n' % q(theme["name"]))
    out.write('\t"author": %s,\n' % q(AUTHOR))
    out.write('\t"variables":\n\t{\n')
    for k, v in theme["variables"]:
        out.write("\t\t%s: %s,\n" % (q(k), q(v)))
    out.write("\n\t\t// JSON nesting levels, outermost first.\n")
    for i, color in enumerate(theme["levels"], 1):
        out.write("\t\t%s: %s,\n" % (q("json_level%d" % i), q(color)))
    out.write("\t},\n")

    out.write('\t"globals":\n\t{\n')
    for k, v in theme["globals"]:
        out.write("\t\t%s: %s,\n" % (q(k), q(v)))
    out.write("\t},\n")

    out.write('\t"rules":\n\t[\n')
    for name, scope, settings in theme["rules"]:
        out.write("\t\t{\n")
        out.write("\t\t\t%s: %s,\n" % (q("name"), q(name)))
        out.write("\t\t\t%s: %s,\n" % (q("scope"), q(scope)))
        for key in ("foreground", "background", "font_style"):
            if key in settings:
                out.write("\t\t\t%s: %s,\n" % (q(key), q(settings[key])))
        out.write("\t\t},\n")

    last_kind = None
    for kind, level, slot, selector in S.all_rules(max_level, palette_size):
        if kind != last_kind:
            out.write(
                "\n\t\t// ---- JSON depth: %s ----\n" % KIND_LABEL[kind]
            )
            last_kind = kind
        out.write("\t\t{\n")
        out.write(
            "\t\t\t%s: %s,\n"
            % (q("name"), q("JSON level %d %s" % (level, KIND_LABEL[kind])))
        )
        out.write("\t\t\t%s: %s,\n" % (q("scope"), q(selector)))
        out.write(
            "\t\t\t%s: %s,\n" % (q("foreground"), q("var(json_level%d)" % slot))
        )
        out.write("\t\t},\n")
    out.write("\t],\n}\n")
    return out.getvalue()


def main():
    for theme in (MONOKAI, MONOKAI_CHALK, MONOKAI_NEON, MONOKAI_NEUE, JAZZ):
        path = os.path.join(
            OUT_ROOT, theme["filename"] + ".sublime-color-scheme"
        )
        text = render(theme)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s (%d bytes)" % (path, len(text.encode("utf-8"))))


if __name__ == "__main__":
    main()
