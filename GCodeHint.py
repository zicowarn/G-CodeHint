#!/usr/bin/env python
# Apache License Version 2
# Copyright [2016] Zhichao Wang and Cmatek GmbH

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: zhichao, wang <zhichao.wang@camtek.de>
.. main moudle for the sublime text 2 plugin named GCodehint
"""

__author__ = 'zhichao,wang'
__email__ = 'zhichao.wang@camtek.de'
__url__ = 'http://www.camtek.de/'
__version__ = '0.1'
__license__ = 'Apache License Version 2'
__status__ = 'Beta'
__revision__ = '$Rev: 03 $'
__date__ = '2016-02-18 12:32:11'


import sublime, sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
    """
    """

    TAG = "===> Description of CN-Code : "

    def run(self, edit):
        """
        """
        # self.view.insert(edit, 0, "Hello, World!")
        sublime.status_message(ExampleCommand.TAG + ".. Try to start plugin!!!")
        fileName = self.view.file_name()
        if fileName.lower().__contains__(".nc"):
            chooseWord = self.focusChoose()
            print chooseWord
            for k in chooseWord:
                if k not in Letter_Description.keys():
                    sublime.status_message(ExampleCommand.TAG + "Sorry, not found this key word")
                    return
                else:
                    break
            if chooseWord.__contains__("M") and len(chooseWord) != 1:
                sublime.status_message(ExampleCommand.TAG + self.getMCodeDescription(chooseWord))
            elif chooseWord.__contains__("G") and len(chooseWord) != 1:
                sublime.status_message(ExampleCommand.TAG + self.getGCodeDescription(chooseWord))
            elif chooseWord.__contains__("N") and len(chooseWord) != 1:
                sublime.status_message(ExampleCommand.TAG + self.getLAddrDescription("N"))
            else:
                sublime.status_message(ExampleCommand.TAG + self.getLAddrDescription(chooseWord[0]))

    def focusChoose(self):
        region1 = self.view.sel()[0]
        return self.view.substr(region1)

    def getMCodeDescription(self, key=None):
        try:
            return M_Code_Description[key]
        except KeyError:
            return "Not found"

    def getGCodeDescription(self, key=None):
        try:
            return G_Code_Description[key]
        except KeyError:
            return "Not found"

    def getLAddrDescription(self, key=None):
        try:
            return Letter_Description[key]
        except KeyError:
            return "Not found"


M_Code_Description = {
    "M00": "Compulsory Stop",
    "M01": "Optinal Stop",
    "M02": "End of Programm",
    "M03": "Spindle on (clockwise rotation)",
    "M04": "Spindle on (counterclockwise rotation)",
    "M05": "Spindle stop",
    "M06": "Automatic tool change (ATC)",
    "M07": "Coolant on (mist)",
    "M08": "Coolant on (float)",
    "M09": "Coolant off",
    "M10": "Pallet clamp on",
    "M11": "Pallet clamp off",
    "M13": "Spindle on (clockwise rotation and coolant on <float>)",
    "M19": "Spindle orientation",
    "M21": "<* Permanently unassigned> in case: Mirror x-axis or tailstock forward",
    "M22": "<* Permanently unassigned> in case: Mirror y-axis or tailstock backward",
    "M23": "<* Permanently unassigned> in case: Mirror off or Thread gradual pullout ON",
    "M24": "<* Permanently unassigned> Thread gradual pullout OFF",
    "M25": "<* Permanently unassigned>",
    "M26": "<* Permanently unassigned>",
    "M27": "<* Permanently unassigned>",
    "M28": "<* Permanently unassigned>",
    "M29": "<* Permanently unassigned>",
    "M30": "End of programm, with return to programm top",
    "M41": "Gear select -- gear 1",
    "M42": "Gear select -- gear 2",
    "M43": "Gear select -- gear 3",
    "M44": "Gear select -- gear 4",
    "M48": "Feedrate override allowed",
    "M49": "Feedrate override  NOT allowed",
    "M52": "Unload Last tool from spindle",
    "M60": "Automatic pallet change (APC)",
    "M98": "Subprogram call",
    "M99": "Subprogram end",
    }

G_Code_Description = {
    "G00": "Rapid positioning",
    "G01": "Linear interpolation",
    "G02": "Circular interpolation, clockwise",
    "G03": "Circular interpolation, counterclockwise",
    "G04": "Dwell",
    "G05": "<P10000> High-precision contour control (HPCC) or something else",
    "G06": "Non-uniform rational B-spline(NURBS) Machining",
    "G07": "Imaginary axis designation",
    "G09": "Exact stop check, non-modal",
    "G10": "Programmable data input",
    "G11": "Data write cancel",
    "G12": "Full-circle interpolation, clockwise",
    "G13": "Full-circle interpolation, counterclockwise",
    "G17": "XY plane selection",
    "G18": "ZX plane selection",
    "G19": "YZ plane selection",
    "G20": "Programming ininches",
    "G21": "Programming inmillimeters (mm)",
    "G28": "Return to home position (machine zero, aka machine reference point)",
    "G30": "Return to secondary home position (machine zero, aka machine reference point)",
    "G31": "Skip function (used for probes and tool length measurement systems)",
    "G32": "Single-point threading, longhand style (if not using a cycle, e.g.. G76)",
    "G33": "Constant-pitchthreading or Single-point threading, longhand style (if not using a cycle, e.g.. G76)",
    "G34": "Variable pitch threading",
    "G40": "Tool radius compensation off",
    "G41": "Tool radius compensation left",
    "G42": "Tool radius compensation right",
    "G43": "Tool height offset compensation negative",
    "G44": "Tool height offset compensation positive",
    "G45": "Axis offset single increase",
    "G46": "Axis offset single decrease",
    "G47": "Axis offset double increase",
    "G48": "Axis offset double decrease",
    "G49": "Tool length offset compensation cancel",
    "G50": "Define the maximum spindle speed",
    "G51": "Local coordinate system (LCS)",
    "G52": "Define the maximum spindle speed",
    "G53": "Machine coordinate system",
    "G54": "Work coordinate systems (WCSs) or Extended work coordinate systems",
    "G55": "Work coordinate systems (WCSs)",
    "G56": "Work coordinate systems (WCSs)",
    "G57": "Work coordinate systems (WCSs)",
    "G58": "Work coordinate systems (WCSs)",
    "G59": "Work coordinate systems (WCSs)",
    "G61": "Exact stop check, modal",
    "G62": "Automatic corner override",
    "G64": "Default cutting mode (cancel exact stop check mode)",
    "G70": "Fixed cycle, multiple repetitive cycle, for finishing (including contours)",
    "G71": "Fixed cycle, multiple repetitive cycle, for roughing (Z-axis emphasis)",
    "G72": "Fixed cycle, multiple repetitive cycle, for roughing (X-axis emphasis)",
    "G73": "Fixed cycle, multiple repetitive cycle, for roughing, with pattern repetition or Peck drilling cycle for,"
           " milling - high-speed (NO full retraction from pecks)",
    "G74": "Peck drilling cycle for turning or Tapping cycle for milling, lefthand thread, M04 spindle direction",
    "G75": "Peck grooving cycle for turning",
    "G76": "Fine boring cycle for milling or Threading cycle for turning, multiple repetitive cycle",
    "G80": "Cancel canned cycle",
    "G81": "Simple drilling cycle",
    "G82": "Drilling cycle with dwell",
    "G83": "Peck drilling cycle (full retraction from pecks)",
    "G84": "Tapping cycle, right hand thread, M03 spindle direction",
    "G85": "boring cycle, feed in/feed out",
    "G86": "boring cycle, feed in/spindle stop/rapid out",
    "G87": "boring cycle, backboring",
    "G88": "boring cycle, feed in/spindle stop/manual operation",
    "G89": "boring cycle, feed in/dwell/feed out",
    "G90": "Absolute programming",
    "G91": "Incremental programming",
    "G92": "Position register (programming of vector from part zero to tool tip)",
    "G94": "Feedrate per minute or Fixed cycle, simple cycle, for roughing (X-axis emphasis)",
    "G95": "Feedrate per revolution or",
    "G96": "Constant surface speed (CSS)",
    "G97": "Constant spindle speed",
    "G98": "Return to initial Z level in canned cycle",
    "G99": "Return to R level in canned cycle or Feed rate per revolution (group type A)",
    }

Letter_Description = {
    "A": "Absolute or incremental position of A axis (rotational axis around X axis)",
    "B": "Absolute or incremental position of A axis (rotational axis around Y axis)",
    "C": "Absolute or incremental position of A axis (rotational axis around C axis)",
    "D": "Defines diameter or radial offset used for cutter compensation. D is used for depth of cut on lathes."
         " It is used for aperture selection and commands on photoplotters.",
    "E": "Precision feed rate for threading on lathes",
    "F": "Defines feed rate",
    "I": "Defines arc center in X axis for G02 or G03 arc commands",
    "J": "Defines arc center in Y axis for G02 or G03 arc commands",
    "K": "Defines arc center in Z axis for G02 or G03 arc commands",
    "G": "Address for preparatory commands",
    "M": "Miscellaneous function",
    "N": "Line (block) number in program",
    "O": "Program name",
    "W": "Incremental axis corresponding to Z axis (typically only lathe group A controls)",
    "X": "Absolute or incremental position of X axis.",
    "Y": "Absolute or incremental position of Y axis.",
    "Z": "Absolute or incremental position of Z axis."
}
