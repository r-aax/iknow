from logging import exception
from worksheet_line import WorksheetLine

#===================================================================================================

class Worksheet:
    """
    Worksheet.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, src=None):
        """
        Init worksheet from any source.

        Parameters
        ----------
        src : WorksheetLine | Worksheet | [WorksheetLine] | [Worksheet] | None
            Source of data.
        """

        self.__lines = []
        self.add_lines(src)

#---------------------------------------------------------------------------------------------------

    @property
    def lines(self):
        """
        Get lines.

        Returns
        -------
        [WorksheetLine]
            Lines.
        """

        return self.__lines

#---------------------------------------------------------------------------------------------------

    def add_lines(self, src):
        """
        Add lines from source.

        Parameters
        ----------
        src : WorksheetLine | Worksheet | [WorksheetLine] | [Worksheet]
            Source.
        """

        if src is None:
            return

        t = type(src)

        if t is WorksheetLine:
            self.__lines.append(src)
        elif t is Worksheet:
            self.add_lines(src.lines)
        elif t is list:
            for e in src:
                self.add_lines(e)
        else:
            # Wrong source.
            raise exception('Worksheet: wrong source')

#---------------------------------------------------------------------------------------------------

    def print(self):
        """
        Print.
        """

        for line in self.lines:
            print(line)

#---------------------------------------------------------------------------------------------------

    def people(self):
        """
        Get people.

        Returns
        -------
        [Person]
            People.
        """

        ps = []

        for wl in self.lines:
            if wl.is_occupied:
                ps.append(wl.employee.personal)

        return ps

#---------------------------------------------------------------------------------------------------

    def slots_sum(self):
        """
        Get sum of slots.

        Returns
        -------
        float
            Sum of slots.
        """

        return sum([wl.slot for wl in self.lines])

#---------------------------------------------------------------------------------------------------

    def occupied_slots_sum(self):
        """
        Get sum of occupied slots.

        Returns
        -------
        float
            Sum of occupied slots.
        """

        return sum([wl.slot for wl in self.lines if wl.is_occupied])

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
