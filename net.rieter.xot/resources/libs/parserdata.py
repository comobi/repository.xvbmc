#==============================================================================
# LICENSE Retrospect-Framework - CC BY-NC-ND
#===============================================================================
# This work is licenced under the Creative Commons
# Attribution-Non-Commercial-No Derivative Works 3.0 Unported License. To view a
# copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/3.0/
# or send a letter to Creative Commons, 171 Second Street, Suite 300,
# San Francisco, California 94105, USA.
#===============================================================================

import re


class ParserData(object):
    __slots__ = ["Name", "Match", "PreProcessor",
                 "Parser", "Creator", "Updater",
                 "IsJson", "MatchType", "LogOnRequired"]

    # define them here so we can just refer to them instead of using the strings all
    # over the place. The values are self explaining.
    MatchStart = "MatchStart"
    MatchEnd = "MatchEnd"
    MatchContains = "Contains"
    MatchExact = "Exact"
    MatchRegex = "Regex"

    # noinspection PyPropertyAccess
    def __init__(self, match):
        """ Creates an instance of ParserData with default values for the properties. """
        self.Match = match
        self.Name = None
        self.PreProcessor = None
        self.Parser = None
        self.Creator = None
        self.Updater = None
        self.IsJson = False
        self.LogOnRequired = False
        self.MatchType = ParserData.MatchStart

    def IsVideoUpdaterOnly(self):
        """ Return whether only this instance is used for updating only """

        return \
            self.PreProcessor is None \
            and self.Parser is None \
            and self.Creator is None \
            and self.Updater is not None

    def IsGenericPreProcessor(self):
        """ Returns True if only a pre-processor is defined. In that case it should be considered a generic
        pre-processor that needs to be processed before other data.

        @return: boolean

        """

        return \
            (self.PreProcessor is not None) \
            and self.Parser is None and self.Creator is None and self.Updater is None

    def Matches(self, url):
        """ Returns true if the DataParser matches the URL.

        @param url: The URL to match
        @return:    Returns True if a match was found

        """

        if self.MatchType == ParserData.MatchStart:
            return url.startswith(self.Match)
        if self.MatchType == ParserData.MatchEnd:
            return url.endswith(self.Match)
        if self.MatchType == ParserData.MatchExact:
            return url == self.Match
        if self.MatchType == ParserData.MatchRegex:
            return re.match(self.Match, url, re.DOTALL + re.IGNORECASE) is not None
        else:
            return self.Match in url

    def __str__(self):
        isGeneric = self.IsGenericPreProcessor()
        generic = ""
        if isGeneric:
            generic = "Generic "

        if self.Name is not None:
            return "%sDataParser '%s' (Json=%s, Generic=%s, MatchType=%s, Logon=%s):\n" \
                   "Match:   %s\n" \
                   "Pre:     %s\n" \
                   "Parser:  %s\n" \
                   "Creator: %s\n" \
                   "Updater: %s\n" % \
                   (generic, self.Name, self.IsJson, self.IsGenericPreProcessor(),
                    self.MatchType,
                    self.LogOnRequired,
                    self.Match,
                    self.PreProcessor,
                    self.Parser, self.Creator, self.Updater)

        return "%sDataParser (Json=%s, Generic=%s, MatchType=%s, Logon=%s):\n" \
               "Match:   %s\n" \
               "Pre:     %s\n" \
               "Parser:  %s\n" \
               "Creator: %s\n" \
               "Updater: %s\n" % \
               (generic, self.IsJson, self.IsGenericPreProcessor(),
                self.MatchType,
                self.LogOnRequired,
                self.Match,
                self.PreProcessor,
                self.Parser, self.Creator, self.Updater)
