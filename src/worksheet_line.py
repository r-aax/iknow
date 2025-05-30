from logging import exception
import job_place, job_title, employee

#===================================================================================================

class WorksheetLine:
    """
    Line - fact of working employee of position.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, job_place, job_title,
                 slot=1.0, employee=None, status=''):
        """
        Worksheet line init.

        Parameters
        ----------
        job_place : job_place.JobPlace
            Job place.
        job_title : job_title.JobTitle
            Job title.
        slot : float
            Slot of time.
        employee : employee.Employee
            Employee.
        status : str
            Status.
        """

        self.__job_place = job_place
        self.__job_title = job_title
        self.__slot = slot
        self.__employee = employee
        self.__status = status

#---------------------------------------------------------------------------------------------------

    @property
    def job_place(self):
        """
        Get job place.

        Returns
        -------
        JobPlace
            Job place.
        """

        if self.__job_place is None:
            raise exception('WorksheetLine: no job place')

        return self.__job_place

#---------------------------------------------------------------------------------------------------

    @property
    def job_title(self):
        """
        Get job title.

        Returns
        -------
        JobTitle
            Job title.
        """

        if self.__job_title is None:
            raise exception('WorksheetLine: no job title')

        return self.__job_title

#---------------------------------------------------------------------------------------------------

    @property
    def slot(self):
        """
        Get time slot.

        Returns
        -------
        float
            Time slot.
        """

        return self.__slot

#---------------------------------------------------------------------------------------------------

    @property
    def status(self):
        """
        Get status.

        Returns
        -------
        str
            Status.
        """

        if self.__status == '':
            raise exception('WorksheetLine: status is empty')

        return self.__status

#---------------------------------------------------------------------------------------------------

    @property
    def is_vacant(self):
        """
        Check if position is vacant.

        Returns
        -------
        bool
            True - if position is vacant,
            False - if position is occupied.
        """

        return self.__employee is None

#---------------------------------------------------------------------------------------------------

    @property
    def is_occupied(self):
        """
        Check if position is occupied.

        Returns
        -------
        bool
            True - if position is occupied,
            False - is poosition is vacant.
        """

        return not self.is_vacant

#---------------------------------------------------------------------------------------------------

    @property
    def employee(self):
        """
        Get employee.

        Returns
        -------
        Employee
            Employee.
        """

        if self.is_vacant:
            raise exception('WorksheetLine: position is vacant, can not return employee')

        return self.__employee

#---------------------------------------------------------------------------------------------------

    @property
    def employee_str(self):
        """
        Get employee string.

        Returns
        -------
        str
            Employee string.
        """

        e = self.__employee

        if e is None:
            return 'VACANCY'
        else:
            p = e.personal
            return f'{p.surname()} {p.name()} {p.patronymic()} ({self.status}, № {e.tabel})'

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String.
        """

        cat = self.__job_title.full_cat
        pre = f'{self.__job_place.short_name} | {self.__job_title.name} ({cat})'

        return f'{pre} | {self.slot} | {self.employee_str}'

#---------------------------------------------------------------------------------------------------

    def split(self, k):
        """
        Split with coefficient [0.0, 1.0].

        Parameters
        ----------
        k : float
            Coefficient.

        Returns
        -------
        [WorksheetLine, WorksheetLine]
            List with splitted line.
        """

        if k == 0.0:
            return [None, self]
        elif k == 1.0:
            return [self, None]
        else:
            slot1 = self.__slot * k
            line1 = WorksheetLine(job_place=self.__job_place, job_title=self.__job_title,
                                  slot=slot1,
                                  employee=self.__employee, status=self.__status)
            line2 = WorksheetLine(job_place=self.__job_place, job_title=self.__job_title,
                                  slot = self.__slot - slot1,
                                  employee=self.__employee, status=self.__status)
            return [line1, line2]

#---------------------------------------------------------------------------------------------------

    def split_by_parts(self, part1, part2):
        """
        Split in terms of parts.
        We suppose there are part1 + part2 parts,
        and part1 goes to the first line, and part2 - to the second.

        Parameters
        ----------
        part1 : int
            Parts for line1.
        part2 : int
            Parts for line2.

        Returns
        -------
        [WorksheetLine, WorksheetLine]
            List with splitted line.
        """

        return self.split(part1 / (part1 + part2))

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
