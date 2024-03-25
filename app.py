"""
app code.

"""

import random

from flask import Flask
from markupsafe import escape

from ecapybara import ecapyworld

app = Flask(__name__)


@app.get("/")
def root_page():
    """
    Tell the user how to use web verison.
    """
    message = """
    How to use: call the API with /rule_number/iterations/,<br />
    where 0 <= rule_number <= 255 and 0 <= iterations <= 1000. <br />
    Known limitations: width currently fixed at 180 chars wide.
    """
    return message


@app.get("/<int:rule>/<int:itercount>/")
def get_initial_params(rule, itercount):
    """
    Set the initial parameters of the universe from user input.
    One fixed value, width, to be dynamic later.
    """
    rule = int(escape(rule))
    itercount = int(escape(itercount))
    colors = get_colors()
    if rule < 0 or rule > 255:
        return "error: rule must be in range 0 - 255."
    if itercount < 0 or itercount > 1000:
        return "error: iterations must be in range 0 - 1000"
    # TODO width currently fixed at 180
    # js: window.innerWidth could get dynamic val
    return eca_driver(180, rule, itercount, colors)

def get_colors():
    """
    Randomly choose a pair of complementary colors.
    """
    color_choices = [["blue", "orange"], ["red", "green"], ["yellow", "purple"]]
    color_pair = random.choice(color_choices)
    color_a = color_pair[0]
    color_b = color_pair[1]
    return (color_a, color_b)

def eca_driver(width: int, rule: int, itercount: int, colors: set):
    """
    Does the main iteration for the colorized web version.
    """
    color_a = colors[0]
    color_b = colors[1]
    ecapy = ecapyworld.Ecapyworld(width)
    output = '<pre style="display:inline-block; line-height: 1em;">'
    trule = ecapy.ruleset[rule]
    for _ in range(itercount):
        ecapy.iterate_state(trule)
    return ecapy.webtextmode(color_a, color_b) + "</pre>"


# TODO add links back and forth between rules
