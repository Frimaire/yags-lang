# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("Range", "Marker")


# (index, line, column) pair for a character
class Marker(tuple):
    # the character index in code (start from 0)
    @property
    def index(this):
        return this[0]

    # the line number (start from 1)
    @property
    def line(this):
        return this[1]

    # the column number (start from 1)
    @property
    def column(this):
        return this[2]

    def toString(this):
        return str(this.line) + ":" + str(this.column + 1)

    def __str__(this):
        return this.toString()

    # constructor, __new__ should be used for tuple type
    def __new__(T, index, line, column):
        if not (int(index) == index and int(line) == line and int(column) == column) or \
           index < 0 or line < 1 or column < 0:
            raise TypeError("invalid parameter")
        return tuple.__new__(T, [index, line, column])


# the range of a slice of code
class Range(tuple):
    # the position of the first char
    @property
    def start(this):
        return this.startMarker.index

    # the position after the last char
    @property
    def end(this):
        return this.endMarker.index

    # the start position
    @property
    def startMarker(this):
        return this[0]

    # the end position
    @property
    def endMarker(this):
        return this[1]

    # the first line (start from 1)
    @property
    def startLine(this):
        return this.startMarker.line

    # the column of the first char in the first line (start from 0)
    @property
    def startColumn(this):
        return this.startMarker.column

    # the last line (start from 1)
    @property
    def endLine(this):
        return this.endMarker.line

    # the column of the last char in the last line (start from 0)
    @property
    def endColumn(this):
        return this.endMarker.column

    # only display the start line/column
    def toString(this):
        return this.startMarker.toString()

    def __str__(this):
        return this.toString()

    # constructor, __new__ should be used for tuple type
    # Range(start, end, startLine, startColumn, endLine, endColumn) or
    # Range(startLocation, endLocation)
    def __new__(T, start, end, *argv):
        if isinstance(start, Marker) and isinstance(end, Marker):
            return tuple.__new__(T, [start, end])
        return tuple.__new__(T, [
            Marker(start, argv[0], argv[1]),
            Marker(end, argv[2], argv[3])
        ])


