################################################################################
#
#  Ole Miss ASCII Art
#
#  Displays Ole Miss branded ASCII art in team colors
#
################################################################################

import datetime as dt
from segment_parent import SegmentParent

INTRO = 'ASCII ART BY METAL SHOP'

RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'

class Segment(SegmentParent):

    def __init__(self, display, init):
        super().__init__(display, init, default_refresh=99999, default_intro=INTRO)

    def refresh_data(self):
        self.data = {'fetched_on': dt.datetime.now()}

    def pr(self, color, text):
        self.d.set_color(color)
        self.d.print(text)

    def pr_38_v4(self, text):
        for c in text:
            if c in '/\\_|<':
                self.d.set_color(BLUE)
            elif c == '#':
                self.d.set_color(RED)
            elif c == '$':
                self.d.set_color(BLUE)
            self.d.print(c, end='')
        self.d.print('')

    def show(self, fmt):
        if self.data_is_stale():
            self.refresh_data()
        d = self.d

        # 38 v4
        d.newline()
        self.pr(WHITE,' YOU ARE WATCHING CHANNEL')
        d.newline()
        self.pr_38_v4('  $$$$$$$$$$$$$$$$$$$$$$ ')
        self.pr_38_v4(' $$$######\\$$$######\\$$$$')
        self.pr_38_v4(' $$## ___##\\$##  __##\\$$$')
        self.pr_38_v4(' $$\\_/$$$## |## /$$## |$$')
        self.pr_38_v4(' $$$$##### /$$######  |$$')
        self.pr_38_v4(' $$$$\\___##\$##  __##<$$$')
        self.pr_38_v4(' $$##\\$$$## |## /$$## |$$')
        self.pr_38_v4(' $$\\######  |\\######  |$$')
        self.pr_38_v4(' $$$\\______/$$\\______/$$$')
        self.pr_38_v4('  $$$$$$$$$$$$$$$$$$$$$$ ')
        d.newline()
        for c in ' A METAL SHOP PRODUCTION':
            self.d.set_color(WHITE)
            self.d.print(c, end='')
        self.d.wait_beats(5)
        d.newline()